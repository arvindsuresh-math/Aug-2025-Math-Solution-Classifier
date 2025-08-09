```python
# --- Hugging Face Login & Installations ---
from google.colab import userdata
from huggingface_hub import notebook_login

hf_token = userdata.get('HF_TOKEN')
if not hf_token:
    raise ValueError("HF_TOKEN not found in Colab Secrets. Please add it.")
# notebook_login(new_session=hf_token) # Unsloth handles token auth automatically
```


```python
# # Install Unsloth for Google Colab
# !pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"

# # Standard installations
# !pip install -U transformers
# !pip install -U datasets
# !pip install -U accelerate # Required for Unsloth

!pip install --no-deps bitsandbytes accelerate xformers==0.0.29.post3 peft trl triton cut_cross_entropy unsloth_zoo
!pip install sentencepiece protobuf "datasets>=3.4.1,<4.0.0" "huggingface_hub>=0.34.0" hf_transfer
!pip install --no-deps unsloth
```

```python
from pathlib import Path
import json
import datetime
import torch
import random
import numpy as np

CONFIG = {
    # Core experiment parameters
    "experiment_type": "equation_extraction",
    # UPDATED to use Unsloth's 4-bit Gemma 3 1B model
    "model_name": "unsloth/gemma-3-1b-it-unsloth-bnb-4bit",
    "max_seq_length": 2048, # Unsloth's FastModel requires this at load time

    # Prompting configuration
    "include_examples": True,
    "few_shot_examples": [
        ('computational_error', 4966),
        ('conceptual_error', 1091),
    ],

    # Training parameters
    "learning_rate": 2e-4,
    "num_epochs": 1, # Set to 1 as requested
    "batch_size": 16, # Halved from 4, since Unsloth uses more VRAM initially
    "gradient_accumulation_steps": 2,

    # LoRa params (Unsloth defaults are often good)
    "lora_rank": 16,
    "lora_alpha": 32, # Often set to rank
    "lora_dropout": 0.05,

    # Paths
    "base_dataset_path": "/content/equation_extraction_dataset_cleaned.csv",
    "output_base_dir": "/content/experiments",
}

# --- Generate Unique Experiment ID ---
model_id_short = "gemma3-1b-unsloth"
experiment_id = f"{CONFIG['experiment_type']}_{model_id_short}_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}"
CONFIG["experiment_id"] = experiment_id
print(f"Experiment ID: {experiment_id}")

# --- Setup Output Directories ---
output_dir = Path(CONFIG["output_base_dir"]) / CONFIG["experiment_id"]
(output_dir / "baseline_results").mkdir(parents=True, exist_ok=True)
(output_dir / "final_results").mkdir(parents=True, exist_ok=True)
CONFIG["output_dir"] = str(output_dir)
CONFIG["final_adapter_dir"] = str(output_dir / "final_adapter")
CONFIG["merged_model_dir"] = str(output_dir / "final_merged_model")

with open(output_dir / "config.json", 'w') as f: json.dump(CONFIG, f, indent=2)
print(f"Output directory created: {output_dir}")

# --- Set Random Seeds for Reproducibility ---
def set_seeds(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available(): torch.cuda.manual_seed_all(seed)
set_seeds(42)

print("\n✅ Setup complete.")
```

    Experiment ID: equation_extraction_gemma3-1b-unsloth_20250808_1357
    Output directory created: /content/experiments/equation_extraction_gemma3-1b-unsloth_20250808_1357
    
    ✅ Setup complete.



```python
### Cell 3: System Prompt for Equation Extraction

# SYSTEM_PROMPT = \
# """[ROLE]
# You are an expert at parsing mathematical solutions.

# [TASK]
# You are given a mathematical solution. Your task is to extract the calculation performed on each line and represent it as a simple equation.

# For each line of the solution, create a key-value pair.
# - The key should be the line identifier (e.g., "L1", "L2", "FA" for the final answer line).
# - The value should be the extracted equation string (e.g., "10+5=15").
# - If a line contains no calculation, the value must be an empty string.

# [RESPONSE FORMAT]
# Your response must be ONLY a single, valid JSON object, with no other text before or after it. The JSON object must map line identifiers to their corresponding equation strings.
# """

SYSTEM_PROMPT = \
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
```


```python
### Cell 4: Core utilities

import pandas as pd
from unsloth import FastModel
from unsloth.chat_templates import get_chat_template
import torch

# 4.1 Loading

def load_base_dataset():
    """Loads the base dataset from the specified CSV file."""
    data = pd.read_csv(CONFIG['base_dataset_path'])
    print(f"Loaded dataset with {len(data)} samples from {CONFIG['base_dataset_path']}")
    return data

def load_unsloth_model_and_tokenizer():
    """
    Loads the 4-bit quantized model and tokenizer using Unsloth's FastModel.
    """
    model_name = CONFIG["model_name"]
    print(f"Loading model and tokenizer: {model_name}")

    model, tokenizer = FastModel.from_pretrained(
        model_name = model_name,
        max_seq_length = CONFIG["max_seq_length"],
        dtype = None, # None for auto detection. Can be torch.bfloat16
        load_in_4bit = True,
    )

    tokenizer = get_chat_template(
        tokenizer,
        chat_template = "gemma-3",
    )

    # Set padding token if it's not already set
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    tokenizer.padding_side = "left" # Use left-padding for generation

    return model, tokenizer

def prepare_model_for_lora_training(model):
    """Applies LoRa adapters to the model for fine-tuning."""
    print("Applying LoRa adapters to the model...")
    model = FastModel.get_peft_model(
        model,
        r = CONFIG["lora_rank"],
        lora_alpha = CONFIG["lora_alpha"],
        lora_dropout = CONFIG["lora_dropout"],
        bias = "none",
        use_gradient_checkpointing = True,
        random_state = 42,
        target_modules = ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    )
    return model

# 4.2 Formatting

def format_user_message(sample: dict) -> str:
    """
    Formats a user message to contain the literal JSON string of the answer mapping.
    - Uses 'wrong_answer_mapping' for computational or conceptual errors.
    - Uses 'correct_answer_mapping' for correct answers.
    """
    error_type = sample.get('error_type', 'correct')
    mapping_str = ""

    if error_type in ['computational_error', 'conceptual_error']:
        mapping_str = sample.get('wrong_answer_mapping', '{}')
    else:  # This covers 'correct' and any other cases
        mapping_str = sample.get('correct_answer_mapping', '{}')

    # Ensure we have a valid string to pass
    if not isinstance(mapping_str, str):
        mapping_str = '{}'

    # The prompt now contains the raw JSON string of the line-by-line solution
    return f"### Solution:\n{mapping_str.strip()}"

def format_expected_output(sample: dict) -> str:
    """
    Selects the correct equation mapping based on the error type and formats it as a clean JSON string.
    - Uses 'wrong_eqn_mapping' for computational or conceptual errors.
    - Uses 'correct_eqn_mapping' for correct answers.
    """
    error_type = sample.get('error_type', 'correct')
    eqn_map_str = ""

    if error_type in ['computational_error', 'conceptual_error']:
        eqn_map_str = sample.get('wrong_eqn_mapping', '{}')
    else: # This covers 'correct' and any other cases
        eqn_map_str = sample.get('correct_eqn_mapping', '{}')

    if not isinstance(eqn_map_str, str):
        return "{}"

    try:
        # Load and re-dump the JSON to ensure consistent, clean formatting for the model to learn.
        # This removes extra whitespace and uses double quotes.
        parsed_json = json.loads(eqn_map_str)
        return json.dumps(parsed_json, indent=2)
    except (json.JSONDecodeError, TypeError):
        # Return an empty JSON object if the source string is invalid
        return "{}"

# 4.3 Prompt Construction (CORRECTED LOGIC)

def _build_conversation_messages(sample, is_training_prompt=True):
    """
    Builds the list of messages for the chat template, correctly placing the system prompt.
    """
    # Prepend the system prompt to the user's message content.
    # This is the correct way to provide instructions for the gemma-3 template.
    user_content = format_user_message(sample)
    instructed_user_content = f"{SYSTEM_PROMPT}\n\n{user_content}"

    # For the few-shot examples, we use a simpler user message
    few_shot_messages = []
    if CONFIG["include_examples"]:
        # NOTE: We use the train_df loaded globally for this.
        example_specs = CONFIG["few_shot_examples"]
        for error_type, index in example_specs:
            example_sample_df = train_df[(train_df['error_type'] == error_type) & (train_df['index'] == index)]
            if not example_sample_df.empty:
                example_sample = example_sample_df.iloc[0].to_dict()
                # The first user turn gets the full instructions
                if not few_shot_messages:
                     few_shot_user_content = f"{SYSTEM_PROMPT}\n\n{format_user_message(example_sample)}"
                else:
                     few_shot_user_content = format_user_message(example_sample)

                few_shot_messages.append({"role": "user", "content": few_shot_user_content})
                few_shot_messages.append({"role": "assistant", "content": format_expected_output(example_sample)})

    # The final conversation list
    messages = []
    if few_shot_messages:
        messages.extend(few_shot_messages)
        # The actual query doesn't need the system prompt if few-shot examples are present
        messages.append({"role": "user", "content": format_user_message(sample)})
    else:
        # If no few-shot examples, the main user query gets the instructions
        messages.append({"role": "user", "content": instructed_user_content})

    # If it's a training prompt, add the final assistant response
    if is_training_prompt:
        messages.append({"role": "assistant", "content": format_expected_output(sample)})

    return messages

# 4.4 Prompt creation for inference
def create_sample_prompt_for_inference(sample, tokenizer):
    """Creates a full prompt for a single sample for inference."""
    messages = _build_conversation_messages(sample, is_training_prompt=False)
    # Apply the chat template with the generation prompt
    return tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
```

    🦥 Unsloth: Will patch your computer to enable 2x faster free finetuning.
    🦥 Unsloth Zoo will now patch everything to make training faster!



```python
### Cell 5: Dataset preparation

from datasets import Dataset

def prepare_datasets(base_df):
    """
    Splits the base DataFrame into training and testing sets using the 'split' column.
    """
    train_df = base_df[base_df['split'] == 'train'].copy()
    test_df = base_df[base_df['split'] == 'test'].copy()
    print(f"Data split using 'split' column: {len(train_df)} training, {len(test_df)} testing samples.")
    return train_df, test_df

def create_training_dataset(df, tokenizer):
    """
    Creates the tokenized training dataset object for the SFTTrainer.
    """
    def create_text_for_sample(sample):
        """Prepares the full conversation text for a single training sample."""
        messages = _build_conversation_messages(sample, is_training_prompt=True)
        return {"text": tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=False)}

    return Dataset.from_pandas(df).map(create_text_for_sample, load_from_cache_file=False)
```


```python
### Cell 6: Evaluation logic

import re
import math
import json
import pandas as pd
from tqdm import tqdm

def _sanitize_equation_string(expression: str) -> str:
    """Cleans a single equation string by stripping whitespace, standardizing
    multiplication, and removing non-mathematical characters."""
    if not isinstance(expression, str):
        return ""
    sanitized = expression.replace(' ', '')
    sanitized = sanitized.replace('x', '*').replace('×', '*')
    sanitized = re.sub(r'/([a-zA-Z]+)', '', sanitized)
    sanitized = re.sub(r'[^\d.()+\-*/=]', '', sanitized)
    return sanitized

def rigorous_compare_equation_dicts(predicted_dict: dict, expected_dict: dict) -> float:
    """
    Compares two pre-sanitized equation dictionaries with flexible checks,
    including operand rounding.
    """
    def _safe_eval(expression: str):
        """Safely evaluates a string, returning a sentinel on error."""
        try:
            if not expression: return None
            return eval(expression, {"__builtins__": None}, {})
        except Exception:
            return object()

    def _extract_components(expression: str) -> tuple[list, list]:
        """Extracts number and operator sequences, with rounding to 2 decimal places."""
        number_strings = re.findall(r'\d+\.?\d*|\.\d+', expression)
        numbers = [round(float(n), 2) for n in number_strings]
        operators = re.findall(r'[+\-*/]', expression)
        return numbers, operators

    def _expressions_are_equivalent(pred_expr: str, exp_expr: str) -> bool:
        """Checks if two expression strings are equivalent."""
        pred_val = _safe_eval(pred_expr)
        exp_val = _safe_eval(exp_expr)

        if not (isinstance(pred_val, (int, float)) and isinstance(exp_val, (int, float))):
            return False
        if not math.isclose(pred_val, exp_val, rel_tol=1e-5):
            return False

        pred_nums, pred_ops = _extract_components(pred_expr)
        exp_nums, exp_ops = _extract_components(exp_expr)

        if pred_nums != exp_nums or pred_ops != exp_ops:
            return False
        return True

    # --- Main comparison logic ---
    items_to_score = [(k, v) for k, v in expected_dict.items() if v]
    if not items_to_score:
        return 1.0 if not any(v for v in predicted_dict.values()) else 0.0

    scores = []
    for key, expected_eqn in items_to_score:
        line_score = 0
        predicted_eqn = predicted_dict.get(key, "")

        if predicted_eqn.count('=') == 1 and expected_eqn.count('=') == 1:
            pred_lhs, pred_rhs = predicted_eqn.split('=', 1)
            exp_lhs, exp_rhs = expected_eqn.split('=', 1)
            if _expressions_are_equivalent(pred_lhs, exp_lhs) and \
               _expressions_are_equivalent(pred_rhs, exp_rhs):
                line_score = 1
        scores.append(line_score)

    return sum(scores) / len(scores) if scores else 1.0

def extract_json_from_response(response: str) -> dict:
    """Extracts a JSON object from a model's text response."""
    match = re.search(r'```json\s*(\{.*?\})\s*```', response, re.DOTALL)
    json_str = match.group(1) if match else re.search(r'(\{.*?\})', response, re.DOTALL)
    if not json_str: return {}
    try:
        cleaned_str = json_str.group(0).replace("'", '"') if hasattr(json_str, 'group') else json_str.replace("'", '"')
        return json.loads(cleaned_str)
    except (json.JSONDecodeError, AttributeError):
        return {}

def run_unsloth_inference(model, tokenizer, df_to_eval, batch_size=32):
    """Runs inference using the provided Unsloth model and tokenizer."""
    print(f"\n--- Running Unsloth native inference ---")
    tokenizer.padding_side = "left"
    prompts = [create_sample_prompt_for_inference(row, tokenizer) for _, row in df_to_eval.iterrows()]
    all_predictions = []
    for i in tqdm(range(0, len(prompts), batch_size), desc="Inference Batches"):
        batch_prompts = prompts[i:i + batch_size]
        tokenizer.padding_side = "left"
        inputs = tokenizer(batch_prompts, return_tensors="pt", padding=True).to("cuda")
        tokenizer.padding_side = "left"
        outputs = model.generate(**inputs, max_new_tokens=300, use_cache=True, pad_token_id=tokenizer.pad_token_id)
        tokenizer.padding_side = "left"
        decoded_outputs = tokenizer.batch_decode(outputs[:, inputs.input_ids.shape[1]:], skip_special_tokens=True)
        all_predictions.extend(decoded_outputs)
    return all_predictions

def evaluate_predictions(test_df, predictions):
    """Parses predictions, sanitizes the data, computes metrics, and returns a comprehensive DataFrame."""
    results_data = []
    for i, pred_text in enumerate(predictions):
        original_sample = test_df.iloc[i].to_dict()

        predicted_json = extract_json_from_response(pred_text)
        expected_json = json.loads(format_expected_output(original_sample))

        sanitized_predicted_json = {key: _sanitize_equation_string(value) for key, value in predicted_json.items()}
        sanitized_expected_json = {key: _sanitize_equation_string(value) for key, value in expected_json.items()}

        score = rigorous_compare_equation_dicts(sanitized_predicted_json, sanitized_expected_json)

        results_data.append({
            'problem_index': original_sample.get('index'),
            'rigorous_score': score,
            'expected_json': json.dumps(expected_json),
            'predicted_json': json.dumps(predicted_json),
            'sanitized_expected_json': json.dumps(sanitized_expected_json),
            'sanitized_predicted_json': json.dumps(sanitized_predicted_json),
            'full_prediction_text': pred_text.strip(),
        })
    results_df = pd.DataFrame(results_data)

    parse_failures = (results_df['predicted_json'] == '{}').sum()
    metrics = {
        "mean_rigorous_score": results_df['rigorous_score'].mean(),
        "total_samples": len(results_df),
        "json_parse_failures": int(parse_failures),
        "failure_rate": parse_failures / len(results_df) if len(results_df) > 0 else 0
    }
    return results_df, metrics
```


```python
### Cell 7: Fine-tuning function

from trl import SFTTrainer, SFTConfig
from transformers import TrainingArguments
from unsloth.chat_templates import train_on_responses_only

def run_fine_tuning(model, tokenizer, train_dataset):
    """Runs fine-tuning using Unsloth and SFTTrainer."""

    # Configure the trainer
    trainer = SFTTrainer(
        model=model,
        tokenizer=tokenizer,
        train_dataset=train_dataset,
        dataset_text_field="text",
        max_seq_length=CONFIG["max_seq_length"],
        dataset_num_proc=2,
        args=SFTConfig(
            per_device_train_batch_size=CONFIG["batch_size"],
            gradient_accumulation_steps=CONFIG["gradient_accumulation_steps"],
            warmup_steps=5,
            num_train_epochs=1,
            learning_rate=CONFIG["learning_rate"],
            fp16=not torch.cuda.is_bf16_supported(),
            bf16=torch.cuda.is_bf16_supported(),
            logging_steps=1,
            optim="adamw_8bit",
            weight_decay=0.01,
            lr_scheduler_type="linear",
            seed=42,
            output_dir=str(Path(CONFIG["output_dir"]) / "training_checkpoints"),
            report_to="none",
        ),
    )

    # Use Unsloth's helper to only train on assistant's responses
    # This is more efficient than manual masking.
    trainer = train_on_responses_only(
        trainer,
        instruction_part="<start_of_turn>user",
        response_part="<start_of_turn>model",
    )

    print(f"\n--- Starting fine-tuning for {CONFIG['num_epochs']} epoch(s) ---")
    trainer_stats = trainer.train()

    # Save the final LoRa adapter
    print(f"\n✅ Fine-tuning finished! Saving final adapter to {CONFIG['final_adapter_dir']}")
    model.save_pretrained(CONFIG["final_adapter_dir"])

    # 4Save Training Log and Configuration
    log_history = [log for log in trainer.state.log_history if 'loss' in log]
    log_history_df = pd.DataFrame(log_history)
    log_path = output_dir / "training_log.csv"
    log_history_df.to_csv(log_path, index=False)
    print(f"✅ Training log saved to: {log_path}")

    return trainer_stats
```


```python
### Cell 8: Pipeline execution
```


```python
# 8.1 Load dataset and few-shot examples
base_df = load_base_dataset()
train_df, test_df = prepare_datasets(base_df)
print("\n✅ Data loaded and split.")
```

    Loaded dataset with 877 samples from /content/equation_extraction_dataset_cleaned.csv
    Data split using 'split' column: 701 training, 176 testing samples.
    
    ✅ Data loaded and split.



```python
# 8.2 Load model and tokenizer
model, tokenizer = load_unsloth_model_and_tokenizer()
print("\n✅ Unsloth model and tokenizer loaded.")
```

    Loading model and tokenizer: unsloth/gemma-3-1b-it-unsloth-bnb-4bit
    ==((====))==  Unsloth 2025.8.1: Fast Gemma3 patching. Transformers: 4.54.1.
       \\   /|    NVIDIA A100-SXM4-40GB. Num GPUs = 1. Max memory: 39.557 GB. Platform: Linux.
    O^O/ \_/ \    Torch: 2.6.0+cu124. CUDA: 8.0. CUDA Toolkit: 12.4. Triton: 3.2.0
    \        /    Bfloat16 = TRUE. FA [Xformers = 0.0.29.post3. FA2 = False]
     "-____-"     Free license: http://github.com/unslothai/unsloth
    Unsloth: Fast downloading is enabled - ignore downloading bars which are red colored!



    model.safetensors:   0%|          | 0.00/1.00G [00:00<?, ?B/s]



    generation_config.json:   0%|          | 0.00/233 [00:00<?, ?B/s]



    tokenizer_config.json: 0.00B [00:00, ?B/s]



    tokenizer.model:   0%|          | 0.00/4.69M [00:00<?, ?B/s]



    tokenizer.json:   0%|          | 0.00/33.4M [00:00<?, ?B/s]



    added_tokens.json:   0%|          | 0.00/35.0 [00:00<?, ?B/s]



    special_tokens_map.json:   0%|          | 0.00/670 [00:00<?, ?B/s]


    
    ✅ Unsloth model and tokenizer loaded.



```python
# 8.3 Apply Formatting (Inspect Message List)
inspection_sample = train_df.iloc[0].to_dict()

conversation_messages = _build_conversation_messages(sample=inspection_sample, is_training_prompt=True)

import json
print("Example conversation:")
for message in conversation_messages:
    print(f"{message['role']}:")
    print(message['content'])
    print()
```

    Example conversation:
    user:
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
    }
    
    assistant:
    {
      "L1": "(2/100)*90=1.8",
      "L2": "(2/100)*60=1.2",
      "L3": "90+1.8+1.2=39",
      "L4": "400-39=361",
      "FA": ""
    }
    
    user:
    ### Solution:
    {
      "L1": "She drinks 2 bottles a day and there are 24 bottles in a case so a case will last 24/2 = 12 days",
      "L2": "She needs enough to last her 240 days and 1 case will last her 12 days so she needs 240/12 = 20 cases",
      "L3": "Each case is on sale for $12.00 and she needs 20 cases so that's 12*20 = $240.00",
      "FA": "240"
    }
    
    assistant:
    {
      "L1": "24/2=12",
      "L2": "240/12=20",
      "L3": "12*20=240.00",
      "FA": ""
    }
    
    user:
    ### Solution:
    {
      "L1": "2% of $90 is (2/100)*$90 = $1.8",
      "L2": "2% of $60 is (2/100)*$60 = $1.2",
      "L3": "The second transaction was reversed without the service charge so only a total of $90+$1.8+$1.2 = $39 was deducted from his account",
      "L4": "He will have a balance of $400-$39 = $361",
      "FA": "361"
    }
    
    assistant:
    {
      "L1": "(2/100)*90=1.8",
      "L2": "(2/100)*60=1.2",
      "L3": "90+1.8+1.2=39",
      "L4": "400-39=361",
      "FA": ""
    }
    



```python
# 8.4 Apply tokenizer and inspect

final_prompt_string = tokenizer.apply_chat_template(
    conversation_messages,
    tokenize=False,
    add_generation_prompt=False # False because it's a training example
)

print(final_prompt_string)
```

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
    



```python
# ===================================================================
# PHASE 1: BASELINE EVALUATION
# ===================================================================

from tqdm import tqdm

print("\n" + "="*50)
print("PHASE 1: BASELINE EVALUATION")
print("="*50)

# Run inference on the base model
baseline_predictions = run_unsloth_inference(
    model=model,
    tokenizer=tokenizer,
    df_to_eval=test_df,
    batch_size=64
)

# Evaluate and save baseline results
baseline_results_df, baseline_metrics = evaluate_predictions(test_df, baseline_predictions)
baseline_results_path = Path(CONFIG["output_dir"]) / "baseline_results" / "baseline_evaluation_results.csv"
baseline_metrics_path = Path(CONFIG["output_dir"]) / "baseline_results" / "baseline_metrics.json"
baseline_results_df.to_csv(baseline_results_path, index=False)
with open(baseline_metrics_path, 'w') as f:
    json.dump(baseline_metrics, f, indent=2)

print("\n--- Baseline Metrics ---")
print(json.dumps(baseline_metrics, indent=2))
print(f"✅ Baseline results saved.")

```

    
    ==================================================
    PHASE 1: BASELINE EVALUATION
    ==================================================
    
    --- Running Unsloth native inference ---


    Inference Batches: 100%|██████████| 3/3 [01:30<00:00, 30.19s/it]

    
    --- Baseline Metrics ---
    {
      "mean_rigorous_score": 0.39001623376623373,
      "total_samples": 176,
      "json_parse_failures": 3,
      "failure_rate": 0.017045454545454544
    }
    ✅ Baseline results saved.


    



```python
baseline_results_df
```





  <div id="df-9b31306c-8404-47d5-9c67-cde9293dde34" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>problem_index</th>
      <th>rigorous_score</th>
      <th>expected_json</th>
      <th>predicted_json</th>
      <th>sanitized_expected_json</th>
      <th>sanitized_predicted_json</th>
      <th>full_prediction_text</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2680</td>
      <td>0.750000</td>
      <td>{"L1": "6/12=0.5", "L2": "2+0.5=2.5", "L3": "2...</td>
      <td>{"L1": "6/12=0.5 years", "L2": "2+0.5=2.5 year...</td>
      <td>{"L1": "6/12=0.5", "L2": "2+0.5=2.5", "L3": "2...</td>
      <td>{"L1": "6/12=0.5", "L2": "2+0.5=2.5", "L3": "2...</td>
      <td>```json\n{\n  "L1": "6/12=0.5 years",\n  "L2":...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4479</td>
      <td>0.250000</td>
      <td>{"L1": "21/14=1.5", "L2": "8+3+12+1.5=24.5", "...</td>
      <td>{"L1": "1.5 bushels", "L2": "24.5 bushels", "L...</td>
      <td>{"L1": "21/14=1.5", "L2": "8+3+12+1.5=24.5", "...</td>
      <td>{"L1": "1.5", "L2": "24.5", "L3": "50-24.5=25....</td>
      <td>```json\n{\n  "L1": "1.5 bushels",\n  "L2": "2...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5650</td>
      <td>0.000000</td>
      <td>{"L1": "75/60=1.25", "L2": "40*1.25=50", "L3":...</td>
      <td>{"L1": "1.25*43=53.25", "L2": "50-16=34", "L3"...</td>
      <td>{"L1": "75/60=1.25", "L2": "40*1.25=50", "L3":...</td>
      <td>{"L1": "1.25*43=53.25", "L2": "50-16=34", "L3"...</td>
      <td>```json\n{\n  "L1": "1.25*43=53.25",\n  "L2": ...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7201</td>
      <td>0.000000</td>
      <td>{"L1": "200/2=100", "L2": "100*0.3=30", "L3": ...</td>
      <td>{"L1": "100 visitors", "L2": "210", "L3": "210...</td>
      <td>{"L1": "200/2=100", "L2": "100*0.3=30", "L3": ...</td>
      <td>{"L1": "100", "L2": "210", "L3": "210", "FA": ""}</td>
      <td>```json\n{\n  "L1": "100 visitors",\n  "L2": "...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2796</td>
      <td>0.250000</td>
      <td>{"L1": "0.4*80=32", "L2": "2*32=64", "L3": "10...</td>
      <td>{"L1": "32", "L2": "64", "L3": "100-64=36", "L...</td>
      <td>{"L1": "0.4*80=32", "L2": "2*32=64", "L3": "10...</td>
      <td>{"L1": "32", "L2": "64", "L3": "100-64=36", "L...</td>
      <td>```json\n{\n  "L1": "32",\n  "L2": "64",\n  "L...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>171</th>
      <td>146</td>
      <td>1.000000</td>
      <td>{"L1": "22+3=25", "L2": "25-4=21", "L3": "22+2...</td>
      <td>{"L1": "22 + 3 = 25 minutes", "L2": "25 - 4 = ...</td>
      <td>{"L1": "22+3=25", "L2": "25-4=21", "L3": "22+2...</td>
      <td>{"L1": "22+3=25", "L2": "25-4=21", "L3": "22+2...</td>
      <td>```json\n{\n  "L1": "22 + 3 = 25 minutes",\n  ...</td>
    </tr>
    <tr>
      <th>172</th>
      <td>4165</td>
      <td>1.000000</td>
      <td>{"L1": "2*2=4", "L2": "2*2*2=8", "L3": "2+4+8=...</td>
      <td>{"L1": "2 x 2 = 4", "L2": "2 x 2 x 2 = 8", "L3...</td>
      <td>{"L1": "2*2=4", "L2": "2*2*2=8", "L3": "2+4+8=...</td>
      <td>{"L1": "2*2=4", "L2": "2*2*2=8", "L3": "2+4+8=...</td>
      <td>```json\n{\n  "L1": "2 x 2 = 4",\n  "L2": "2 x...</td>
    </tr>
    <tr>
      <th>173</th>
      <td>1959</td>
      <td>0.000000</td>
      <td>{"L1": "11-2=9", "L2": "9-3=6", "FA": ""}</td>
      <td>{"L1": "9 - 2=7", "L2": "6", "FA": "6"}</td>
      <td>{"L1": "11-2=9", "L2": "9-3=6", "FA": ""}</td>
      <td>{"L1": "9-2=7", "L2": "6", "FA": "6"}</td>
      <td>```json\n{\n  "L1": "9 - 2=7",\n  "L2": "6",\n...</td>
    </tr>
    <tr>
      <th>174</th>
      <td>4877</td>
      <td>0.250000</td>
      <td>{"L1": "12*2=24", "L2": "8-2=6", "L3": "6+8+6=...</td>
      <td>{"L1": "12 * 2 = 24", "L2": "24 + 8 - 2 = 30",...</td>
      <td>{"L1": "12*2=24", "L2": "8-2=6", "L3": "6+8+6=...</td>
      <td>{"L1": "12*2=24", "L2": "24+8-2=30", "L3": "12...</td>
      <td>```json\n{\n  "L1": "12 * 2 = 24",\n  "L2": "2...</td>
    </tr>
    <tr>
      <th>175</th>
      <td>3068</td>
      <td>0.333333</td>
      <td>{"L1": "20-5=15", "L2": "3+7=10", "L3": "15-10...</td>
      <td>{"L1": "15 - 5 = 10", "L2": "3 + 7 = 10", "L3"...</td>
      <td>{"L1": "20-5=15", "L2": "3+7=10", "L3": "15-10...</td>
      <td>{"L1": "15-5=10", "L2": "3+7=10", "L3": "10-5=...</td>
      <td>```json\n{\n  "L1": "15 - 5 = 10",\n  "L2": "3...</td>
    </tr>
  </tbody>
</table>

```python
# ===================================================================
# PHASE 2: FINE-TUNE
# ===================================================================

print("\n" + "="*50)
print("PHASE 2: FINE-TUNING")
print("="*50)

# 1. Apply LoRa adapters to the existing model object for training
model = prepare_model_for_lora_training(model)

# 2. Prepare the Hugging Face Dataset for the trainer
train_dataset = create_training_dataset(train_df, tokenizer)

# 3. Run the fine-tuning process
training_stats = run_fine_tuning(model, tokenizer, train_dataset)

print("✅ Fine-tuning complete. The model object in memory is now updated.")
```

    
    ==================================================
    PHASE 2: FINE-TUNING
    ==================================================
    Applying LoRa adapters to the model...


    Unsloth: Dropout = 0 is supported for fast patching. You are using dropout = 0.05.
    Unsloth will patch all other layers, except LoRA matrices, causing a performance hit.


    Unsloth: Making `model.base_model.model.model` require gradients



    Map:   0%|          | 0/701 [00:00<?, ? examples/s]



    Unsloth: Tokenizing ["text"] (num_proc=2):   0%|          | 0/701 [00:00<?, ? examples/s]



    Map (num_proc=12):   0%|          | 0/701 [00:00<?, ? examples/s]


    
    --- Starting fine-tuning for 1 epoch(s) ---


    ==((====))==  Unsloth - 2x faster free finetuning | Num GPUs used = 1
       \\   /|    Num examples = 701 | Num Epochs = 1 | Total steps = 22
    O^O/ \_/ \    Batch size per device = 16 | Gradient accumulation steps = 2
    \        /    Data Parallel GPUs = 1 | Total batch size (16 x 2 x 1) = 32
     "-____-"     Trainable parameters = 13,045,760 of 1,012,931,712 (1.29% trained)
    `use_cache=True` is incompatible with gradient checkpointing. Setting `use_cache=False`.


    Unsloth: Will smartly offload gradients to save VRAM!




    <div>

      <progress value='22' max='22' style='width:300px; height:20px; vertical-align: middle;'></progress>
      [22/22 01:00, Epoch 1/1]
    </div>
    <table border="1" class="dataframe">
  <thead>
 <tr style="text-align: left;">
      <th>Step</th>
      <th>Training Loss</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>0.774000</td>
    </tr>
    <tr>
      <td>2</td>
      <td>0.752700</td>
    </tr>
    <tr>
      <td>3</td>
      <td>0.635100</td>
    </tr>
    <tr>
      <td>4</td>
      <td>0.273200</td>
    </tr>
    <tr>
      <td>5</td>
      <td>0.143000</td>
    </tr>
    <tr>
      <td>6</td>
      <td>0.084600</td>
    </tr>
    <tr>
      <td>7</td>
      <td>0.038700</td>
    </tr>
    <tr>
      <td>8</td>
      <td>0.033400</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.021500</td>
    </tr>
    <tr>
      <td>10</td>
      <td>0.019900</td>
    </tr>
    <tr>
      <td>11</td>
      <td>0.014500</td>
    </tr>
    <tr>
      <td>12</td>
      <td>0.016800</td>
    </tr>
    <tr>
      <td>13</td>
      <td>0.008100</td>
    </tr>
    <tr>
      <td>14</td>
      <td>0.012100</td>
    </tr>
    <tr>
      <td>15</td>
      <td>0.008900</td>
    </tr>
    <tr>
      <td>16</td>
      <td>0.010000</td>
    </tr>
    <tr>
      <td>17</td>
      <td>0.012200</td>
    </tr>
    <tr>
      <td>18</td>
      <td>0.022300</td>
    </tr>
    <tr>
      <td>19</td>
      <td>0.007200</td>
    </tr>
    <tr>
      <td>20</td>
      <td>0.005000</td>
    </tr>
    <tr>
      <td>21</td>
      <td>0.014000</td>
    </tr>
    <tr>
      <td>22</td>
      <td>0.010000</td>
    </tr>
  </tbody>
</table><p>


    
    ✅ Fine-tuning finished! Saving final adapter to /content/experiments/equation_extraction_gemma3-1b-unsloth_20250808_1357/final_adapter
    ✅ Training log saved to: /content/experiments/equation_extraction_gemma3-1b-unsloth_20250808_1357/training_log.csv
    ✅ Fine-tuning complete. The model object in memory is now updated.



```python
# ===================================================================
# PHASE 3: FINAL EVALUATION
# ===================================================================

import gc

print("\n" + "="*50)
print("PHASE 3: FINAL EVALUATION")
print("="*50)

# Run inference with the fine-tuned LoRa model
final_predictions = run_unsloth_inference(
    model=model,
    tokenizer=tokenizer,
    df_to_eval=test_df,
    batch_size=64
)

# Evaluate and save final results
final_results_df, final_metrics = evaluate_predictions(test_df, final_predictions)
final_results_path = Path(CONFIG["output_dir"]) / "final_results" / "final_evaluation_results.csv"
final_metrics_path = Path(CONFIG["output_dir"]) / "final_results" / "final_metrics.json"
final_results_df.to_csv(final_results_path, index=False)
with open(final_metrics_path, 'w') as f:
    json.dump(final_metrics, f, indent=2)

print("\n--- Final Metrics ---")
print(json.dumps(final_metrics, indent=2))
print(f"✅ Final results saved.")

# # --- Clean up ---
# del model, tokenizer, final_predictions, final_results_df
# gc.collect()
# torch.cuda.empty_cache()
```

    
    ==================================================
    PHASE 3: FINAL EVALUATION
    ==================================================
    
    --- Running Unsloth native inference ---


    Inference Batches: 100%|██████████| 3/3 [01:31<00:00, 30.48s/it]
    <string>:1: SyntaxWarning: 'int' object is not callable; perhaps you missed a comma?


    
    --- Final Metrics ---
    {
      "mean_rigorous_score": 0.9353490259740259,
      "total_samples": 176,
      "json_parse_failures": 0,
      "failure_rate": 0.0
    }
    ✅ Final results saved.



```python
# --- FINAL COMPARISON ---
print("\n" + "="*50)
print("PERFORMANCE COMPARISON")
print("="*50)

print("\n--- Baseline Metrics ---")
print(json.dumps(baseline_metrics, indent=2))

print("\n--- Final Fine-Tuned Metrics ---")
print(json.dumps(final_metrics, indent=2))
print("\n" + "="*50)

print("\n✅✅✅ Experiment Complete! ✅✅✅")
```

    
    ==================================================
    PERFORMANCE COMPARISON
    ==================================================
    
    --- Baseline Metrics ---
    {
      "mean_rigorous_score": 0.23005952380952382,
      "total_samples": 176,
      "json_parse_failures": 3,
      "failure_rate": 0.017045454545454544
    }
    
    --- Final Fine-Tuned Metrics ---
    {
      "mean_rigorous_score": 0.9310673701298703,
      "total_samples": 176,
      "json_parse_failures": 0,
      "failure_rate": 0.0
    }
    
    ==================================================
    
    ✅✅✅ Experiment Complete! ✅✅✅



```python
from unsloth import FastModel
from peft import PeftModel
import torch

print("--- Reloading fine-tuned model from local adapter checkpoint ---")

# --- 1. Define the paths from your CONFIG dictionary ---
base_model_name = CONFIG["model_name"]
adapter_path = CONFIG["final_adapter_dir"]

# --- 2. Load the 4-bit base model first ---
# It's crucial to load the original base model that the adapters were trained on.
print(f"Loading base model: {base_model_name}")
model, tokenizer = FastModel.from_pretrained(
    model_name=base_model_name,
    max_seq_length=CONFIG["max_seq_length"],
    dtype=None,
    load_in_4bit=True,
)

# --- 3. Apply your saved LoRa adapters ---
# This merges your fine-tuning into the base model.
print(f"Applying LoRa adapters from: {adapter_path}")
model = PeftModel.from_pretrained(model, adapter_path)

print("\n✅ Model successfully reloaded from checkpoint.")
print("You can now proceed with inference or pushing to the Hub.")
```

    --- Reloading fine-tuned model from local adapter checkpoint ---
    Loading base model: unsloth/gemma-3-1b-it-unsloth-bnb-4bit
    ==((====))==  Unsloth 2025.8.1: Fast Gemma3 patching. Transformers: 4.54.1.
       \\   /|    NVIDIA A100-SXM4-40GB. Num GPUs = 1. Max memory: 39.557 GB. Platform: Linux.
    O^O/ \_/ \    Torch: 2.6.0+cu124. CUDA: 8.0. CUDA Toolkit: 12.4. Triton: 3.2.0
    \        /    Bfloat16 = TRUE. FA [Xformers = 0.0.29.post3. FA2 = False]
     "-____-"     Free license: http://github.com/unslothai/unsloth
    Unsloth: Fast downloading is enabled - ignore downloading bars which are red colored!
    Applying LoRa adapters from: /content/experiments/equation_extraction_gemma3-1b-unsloth_20250808_1357/final_adapter
    
    ✅ Model successfully reloaded from checkpoint.
    You can now proceed with inference or pushing to the Hub.



```python
# ===================================================================
# CELL 11: PUSH ADAPTERS TO HUGGING FACE HUB
# ===================================================================

# --- Configuration ---
# Replace with your Hugging Face username and desired repo name
hf_username = "arvindsuresh-math"
hf_repo_name = "gemma-3-1b-equation-extractor-lora"
commit_message = "Fine-tuned with Unsloth on equation extraction dataset"

# --- Login to Hugging Face ---
# This uses the token you provided at the start of the notebook
from huggingface_hub import login
from google.colab import userdata

# hf_token = userdata.get('HF_TOKEN')
login(token=hf_token)

# --- Push the LoRa adapters ---
# The 'model' object currently in memory is the fine-tuned adapter model
print(f"Pushing LoRa adapters to: {hf_username}/{hf_repo_name}")
model.push_to_hub(f"{hf_username}/{hf_repo_name}", use_auth_token=True, commit_message=commit_message)
tokenizer.push_to_hub(f"{hf_username}/{hf_repo_name}", use_auth_token=True, commit_message=commit_message)

print("✅ Adapters successfully pushed to the Hugging Face Hub.")

### How to use these adapters in your HF Space `app.py`:

# from unsloth import FastModel
# from peft import PeftModel
# import torch

# # Your chosen repo and the original base model
# adapter_repo = "your-hf-username/gemma-3-1b-equation-extractor-lora"
# base_model_name = "unsloth/gemma-3-1b-it-unsloth-bnb-4bit"

# # 1. Load the 4-bit base model
# model, tokenizer = FastModel.from_pretrained(
#     model_name = base_model_name,
#     max_seq_length = 2048,
#     dtype = None,
#     load_in_4bit = True,
# )

# # 2. Apply your fine-tuned adapters
# model = PeftModel.from_pretrained(model, adapter_repo)

# # Now the 'model' is ready for inference
```

    Pushing LoRa adapters to: arvindsuresh-math/gemma-3-1b-equation-extractor-lora


    /usr/local/lib/python3.11/dist-packages/transformers/utils/hub.py:914: FutureWarning: The `use_auth_token` argument is deprecated and will be removed in v5 of Transformers. Please use `token` instead.
      warnings.warn(



    Processing Files (0 / 0)                : |          |  0.00B /  0.00B            



    New Data Upload                         : |          |  0.00B /  0.00B            



      ...pslegnhc5/adapter_model.safetensors:   1%|1         |  569kB / 52.2MB            



    README.md: 0.00B [00:00, ?B/s]



    Processing Files (0 / 0)                : |          |  0.00B /  0.00B            



    New Data Upload                         : |          |  0.00B /  0.00B            



      /tmp/tmphna2dtpg/tokenizer.json       : 100%|##########| 33.4MB / 33.4MB            



      /tmp/tmphna2dtpg/tokenizer.model      : 100%|##########| 4.69MB / 4.69MB            


    ✅ Adapters successfully pushed to the Hugging Face Hub.



```python
import zipfile
from pathlib import Path
import os

print("\n" + "="*50)
print("COMPRESSING RESULTS FOR DOWNLOAD")
print("="*50)

# Define paths from the global CONFIG
output_dir = Path(CONFIG["output_dir"])
experiment_id = CONFIG["experiment_id"]
adapter_path = Path(CONFIG["final_adapter_dir"])

# Define the name and location of the output zip file
zip_path = output_dir / f"{experiment_id}_results.zip"

# List of files and directories to be included in the zip archive
files_to_zip = [
    output_dir / "baseline_results" / "baseline_evaluation_results.csv",
    output_dir / "baseline_results" / "baseline_metrics.json",
    output_dir / "final_results" / "final_evaluation_results.csv",
    output_dir / "final_results" / "final_metrics.json",
    output_dir / "training_log.csv",
    output_dir / "config.json",
]

try:
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        print(f"Creating zip archive at: {zip_path}")
        for file_path in files_to_zip:
            if file_path.exists():
                # The arcname is the path of the file relative to the experiment directory,
                # which keeps the folder structure (e.g., 'baseline_results/...') inside the zip.
                arcname = file_path.relative_to(output_dir)
                zipf.write(file_path, arcname)
                print(f"  - Adding: {arcname}")
            else:
                print(f"  - Skipping (not found): {file_path}")

    print(f"\n✅ Successfully created results zip archive at: {zip_path}")

except Exception as e:
    print(f"\n❌ An error occurred while creating the zip file: {e}")
```

    
    ==================================================
    COMPRESSING RESULTS FOR DOWNLOAD
    ==================================================
    Creating zip archive at: /content/experiments/equation_extraction_gemma3-1b-unsloth_20250808_1357/equation_extraction_gemma3-1b-unsloth_20250808_1357_results.zip
      - Adding: baseline_results/baseline_evaluation_results.csv
      - Adding: baseline_results/baseline_metrics.json
      - Adding: final_results/final_evaluation_results.csv
      - Adding: final_results/final_metrics.json
      - Adding: training_log.csv
      - Adding: config.json
    
    ✅ Successfully created results zip archive at: /content/experiments/equation_extraction_gemma3-1b-unsloth_20250808_1357/equation_extraction_gemma3-1b-unsloth_20250808_1357_results.zip

