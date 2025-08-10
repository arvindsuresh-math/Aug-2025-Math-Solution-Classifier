```python
# Cell 1: Installations
!pip install -U transformers==4.53.2
!pip install -U accelerate
!pip install -U bitsandbytes

!pip install flash-attn==2.7.4.post1 \
  --extra-index-url https://download.pytorch.org/whl/cu124 \
  --no-build-isolation
```

```python
!pip install --no-deps bitsandbytes accelerate xformers==0.0.29.post3 peft trl triton unsloth_zoo
!pip install sentencepiece protobuf "datasets>=3.4.1,<4.0.0" "huggingface_hub>=0.34.0" hf_transfer
!pip install --no-deps unsloth
```

```python
import unsloth
from unsloth import FastModel
import torch
import torch.nn as nn
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel
from huggingface_hub import hf_hub_download
import json
import re
import math

print("✅ All modules imported.")
```

    🦥 Unsloth: Will patch your computer to enable 2x faster free finetuning.
    🦥 Unsloth Zoo will now patch everything to make training faster!
    ✅ All modules imported.



```python
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
```


```python
# ===================================================================
# 2. LOAD MODELS AND TOKENIZERS
# ===================================================================
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# --- Model 1: Equation Extractor (Gemma-3 with Unsloth) ---
print("\nLoading Equation Extraction Model...")
extractor_adapter_repo = "arvindsuresh-math/gemma-3-1b-equation-extractor-lora"
base_gemma_model = "unsloth/gemma-3-1b-it-unsloth-bnb-4bit"

gemma_model, gemma_tokenizer = FastModel.from_pretrained(
    model_name=base_gemma_model,
    max_seq_length=2048,
    dtype=None,
    load_in_4bit=True,
)
gemma_model = PeftModel.from_pretrained(gemma_model, extractor_adapter_repo)
print("✅ Equation Extraction Model loaded.")


# --- Model 2: Conceptual Error Classifier (Phi-4) ---
print("\nLoading Conceptual Error Classifier Model...")
classifier_adapter_repo = "arvindsuresh-math/phi-4-error-binary-classifier"
base_phi_model = "microsoft/Phi-4-mini-instruct"

DTYPE = torch.bfloat16
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
classifier_model = classifier_model.to(torch.bfloat16)

classifier_model.eval() # Set model to evaluation mode
print("✅ Conceptual Error Classifier Model loaded.")
```

    Using device: cuda
    
    Loading Equation Extraction Model...
    ==((====))==  Unsloth 2025.8.4: Fast Gemma3 patching. Transformers: 4.53.2.
       \\   /|    NVIDIA A100-SXM4-40GB. Num GPUs = 1. Max memory: 39.557 GB. Platform: Linux.
    O^O/ \_/ \    Torch: 2.6.0+cu124. CUDA: 8.0. CUDA Toolkit: 12.4. Triton: 3.2.0
    \        /    Bfloat16 = TRUE. FA [Xformers = 0.0.29.post3. FA2 = True]
     "-____-"     Free license: http://github.com/unslothai/unsloth
    Unsloth: Fast downloading is enabled - ignore downloading bars which are red colored!


    <string>:36: UserWarning: You passed `quantization_config` or equivalent parameters to `from_pretrained` but the model you're loading already has a `quantization_config` attribute. The `quantization_config` from the model will be used.


    ✅ Equation Extraction Model loaded.
    
    Loading Conceptual Error Classifier Model...



    Loading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]


    ✅ Conceptual Error Classifier Model loaded.



```python
# --- Prompts ---

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
```


```python
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

                # Return a more detailed dictionary for better explanations
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

def extract_json_from_response(response: str) -> dict:
    """
    (Bulletproof Version)
    Manually parses the model's output using regex instead of relying on
    perfectly-formed JSON. This is robust to syntax errors from the LLM.
    """
    # Regex to find all keys like "L1", "L2", "FA", etc.
    keys = re.findall(r'"(L\d+|FA)"\s*:', response)

    # Regex to find all values associated with the keys.
    # It looks for text enclosed in double quotes.
    values = re.findall(r':\s*"([^"]*)"', response)

    # If the number of keys and values doesn't match, something is very wrong.
    # This is a safety check.
    if len(keys) != len(values):
        # Fallback for cases where the format is extremely broken
        if not keys and not values:
            return {} # Truly empty
        # Try to at least salvage something if possible
        min_len = min(len(keys), len(values))
        return dict(zip(keys[:min_len], values[:min_len]))

    # Combine the extracted keys and values into a dictionary
    return dict(zip(keys, values))

# def extract_json_from_response(response: str) -> dict:
#     match = re.search(r'```json\s*(\{.*?\})\s*```', response, re.DOTALL)
#     json_str = match.group(1) if match else re.search(r'(\{.*?\})', response, re.DOTALL)
#     if not json_str: return {}
#     try:
#         return json.loads(json_str.group(0) if hasattr(json_str, 'group') else json_str)
#     except (json.JSONDecodeError, AttributeError): return {}
```


```python
def test_analysis_pipeline(math_question, proposed_solution):
    """
    Notebook version of the analysis pipeline for testing.
    Prints progress and returns a final dictionary.
    """
    print("-" * 50)
    print(f"Testing problem: {math_question[:50]}...")

    # --- STAGE 1: COMPUTATIONAL CHECK ---
    print("Step 1: Extracting equations...")
    solution_json_str = format_solution_into_json_str(proposed_solution)
    messages = [{"role": "user", "content": f"{EXTRACTOR_SYSTEM_PROMPT}\n\n### Solution:\n{solution_json_str}"}]
    prompt = gemma_tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

    inputs = gemma_tokenizer([prompt], return_tensors="pt").to(device)
    outputs = gemma_model.generate(**inputs, max_new_tokens=300, use_cache=True)
    extracted_text = gemma_tokenizer.batch_decode(outputs[:, inputs.input_ids.shape[1]:], skip_special_tokens=True)[0]
    extracted_eq_dict = extract_json_from_response(extracted_text)
    print(f"  > Extracted equations: {json.dumps(extracted_eq_dict)}")

    computational_error = evaluate_equations(extracted_eq_dict, json.loads(solution_json_str))

    if computational_error["error"]:
        explanation = (
            f"A computational error was found.\n"
            f"On line: \"{computational_error['line_text']}\"\n"
            f"The calculation was: {computational_error['flawed_calc']}\n"
            f"The correct calculation should be: {computational_error['correct_calc']}"
        )
        return {"classification": "Computational Error", "confidence": "100%", "explanation": explanation}

    # --- STAGE 2: CONCEPTUAL CHECK ---
    print("\nStep 2: Checking for conceptual errors...")
    input_text = f"{CLASSIFIER_SYSTEM_PROMPT}\n\n### Problem:\n{math_question}\n\n### Answer:\n{proposed_solution}"
    inputs = classifier_tokenizer(input_text, return_tensors="pt", truncation=True, max_length=512).to(device)

    with torch.no_grad():
        outputs = classifier_model(**inputs)
        logits = outputs["logits"]
        probs = torch.softmax(logits, dim=-1).squeeze().tolist()
        print(f"  > Raw probabilities [Correct, Flawed]: {probs}")

    is_flawed_prob = probs[1]
    is_correct_prob = probs[0]

    if is_flawed_prob > 0.5:
        return {"classification": "Conceptual Error", "confidence": f"{is_flawed_prob:.2%}", "explanation": "Logic or setup appears to have a conceptual error."}
    else:
        return {"classification": "Correct", "confidence": f"{is_correct_prob:.2%}", "explanation": "Solution appears correct."}
```


```python
def debug_analysis_pipeline(math_question, proposed_solution):
    """
    (Complete, Refactored Version)
    Orchestrates the pipeline by calling helper functions and printing the
    inputs/outputs at each stage for clear debugging.
    """
    print("="*80)
    print(f"🕵️  STARTING DEBUG FOR: {math_question[:60]}...")
    print("="*80)

    # ===================================================================
    # --- STAGE 1: COMPUTATIONAL CHECK (GEMMA MODEL) ---
    # ===================================================================
    stage1_start_time = time.monotonic()
    print("\n--- STAGE 1: Equation Extraction (Gemma) ---")

    # [1.1] Format the solution
    print("\n[1.1] Calling format_solution_into_json_str...")
    solution_json_str = format_solution_into_json_str(proposed_solution)
    solution_dict = json.loads(solution_json_str)
    print("  > Output:")
    print(solution_json_str)

    # [1.2] Build the message list using the new helper function
    print("\n[1.2] Calling create_extractor_messages...")
    messages = create_extractor_messages(solution_json_str)
    print(f"  > Output: Generated a list of {len(messages)} messages.")

    # [1.3] Apply the chat template to create the full prompt string
    prompt = gemma_tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    print("\n[1.3] Full Prompt for Gemma Model (with few-shot examples):")
    print("--------------------")
    print(prompt)
    print("--------------------")

    # [1.4] Run inference with the Gemma model
    inputs = gemma_tokenizer([prompt], return_tensors="pt").to(device)
    outputs = gemma_model.generate(**inputs, max_new_tokens=300, use_cache=True)
    extracted_text = gemma_tokenizer.batch_decode(outputs[:, inputs.input_ids.shape[1]:], skip_special_tokens=True)[0]

    print("\n[1.4] Raw Text Output from Gemma Model:")
    print("--------------------")
    print(extracted_text)
    print("--------------------")

    # [1.5] Parse the raw text using the robust regex-based function
    print("\n[1.5] Calling extract_json_from_response...")
    extracted_eq_dict = extract_json_from_response(extracted_text)
    print("  > Output (Parsed JSON dict):")
    print(json.dumps(extracted_eq_dict, indent=2))

    # [1.6] Filter out equations for lines that contain no digits
    print("\n[1.6] Filtering out equations for non-numeric lines:")
    final_eq_to_eval = {}
    for key, eq_str in extracted_eq_dict.items():
        original_line = solution_dict.get(key, "")
        if any(char.isdigit() for char in original_line):
            final_eq_to_eval[key] = eq_str
        else:
            print(f"  > Line '{key}' has no digits. Discarding extracted equation: '{eq_str}'")
    print("  > Final equations to be evaluated:", json.dumps(final_eq_to_eval, indent=2))

    # [1.7] Evaluate the final, filtered set of equations
    print("\n[1.7] Calling evaluate_equations...")
    computational_error = evaluate_equations(final_eq_to_eval, solution_dict)
    stage1_end_time = time.monotonic()
    print(f"  > Output (Latency: {stage1_end_time - stage1_start_time:.2f}s):")
    print(f"  > {computational_error}")

    # [1.8] Check the result and exit if a computational error was found
    if computational_error["error"]:
        print("\n  > 🔴 Error Found!")
        lhs, rhs, correct_rhs = computational_error['sanitized_lhs'], computational_error['original_rhs'], computational_error['correct_rhs']
        explanation = f"A computational error was found.\nOn line: \"{computational_error['line_text']}\"\nThe student wrote '{lhs} = {rhs}', but the correct result of '{lhs}' is {correct_rhs}."
        final_result = {"classification": "Computational Error", "confidence": "100%", "explanation": explanation}
        print("\n" + "="*80)
        print(f"🏁 FINAL RESULT: {final_result['classification']}")
        print("="*80 + "\n\n")
        return final_result
    else:
        print("\n  > ✅ All calculations are correct. Proceeding to Stage 2.")

    # ===================================================================
    # --- STAGE 2: CONCEPTUAL CHECK (PHI-4 MODEL) ---
    # ===================================================================
    stage2_start_time = time.monotonic()
    print("\n\n--- STAGE 2: Conceptual Check (Phi-4) ---")

    # [2.1] Create the prompt for the Phi-4 model
    input_text = f"{CLASSIFIER_SYSTEM_PROMPT}\n\n### Problem:\n{math_question}\n\n### Answer:\n{proposed_solution}"
    print("\n[2.1] Full Prompt for Phi-4 Model:")
    print("--------------------")
    print(input_text)
    print("--------------------")

    # [2.2] Run inference with the Phi-4 model
    inputs = classifier_tokenizer(input_text, return_tensors="pt", truncation=True, max_length=512).to(device)
    with torch.no_grad():
        outputs = classifier_model(**inputs)
        logits = outputs["logits"]
        probs = torch.softmax(logits, dim=-1).squeeze().tolist()

    # [2.3] Display the model's raw outputs
    print(f"\n[2.3] Raw Logits from Phi-4 Model: {logits.to(torch.float32).cpu().numpy()}")
    print(f"\n[2.4] Softmax Probabilities [Correct, Flawed]: {probs}")

    # [2.5] Determine the final classification based on the probabilities
    stage2_end_time = time.monotonic()
    print(f"\n[2.5] Final Decision Logic (Latency: {stage2_end_time - stage2_start_time:.2f}s):")

    is_flawed_prob = probs[1]
    is_correct_prob = probs[0]

    if is_flawed_prob > 0.5:
        print(f"  > Flawed probability ({is_flawed_prob:.2%}) is > 50%.")
        final_result = {"classification": "Conceptual Error", "confidence": f"{is_flawed_prob:.2%}", "explanation": "Logic or setup appears to have a conceptual error."}
    else:
        print(f"  > Correct probability ({is_correct_prob:.2%}) is > 50%.")
        final_result = {"classification": "Correct", "confidence": f"{is_correct_prob:.2%}", "explanation": "Solution appears correct."}

    print("\n" + "="*80)
    print(f"🏁 FINAL RESULT: {final_result['classification']}")
    print("="*80 + "\n\n")
    return final_result
```


```python
test_cases = [
    {
        "name": "Computational Error",
        "question": "John has three apples and Mary has seven, how many apples do they have together?",
        "solution": "They have 7 + 3 = 11 apples.\nFINAL ANSWER: 11"
    },
    {
        "name": "Correct Solution",
        "question": "A grocery store sells apples for $0.50 each and oranges for $0.75 each. If a customer buys 10 apples and 5 oranges, what is the total cost?",
        "solution": "Apple cost: 10 * 0.50 = 5.00\nOrange cost: 5 * 0.75 = 3.75\nTotal cost: 5.00 + 3.75 = 8.75\nFINAL ANSWER: 8.75"
    },
    {
        "name": "Conceptual Error",
        "question": "A car travels at 60 miles per hour. How long will it take to travel 180 miles?",
        "solution": "Time = Speed / Distance\nTime = 60 / 180 = 0.33 hours\nFINAL ANSWER: 0.33"
    }
]

for test in test_cases:
    result = debug_analysis_pipeline(test["question"], test["solution"])
    print("\n--- FINAL RESULT ---")
    print(f"Case: {test['name']}")
    print(f"Classification: {result['classification']}")
    print(f"Confidence: {result['confidence']}")
    print(f"Explanation: {result['explanation']}")
    print("="*50 + "\n")
```

    ================================================================================
    🕵️  STARTING DEBUG FOR: John has three apples and Mary has seven, how many apples do...
    ================================================================================
    
    --- STAGE 1: Equation Extraction (Gemma) ---
    
    [1.1] Calling format_solution_into_json_str...
      > Output:
    {
      "L1": "They have 7 + 3 = 11 apples.",
      "FA": "11"
    }
    
    [1.2] Calling create_extractor_messages...
      > Output: Generated a list of 5 messages.
    
    [1.3] Full Prompt for Gemma Model (with few-shot examples):
    --------------------
    <bos><start_of_turn>user
    [ROLE]
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
    
    
    ### Solution:
    {
      "L1": "2% of $90 is (2/100)*$90 = $1.8",
      "L2": "2% of $60 is (2/100)*$60 = $1.2",
      "L3": "The second transaction was reversed without the service charge so only a total of $90+$1.8+$1.2 = $39 was deducted from his account",
      "L4": "He will have a balance of $400-$39 = $361",
      "FA": "361"
    }<end_of_turn>
    <start_of_turn>model
    {
      "L1": "(2/100)*90=1.8",
      "L2": "(2/100)*60=1.2",
      "L3": "90+1.8+1.2=39",
      "L4": "400-39=361",
      "FA": ""
    }<end_of_turn>
    <start_of_turn>user
    ### Solution:
    {
      "L1": "She drinks 2 bottles a day and there are 24 bottles in a case so a case will last 24/2 = 12 days",
      "L2": "She needs enough to last her 240 days and 1 case will last her 12 days so she needs 240/12 = 20 cases",
      "L3": "Each case is on sale for $12.00 and she needs 20 cases so that's 12*20 = $240.00",
      "FA": "240"
    }<end_of_turn>
    <start_of_turn>model
    {
      "L1": "24/2=12",
      "L2": "240/12=20",
      "L3": "12*20=240.00",
      "FA": ""
    }<end_of_turn>
    <start_of_turn>user
    ### Solution:
    {
      "L1": "They have 7 + 3 = 11 apples.",
      "FA": "11"
    }<end_of_turn>
    <start_of_turn>model
    
    --------------------
    
    [1.4] Raw Text Output from Gemma Model:
    --------------------
    {
      "L1": "7+3=11",
      "FA": ""
    }
    --------------------
    
    [1.5] Calling extract_json_from_response...
      > Output (Parsed JSON dict):
    {
      "L1": "7+3=11",
      "FA": ""
    }
    
    [1.6] Filtering out equations for non-numeric lines:
      > Final equations to be evaluated: {
      "L1": "7+3=11",
      "FA": ""
    }
    
    [1.7] Calling evaluate_equations...
      > Output (Latency: 3.77s):
      > {'error': True, 'line_key': 'L1', 'line_text': 'They have 7 + 3 = 11 apples.', 'original_flawed_calc': '7+3=11', 'sanitized_lhs': '7+3', 'original_rhs': '11', 'correct_rhs': '10'}
    
      > 🔴 Error Found!
    
    ================================================================================
    🏁 FINAL RESULT: Computational Error
    ================================================================================
    
    
    
    --- FINAL RESULT ---
    Case: Computational Error
    Classification: Computational Error
    Confidence: 100%
    Explanation: A computational error was found.
    On line: "They have 7 + 3 = 11 apples."
    The student wrote '7+3 = 11', but the correct result of '7+3' is 10.
    ==================================================
    
    ================================================================================
    🕵️  STARTING DEBUG FOR: A grocery store sells apples for $0.50 each and oranges for ...
    ================================================================================
    
    --- STAGE 1: Equation Extraction (Gemma) ---
    
    [1.1] Calling format_solution_into_json_str...
      > Output:
    {
      "L1": "Apple cost: 10 * 0.50 = 5.00",
      "L2": "Orange cost: 5 * 0.75 = 3.75",
      "L3": "Total cost: 5.00 + 3.75 = 8.75",
      "FA": "8.75"
    }
    
    [1.2] Calling create_extractor_messages...
      > Output: Generated a list of 5 messages.
    
    [1.3] Full Prompt for Gemma Model (with few-shot examples):
    --------------------
    <bos><start_of_turn>user
    [ROLE]
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
    
    
    ### Solution:
    {
      "L1": "2% of $90 is (2/100)*$90 = $1.8",
      "L2": "2% of $60 is (2/100)*$60 = $1.2",
      "L3": "The second transaction was reversed without the service charge so only a total of $90+$1.8+$1.2 = $39 was deducted from his account",
      "L4": "He will have a balance of $400-$39 = $361",
      "FA": "361"
    }<end_of_turn>
    <start_of_turn>model
    {
      "L1": "(2/100)*90=1.8",
      "L2": "(2/100)*60=1.2",
      "L3": "90+1.8+1.2=39",
      "L4": "400-39=361",
      "FA": ""
    }<end_of_turn>
    <start_of_turn>user
    ### Solution:
    {
      "L1": "She drinks 2 bottles a day and there are 24 bottles in a case so a case will last 24/2 = 12 days",
      "L2": "She needs enough to last her 240 days and 1 case will last her 12 days so she needs 240/12 = 20 cases",
      "L3": "Each case is on sale for $12.00 and she needs 20 cases so that's 12*20 = $240.00",
      "FA": "240"
    }<end_of_turn>
    <start_of_turn>model
    {
      "L1": "24/2=12",
      "L2": "240/12=20",
      "L3": "12*20=240.00",
      "FA": ""
    }<end_of_turn>
    <start_of_turn>user
    ### Solution:
    {
      "L1": "Apple cost: 10 * 0.50 = 5.00",
      "L2": "Orange cost: 5 * 0.75 = 3.75",
      "L3": "Total cost: 5.00 + 3.75 = 8.75",
      "FA": "8.75"
    }<end_of_turn>
    <start_of_turn>model
    
    --------------------
    
    [1.4] Raw Text Output from Gemma Model:
    --------------------
    {
      "L1": "10*0.50=5.00",
      "L2": "5*0.75=3.75",
      "L3": "5+3.75=8.75",
      "FA": ""
    }
    --------------------
    
    [1.5] Calling extract_json_from_response...
      > Output (Parsed JSON dict):
    {
      "L1": "10*0.50=5.00",
      "L2": "5*0.75=3.75",
      "L3": "5+3.75=8.75",
      "FA": ""
    }
    
    [1.6] Filtering out equations for non-numeric lines:
      > Final equations to be evaluated: {
      "L1": "10*0.50=5.00",
      "L2": "5*0.75=3.75",
      "L3": "5+3.75=8.75",
      "FA": ""
    }
    
    [1.7] Calling evaluate_equations...
      > Output (Latency: 10.66s):
      > {'error': False}
    
      > ✅ All calculations are correct. Proceeding to Stage 2.
    
    
    --- STAGE 2: Conceptual Check (Phi-4) ---
    
    [2.1] Full Prompt for Phi-4 Model:
    --------------------
    You are a mathematics tutor.
    You will be given a math word problem and a solution written by a student.
    Carefully analyze the problem and solution LINE-BY-LINE and determine whether there are any errors in the solution.
    
    ### Problem:
    A grocery store sells apples for $0.50 each and oranges for $0.75 each. If a customer buys 10 apples and 5 oranges, what is the total cost?
    
    ### Answer:
    Apple cost: 10 * 0.50 = 5.00
    Orange cost: 5 * 0.75 = 3.75
    Total cost: 5.00 + 3.75 = 8.75
    FINAL ANSWER: 8.75
    --------------------
    
    [2.3] Raw Logits from Phi-4 Model: [[ 2.421875 -3.546875]]
    
    [2.4] Softmax Probabilities [Correct, Flawed]: [0.99609375, 0.0025482177734375]
    
    [2.5] Final Decision Logic (Latency: 0.10s):
      > Correct probability (99.61%) is > 50%.
    
    ================================================================================
    🏁 FINAL RESULT: Correct
    ================================================================================
    
    
    
    --- FINAL RESULT ---
    Case: Correct Solution
    Classification: Correct
    Confidence: 99.61%
    Explanation: Solution appears correct.
    ==================================================
    
    ================================================================================
    🕵️  STARTING DEBUG FOR: A car travels at 60 miles per hour. How long will it take to...
    ================================================================================
    
    --- STAGE 1: Equation Extraction (Gemma) ---
    
    [1.1] Calling format_solution_into_json_str...
      > Output:
    {
      "L1": "Time = Speed / Distance",
      "L2": "Time = 60 / 180 = 0.33 hours",
      "FA": "0.33"
    }
    
    [1.2] Calling create_extractor_messages...
      > Output: Generated a list of 5 messages.
    
    [1.3] Full Prompt for Gemma Model (with few-shot examples):
    --------------------
    <bos><start_of_turn>user
    [ROLE]
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
    
    
    ### Solution:
    {
      "L1": "2% of $90 is (2/100)*$90 = $1.8",
      "L2": "2% of $60 is (2/100)*$60 = $1.2",
      "L3": "The second transaction was reversed without the service charge so only a total of $90+$1.8+$1.2 = $39 was deducted from his account",
      "L4": "He will have a balance of $400-$39 = $361",
      "FA": "361"
    }<end_of_turn>
    <start_of_turn>model
    {
      "L1": "(2/100)*90=1.8",
      "L2": "(2/100)*60=1.2",
      "L3": "90+1.8+1.2=39",
      "L4": "400-39=361",
      "FA": ""
    }<end_of_turn>
    <start_of_turn>user
    ### Solution:
    {
      "L1": "She drinks 2 bottles a day and there are 24 bottles in a case so a case will last 24/2 = 12 days",
      "L2": "She needs enough to last her 240 days and 1 case will last her 12 days so she needs 240/12 = 20 cases",
      "L3": "Each case is on sale for $12.00 and she needs 20 cases so that's 12*20 = $240.00",
      "FA": "240"
    }<end_of_turn>
    <start_of_turn>model
    {
      "L1": "24/2=12",
      "L2": "240/12=20",
      "L3": "12*20=240.00",
      "FA": ""
    }<end_of_turn>
    <start_of_turn>user
    ### Solution:
    {
      "L1": "Time = Speed / Distance",
      "L2": "Time = 60 / 180 = 0.33 hours",
      "FA": "0.33"
    }<end_of_turn>
    <start_of_turn>model
    
    --------------------
    
    [1.4] Raw Text Output from Gemma Model:
    --------------------
    {
      "L1": "9/60=0.16",
      "L2": "60/180=0.33",
      "FA": ""
    }
    --------------------
    
    [1.5] Calling extract_json_from_response...
      > Output (Parsed JSON dict):
    {
      "L1": "9/60=0.16",
      "L2": "60/180=0.33",
      "FA": ""
    }
    
    [1.6] Filtering out equations for non-numeric lines:
      > Line 'L1' has no digits. Discarding extracted equation: '9/60=0.16'
      > Final equations to be evaluated: {
      "L2": "60/180=0.33",
      "FA": ""
    }
    
    [1.7] Calling evaluate_equations...
      > Output (Latency: 7.20s):
      > {'error': False}
    
      > ✅ All calculations are correct. Proceeding to Stage 2.
    
    
    --- STAGE 2: Conceptual Check (Phi-4) ---
    
    [2.1] Full Prompt for Phi-4 Model:
    --------------------
    You are a mathematics tutor.
    You will be given a math word problem and a solution written by a student.
    Carefully analyze the problem and solution LINE-BY-LINE and determine whether there are any errors in the solution.
    
    ### Problem:
    A car travels at 60 miles per hour. How long will it take to travel 180 miles?
    
    ### Answer:
    Time = Speed / Distance
    Time = 60 / 180 = 0.33 hours
    FINAL ANSWER: 0.33
    --------------------
    
    [2.3] Raw Logits from Phi-4 Model: [[-7.      5.9375]]
    
    [2.4] Softmax Probabilities [Correct, Flawed]: [2.3990869522094727e-06, 1.0]
    
    [2.5] Final Decision Logic (Latency: 0.10s):
      > Flawed probability (100.00%) is > 50%.
    
    ================================================================================
    🏁 FINAL RESULT: Conceptual Error
    ================================================================================
    
    
    
    --- FINAL RESULT ---
    Case: Conceptual Error
    Classification: Conceptual Error
    Confidence: 100.00%
    Explanation: Logic or setup appears to have a conceptual error.
    ==================================================
    



```python
import pandas as pd
from tqdm.notebook import tqdm
import time
import json
import torch

def run_batch_evaluation(df: pd.DataFrame, batch_size: int = 128) -> pd.DataFrame:
    """
    Performs a full, timed, batched evaluation of the two-stage pipeline.

    Args:
        df: The input DataFrame with columns 'index', 'question', 'correct_answer',
            'wrong_answer', and 'error_type'.
        batch_size: The number of samples to process in each batch.

    Returns:
        A pandas DataFrame containing detailed results and metadata for each test sample.
    """
    print("="*80)
    print("🚀 Starting Batch Evaluation...")
    print("="*80)

    overall_start_time = time.monotonic()

    # 1. Double the test set by preparing correct and incorrect samples
    print(f"[1/5] Preparing {len(df) * 2} test samples...")
    prepared_samples = []
    for _, row in df.iterrows():
        # Case 1: The correct solution
        prepared_samples.append({
            'original_index': row['index'],
            'question': row['question'],
            'solution': row['correct_answer'],
            'true_label': 'Correct'
        })
        # Case 2: The flawed solution
        error_map = {'comp': 'Computational Error', 'concep': 'Conceptual Error'}
        prepared_samples.append({
            'original_index': row['index'],
            'question': row['question'],
            'solution': row['wrong_answer'],
            'true_label': error_map.get(row['error_type'], 'Unknown Error')
        })

    # ===================================================================
    # --- STAGE 1: BATCHED EQUATION EXTRACTION (GEMMA) ---
    # ===================================================================
    print(f"[2/5] Running Stage 1 (Gemma Equation Extraction) on {len(prepared_samples)} samples...")
    stage1_start_time = time.monotonic()

    # Generate all prompts for Stage 1 first
    gemma_prompts = []
    for sample in prepared_samples:
        solution_json_str = format_solution_into_json_str(sample['solution'])
        messages = create_extractor_messages(solution_json_str)
        gemma_prompts.append(gemma_tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True))

    # Run batched inference
    gemma_raw_outputs = []
    for i in tqdm(range(0, len(gemma_prompts), batch_size), desc="Stage 1 Batches"):
        batch_prompts = gemma_prompts[i:i + batch_size]
        inputs = gemma_tokenizer(batch_prompts, return_tensors="pt", padding=True).to(device)
        outputs = gemma_model.generate(**inputs, max_new_tokens=300, use_cache=True, pad_token_id=gemma_tokenizer.pad_token_id)
        # Decode only the newly generated tokens
        decoded_outputs = gemma_tokenizer.batch_decode(outputs[:, inputs.input_ids.shape[1]:], skip_special_tokens=True)
        gemma_raw_outputs.extend(decoded_outputs)

    stage1_latency = time.monotonic() - stage1_start_time

    # ===================================================================
    # --- STAGE 1 POST-PROCESSING & STAGE 2 PREPARATION ---
    # ===================================================================
    print(f"[3/5] Processing Stage 1 results and preparing Stage 2 batch...")

    results_data = []
    stage2_batch = [] # This will hold only the samples that need conceptual checking

    for i, sample in enumerate(prepared_samples):
        # Initial data entry
        result_entry = {
            'original_index': sample['original_index'],
            'question': sample['question'],
            'solution': sample['solution'],
            'true_label': sample['true_label'],
            'gemma_raw_output': gemma_raw_outputs[i]
        }

        # Process Gemma's output
        extracted_eq_dict = extract_json_from_response(gemma_raw_outputs[i])
        result_entry['extracted_json_str'] = json.dumps(extracted_eq_dict)

        # Filter and evaluate
        solution_dict = json.loads(format_solution_into_json_str(sample['solution']))
        final_eq_to_eval = {
            k: v for k, v in extracted_eq_dict.items()
            if any(char.isdigit() for char in solution_dict.get(k, ""))
        }
        computational_error = evaluate_equations(final_eq_to_eval, solution_dict)

        # Make a decision: stop or proceed to Stage 2
        if computational_error["error"]:
            result_entry['predicted_classification'] = 'Computational Error'
            result_entry['pipeline_stage_stopped'] = 1
        else:
            result_entry['predicted_classification'] = None # Placeholder
            result_entry['pipeline_stage_stopped'] = 2
            # This sample needs to go to Stage 2. We store its prompt and its index in the main results list.
            stage2_batch.append({
                'prompt': f"{CLASSIFIER_SYSTEM_PROMPT}\n\n### Problem:\n{sample['question']}\n\n### Answer:\n{sample['solution']}",
                'result_index': i
            })

        results_data.append(result_entry)

    # ===================================================================
    # --- STAGE 2: BATCHED CONCEPTUAL CHECK (PHI-4) ---
    # ===================================================================
    print(f"[4/5] Running Stage 2 (Phi-4 Conceptual Check) on {len(stage2_batch)} samples...")
    stage2_start_time = time.monotonic()

    if stage2_batch:
        phi4_prompts = [item['prompt'] for item in stage2_batch]
        phi4_logits_list = []

        for i in tqdm(range(0, len(phi4_prompts), batch_size), desc="Stage 2 Batches"):
            batch_prompts = phi4_prompts[i:i + batch_size]
            inputs = classifier_tokenizer(batch_prompts, return_tensors="pt", padding=True, truncation=True, max_length=512).to(device)
            with torch.no_grad():
                outputs = classifier_model(**inputs)
                # Move logits to CPU immediately to free up VRAM
                phi4_logits_list.extend(outputs['logits'].cpu())

        # Update the main results list with the Stage 2 outcomes
        for i, item in enumerate(stage2_batch):
            result_index = item['result_index']
            logits = phi4_logits_list[i]
            probs = torch.softmax(logits, dim=-1).tolist()

            results_data[result_index]['phi4_correct_proba'] = probs[0]
            results_data[result_index]['phi4_flawed_proba'] = probs[1]
            results_data[result_index]['phi4_raw_logits'] = str(logits.numpy())

            if probs[1] > 0.5: # Flawed
                results_data[result_index]['predicted_classification'] = 'Conceptual Error'
            else: # Correct
                results_data[result_index]['predicted_classification'] = 'Correct'

    stage2_latency = time.monotonic() - stage2_start_time

    # ===================================================================
    # --- FINALIZATION ---
    # ===================================================================
    print("[5/5] Finalizing results and creating DataFrame...")

    results_df = pd.DataFrame(results_data)

    overall_latency = time.monotonic() - overall_start_time

    print("\n" + "="*80)
    print("✅ Batch Evaluation Complete!")
    print(f"  > Total Samples Processed: {len(results_df)}")
    print(f"  > Overall Time: {overall_latency:.2f} seconds")
    print(f"  > Avg Time per Sample: {overall_latency / len(results_df):.3f} seconds")
    print("-" * 40)
    print(f"  > Stage 1 Latency (Gemma): {stage1_latency:.2f} seconds")
    print(f"  > Stage 2 Latency (Phi-4): {stage2_latency:.2f} seconds")
    print("-" * 40)
    print("  > Predicted Classification Counts:")
    print(results_df['predicted_classification'].value_counts().to_string())
    print("="*80)

    return results_df
```


```python
df = pd.read_csv('/content/final-test-with-wrong-answers.csv')
```


```python
# Make sure all your models and helper functions are defined in previous cells
evaluation_results_df = run_batch_evaluation(df, batch_size=128)
```

    ================================================================================
    🚀 Starting Batch Evaluation...
    ================================================================================
    [1/5] Preparing 302 test samples...
    [2/5] Running Stage 1 (Gemma Equation Extraction) on 302 samples...



    Stage 1 Batches:   0%|          | 0/3 [00:00<?, ?it/s]


    A decoder-only architecture is being used, but right-padding was detected! For correct generation results, please set `padding_side='left'` when initializing the tokenizer.
    A decoder-only architecture is being used, but right-padding was detected! For correct generation results, please set `padding_side='left'` when initializing the tokenizer.
    A decoder-only architecture is being used, but right-padding was detected! For correct generation results, please set `padding_side='left'` when initializing the tokenizer.


    [3/5] Processing Stage 1 results and preparing Stage 2 batch...
    [4/5] Running Stage 2 (Phi-4 Conceptual Check) on 259 samples...



    Stage 2 Batches:   0%|          | 0/3 [00:00<?, ?it/s]



    ---------------------------------------------------------------------------

    OutOfMemoryError                          Traceback (most recent call last)

    /tmp/ipython-input-471946676.py in <cell line: 0>()
          1 # Make sure all your models and helper functions are defined in previous cells
    ----> 2 evaluation_results_df = run_batch_evaluation(df, batch_size=128)
    

    /tmp/ipython-input-749445336.py in run_batch_evaluation(df, batch_size)
        127             inputs = classifier_tokenizer(batch_prompts, return_tensors="pt", padding=True, truncation=True, max_length=512).to(device)
        128             with torch.no_grad():
    --> 129                 outputs = classifier_model(**inputs)
        130                 # Move logits to CPU immediately to free up VRAM
        131                 phi4_logits_list.extend(outputs['logits'].cpu())


    /usr/local/lib/python3.11/dist-packages/torch/nn/modules/module.py in _wrapped_call_impl(self, *args, **kwargs)
       1737             return self._compiled_call_impl(*args, **kwargs)  # type: ignore[misc]
       1738         else:
    -> 1739             return self._call_impl(*args, **kwargs)
       1740 
       1741     # torchrec tests the code consistency with the following code


    /usr/local/lib/python3.11/dist-packages/torch/nn/modules/module.py in _call_impl(self, *args, **kwargs)
       1748                 or _global_backward_pre_hooks or _global_backward_hooks
       1749                 or _global_forward_hooks or _global_forward_pre_hooks):
    -> 1750             return forward_call(*args, **kwargs)
       1751 
       1752         result = None


    /tmp/ipython-input-4035225597.py in forward(self, input_ids, attention_mask, labels, **kwargs)
         11 
         12     def forward(self, input_ids=None, attention_mask=None, labels=None, **kwargs):
    ---> 13         outputs = self.base(input_ids=input_ids, attention_mask=attention_mask, output_hidden_states=True, **kwargs)
         14         last_hidden_state = outputs.hidden_states[-1]
         15         pooled_output = last_hidden_state[:, -1, :]


    /usr/local/lib/python3.11/dist-packages/torch/nn/modules/module.py in _wrapped_call_impl(self, *args, **kwargs)
       1737             return self._compiled_call_impl(*args, **kwargs)  # type: ignore[misc]
       1738         else:
    -> 1739             return self._call_impl(*args, **kwargs)
       1740 
       1741     # torchrec tests the code consistency with the following code


    /usr/local/lib/python3.11/dist-packages/torch/nn/modules/module.py in _call_impl(self, *args, **kwargs)
       1748                 or _global_backward_pre_hooks or _global_backward_hooks
       1749                 or _global_forward_hooks or _global_forward_pre_hooks):
    -> 1750             return forward_call(*args, **kwargs)
       1751 
       1752         result = None


    /usr/local/lib/python3.11/dist-packages/peft/peft_model.py in forward(self, input_ids, attention_mask, inputs_embeds, labels, output_attentions, output_hidden_states, return_dict, task_ids, **kwargs)
       1650                 if peft_config.peft_type == PeftType.POLY:
       1651                     kwargs["task_ids"] = task_ids
    -> 1652                 return self.base_model(
       1653                     input_ids=input_ids,
       1654                     attention_mask=attention_mask,


    /usr/local/lib/python3.11/dist-packages/torch/nn/modules/module.py in _wrapped_call_impl(self, *args, **kwargs)
       1737             return self._compiled_call_impl(*args, **kwargs)  # type: ignore[misc]
       1738         else:
    -> 1739             return self._call_impl(*args, **kwargs)
       1740 
       1741     # torchrec tests the code consistency with the following code


    /usr/local/lib/python3.11/dist-packages/torch/nn/modules/module.py in _call_impl(self, *args, **kwargs)
       1748                 or _global_backward_pre_hooks or _global_backward_hooks
       1749                 or _global_forward_hooks or _global_forward_pre_hooks):
    -> 1750             return forward_call(*args, **kwargs)
       1751 
       1752         result = None


    /usr/local/lib/python3.11/dist-packages/peft/tuners/tuners_utils.py in forward(self, *args, **kwargs)
        220 
        221     def forward(self, *args: Any, **kwargs: Any):
    --> 222         return self.model.forward(*args, **kwargs)
        223 
        224     def _pre_injection_hook(self, model: nn.Module, config: PeftConfig, adapter_name: str) -> None:


    /usr/local/lib/python3.11/dist-packages/transformers/utils/deprecation.py in wrapped_func(*args, **kwargs)
        170                 warnings.warn(message, FutureWarning, stacklevel=2)
        171 
    --> 172             return func(*args, **kwargs)
        173 
        174         return wrapped_func


    ~/.cache/huggingface/modules/transformers_modules/microsoft/Phi-4-mini-instruct/5a149550068a1eb93398160d8953f5f56c3603e9/modeling_phi3.py in forward(self, input_ids, attention_mask, position_ids, past_key_values, inputs_embeds, labels, use_cache, output_attentions, output_hidden_states, return_dict, cache_position, logits_to_keep, **kwargs)
        911 
        912         # decoder outputs consists of (dec_features, layer_state, dec_hidden, dec_attn)
    --> 913         outputs = self.model(
        914             input_ids=input_ids,
        915             attention_mask=attention_mask,


    /usr/local/lib/python3.11/dist-packages/torch/nn/modules/module.py in _wrapped_call_impl(self, *args, **kwargs)
       1737             return self._compiled_call_impl(*args, **kwargs)  # type: ignore[misc]
       1738         else:
    -> 1739             return self._call_impl(*args, **kwargs)
       1740 
       1741     # torchrec tests the code consistency with the following code


    /usr/local/lib/python3.11/dist-packages/torch/nn/modules/module.py in _call_impl(self, *args, **kwargs)
       1748                 or _global_backward_pre_hooks or _global_backward_hooks
       1749                 or _global_forward_hooks or _global_forward_pre_hooks):
    -> 1750             return forward_call(*args, **kwargs)
       1751 
       1752         result = None


    ~/.cache/huggingface/modules/transformers_modules/microsoft/Phi-4-mini-instruct/5a149550068a1eb93398160d8953f5f56c3603e9/modeling_phi3.py in forward(self, input_ids, attention_mask, position_ids, past_key_values, inputs_embeds, use_cache, output_attentions, output_hidden_states, return_dict, cache_position, **flash_attn_kwargs)
        634                 )
        635             else:
    --> 636                 layer_outputs = decoder_layer(
        637                     hidden_states,
        638                     attention_mask=causal_mask,


    /usr/local/lib/python3.11/dist-packages/torch/nn/modules/module.py in _wrapped_call_impl(self, *args, **kwargs)
       1737             return self._compiled_call_impl(*args, **kwargs)  # type: ignore[misc]
       1738         else:
    -> 1739             return self._call_impl(*args, **kwargs)
       1740 
       1741     # torchrec tests the code consistency with the following code


    /usr/local/lib/python3.11/dist-packages/torch/nn/modules/module.py in _call_impl(self, *args, **kwargs)
       1748                 or _global_backward_pre_hooks or _global_backward_hooks
       1749                 or _global_forward_hooks or _global_forward_pre_hooks):
    -> 1750             return forward_call(*args, **kwargs)
       1751 
       1752         result = None


    ~/.cache/huggingface/modules/transformers_modules/microsoft/Phi-4-mini-instruct/5a149550068a1eb93398160d8953f5f56c3603e9/modeling_phi3.py in forward(self, hidden_states, attention_mask, position_ids, past_key_value, output_attentions, use_cache, cache_position, position_embeddings, **kwargs)
        309         residual = hidden_states
        310         hidden_states = self.post_attention_layernorm(hidden_states)
    --> 311         hidden_states = self.mlp(hidden_states)
        312         hidden_states = residual + self.resid_mlp_dropout(hidden_states)  # main diff with Llama
        313 


    /usr/local/lib/python3.11/dist-packages/torch/nn/modules/module.py in _wrapped_call_impl(self, *args, **kwargs)
       1737             return self._compiled_call_impl(*args, **kwargs)  # type: ignore[misc]
       1738         else:
    -> 1739             return self._call_impl(*args, **kwargs)
       1740 
       1741     # torchrec tests the code consistency with the following code


    /usr/local/lib/python3.11/dist-packages/torch/nn/modules/module.py in _call_impl(self, *args, **kwargs)
       1748                 or _global_backward_pre_hooks or _global_backward_hooks
       1749                 or _global_forward_hooks or _global_forward_pre_hooks):
    -> 1750             return forward_call(*args, **kwargs)
       1751 
       1752         result = None


    ~/.cache/huggingface/modules/transformers_modules/microsoft/Phi-4-mini-instruct/5a149550068a1eb93398160d8953f5f56c3603e9/modeling_phi3.py in forward(self, hidden_states)
         63 
         64     def forward(self, hidden_states: torch.FloatTensor) -> torch.FloatTensor:
    ---> 65         up_states = self.gate_up_proj(hidden_states)
         66 
         67         gate, up_states = up_states.chunk(2, dim=-1)


    /usr/local/lib/python3.11/dist-packages/torch/nn/modules/module.py in _wrapped_call_impl(self, *args, **kwargs)
       1737             return self._compiled_call_impl(*args, **kwargs)  # type: ignore[misc]
       1738         else:
    -> 1739             return self._call_impl(*args, **kwargs)
       1740 
       1741     # torchrec tests the code consistency with the following code


    /usr/local/lib/python3.11/dist-packages/torch/nn/modules/module.py in _call_impl(self, *args, **kwargs)
       1748                 or _global_backward_pre_hooks or _global_backward_hooks
       1749                 or _global_forward_hooks or _global_forward_pre_hooks):
    -> 1750             return forward_call(*args, **kwargs)
       1751 
       1752         result = None


    /content/unsloth_compiled_cache/Linear4bit_peft_forward.py in unsloth_forward(self, x, *args, **kwargs)
         76 
         77             if active_adapter not in self.lora_variant:  # vanilla LoRA
    ---> 78                 return lora_forward(result, lora_A, lora_B, dropout, x, scaling)
         79                 if requires_conversion:
         80                     output = output.to(expected_dtype)


    /content/unsloth_compiled_cache/Linear4bit_peft_forward.py in lora_forward(result, lora_A, lora_B, dropout, x, scaling)
         23     # output = result + scaling * xA @ lora_B.weight.t()
         24     shape = result.shape
    ---> 25     output = torch_addmm(
         26         result.view(-1, shape[-1]),
         27         xA.view(-1, xA.shape[-1]),


    OutOfMemoryError: CUDA out of memory. Tried to allocate 1.75 GiB. GPU 0 has a total capacity of 39.56 GiB of which 886.88 MiB is free. Process 129420 has 38.68 GiB memory in use. Of the allocated memory 37.57 GiB is allocated by PyTorch, and 605.87 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)



```python
# Display the first few rows of the detailed output
display(evaluation_results_df.head())

# Save the results to a CSV for offline analysis in Excel, etc.
evaluation_results_df.to_csv("/content/batch_evaluation_results.csv", index=False)
```
