# app.py

import gradio as gr
import torch
import torch.nn as nn
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from unsloth import FastModel
from peft import PeftModel
import json
import re
import math

# ===================================================================
# 1. DEFINE CUSTOM CLASSIFIER (from your notebook)
# This class is required to load the Phi-4 classification model correctly.
# ===================================================================
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
# This section runs only once when the Space starts up.
# ===================================================================

# --- Model 1: Equation Extractor (Gemma-3 with Unsloth) ---
print("Loading Equation Extraction Model...")
extractor_adapter_repo = "arvindsuresh-math/gemma-3-1b-equation-extractor-lora"
base_gemma_model = "unsloth/gemma-3-1b-it-unsloth-bnb-4bit"

# Use try-except for robust loading on different hardware
try:
    gemma_model, gemma_tokenizer = FastModel.from_pretrained(
        model_name=base_gemma_model, max_seq_length=2048, dtype=None, load_in_4bit=True,
    )
except Exception as e:
    print(f"Could not load Gemma in 4-bit, trying 8-bit. Error: {e}")
    gemma_model, gemma_tokenizer = FastModel.from_pretrained(
        model_name=base_gemma_model, max_seq_length=2048, dtype=None, load_in_8bit=True,
    )

gemma_tokenizer = FastModel.get_peft_model(gemma_model, gemma_adapter_repo)
print("Equation Extraction Model loaded.")


# --- Model 2: Conceptual Error Classifier (Phi-4) ---
print("Loading Conceptual Error Classifier Model...")
classifier_adapter_repo = "arvindsuresh-math/phi-4-error-binary-classifier"
base_phi_model = "microsoft/Phi-4-mini-instruct"

DTYPE = torch.bfloat16
quantization_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=DTYPE)

# Load the base model and tokenizer
classifier_backbone_base = AutoModelForCausalLM.from_pretrained(
    base_phi_model, quantization_config=quantization_config, device_map="auto", trust_remote_code=True,
)
classifier_tokenizer = AutoTokenizer.from_pretrained(base_phi_model, trust_remote_code=True)
classifier_tokenizer.padding_side = "left"
if classifier_tokenizer.pad_token is None:
    classifier_tokenizer.pad_token = classifier_tokenizer.eos_token

# Apply the LoRA adapter to the backbone
classifier_backbone_peft = PeftModel.from_pretrained(classifier_backbone_base, classifier_adapter_repo)

# Initialize the full classifier model with the custom head
classifier_model = GPTSequenceClassifier(classifier_backbone_peft, num_labels=2) # 0 for correct, 1 for flawed

# Load the state dictionary for the classification head
# Note: map_location is crucial for loading correctly on CPU or GPU
classifier_head_path = hf_hub_download(repo_id=classifier_adapter_repo, filename="classifier_head.pth")
classifier_model.classifier.load_state_dict(torch.load(classifier_head_path, map_location=torch.device("cuda" if torch.cuda.is_available() else "cpu")))

classifier_model.eval() # Set model to evaluation mode
print("Conceptual Error Classifier Model loaded.")


# ===================================================================
# 3. DEFINE BACKEND LOGIC
# ===================================================================

# --- Prompts (taken from notebooks) ---
EXTRACTOR_SYSTEM_PROMPT = \
"""[ROLE]
You are an expert at parsing mathematical solutions.

[TASK]
You are given a mathematical solution. Your task is to extract the calculation performed on each line and represent it as a simple equation.

**This is a literal transcription task. Follow these rules with extreme precision:**
- **RULE 1: Transcribe EXACTLY.** Do not correct mathematical errors. If a line implies `2+2=5`, your output for that line must be `2+2=5`.
- **RULE 2: Isolate the Equation.** Your output must contain ONLY the equation. Do not include any surrounding text, units (like `/hour`), or currency symbols (like `$`).
- **RULE 3: Use Standard Operators.** Always use `*` for multiplication. Never use `x`.

[RESPONSE FORMAT]
Your response must be ONLY a single, valid JSON object, adhering strictly to these rules:
For each line of the solution, create a key-value pair.
- The key should be the line identifier (e.g., "L1", "L2", "FA" for the final answer line).
- The value should be the extracted equation string (e.g., "10+5=15").
- If a line contains no calculation, the value must be an empty string.
"""

CLASSIFIER_SYSTEM_PROMPT = \
"""You are a mathematics tutor.
You will be given a math word problem and a solution written by a student.
Carefully analyze the problem and solution LINE-BY-LINE and determine whether there are any errors in the solution."""


def format_solution_into_json_str(solution_text: str) -> str:
    """Converts a multi-line solution string into a JSON-formatted string."""
    lines = [line.strip() for line in solution_text.strip().split('\n') if line.strip()]
    final_answer = ""
    if lines and "FINAL ANSWER:" in lines[-1].upper():
        final_answer = lines[-1][len("FINAL ANSWER:"):].strip()
        lines = lines[:-1]
        
    solution_dict = {f"L{i+1}": line for i, line in enumerate(lines)}
    solution_dict["FA"] = final_answer
    return json.dumps(solution_dict, indent=2)

def evaluate_equations(eq_dict: dict, sol_dict: dict):
    """
    Evaluates extracted equations and returns details of the first computational error found.
    """
    for key, eq_str in eq_dict.items():
        if not eq_str or "=" not in eq_str:
            continue
        try:
            lhs, rhs = eq_str.split('=', 1)
            # Use a safe eval environment
            lhs_val = eval(lhs, {"__builtins__": None}, {})
            rhs_val = eval(rhs, {"__builtins__": None}, {})
            
            if not math.isclose(lhs_val, rhs_val, rel_tol=1e-2):
                correct_rhs_val = round(lhs_val, 4)
                # Clean up trailing zeros
                correct_rhs = f"{correct_rhs_val:.4f}".rstrip('0').rstrip('.')
                
                return {
                    "error": True,
                    "line_key": key,
                    "line_text": sol_dict.get(key, "N/A"),
                    "flawed_calc": eq_str,
                    "correct_calc": f"{lhs}={correct_rhs}"
                }
        except Exception:
            # This will catch syntax errors in the equation string, etc.
            continue
    return {"error": False}

def extract_json_from_response(response: str) -> dict:
    """Extracts a JSON object from a model's text response, handling markdown code blocks."""
    match = re.search(r'```json\s*(\{.*?\})\s*```', response, re.DOTALL)
    json_str = match.group(1) if match else re.search(r'(\{.*?\})', response, re.DOTALL)
    if not json_str: return {}
    try:
        # Use .group(0) if it's a match object, otherwise use the string itself
        return json.loads(json_str.group(0) if hasattr(json_str, 'group') else json_str)
    except (json.JSONDecodeError, AttributeError):
        return {}

# --- The Main Pipeline Function ---
def full_analysis_pipeline(math_question, proposed_solution):
    """
    The core function that runs the two-stage analysis and yields updates for the UI.
    """
    if not math_question or not proposed_solution:
        yield "Waiting for input", "Waiting for input", "Please provide a math question and a solution."
        return

    # --- STAGE 1: COMPUTATIONAL CHECK ---
    yield "Running...", "Running...", "Step 1: Extracting equations from the solution..."

    # Format the input for the Gemma model
    solution_json_str = format_solution_into_json_str(proposed_solution)
    messages = [{"role": "user", "content": f"{EXTRACTOR_SYSTEM_PROMPT}\n\n### Solution:\n{solution_json_str}"}]
    prompt = gemma_tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    
    # Run inference
    inputs = gemma_tokenizer([prompt], return_tensors="pt").to("cuda")
    outputs = gemma_model.generate(**inputs, max_new_tokens=300, use_cache=True)
    extracted_text = gemma_tokenizer.batch_decode(outputs[:, inputs.input_ids.shape[1]:], skip_special_tokens=True)[0]
    extracted_eq_dict = extract_json_from_response(extracted_text)

    # Programmatically evaluate the extracted equations
    computational_error = evaluate_equations(extracted_eq_dict, json.loads(solution_json_str))

    # If a computational error is found, stop and report it.
    if computational_error["error"]:
        explanation = (
            f"A computational error was found.\n"
            f"On line: \"{computational_error['line_text']}\"\n"
            f"The calculation was: {computational_error['flawed_calc']}\n"
            f"The correct calculation should be: {computational_error['correct_calc']}"
        )
        yield "Computational Error", "100% (Programmatic Check)", explanation
        return

    # --- STAGE 2: CONCEPTUAL CHECK ---
    yield "Running...", "Running...", "✅ Calculations correct. Step 2: Checking for conceptual errors..."
    
    # Format the input for the Phi-4 model
    input_text = f"{CLASSIFIER_SYSTEM_PROMPT}\n\n### Problem:\n{math_question}\n\n### Answer:\n{proposed_solution}"
    inputs = classifier_tokenizer(input_text, return_tensors="pt", truncation=True, max_length=512).to("cuda")
    
    # Run inference
    with torch.no_grad():
        outputs = classifier_model(**inputs)
        logits = outputs["logits"]
        probs = torch.softmax(logits, dim=-1).squeeze().tolist()

    # Report the final classification based on the Phi-4 model's output
    is_flawed_prob = probs[1]
    is_correct_prob = probs[0]
    
    if is_flawed_prob > 0.5:
        explanation = "The calculations are correct, but there appears to be a conceptual error in the logic or setup of the solution."
        yield "Conceptual Error", f"{is_flawed_prob:.2%}", explanation
    else:
        explanation = "No errors detected. The solution appears to be both computationally and conceptually correct."
        yield "Correct", f"{is_correct_prob:.2%}", explanation


# ===================================================================
# 4. BUILD THE GRADIO INTERFACE
# ===================================================================
with gr.Blocks(theme=gr.themes.Default(primary_hue="indigo", secondary_hue="blue")) as demo:
    gr.Markdown("# 🧮 Math Solution Classifier")
    gr.Markdown("This app uses a two-stage process to classify a math solution: first checking for **computational errors**, then for **conceptual errors**.")

    with gr.Row():
        with gr.Column(scale=2):
            math_question_box = gr.Textbox(label="Math Question", placeholder="e.g., A farm has 15 chickens and 10 cows. How many legs are there in total?")
            proposed_solution_box = gr.Textbox(
                label="Proposed Solution",
                lines=5,
                placeholder="e.g., Chicken legs: 15 * 2 = 30\nCow legs: 10 * 4 = 40\nTotal legs: 30 + 40 = 70\nFINAL ANSWER: 70"
            )
            classify_button = gr.Button("Classify Solution", variant="primary", scale=1)
        with gr.Column(scale=2):
            classification_output = gr.Textbox(label="Classification", interactive=False)
            confidence_output = gr.Textbox(label="Confidence", interactive=False)
            explanation_output = gr.Textbox(label="Explanation", lines=5, interactive=False)

    gr.Examples(
        examples=[
            ["A grocery store sells apples for $0.50 each and oranges for $0.75 each. If a customer buys 10 apples and 5 oranges, what is the total cost?", "Apple cost: 10 * 0.50 = 5.00\nOrange cost: 5 * 0.75 = 3.75\nTotal cost: 5.00 + 3.75 = 8.75\nFINAL ANSWER: 8.75"],
            ["John has three apples and Mary has seven, how many apples do they have together?", "They have 7 + 3 = 11 apples.\nFINAL ANSWER: 11"],
            ["A car travels at 60 miles per hour. How long will it take to travel 180 miles?", "Time = Speed / Distance\nTime = 60 / 180 = 0.33 hours\nFINAL ANSWER: 0.33"],
        ],
        inputs=[math_question_box, proposed_solution_box],
        fn=full_analysis_pipeline,
        outputs=[classification_output, confidence_output, explanation_output],
        cache_examples=False,
    )
    
    classify_button.click(
        fn=full_analysis_pipeline,
        inputs=[math_question_box, proposed_solution_box],
        outputs=[classification_output, confidence_output, explanation_output]
    )

demo.launch(debug=True)