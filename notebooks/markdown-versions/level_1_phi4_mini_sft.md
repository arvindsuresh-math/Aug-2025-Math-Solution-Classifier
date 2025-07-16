Initial setup


```python
# --- 1. Mount Google Drive to access your data ---
from google.colab import drive
drive.mount('/content/drive')
print("Google Drive mounted successfully.")
```

    Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount("/content/drive", force_remount=True).
    Google Drive mounted successfully.



```python
# --- 2. Install required libraries ---
# We install the latest versions for compatibility with new models.
!pip install -Uq transformers peft trl accelerate datasets
!pip install -Uq bitsandbytes
!pip install -q --upgrade fsspec # Resolve dependency conflicts
print("Required libraries installed and dependencies reconciled.")
```

    [31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
    gcsfs 2025.3.2 requires fsspec==2025.3.2, but you have fsspec 2025.3.0 which is incompatible.[0m[31m
    [0m[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
    datasets 4.0.0 requires fsspec[http]<=2025.3.0,>=2023.1.0, but you have fsspec 2025.7.0 which is incompatible.
    gcsfs 2025.3.2 requires fsspec==2025.3.2, but you have fsspec 2025.7.0 which is incompatible.[0m[31m
    [0mRequired libraries installed and dependencies reconciled.



```python
# --- 3. Unzip your dataset from Google Drive ---
# This assumes you uploaded 'level-1-binary.zip' to the root of your Drive.
!unzip -q /content/drive/My\ Drive/level-1-binary.zip -d /content/
print("Dataset unzipped successfully to '/content/level-1-binary'.")
```

    replace /content/__MACOSX/._level-1-binary? [y]es, [n]o, [A]ll, [N]one, [r]ename: A
    Dataset unzipped successfully to '/content/level-1-binary'.


Configuration


```python
class Config:
    # --- Model and Tokenizer ---
    MODEL_ID = "microsoft/Phi-4-mini-instruct"
    # --- Path to save the base model in Google Drive ---
    MODEL_SAVE_PATH = "/content/drive/My Drive/phi-4-mini-base-model"

    # --- Dataset ---
    DATASET_PATH = "/content/level-1-binary"

    # --- Fine-Tuning Output ---
    OUTPUT_DIR = "/content/solution-verifier-level1"

    # LoRA Config
    LORA_R = 16
    LORA_ALPHA = 32
    LORA_DROPOUT = 0.05
    LORA_TARGET_MODULES = "all-linear"

    # Training Config
    LEARNING_RATE = 2e-4
    NUM_EPOCHS = 5
    BATCH_SIZE = 8
    GRADIENT_ACCUMULATION_STEPS = 1
    LOGGING_STEPS = 10
    SAVE_STEPS = 500
    MAX_SEQ_LENGTH = 1024
```

Load and prepare the dataset


```python
from datasets import load_from_disk

def format_prompt(example):
    """Formats a data sample into the required 'text' field for SFTTrainer."""
    return {
        "text": f"""Analyze the following mathematical problem and solution to determine if the solution is correct or flawed.

### Problem:
{example['question']}

### Solution:
{example['solution']}

### Analysis:
{example['label']}"""
    }

# Load from disk
sft_dataset = load_from_disk(Config.DATASET_PATH)

# Apply formatting and remove original columns
formatted_dataset = sft_dataset.map(
    format_prompt,
    remove_columns=sft_dataset['train'].column_names
)

print("--- Dataset formatted and ready for training ---")
print(formatted_dataset)
print("\nExample of a formatted training sample:")
print(formatted_dataset['train'][0]['text'])
```

    --- Dataset formatted and ready for training ---
    DatasetDict({
        train: Dataset({
            features: ['text'],
            num_rows: 3296
        })
        validation: Dataset({
            features: ['text'],
            num_rows: 412
        })
        test: Dataset({
            features: ['text'],
            num_rows: 412
        })
    })
    
    Example of a formatted training sample:
    Analyze the following mathematical problem and solution to determine if the solution is correct or flawed.
    
    ### Problem:
    Sally earned $1000 at work last month. This month, she received a 10% raise. How much money will she make in total for the two months?
    
    ### Solution:
    This month she will earn $1000 * (10/100) = $<<1000*(10/100)=100>>100.
    In total, she will make $1000 + $100 = $<<1000+100=1100>>1100.
    #### 1100
    
    ### Analysis:
    1


Load Base Model and Tokenizer


```python
import torch
import gc

def clear_gpu_memory():
    """
    Deletes major model and trainer objects, forces garbage collection,
    and empties the PyTorch CUDA cache to free up GPU memory.
    """
    print("--- Clearing GPU Memory ---")

    # Check if variables exist in the global scope before trying to delete
    variables_to_delete = ['model', 'trainer', 'peft_model', 'eval_model', 'base_model']
    for var_name in variables_to_delete:
        if var_name in globals():
            del globals()[var_name]
            print(f"Deleted '{var_name}'")

    # Force garbage collection
    print("Collecting garbage...")
    gc.collect()

    # Empty the PyTorch CUDA cache
    if torch.cuda.is_available():
        print("Emptying CUDA cache...")
        torch.cuda.empty_cache()
        print("--- GPU Memory Cleared ---")

        # Print a summary to confirm
        print(torch.cuda.memory_summary(device=None, abbreviated=False))
    else:
        print("No CUDA device found.")

# --- Example of how to call the function ---
# You would run this line in a cell by itself after a run fails.
clear_gpu_memory()
```

    --- Clearing GPU Memory ---
    Collecting garbage...
    Emptying CUDA cache...
    --- GPU Memory Cleared ---
    |===========================================================================|
    |                  PyTorch CUDA memory summary, device ID 0                 |
    |---------------------------------------------------------------------------|
    |            CUDA OOMs: 0            |        cudaMalloc retries: 0         |
    |===========================================================================|
    |        Metric         | Cur Usage  | Peak Usage | Tot Alloc  | Tot Freed  |
    |---------------------------------------------------------------------------|
    | Allocated memory      |      0 B   |      0 B   |      0 B   |      0 B   |
    |       from large pool |      0 B   |      0 B   |      0 B   |      0 B   |
    |       from small pool |      0 B   |      0 B   |      0 B   |      0 B   |
    |---------------------------------------------------------------------------|
    | Active memory         |      0 B   |      0 B   |      0 B   |      0 B   |
    |       from large pool |      0 B   |      0 B   |      0 B   |      0 B   |
    |       from small pool |      0 B   |      0 B   |      0 B   |      0 B   |
    |---------------------------------------------------------------------------|
    | Requested memory      |      0 B   |      0 B   |      0 B   |      0 B   |
    |       from large pool |      0 B   |      0 B   |      0 B   |      0 B   |
    |       from small pool |      0 B   |      0 B   |      0 B   |      0 B   |
    |---------------------------------------------------------------------------|
    | GPU reserved memory   |      0 B   |      0 B   |      0 B   |      0 B   |
    |       from large pool |      0 B   |      0 B   |      0 B   |      0 B   |
    |       from small pool |      0 B   |      0 B   |      0 B   |      0 B   |
    |---------------------------------------------------------------------------|
    | Non-releasable memory |      0 B   |      0 B   |      0 B   |      0 B   |
    |       from large pool |      0 B   |      0 B   |      0 B   |      0 B   |
    |       from small pool |      0 B   |      0 B   |      0 B   |      0 B   |
    |---------------------------------------------------------------------------|
    | Allocations           |       0    |       0    |       0    |       0    |
    |       from large pool |       0    |       0    |       0    |       0    |
    |       from small pool |       0    |       0    |       0    |       0    |
    |---------------------------------------------------------------------------|
    | Active allocs         |       0    |       0    |       0    |       0    |
    |       from large pool |       0    |       0    |       0    |       0    |
    |       from small pool |       0    |       0    |       0    |       0    |
    |---------------------------------------------------------------------------|
    | GPU reserved segments |       0    |       0    |       0    |       0    |
    |       from large pool |       0    |       0    |       0    |       0    |
    |       from small pool |       0    |       0    |       0    |       0    |
    |---------------------------------------------------------------------------|
    | Non-releasable allocs |       0    |       0    |       0    |       0    |
    |       from large pool |       0    |       0    |       0    |       0    |
    |       from small pool |       0    |       0    |       0    |       0    |
    |---------------------------------------------------------------------------|
    | Oversize allocations  |       0    |       0    |       0    |       0    |
    |---------------------------------------------------------------------------|
    | Oversize GPU segments |       0    |       0    |       0    |       0    |
    |===========================================================================|
    



```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from pathlib import Path

print("Imports worked.")

# --- FIX: Define the 4-bit quantization configuration for QLoRA ---
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_quant_type="nf4"
)

# We do not need to cache the quantized model, as it must be loaded this way each time.
print(f"--- Downloading and loading model in 4-bit (QLoRA)... ---")
model = AutoModelForCausalLM.from_pretrained(
    Config.MODEL_ID,
    quantization_config=quantization_config, # Apply the 4-bit config
    device_map="auto", # device_map is efficient with quantization
    trust_remote_code=True,
    # attn_implementation="flash_attention_2"
)

model.gradient_checkpointing_disable()


tokenizer = AutoTokenizer.from_pretrained(
    Config.MODEL_ID,
    trust_remote_code=True
)

# --- Configure the tokenizer's padding token ---
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

print("\n--- Base model (4-bit) and tokenizer are ready ---")
```

    Imports worked.
    --- Downloading and loading model in 4-bit (QLoRA)... ---


    /usr/local/lib/python3.11/dist-packages/huggingface_hub/utils/_auth.py:94: UserWarning: 
    The secret `HF_TOKEN` does not exist in your Colab secrets.
    To authenticate with the Hugging Face Hub, create a token in your settings tab (https://huggingface.co/settings/tokens), set it as secret in your Google Colab and restart your session.
    You will be able to reuse this secret in all of your notebooks.
    Please note that authentication is recommended but still optional to access public models or datasets.
      warnings.warn(



    Loading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]


    
    --- Base model (4-bit) and tokenizer are ready ---



```python
 # import torch
# from transformers import AutoModelForCausalLM, AutoTokenizer
# from pathlib import Path

# # --- Check if the model is already saved in Google Drive ---
# model_save_path = Path(Config.MODEL_SAVE_PATH)

# if model_save_path.exists():
#     print(f"--- Loading model and tokenizer from Google Drive: {model_save_path} ---")
#     model = AutoModelForCausalLM.from_pretrained(
#         model_save_path,
#         torch_dtype=torch.bfloat16,
#         trust_remote_code=True
#         # device_map="auto" is removed
#     )
#     tokenizer = AutoTokenizer.from_pretrained(
#         model_save_path,
#         trust_remote_code=True
#     )
# else:
#     print(f"--- Model not found in Google Drive. Downloading from Hugging Face Hub... ---")
#     model = AutoModelForCausalLM.from_pretrained(
#         Config.MODEL_ID,
#         torch_dtype=torch.bfloat16,
#         trust_remote_code=True
#         # device_map="auto" is removed
#     )
#     tokenizer = AutoTokenizer.from_pretrained(
#         Config.MODEL_ID,
#         trust_remote_code=True
#     )

#     print(f"--- Saving model and tokenizer to Google Drive for future use... ---")
#     model_save_path.mkdir(parents=True, exist_ok=True)
#     model.save_pretrained(model_save_path)
#     tokenizer.save_pretrained(model_save_path)

# # --- Configure the tokenizer's padding token ---
# if tokenizer.pad_token is None:
#     tokenizer.pad_token = tokenizer.eos_token
# tokenizer.padding_side = "right"

# print("\n--- Base model and tokenizer are ready ---")
```


```python
import numpy as np
from transformers import EvalPrediction

# Get the token IDs for the labels "0" and "1"
# We are interested in the actual token ID, not the special start/end tokens.
# The exact index [0] or [1] might vary based on tokenizer, but for single chars it's usually the first non-special token.
label_0_token_id = tokenizer("0", add_special_tokens=False).input_ids[0]
label_1_token_id = tokenizer("1", add_special_tokens=False).input_ids[0]


def compute_metrics(p: EvalPrediction):
    """
    Accuracy on the **last real token** of each sequence.
    Works whether p.predictions / p.label_ids come in as
    NumPy arrays (Trainer default) or torch tensors.
    """

    # --- ensure torch tensors on CPU ---
    logits = (torch.from_numpy(p.predictions)
              if isinstance(p.predictions, np.ndarray) else
              p.predictions).cpu()           # (B, L, V)
    labels = (torch.from_numpy(p.label_ids)
              if isinstance(p.label_ids, np.ndarray) else
              p.label_ids).cpu()             # (B, L)

    # length of each sequence *before* padding (-100 marks padding)
    seq_lens = (labels != -100).sum(dim=1) - 1      # (B,)

    # gather logits and labels at that position
    batch_idx = torch.arange(logits.size(0))
    last_logits = logits[batch_idx, seq_lens]        # (B, V)
    gold        = labels[batch_idx, seq_lens]        # (B,)

    preds = last_logits.argmax(dim=-1)               # (B,)
    accuracy = (preds == gold).float().mean().item()

    # free memory early (optional)
    del logits, labels, last_logits
    return {"accuracy": accuracy}

print("Metrics computation function is ready.")
print(f"Token ID for '0': {label_0_token_id}")
print(f"Token ID for '1': {label_1_token_id}")
```

    Metrics computation function is ready.
    Token ID for '0': 15
    Token ID for '1': 16


Configure Fine-Tuning parameters


```python
from peft import LoraConfig, prepare_model_for_kbit_training

# --- FIX: Add this crucial step to prepare the quantized model for training ---
model = prepare_model_for_kbit_training(model)

# Define LoRA Configuration
peft_config = LoraConfig(
    r=8,  # A smaller rank is fine for QLoRA and saves additional memory
    lora_alpha=16, # Typically 2*r
    lora_dropout=Config.LORA_DROPOUT,
    target_modules=Config.LORA_TARGET_MODULES,
    bias="none",
    task_type="CAUSAL_LM",
)

print("--- LoRA Configuration defined ---")
```

    --- LoRA Configuration defined ---



```python
from transformers import TrainingArguments

# # Define Training Arguments with Evaluation and Early Stopping
# training_args = TrainingArguments(
#     output_dir=Config.OUTPUT_DIR,
#     num_train_epochs=Config.NUM_EPOCHS,
#     per_device_train_batch_size=Config.BATCH_SIZE,
#     gradient_accumulation_steps=Config.GRADIENT_ACCUMULATION_STEPS,
#     learning_rate=Config.LEARNING_RATE,
#     logging_steps=Config.LOGGING_STEPS,
#     fp16=False,
#     bf16=True,
#     report_to="none",
#     # --- START FIX ---
#     # To load the best model, saving and evaluation must happen at the same interval.
#     save_steps=200,
#     eval_steps=200,
#     eval_strategy="steps",   # match save_strategy
#     save_strategy="steps",         # both are "steps"
#     save_total_limit=3,
#     load_best_model_at_end=True,
#     metric_for_best_model="accuracy", # Specify the metric to monitor
#     greater_is_better=True, # Higher accuracy is better
#     per_device_eval_batch_size = 4,
#     eval_accumulation_steps   = 1
#     # --- END FIX ---
# )

training_args = TrainingArguments(
    output_dir                 = Config.OUTPUT_DIR,
    num_train_epochs           = Config.NUM_EPOCHS,
    learning_rate              = Config.LEARNING_RATE,
    fp16                       = False,
    # logging & evaluation strategies

    # --- speed vs memory ---
    per_device_train_batch_size= 4,    # was 1
    gradient_accumulation_steps= 1,    # net batch = 4
    per_device_eval_batch_size = 8,
    eval_accumulation_steps    = 2,

    # logging / saving
    eval_strategy        = "steps",
    save_strategy              = "steps",
    eval_steps                 = 200,
    save_steps                 = 200,
    save_total_limit           = 3,
    load_best_model_at_end     = True,
    metric_for_best_model      = "accuracy",
    greater_is_better          = True,
    gradient_checkpointing      = False,
    include_inputs_for_metrics = True, # ensures

    # precision & perf
    bf16                       = True,
    tf32                       = True,              # needs nightly or torch>=2.3
    optim                      = "paged_adamw_8bit",
    report_to                  = "none",
    logging_steps              = 50
)

# After loading the model (4-bit LoRA)
model.gradient_checkpointing_disable()
model.config.use_cache = False

print("--- training args configured for QLoRA ---")
```

    Using `include_inputs_for_metrics` is deprecated and will be removed in version 5 of 🤗 Transformers. Please use `include_for_metrics` list argument instead.


    --- training args configured for QLoRA ---


Initialize trainer


```python
from trl import SFTTrainer

# Initialize the SFTTrainer
trainer = SFTTrainer(
    model=model,
    args=training_args,
    train_dataset=formatted_dataset["train"],
    # --- START MODIFICATION ---
    eval_dataset=formatted_dataset["validation"], # Pass the validation set
    compute_metrics=compute_metrics, # Pass the metrics function
    # --- END MODIFICATION ---
    peft_config=peft_config,
    # max_seq_length=Config.MAX_SEQ_LENGTH,
)


```

    Using `include_inputs_for_metrics` is deprecated and will be removed in version 5 of 🤗 Transformers. Please use `include_for_metrics` list argument instead.
    Using `include_inputs_for_metrics` is deprecated and will be removed in version 5 of 🤗 Transformers. Please use `include_for_metrics` list argument instead.
    No label_names provided for model class `PeftModelForCausalLM`. Since `PeftModel` hides base models input arguments, if label_names is not given, label_names can't be set automatically within `Trainer`. Note that empty label_names list will be used instead.


Train it!


```python
# Start the fine-tuning process
print("--- Starting Fine-Tuning with in-training evaluation ---")
trainer.train()
print("--- Fine-Tuning Complete ---")
```

    --- Starting Fine-Tuning with in-training evaluation ---




    <div>

      <progress value='201' max='4120' style='width:300px; height:20px; vertical-align: middle;'></progress>
      [ 201/4120 01:09 < 22:54, 2.85 it/s, Epoch 0.24/5]
    </div>
    <table border="1" class="dataframe">
  <thead>
 <tr style="text-align: left;">
      <th>Step</th>
      <th>Training Loss</th>
      <th>Validation Loss</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table><p>
    <div>

      <progress value='20' max='52' style='width:300px; height:20px; vertical-align: middle;'></progress>
      [20/52 01:55 < 03:14, 0.16 it/s]
    </div>



Save Final Adapter Model


```python
final_model_path = f"{Config.OUTPUT_DIR}/final_model"
trainer.save_model(final_model_path)
print(f"Final adapter model saved to {final_model_path}")
```

Load trained model for inference


```python
from peft import PeftModel

# Load the base model again (fast, from cache)
base_model = AutoModelForCausalLM.from_pretrained(
    Config.MODEL_ID,
    torch_dtype=torch.bfloat16,
    device_map=None,
    trust_remote_code=True
)
```


```python
print(f"--- Loading fine-tuned adapter from: {final_model_path} ---")
# Load the LoRA adapter
peft_model = PeftModel.from_pretrained(base_model, final_model_path)
```


```python
print("--- Merging adapter weights into base model ---")
# --- FIX: Merge the adapter weights and unload the PEFT model ---
# This returns a standard AutoModelForCausalLM object.
eval_model = peft_model.merge_and_unload()
```


```python
print("--- Moving final model to GPU for evaluation ---")
# --- FIX: Explicitly move the final, merged model to the GPU ---
eval_model.to("cuda")
```


```python
# The tokenizer is the same one we loaded earlier
eval_tokenizer = tokenizer

print("--- Trained model ready for evaluation ---")
```

Run evaluation


```python
from tqdm import tqdm
import re

eval_dataset = sft_dataset["validation"]
correct_predictions = 0
total_predictions = len(eval_dataset)

print(f"\n--- Evaluating model on {total_predictions} validation samples ---")

for i in tqdm(range(total_predictions)):
    sample = eval_dataset[i]

    prompt_text = f"""Analyze the following mathematical problem and solution to determine if the solution is correct or flawed.

### Problem:
{sample['question']}

### Solution:
{sample['solution']}

### Analysis:
"""

    inputs = eval_tokenizer(prompt_text, return_tensors="pt").to("cuda")

    with torch.no_grad():
        outputs = eval_model.generate(
            **inputs, max_new_tokens=5, eos_token_id=eval_tokenizer.eos_token_id
        )

    full_output_text = eval_tokenizer.decode(outputs[0], skip_special_tokens=True)
    generated_text = full_output_text[len(prompt_text):].strip()

    match = re.search(r'\d', generated_text)
    prediction = match.group(0) if match else None

    if prediction == str(sample['label']):
        correct_predictions += 1

accuracy = (correct_predictions / total_predictions) * 100
print(f"\n--- Evaluation Complete ---")
print(f"Correct Predictions: {correct_predictions} / {total_predictions}")
print(f"Validation Accuracy: {accuracy:.2f}%")
```


```python

```
