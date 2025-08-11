import gradio as gr
import torch
import torch.nn as nn
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from unsloth import FastModel
from peft import PeftModel
import json
import re
import math
import time

# ===================================================================
# 1. DEFINE CUSTOM CLASSIFIER (from your notebook)
# ===================================================================
# This class is required to load the Phi-4 classification model correctly.
class GPTSequenceClassifier(nn.Module):
    def __init__(self, base_model, num_labels):
        super().__init__()
        self.base = base_model
        hidden_size = base_model.config.hidden_size
        self.classifier = nn.Linear(hidden_size, num_labels, bias=True)
        self.num_labels = num_labels

    def forward(self, input_ids=None, attention_mask=None, labels=None, **kwargs):
        outputs = self.base(input_ids=input_ids, attention_mask=attention_mask, output_hidden_states=True, **kwargs)
        last_hidden_state = outputs.hidden_states[-1]
        pooled_output = last_hidden_state[:, -1, :]
        logits = self.classifier(pooled_output)
        loss = None
        if labels is not None:
            loss = nn.functional.cross_entropy(logits.view(-1, self.num_labels), labels.view(-1))
        return {"loss": loss, "logits": logits} if loss is not None else {"logits": logits}

# ===================================================================
# 2. LOAD MODELS AND TOKENIZERS
# ===================================================================
# This section runs only once when the Space starts up.

# --- Model 1: Equation Extractor (Gemma-3 with Unsloth) ---
print("Loading Equation Extraction Model...")
extractor_adapter_repo = "your-hf-username/gemma-3-1b-equation-extractor-lora"  # <--- REPLACE
base_gemma_model = "unsloth/gemma-3-1b-it-unsloth-bnb-4bit"
extractor_model, extractor_tokenizer = FastModel.from_pretrained(
    model_name=base_gemma_model, max_seq_length=2048, dtype=None, load_in_4bit=True,
)
extractor_model = PeftModel.from_pretrained(extractor_model, extractor_adapter_repo)
print("Equation Extraction Model loaded.")

# --- Model 2: Conceptual Error Classifier (Phi-4) ---
print("Loading Conceptual Error Classifier Model...")
classifier_adapter_repo = "your-hf-username/phi-4-conceptual-error-classifier-lora" # <--- REPLACE
base_phi_model = "microsoft/Phi-4-mini-instruct"

DTYPE = torch.bfloat16
quantization_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=DTYPE)

classifier_backbone = AutoModelForCausalLM.from_pretrained(
    base_phi_model, quantization_config=quantization_config, device_map="auto", trust_remote_code=True,
)
classifier_backbone = PeftModel.from_pretrained(classifier_backbone, classifier_adapter_repo)
classifier_model = GPTSequenceClassifier(classifier_backbone, num_labels=2) # 0 for correct, 1 for flawed
classifier_tokenizer = AutoTokenizer.from_pretrained(base_phi_model, trust_remote_code=True)
classifier_tokenizer.padding_side = "left"
if classifier_tokenizer.pad_token is None:
    classifier_tokenizer.pad_token = classifier_tokenizer.eos_token
print("Conceptual Error Classifier Model loaded.")


# ===================================================================
# 3. DEFINE BACKEND LOGIC
# ===================================================================

# --- Prompts ---
EXTRACTOR_SYSTEM_PROMPT = "[ROLE]..." # Your full equation extractor prompt here
CLASSIFIER_SYSTEM_PROMPT = "Analyze the following mathematical problems and answers to determine if the solution is correct or incorrect."

def format_solution_into_json_str(solution_text: str) -> str:
    lines = [line.strip() for line in solution_text.strip().split('\n')]
    final_answer = ""
    # Check if the last line contains the final answer
    if "FINAL ANSWER:" in lines[-1]:
        final_answer = lines[-1].replace("FINAL ANSWER:", "").strip()
        lines = lines[:-1] # Remove the final answer line from the main body
        
    solution_dict = {f"L{i+1}": line for i, line in enumerate(lines)}
    solution_dict["FA"] = final_answer
    return json.dumps(solution_dict, indent=2)

def evaluate_equations(eq_dict: dict, sol_dict: dict):
    """Evaluates equations and returns the first error found."""
    for key, eq_str in eq_dict.items():
        if "=" not in eq_str or not eq_str:
            continue
        try:
            lhs, rhs = eq_str.split('=', 1)
            lhs_val = eval(lhs, {"__builtins__": None}, {})
            rhs_val = eval(rhs, {"__builtins__": None}, {})
            if not math.isclose(lhs_val, rhs_val, rel_tol=1e-2):
                correct_rhs = f"{lhs_val:.2f}".rstrip('0').rstrip('.')
                return {
                    "error": True,
                    "line_key": key,
                    "line_text": sol_dict.get(key, "N/A"),
                    "flawed_calc": eq_str,
                    "correct_calc": f"{lhs}={correct_rhs}"
                }
        except Exception:
            continue # Skip lines that can't be evaluated
    return {"error": False}

def extract_json_from_response(response: str) -> dict:
    match = re.search(r'```json\s*(\{.*?\})\s*```', response, re.DOTALL)
    json_str = match.group(1) if match else re.search(r'(\{.*?\})', response, re.DOTALL)
    if not json_str: return {}
    try:
        return json.loads(json_str.group(0) if hasattr(json_str, 'group') else json_str)
    except:
        return {}

# --- The Main Pipeline Function ---
def full_analysis_pipeline(math_question, proposed_solution):
    if not math_question or not proposed_solution:
        yield "Waiting for input...", "Waiting for input...", "Please provide a math question and a solution."
        return

    # --- i. Run Equation Extraction ---
    solution_json_str = format_solution_into_json_str(proposed_solution)
    messages = [{"role": "user", "content": f"{EXTRACTOR_SYSTEM_PROMPT}\n\n### Solution:\n{solution_json_str}"}]
    prompt = extractor_tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = extractor_tokenizer([prompt], return_tensors="pt").to("cuda")
    outputs = extractor_model.generate(**inputs, max_new_tokens=300, use_cache=True)
    extracted_text = extractor_tokenizer.batch_decode(outputs[:, inputs.input_ids.shape[1]:], skip_special_tokens=True)[0]
    extracted_eq_dict = extract_json_from_response(extracted_text)

    # --- ii. Evaluate the Equations ---
    computational_error = evaluate_equations(extracted_eq_dict, json.loads(solution_json_str))

    # --- iii. If a Computational Error is Found, Stop Here ---
    if computational_error["error"]:
        explanation = (
            f"There is a computational error in this solution line: \"{computational_error['line_text']}\".\n"
            f"The calculation being carried out is {computational_error['flawed_calc']}, "
            f"but the correct calculation should be {computational_error['correct_calc']}."
        )
        yield {
            classification_output: "Computational Error",
            confidence_output: "100% (Programmatic Check)",
            explanation_output: explanation
        }
        return

    # --- iv. If No Computational Error, Proceed to Conceptual Check ---
    # a. Update UI with status message
    yield {
        classification_output: "Pending...",
        confidence_output: "Pending...",
        explanation_output: "✅ All calculations appear to be correct. Now checking for conceptual errors..."
    }
    
    # b. Run conceptual error classification
    input_text = f"{CLASSIFIER_SYSTEM_PROMPT}\n\n### Problem:\n{math_question}\n\n### Answer:\n{proposed_solution}"
    inputs = classifier_tokenizer(input_text, return_tensors="pt", truncation=True, max_length=512).to("cuda")
    with torch.no_grad():
        outputs = classifier_model(**inputs)
        logits = outputs["logits"]
        probs = torch.softmax(logits, dim=-1).squeeze().tolist()

    # --- v & vi. Report Final Classification ---
    is_flawed_prob = probs[1]
    is_correct_prob = probs[0]

    if is_flawed_prob > 0.5: # Flawed
        yield {
            classification_output: "Conceptual Error",
            confidence_output: f"{is_flawed_prob:.2%}",
            explanation_output: "There appears to be a conceptual error in the logic or setup of the solution."
        }
    else: # Correct
        yield {
            classification_output: "Correct",
            confidence_output: f"{is_correct_prob:.2%}",
            explanation_output: "No errors detected. The solution appears to be correct."
        }

# ===================================================================
# 4. BUILD THE GRADIO INTERFACE
# ===================================================================
with gr.Blocks(theme=gr.themes.Default(primary_hue="indigo", secondary_hue="blue")) as demo:
    gr.Markdown("# 🧮 Math Solution Classifier")
    gr.Markdown("Classify math solutions as correct, conceptually flawed, or computationally flawed.")

    with gr.Row():
        with gr.Column(scale=2):
            math_question_box = gr.Textbox(label="Math Question", placeholder="e.g., Solve for x: 2x + 5 = 13")
            proposed_solution_box = gr.Textbox(label="Proposed Solution", lines=5, placeholder="e.g., 2x + 5 = 13\n2x = 13 - 5\n2x = 8\nFINAL ANSWER: 4")
            classify_button = gr.Button("Classify Solution", variant="primary", scale=1)
        with gr.Column(scale=2):
            classification_output = gr.Textbox(label="Classification")
            confidence_output = gr.Textbox(label="Confidence")
            explanation_output = gr.Textbox(label="Explanation", lines=5)

    gr.Examples(
        examples=[
            ["Solve for x: 2x + 5 = 13", "2x + 5 = 13\n2x = 13 - 5\n2x = 8\nFINAL ANSWER: 4"],
            ["John has three apples and Mary has seven, how many apples do they have together?", "They have 7 + 3 = 11 apples.\nFINAL ANSWER: 11"],
            ["What is 15% of 200?", "15% = 15/100 = 0.15\n0.15 * 200 = 30\nFINAL ANSWER: 30"]
        ],
        inputs=[math_question_box, proposed_solution_box]
    )
    
    classify_button.click(
        fn=full_analysis_pipeline,
        inputs=[math_question_box, proposed_solution_box],
        outputs=[classification_output, confidence_output, explanation_output]
    )

demo.launch(debug=True)