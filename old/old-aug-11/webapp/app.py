# app.py - Gradio version (much simpler for HF Spaces)
import unsloth
from unsloth import FastModel

import gradio as gr
import logging
import spaces

import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig


from peft import PeftModel
from huggingface_hub import hf_hub_download

import json
import re
import math
import time

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# --- compat shim for newer Phi-3/4 modeling files ---
import transformers as _tf
# Some HF model repos do: `from transformers.utils import LossKwargs`
# Older/newer lib versions may not re-export it, so we provide a fallback.
if not hasattr(_tf.utils, "LossKwargs"):
    from typing import Dict, Any
    class _LossKwargs(dict):
        """Duck-typed placeholder; used only for type hints / Unpack at runtime."""
        pass
    _tf.utils.LossKwargs = _LossKwargs
# -----------------------------------------------------


# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global variables for model and tokenizer
label_mapping = {0: "✅ Correct", 1: "🤔 Conceptually Flawed", 2: "🔢 Computationally Flawed"}




# ===================================================================
# 1. DEFINE CUSTOM CLASSIFIER (Required for Phi-4)
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
        

        
        
# --- Helper Functions ---
def format_solution_into_json_str(solution_text: str) -> str:
    lines = [line.strip() for line in solution_text.strip().split('\n') if line.strip()]
    final_answer = ""
    if lines and "FINAL ANSWER:" in lines[-1].upper():
        final_answer = lines[-1][len("FINAL ANSWER:"):].strip()
        lines = lines[:-1]
    solution_dict = {f"L{i+1}": line for i, line in enumerate(lines)}
    solution_dict["FA"] = final_answer
    return json.dumps(solution_dict, indent=2)

def sanitize_equation_string(expression: str) -> str:
    if not isinstance(expression, str):
        return ""

    s = expression.strip()

    # Normalize common symbols
    s = s.replace('×', '*').replace('·', '*').replace('x', '*')

    # Convert percentages like '12%' -> '(12/100)'
    s = re.sub(r'(?<!\d)(\d+(?:\.\d+)?)\s*%', r'(\1/100)', s)

    # Simple paren balancing trims (only when a single stray exists at an edge)
    if s.count('(') > s.count(')') and s.startswith('('):
        s = s[1:]
    elif s.count(')') > s.count('(') and s.endswith(')'):
        s = s[:-1]

    # Drop units right after a slash: /hr, /dogs
    s = re.sub(r'/([a-zA-Z]+)', '', s)

    # Keep only numeric math tokens
    s = re.sub(r'[^\d.()+\-*/=%]', '', s)

    # Collapse repeated '=' (e.g., '==24/2=12' -> '=24/2=12')
    s = re.sub(r'=+', '=', s)

    return s

import re, math

def _parse_equation(eq_str: str):
    s = sanitize_equation_string(eq_str or "")
    s = s.lstrip('=')  # handle lines like '=24/2=12'
    if '=' not in s:
        return None
    if s.count('=') > 1:
        pos = s.rfind('=')
        lhs, rhs = s[:pos], s[pos+1:]
    else:
        lhs, rhs = s.split('=', 1)
    lhs, rhs = lhs.strip(), rhs.strip()
    if not lhs or not rhs:
        return None
    return lhs, rhs

def _abs_tol_from_display(rhs_str: str):
    """
    If RHS is a single numeric literal like 0.33, use half-ULP at that precision.
    e.g., '0.33' -> 0.5 * 10^-2 = 0.005
    Otherwise return None and fall back to base tolerances.
    """
    s = rhs_str.strip()
    # allow optional parens and sign
    m = re.fullmatch(r'\(?\s*[-+]?\d+(?:\.(\d+))?\s*\)?', s)
    if not m:
        return None
    frac = m.group(1) or ""
    d = len(frac)
    return 0.5 * (10 ** (-d)) if d > 0 else 0.5  # if integer shown, allow ±0.5

def evaluate_equations(eq_dict: dict, sol_dict: dict,
                       base_rel_tol: float = 1e-6,
                       base_abs_tol: float = 1e-9,
                       honor_display_precision: bool = True):
    """
    Evaluates extracted equations. Accepts rounded RHS values based on displayed precision.
    """
    for key, eq_str in (eq_dict or {}).items():
        parsed = _parse_equation(eq_str)
        if not parsed:
            continue
        lhs, rhs_str = parsed

        try:
            lhs_val = eval(lhs, {"__builtins__": None}, {})
            rhs_val = eval(rhs_str, {"__builtins__": None}, {})
        except Exception:
            continue

        # dynamic absolute tolerance from RHS formatting (e.g., 0.33 -> 0.005)
        abs_tol = base_abs_tol
        if honor_display_precision:
            dyn = _abs_tol_from_display(rhs_str)
            if dyn is not None:
                abs_tol = max(abs_tol, dyn)

        if not math.isclose(lhs_val, rhs_val, rel_tol=base_rel_tol, abs_tol=abs_tol):
            correct_rhs_val = round(lhs_val, 6)
            correct_rhs_str = f"{correct_rhs_val:.6f}".rstrip('0').rstrip('.')
            return {
                "error": True,
                "line_key": key,
                "line_text": sol_dict.get(key, "N/A"),
                "original_flawed_calc": eq_str,
                "sanitized_lhs": lhs,
                "original_rhs": rhs_str,
                "correct_rhs": correct_rhs_str,
            }

    return {"error": False}





def extract_json_from_response(response: str) -> dict:
    """
    Recover equations from the extractor's output.

    Strategy:
      1) Try to parse a real JSON object (if present).
      2) Parse relaxed key-value lines like 'L1: ...' or 'FA=...'.
      3) Also fall back to linewise equations (e.g., '=24/2=12', '7*2=14') and
         merge them as L1, L2, ... preserving order. Keep FA if present.
    """
    out = {}

    if not response or not isinstance(response, str):
        return out

    text = response.strip()

    # --- 1) strict JSON block, if any ---
    m = re.search(r'\{.*\}', text, flags=re.S)
    if m:
        try:
            obj = json.loads(m.group(0))
            if isinstance(obj, dict) and any(k.startswith("L") for k in obj):
                return obj
            elif isinstance(obj, dict):
                out.update(obj)  # keep FA etc., then continue
        except Exception:
            pass

    # --- 2) relaxed key/value lines: Lk : value   or   FA = value ---
    relaxed = {}
    for ln in text.splitlines():
        ln = ln.strip().strip(',')
        if not ln:
            continue
        m = re.match(r'(?i)^(L\d+|FA)\s*[:=]\s*(.+?)\s*$', ln)
        if m:
            k = m.group(1).strip()
            v = m.group(2).strip().rstrip(',')
            relaxed[k] = v
    out.update(relaxed)

    # Count how many L-keys we already have
    existing_L = sorted(
        int(k[1:]) for k in out.keys()
        if k.startswith("L") and k[1:].isdigit()
    )
    next_L = (max(existing_L) + 1) if existing_L else 1

    # --- 3) linewise fallback: harvest bare equations and merge ---
    def _looks_like_equation(s: str) -> str | None:
        s = sanitize_equation_string(s or "").lstrip('=')
        if '=' in s and any(ch.isdigit() for ch in s):
            return s
        return None

    # set of existing equation strings to avoid duplicates
    seen_vals = set(v for v in out.values() if isinstance(v, str))

    for ln in text.splitlines():
        ln = ln.strip().strip(',')
        if not ln or re.match(r'(?i)^(L\d+|FA)\s*[:=]', ln):
            # skip lines we already captured as relaxed pairs
            continue
        eq = _looks_like_equation(ln)
        if eq and eq not in seen_vals:
            out[f"L{next_L}"] = eq
            seen_vals.add(eq)
            next_L += 1

    return out

# --- Prompts ---
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

# --- Example 1 ---
FEW_SHOT_EXAMPLE_1_SOLUTION = {
  "L1": "2% of $90 is (2/100)*$90 = $1.8",
  "L2": "2% of $60 is (2/100)*$60 = $1.2",
  "L3": "The second transaction was reversed without the service charge so only a total of $90+$1.8+$1.2 = $39 was deducted from his account",
  "L4": "He will have a balance of $400-$39 = $361",
  "FA": "361"
}

FEW_SHOT_EXAMPLE_1_EQUATIONS = {
  "L1": "(2/100)*90=1.8",
  "L2": "(2/100)*60=1.2",
  "L3": "90+1.8+1.2=39",
  "L4": "400-39=361",
  "FA": ""
}


# --- Example 2 ---
FEW_SHOT_EXAMPLE_2_SOLUTION = {
  "L1": "She drinks 2 bottles a day and there are 24 bottles in a case so a case will last 24/2 = 12 days",
  "L2": "She needs enough to last her 240 days and 1 case will last her 12 days so she needs 240/12 = 20 cases",
  "L3": "Each case is on sale for $12.00 and she needs 20 cases so that's 12*20 = $240.00",
  "FA": "240"
}

FEW_SHOT_EXAMPLE_2_EQUATIONS = {
  "L1": "24/2=12",
  "L2": "240/12=20",
  "L3": "12*20=240.00",
  "FA": ""
}

def create_extractor_messages(solution_json_str: str) -> list:
    """
    Returns a list of dictionaries representing the conversation history for the prompt.
    """
    # Start with the constant few-shot examples defined globally
    messages = [
        {"role": "user", "content": f"{EXTRACTOR_SYSTEM_PROMPT}\n\n### Solution:\n{json.dumps(FEW_SHOT_EXAMPLE_1_SOLUTION, indent=2)}"},
        {"role": "assistant", "content": json.dumps(FEW_SHOT_EXAMPLE_1_EQUATIONS, indent=2)},
        {"role": "user", "content": f"### Solution:\n{json.dumps(FEW_SHOT_EXAMPLE_2_SOLUTION, indent=2)}"},
        {"role": "assistant", "content": json.dumps(FEW_SHOT_EXAMPLE_2_EQUATIONS, indent=2)},
    ]

    # Add the final user query to the end of the conversation
    final_user_prompt = f"### Solution:\n{solution_json_str}"
    messages.append({"role": "user", "content": final_user_prompt})

    return messages
        
gemma_model = None
gemma_tokenizer = None
classifier_model = None
classifier_tokenizer = None

def load_model():
    """Load your trained model here"""
    global gemma_model, gemma_tokenizer, classifier_model, classifier_tokenizer, DEVICE
    
    try:
        device = DEVICE

        # --- Model 1: Equation Extractor (Gemma-3 with Unsloth) ---
        extractor_adapter_repo = "arvindsuresh-math/gemma-3-1b-equation-extractor-lora"
        base_gemma_model = "unsloth/gemma-3-1b-it-unsloth-bnb-4bit"

        gemma_model, gemma_tokenizer = FastModel.from_pretrained(
            model_name=base_gemma_model,
            max_seq_length=2048,
            dtype=None,
            load_in_4bit=True,
        )

        # --- Gemma tokenizer hygiene (fix the right-padding warning) ---
        if gemma_tokenizer.pad_token is None:
            gemma_tokenizer.pad_token = gemma_tokenizer.eos_token
        gemma_tokenizer.padding_side = "left"   # align last tokens across the batch

        gemma_model = PeftModel.from_pretrained(gemma_model, extractor_adapter_repo)


        # --- Model 2: Conceptual Error Classifier (Phi-4) ---
        classifier_adapter_repo = "arvindsuresh-math/phi-4-error-binary-classifier"
        base_phi_model = "microsoft/Phi-4-mini-instruct"

        # T4 does fp16 (not bf16)
        DTYPE = torch.float32
        quantization_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=DTYPE,
        )


        classifier_backbone_base = AutoModelForCausalLM.from_pretrained(
            base_phi_model,
            quantization_config=quantization_config,
            device_map={"": 0},
            trust_remote_code=False,      # keep this if you switched it earlier
            # safest with eager attention when mixing kernels:
            attn_implementation="eager",
        )

        classifier_tokenizer = AutoTokenizer.from_pretrained(
            base_phi_model,
            trust_remote_code=False      # <-- match above
        )

        classifier_tokenizer.padding_side = "left"
        if classifier_tokenizer.pad_token is None:
            classifier_tokenizer.pad_token = classifier_tokenizer.eos_token

        classifier_backbone_peft = PeftModel.from_pretrained(
            classifier_backbone_base,
            classifier_adapter_repo
            )
        classifier_model = GPTSequenceClassifier(classifier_backbone_peft, num_labels=2)

        # Download and load the custom classifier head's state dictionary
        classifier_head_path = hf_hub_download(repo_id=classifier_adapter_repo, filename="classifier_head.pth")
        classifier_model.classifier.load_state_dict(torch.load(classifier_head_path, map_location=device))

        classifier_model.to(device)
        classifier_model = classifier_model.to(device=DEVICE, dtype=torch.float32)

        classifier_model.eval() # Set model to evaluation mode  
        
        logger.info("Model loaded successfully")
        return "Model loaded successfully!"
        
    except Exception as e:
        logger.error(f"Error loading model: {e}")
        return f"Error loading model: {e}"
def models_ready():
    return all([gemma_model, gemma_tokenizer, classifier_model, classifier_tokenizer])

def analyze_single(math_question: str, proposed_solution: str, debug: bool = False):
    """
    Single (question, solution) classifier.
    Stage 1: computational check via Gemma extraction + evaluator.
    Stage 2: conceptual/correct check via Phi-4 classifier.
    Returns: {"classification": "...", "confidence": "...", "explanation": "..."}
    """
    global DEVICE
    device = DEVICE
    # -----------------------------
    # STAGE 1: COMPUTATIONAL CHECK
    # -----------------------------
    # 1) Format and extract equations
    solution_json_str = format_solution_into_json_str(proposed_solution)
    solution_dict = json.loads(solution_json_str)

    messages = create_extractor_messages(solution_json_str)
    prompt = gemma_tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

    inputs = gemma_tokenizer([prompt], return_tensors="pt").to(device)
    outputs = gemma_model.generate(
        **inputs,
        max_new_tokens=300,
        use_cache=True,
        pad_token_id=gemma_tokenizer.pad_token_id,
        do_sample=False,
        temperature=0.0,
    )

    extracted_text = gemma_tokenizer.batch_decode(
        outputs[:, inputs.input_ids.shape[1]:], skip_special_tokens=True
    )[0]

    if debug:
        print("\n[Gemma raw output]\n", extracted_text)

    extracted_eq_dict = extract_json_from_response(extracted_text)

    # 2) Keep only lines that actually contain digits in the original text
    final_eq_to_eval = {
        k: v
        for k, v in extracted_eq_dict.items()
        if any(ch.isdigit() for ch in solution_dict.get(k, ""))
    }
    if debug:
        print("\n[Equations to evaluate]\n", json.dumps(final_eq_to_eval, indent=2))

    # 3) Evaluate
    computational_error = evaluate_equations(final_eq_to_eval, solution_dict)
    if computational_error.get("error"):
        lhs = computational_error["sanitized_lhs"]
        rhs = computational_error["original_rhs"]
        correct_rhs = computational_error["correct_rhs"]
        line_txt = computational_error.get("line_text", "")
        explanation = (
            "A computational error was found.\n"
            f'On line: "{line_txt}"\n'
            f"The student wrote '{lhs} = {rhs}', but the correct result of '{lhs}' is {correct_rhs}."
        )
        return {
            "classification": "Computational Error",
            "confidence": "100%",
            "explanation": explanation,
        }

    # --------------------------
    # STAGE 2: CONCEPTUAL CHECK
    # --------------------------
    input_text = (
        f"{CLASSIFIER_SYSTEM_PROMPT}\n\n"
        f"### Problem:\n{math_question}\n\n"
        f"### Answer:\n{proposed_solution}"
    )
    cls_inputs = classifier_tokenizer(
        input_text, return_tensors="pt", truncation=True, max_length=512
    ).to(device)

    with torch.no_grad():
        logits = classifier_model(**cls_inputs)["logits"]
        probs = torch.softmax(logits, dim=-1).squeeze()

    is_correct_prob = float(probs[0])
    is_flawed_prob  = float(probs[1])

    if debug:
        print("\n[Phi-4 logits]", logits.to(torch.float32).cpu().numpy())
        print("[Phi-4 probs] [Correct, Flawed]:", [is_correct_prob, is_flawed_prob])

    if is_flawed_prob > 0.5:
        return {
            "classification": "Conceptual Error",
            "confidence": f"{is_flawed_prob:.2%}",
            "explanation": "Logic or setup appears to have a conceptual error.",
        }
    else:
        return {
            "classification": "Correct",
            "confidence": f"{is_correct_prob:.2%}",
            "explanation": "Solution appears correct.",
        }


def classify_solution(question: str, solution: str):
    """
    Classify the math solution
    Returns: (classification_label, confidence_score, explanation)
    """
    if not question.strip() or not solution.strip():
        return "Please fill in both fields", 0.0, ""
    
    if not models_ready():
        return "Models not loaded", 0.0, ""
    
    try:
        res = analyze_single(question, solution)
        
        return res["classification"], res["confidence"], res["explanation"]
    except Exception:
        logger.exception("inference failed")
        
        
        

# Load model on startup
load_model()

# Create Gradio interface
with gr.Blocks(title="Math Solution Classifier", theme=gr.themes.Soft()) as app:
    gr.Markdown("# 🧮 Math Solution Classifier")
    gr.Markdown("Classify math solutions as correct, conceptually flawed, or computationally flawed.")
    
    with gr.Row():
        with gr.Column():
            question_input = gr.Textbox(
                label="Math Question",
                placeholder="e.g., Solve for x: 2x + 5 = 13",
                lines=3
            )
            
            solution_input = gr.Textbox(
                label="Proposed Solution", 
                placeholder="e.g., 2x + 5 = 13\n2x = 13 - 5\n2x = 8\nx = 4",
                lines=5
            )
            
            classify_btn = gr.Button("Classify Solution", variant="primary")
        
        with gr.Column():
            classification_output = gr.Textbox(label="Classification", interactive=False)
            confidence_output = gr.Textbox(label="Confidence", interactive=False)
            explanation_output = gr.Textbox(label="Explanation", interactive=False, lines=3)
    
    # Examples
    gr.Examples(
        examples=[
            [
                "Solve for x: 2x + 5 = 13",
                "2x + 5 = 13\n2x = 13 - 5\n2x = 8\nx = 4"
            ],
            [
                "John has three apples and Mary has seven, how many apples do they have together?", 
                "They have 7 + 3 = 11 apples."  # This should be computationally flawed
            ],
            [
                "What is 15% of 200?",
                "15% = 15/100 = 0.15\n0.15 × 200 = 30"
            ]
        ],
        inputs=[question_input, solution_input]
    )
    
    classify_btn.click(
        fn=classify_solution,
        inputs=[question_input, solution_input],
        outputs=[classification_output, confidence_output, explanation_output]
    )

if __name__ == "__main__":
    app.launch()