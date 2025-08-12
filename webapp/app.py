# app.py 
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

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")





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
        
        
# ===================================================================
#HELPERS
# ===================================================================

# --- Helper Functions ---
def extract_equation_from_response(response: str) -> str | None:
    """Extracts content from between <eq> and </eq> tags."""
    match = re.search(r'<eq>(.*?)</eq>', response, re.DOTALL)
    return match.group(1) if match else None

def sanitize_equation_string(expression: str) -> str:
    """
    Enhanced version with your requested simplified parenthesis logic.
    """
    if not isinstance(expression, str):
        return ""

    # Your requested parenthesis logic:
    if expression.count('(') > expression.count(')') and expression.startswith('('):
        expression = expression[1:]
    elif expression.count(')') > expression.count('(') and expression.endswith(')'):
        expression = expression[:-1]

    sanitized = expression.replace(' ', '')
    sanitized = sanitized.replace('x', '*').replace('×', '*')
    sanitized = re.sub(r'/([a-zA-Z]+)', '', sanitized)
    sanitized = re.sub(r'[^\d.()+\-*/=]', '', sanitized)
    return sanitized

def evaluate_equations(eq_dict: dict, sol_dict: dict):
    """
    Evaluates extracted equations and returns a more detailed dictionary for
    building clearer explanations.
    """
    for key, eq_str in eq_dict.items():
        if not eq_str or "=" not in eq_str:
            continue
        try:
            sanitized_eq = sanitize_equation_string(eq_str)

            if not sanitized_eq or "=" not in sanitized_eq:
                continue

            lhs, rhs_str = sanitized_eq.split('=', 1)

            if not lhs or not rhs_str:
                continue

            lhs_val = eval(lhs, {"__builtins__": None}, {})
            rhs_val = eval(rhs_str, {"__builtins__": None}, {})

            if not math.isclose(lhs_val, rhs_val, rel_tol=1e-2):
                correct_rhs_val = round(lhs_val, 4)
                correct_rhs_str = f"{correct_rhs_val:.4f}".rstrip('0').rstrip('.')

         
                return {
                    "error": True,
                    "line_key": key,
                    "line_text": sol_dict.get(key, "N/A"),
                    "original_flawed_calc": eq_str, # The raw model output
                    "sanitized_lhs": lhs,           # The clean left side
                    "original_rhs": rhs_str,        # The clean right side
                    "correct_rhs": correct_rhs_str, # The correct right side
                }
        except Exception:
            continue

    return {"error": False}

# --- Prompts ---
EXTRACTOR_SYSTEM_PROMPT = \
"""[ROLE]
You are an expert at parsing mathematical solutions.

[TASK]
You are given a single line from a mathematical solution. Your task is to extract the calculation from this line.

**This is a literal transcription task. Follow these rules with extreme precision:**
- **RULE 1: Transcribe EXACTLY.** Do not correct mathematical errors. If a line implies `2+2=5`, your output for that line must be `2+2=5`.
- **RULE 2: Isolate the Equation.** Your output must contain ONLY the equation, with no surrounding text, units, or currency symbols. Always use `*` for multiplication.

[RESPONSE FORMAT]
Your response must ONLY contain the extracted equation, wrapped in <eq> and </eq> tags.
If the line contains no calculation, respond with empty tags: <eq></eq>.
"""
CLASSIFIER_SYSTEM_PROMPT = \
"""You are a mathematics tutor.
You will be given a math word problem and a solution written by a student.
Carefully analyze the problem and solution LINE-BY-LINE and determine whether there are any errors in the solution."""


        
gemma_model = None
gemma_tokenizer = None
classifier_model = None
classifier_tokenizer = None

def load_model():
    """Load your trained model here"""
    global gemma_model, gemma_tokenizer, classifier_model, classifier_tokenizer
    
    try:
        device = DEVICE

        # --- Model 1: Equation Extractor (Gemma-3 with Unsloth) ---
        extractor_adapter_repo = "arvindsuresh-math/gemma-3-1b-equation-line-extractor-aug-10"
        base_gemma_model = "unsloth/gemma-3-1b-it-unsloth-bnb-4bit"

        gemma_model, gemma_tokenizer = FastModel.from_pretrained(
            model_name=base_gemma_model,
            max_seq_length=350,
            dtype=None,
            load_in_4bit=True,
        )
        gemma_model = PeftModel.from_pretrained(gemma_model, extractor_adapter_repo)

        # --- Model 2: Conceptual Error Classifier (Phi-4) ---
        classifier_adapter_repo = "arvindsuresh-math/phi-4-error-binary-classifier"
        base_phi_model = "microsoft/Phi-4-mini-instruct"

        DTYPE = torch.float16
        quantization_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=DTYPE
            )
        classifier_backbone_base = AutoModelForCausalLM.from_pretrained(
            base_phi_model,
            quantization_config=quantization_config,
            device_map="auto",
            trust_remote_code=True,
            )

        classifier_tokenizer = AutoTokenizer.from_pretrained(
            base_phi_model,
            trust_remote_code=True
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
        classifier_model = classifier_model.to(torch.float16)

        classifier_model.eval() # Set model to evaluation mode
        
    except Exception as e:
        logger.error(f"Error loading model: {e}")
        return f"Error loading model: {e}"
        
def models_ready() -> bool:
    ready = all(x is not None for x in [
        gemma_model, gemma_tokenizer, classifier_model, classifier_tokenizer
    ])
    if not ready:
        logger.warning(
            "models_ready=False  gemma_model=%s gemma_tok=%s phi_model=%s phi_tok=%s",
            type(gemma_model).__name__ if gemma_model is not None else None,
            type(gemma_tokenizer).__name__ if gemma_tokenizer is not None else None,
            type(classifier_model).__name__ if classifier_model is not None else None,
            type(classifier_tokenizer).__name__ if classifier_tokenizer is not None else None,
        )
    return ready

# Load model on startup
msg = load_model()
logger.info("load_model(): %s", msg)
    
    
# ===================================================================
# PIPELINE COMPONENTS
# ===================================================================

def run_conceptual_check(question: str, solution: str, model, tokenizer) -> dict:
    """
    STAGE 1: Runs the Phi-4 classifier with memory optimizations.
    """
    device = DEVICE
    
    input_text = f"{CLASSIFIER_SYSTEM_PROMPT}\n\n### Problem:\n{question}\n\n### Answer:\n{solution}"
    inputs = tokenizer(
        input_text,
        return_tensors="pt",
        truncation=True,
        max_length=512).to(device)

    # Use inference_mode and disable cache for better performance and memory management
    with torch.inference_mode():
        outputs = model(**inputs, use_cache=False)

     
        logits = outputs["logits"].to(torch.float32)
        probs = torch.softmax(logits, dim=-1).squeeze().tolist()

    is_flawed_prob = probs[1]
    prediction = "flawed" if is_flawed_prob > 0.5 else "correct"

    return {
        "prediction": prediction,
        "probabilities": {"correct": probs[0], "flawed": probs[1]}
    }


def run_computational_check(solution: str, model, tokenizer, batch_size: int = 32) -> dict:
    """
    STAGE 2: Splits a solution into lines and performs a batched computational check.
    (Corrected to handle PEMDAS/parentheses)
    """
    device = DEVICE
    
    lines = [line.strip() for line in solution.strip().split('\n') if line.strip() and "FINAL ANSWER:" not in line.upper()]
    if not lines:
        return {"error": False}

    # Create a batch of prompts, one for each line
    prompts = []
    for line in lines:
        messages = [{"role": "user", "content": f"{EXTRACTOR_SYSTEM_PROMPT}\n\n### Solution Line:\n{line}"}]
        prompts.append(tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True))

    # Run batched inference
    tokenizer.padding_side = "left"
    inputs = tokenizer(prompts, return_tensors="pt", padding=True).to(device)
    tokenizer.padding_side = "left"
    outputs = model.generate(**inputs, max_new_tokens=64, use_cache=True, pad_token_id=tokenizer.pad_token_id)
    tokenizer.padding_side = "left"
    decoded_outputs = tokenizer.batch_decode(outputs[:, inputs.input_ids.shape[1]:], skip_special_tokens=True)

    # Evaluate each line's extracted equation
    for i, raw_output in enumerate(decoded_outputs):
        equation = extract_equation_from_response(raw_output)
        if not equation or "=" not in equation:
            continue

        try:
            # Sanitize the full equation string, preserving parentheses
            sanitized_eq = sanitize_equation_string(equation)
            if "=" not in sanitized_eq:
                continue

            lhs, rhs_str = sanitized_eq.split('=', 1)

            # Evaluate the sanitized LHS, which now correctly includes parentheses
            lhs_val = eval(lhs, {"__builtins__": None}, {})

            # Compare with the RHS
            if not math.isclose(lhs_val, float(rhs_str), rel_tol=1e-2):
                return {
                    "error": True,
                    "line_text": lines[i],
                    "correct_calc": f"{lhs} = {round(lhs_val, 4)}"
                }
        except Exception:
            continue # Skip lines where evaluation fails

    return {"error": False}


def analyze_solution(question: str, solution: str):
    """
    Main orchestrator that runs the full pipeline and generates the final explanation.
    """
    # STAGE 1: Conceptual Check 
    conceptual_result = run_conceptual_check(question, solution, classifier_model, classifier_tokenizer)
    confidence = conceptual_result['probabilities'][conceptual_result['prediction']]

    # STAGE 2: Computational Check 
    computational_result = run_computational_check(solution, gemma_model, gemma_tokenizer)

    # FINAL VERDICT LOGIC
    if computational_result["error"]:
        classification = "computational_error"
        explanation = (
            f"A calculation error was found.\n"
            f"On the line: \"{computational_result['line_text']}\"\n"
            f"The correct calculation should be: {computational_result['correct_calc']}"
        )
    else:
        # If calculations are fine, the final verdict is the conceptual one.
        if conceptual_result['prediction'] == 'correct':
            classification = 'correct'
            explanation = "All calculations are correct and the overall logic appears to be sound."
        else: # This now correctly corresponds to 'flawed'
            classification = 'conceptual_error' # Produce the user-facing label
            explanation = "All calculations are correct, but there appears to be a conceptual error in the logic or setup of the solution."
    final_verdict = {
        "classification": classification,
        "explanation": explanation
    }

    return final_verdict    
     
def classify_solution_stream(question: str, solution: str):
    """
    Streams (classification, explanation, status_markdown)
    Status shows a growing checklist:
      ⏳ Stage 1 ...
      ✅ Stage 1 ... done
      ⏳ Stage 2 ...
      ✅ / 🟥 Stage 2 ... result
    """
    def render(log_lines):
        # join as a bulleted list
        return "\n".join(f"- {line}" for line in log_lines) or "*(idle)*"

    log = []

    
    if not question.strip() or not solution.strip():
        log.append("⚠️ Provide a question and a solution.")
        yield "Please fill in both fields", "", render(log)
        return

    
    if not models_ready():
        log.append("⏳ Loading models…")
        yield "⏳ Working…", "", render(log)
        msg = load_model()
        if not models_ready():
            log[-1] = f"🟥 Failed to load models — {msg}"
            yield "Models not loaded", "", render(log)
            return
        log[-1] = "✅ Models loaded."
    
    verdicts_mapping = {"correct": "Correct.", "conceptual_error": "Conceptually flawed.", "computational_error": "Computationally flawed."}

    try:
        # ---------- Stage 1: Conceptual ----------
        log.append("⏳ **Stage 1: Initial check**")
        yield "⏳ Working…", "Starting initial check…", render(log)
        conceptual = run_conceptual_check(question, solution, classifier_model, classifier_tokenizer)
        pred = conceptual["prediction"]
        conf = conceptual["probabilities"][pred]
        if pred == "flawed":   
            log[-1] = f"🟥 **Stage 1: Initial check** — (Complete) — prediction: **{pred}** (p={conf:.2%})"
        elif pred == "correct":
            log[-1] = f"✅ **Stage 1: Initial check** — (Complete) — prediction: **{pred}** (p={conf:.2%})"
            
        yield "⏳ Working…", f"Stage 1: {pred} (p={conf:.2%}). Now checking calculations…", render(log)

        # ---------- Stage 2: Computational ----------
        log.append("⏳ **Stage 2: Computational check**")
        yield "⏳ Working…", "Extracting and checking computations…", render(log)

        computational = run_computational_check(solution, gemma_model, gemma_tokenizer)

        # ---------- Final verdict ----------
        if computational["error"]:
            # mark stage 2 as failed
            line_txt = computational["line_text"]
            corr = computational["correct_calc"]
            log[-1] = f"🟥 **Stage 2: Computational check** — (Completed; error found) — — error on line “{line_txt}” (correct: `{corr}`)"
            classification = "computational_error"
            explanation = (
                "A calculation error was found.\n"
                f'On the line: "{line_txt}"\n'
                f"The correct calculation should be: {corr}"
            )
        else:
            log[-1] = "✅ **Stage 2: Computational check** — (Complete) — no arithmetic issues found."
            if pred == "correct":
                classification = "correct"
                explanation = "All calculations are correct and the overall logic appears to be sound."
            else:
                classification = "conceptual_error"
                explanation = (
                    "All calculations are correct, but there appears to be a conceptual error "
                    "in the logic or setup of the solution."
                )
        classification = verdicts_mapping[classification]
        # final yield updates both result fields + the complete checklist
        yield classification, explanation, render(log)

    except Exception as e:
        logger.exception("inference failed")
        log.append(f"🟥 Exception during inference: **{type(e).__name__}** — {e}")
        yield "Runtime error", f"{type(e).__name__}: {e}", render(log)


        # ---------------- UI: streaming ----------------
with gr.Blocks(title="Math Solution Classifier", theme=gr.themes.Soft()) as app:
    gr.Markdown("# 🧮 Math Solution Classifier")
    gr.Markdown(
        "Classify math solutions as **correct**, **conceptually flawed**, or **computationally flawed**. "
        "Live status updates appear below as the two-stage pipeline runs."
    )

    with gr.Row():
        # -------- Left: inputs --------
        with gr.Column(scale=1):
            question_input = gr.Textbox(
                label="Math Question",
                placeholder="e.g., What is 15 divided by 3?",
                lines=3,
            )
            solution_input = gr.Textbox(
                label="Proposed Solution",
                placeholder="e.g.,15/3 = 7",
                lines=8,
            )
            with gr.Row():
                classify_btn = gr.Button("Classify Solution", variant="primary")
                clear_btn = gr.Button("Clear")

        # -------- Right: outputs --------
        with gr.Column(scale=1):
            classification_output = gr.Textbox(label="Classification", interactive=False)
            explanation_output   = gr.Textbox(label="Explanation",   interactive=False, lines=6)
            status_output        = gr.Markdown(value="*(idle)*")  # live stage updates

    # -------- Examples --------
    
    
import csv, random
from typing import Dict, Optional, List, Tuple

# ---------- Data structures ----------
class QAItem:
    __slots__ = ("id", "question", "correct", "wrong", "error_type")
    def __init__(self, id: int, question: str,
                 correct: Optional[str], wrong: Optional[str], error_type: Optional[str]):
        self.id = id
        self.question = question
        self.correct = correct or None
        self.wrong = wrong or None
        self.error_type = (error_type or "").strip() or None  # e.g., "computational_error" / "conceptual_error"

# ---------- CSV loader ----------
def load_examples_csv(path: str) -> Dict[int, QAItem]:
    """
    Loads CSV and returns a dict: {question_id: QAItem}
    Accepts either 1 row per question (both solutions present) or 2 rows merged by `index`.
    """
    def norm(s: Optional[str]) -> str:
        return (s or "").strip()

    pool: Dict[int, QAItem] = {}
    with open(path, "r", encoding="utf-8") as f:
        rdr = csv.DictReader(f)
        # normalize headers
        fieldmap = {k: k.strip().lower() for k in rdr.fieldnames or []}
        rows = []
        for row in rdr:
            r = {fieldmap.get(k, k).lower(): v for k, v in row.items()}
            rows.append(r)

    for r in rows:
        try:
            qid = int(norm(r.get("index")))
        except Exception:
            # skip bad index rows
            continue

        q = norm(r.get("question"))
        ca = norm(r.get("correct_answer"))
        wa = norm(r.get("wrong_answer"))
        et = norm(r.get("error_type"))

        if qid not in pool:
            pool[qid] = QAItem(qid, q, ca, wa, et)
        else:
            # merge if the CSV has multiple rows per id
            item = pool[qid]
            if not item.question and q:
                item.question = q
            if ca and not item.correct:
                item.correct = ca
            if wa and not item.wrong:
                item.wrong = wa
            if et and not item.error_type:
                item.error_type = et

    # drop questions that have neither solution
    pool = {k: v for k, v in pool.items() if (v.correct or v.wrong)}
    return pool

# ---------- Selection state with balance ----------
class ExampleSelector:
    """
    Keeps one solution per question, balances correct vs wrong across picks,
    and supports label filtering.
    """
    def __init__(self, pool: Dict[int, QAItem], seed: Optional[int] = None):
        self.pool = pool
        self._rng = random.Random(seed)
        self.reset()

    def reset(self):
        self.ids: List[int] = list(self.pool.keys())
        self._rng.shuffle(self.ids)
        self.cursor: int = 0
        self.seen_ids: set[int] = set()
        self.balance = {"correct": 0, "wrong": 0}

    # ---- public API ----
    def next_batch(self, k: int, filter_label: str = "any") -> List[Dict]:
        """Return up to k rows (id, question, solution, label), updating internal state."""
        out: List[Dict] = []
        # iterate over id list cyclically until filled or exhausted
        tried = 0
        max_tries = len(self.ids) * 2  # guard
        while len(out) < k and tried < max_tries:
            if self.cursor >= len(self.ids):
                break
            qid = self.ids[self.cursor]
            self.cursor += 1
            tried += 1

            if qid in self.seen_ids:
                continue

            item = self.pool[qid]
            variant = self._choose_variant(item, filter_label)
            if variant is None:
                continue  # no variant matches filter

            row = self._build_row(item, variant)
            out.append(row)
            self._mark_used(item, variant)
        return out

    def surprise(self, filter_label: str = "any") -> Optional[Dict]:
        """Pick a single row at random (respecting filter & balance)."""
        candidates = [qid for qid in self.ids if qid not in self.seen_ids and self._variant_available(self.pool[qid], filter_label)]
        if not candidates:
            return None
        qid = self._rng.choice(candidates)
        item = self.pool[qid]
        variant = self._choose_variant(item, filter_label)
        if variant is None:
            return None
        row = self._build_row(item, variant)
        self._mark_used(item, variant)
        return row

    # ---- helpers ----
    def _variant_available(self, item: QAItem, filter_label: str) -> bool:
        return self._choose_variant(item, filter_label, dry_run=True) is not None

    def _choose_variant(self, item: QAItem, filter_label: str, dry_run: bool = False) -> Optional[str]:
        """
        Returns 'correct' or 'wrong' or None given availability, filter, and current balance.
        filter_label ∈ {"any","correct","wrong","computational_error","conceptual_error"}
        """
        has_correct = bool(item.correct)
        has_wrong = bool(item.wrong)

        want_correct = (filter_label == "correct")
        want_wrong   = (filter_label == "wrong") or (filter_label in ("computational_error", "conceptual_error"))

        # Build allowed set based on filter
        allowed = []
        if filter_label == "any":
            if has_correct: allowed.append("correct")
            if has_wrong:   allowed.append("wrong")
        elif want_correct:
            if has_correct: allowed.append("correct")
        elif want_wrong:
            if has_wrong and (filter_label in ("wrong", "any") or (item.error_type == filter_label)):
                allowed.append("wrong")

        if not allowed:
            return None

        if len(allowed) == 1:
            return allowed[0]

        # Balance correct vs wrong across already-shown items
        c, w = self.balance["correct"], self.balance["wrong"]
        if c > w and "wrong" in allowed:
            return "wrong"
        if w > c and "correct" in allowed:
            return "correct"
        # tie-breaker: prefer wrong when specifically filtering to an error type
        if filter_label in ("computational_error", "conceptual_error") and "wrong" in allowed:
            return "wrong"
        return self._rng.choice(allowed)

    def _build_row(self, item: QAItem, variant: str) -> Dict:
        if variant == "correct":
            label = "correct"
            sol = item.correct
        else:
            label = item.error_type or "wrong"
            sol = item.wrong
        return {
            "id": item.id,
            "question": item.question,
            "solution": sol,
            "label": label,  # "correct" | "computational_error" | "conceptual_error" | "wrong"
        }

    def _mark_used(self, item: QAItem, variant: str):
        # we mark the whole question as used so we never show both solutions
        self.seen_ids.add(item.id)
        if variant == "correct":
            self.balance["correct"] += 1
        else:
            self.balance["wrong"] += 1

# ===== CSV hookup =====
from pathlib import Path
import time

CSV_PATH = Path(__file__).resolve().parent / "final-test-with-wrong-answers.csv"
POOL = load_examples_csv(str(CSV_PATH))

def new_selector(seed: int | None = None):
    
    return ExampleSelector(POOL, seed=seed or int(time.time()) & 0xFFFF)


def _truncate(s: str, n: int = 100) -> str:
    s = s or ""
    return s if len(s) <= n else s[: n - 1] + "…"

def _rows_to_table(rows: list[dict]) -> list[list[str]]:
    # Dataframe value: list of rows [ID, Label, Question, Solution]
    table = []
    for r in rows:
        table.append([
            str(r["id"]),
            r["label"],
            _truncate(r["question"], 120),
            _truncate(r["solution"], 120),
        ])
    return table


def ui_surprise(selector, filter_label="any"):
    """Pick one example and push it straight to inputs; persist selector state."""
    if selector is None or not POOL:
        return selector, gr.update(), gr.update()
    r = selector.surprise(filter_label=filter_label)
    if not r:
        return selector, gr.update(), gr.update()
    return selector, r["question"], r["solution"]
    
def _clear_all():
    return (
        "",           # question_input
        "",           # solution_input
        "",           # expected_label_example (hidden)
        "",           # classification_output
        "",           # explanation_output
        "*(idle)*",   # status_output (Markdown)
    )

components_to_clear = [
    question_input,
    solution_input,
]


with gr.Blocks(title="Math Solution Classifier", theme=gr.themes.Soft()) as app:
    gr.Markdown("# 🧮 Math Solution Classifier")
    gr.Markdown(
        "Classify math solutions as **correct**, **conceptually flawed**, or **computationally flawed**. "
        "Live status updates appear below as the two-stage pipeline runs. "
        " \n Press 'Surprise me' to randomly select a sample question/answer pair from our dataset."
    )

    
    selector_state = gr.State(new_selector())

    with gr.Row():
        # -------- Left: inputs --------
        with gr.Column(scale=1):
            question_input = gr.Textbox(
                label="Math Question",
                placeholder="e.g., What is 14 divided by 2?",
                lines=3,
            )
            solution_input = gr.Textbox(
                label="Proposed Solution",
                placeholder="e.g., 14/2 = 9",
                lines=8,
            )
            expected_label_example = gr.Textbox(
                label="Expected Label",
                visible=False
            )
            with gr.Row():
                classify_btn = gr.Button("Classify Solution", variant="primary")
                surprise_btn = gr.Button("Surprise me")   
                clear_btn    = clear_btn = gr.Button("Clear")

        # -------- Right: outputs --------
        with gr.Column(scale=1):
            classification_output = gr.Textbox(label="Classification", interactive=False)
            explanation_output   = gr.Textbox(label="Explanation",   interactive=False, lines=6)
            status_output        = gr.Markdown(value="*(idle)*")  # live stage updates

    # -------- Curated starter examples --------
    gr.Examples(
        examples=[
                ["John has three apples and Mary has seven, how many apples do they have together?",
             "They have 7 + 3 = 11 apples.\n Final answer: 11",
             "Computationally flawed"],
        ["A rectangle's length is twice its width. If the width is 7 cm, what is the perimeter of the rectangle?",
        "The length of the rectangle is 2 * 7 = 14 cm.\n The perimeter is 14 + 7 = 21 cm.\n Final answer: 21",
        "Conceptually flawed"],
        ["A baker is making a large cake with three layers. Each layer is a cylinder with a height of 8 cm. The bottom layer has a radius of 20 cm, the middle layer has a radius of 15 cm, and the top layer has a radius of 10 cm. The baker needs to cover the exposed top and side surfaces of the stacked cake with frosting. What is the total surface area to be frosted in square centimeters? Use pi = 3.14.",
"The lateral area of the bottom layer is 2 * 3.14 * 20 * 8 = 1004.8.\n The lateral area of the middle layer is 2 * 3.14 * 15 * 8 = 753.6.\n The lateral area of the top layer is 2 * 3.14 * 10 * 8 = 502.4.\n The exposed top surface is the area of the smallest circle: 3.14 * (10*10) = 314.\n The total frosted area is 1004.8 + 753.6 + 502.4 + 314 = 2888.8 sq cm.\n FINAL ANSWER: 2888.8",
"Computationally flawed"],
            ["What is 15% of 200?",
             "15% = 15/100 = 0.15\n0.15 × 200 = 30\n Final answer: 30",
             "Correct"],
             ["A circle has a radius of 5 cm. Using the approximation pi = 3.14, what is the circumference of the circle?",
             "The circumference of the circle is 3.14 * 5 = 15.7 cm.\n Final answer: 15.7",
             "Conceptually flawed"],
             ["A library is building new shelves. Each shelf is 1.2 meters long. A standard book is 3 cm thick, and a large book is 5 cm thick. A shelf must hold 20 standard books and 10 large books. After filling a shelf with these books, how much space, in centimeters, is left on the shelf?",
             "The shelf length in centimeters is 1.2 * 100 = 120 cm.\n The space taken by standard books is 20 * 3 = 60 cm.\n The space taken by large books is 10 * 5 = 50 cm.\n The total space taken is 60 + 50 = 110 cm.\n The remaining space is 120 + 110 = 230 cm.\n FINAL ANSWER: 230",
             "Conceptually flawed"],
             ["A 24-meter rope is cut into 6 equal pieces. A climber uses 2 of those pieces. How many meters of rope are still unused?",
             "The length of each piece is 24 / 6 = 4 m.\n The climber uses 2 × 4 m = 8 m of rope.\n There are 24 m − 8 m = 16 m of rope still unused.\n Final answer: 16",
             "Correct"]
        ],
        inputs=[question_input, solution_input, expected_label_example],
    )
    

    # ---------- Wiring ----------
    # Main classify
    classify_btn.click(
        fn=classify_solution_stream,
        inputs=[question_input, solution_input],
        outputs=[classification_output, explanation_output, status_output],
        show_progress=False,
        concurrency_limit=1,
    )

    surprise_btn.click(
        fn=ui_surprise,
        inputs=[selector_state],                              
        outputs=[selector_state, question_input, solution_input],  
        queue=True,
    )
    clear_btn.click(
    fn=_clear_all,
    inputs=[],
    outputs=[
        question_input,
        solution_input,
        expected_label_example,
        classification_output,
        explanation_output,
        status_output,
    ],
)


app.queue()

if __name__ == "__main__":
    app.launch()

    
