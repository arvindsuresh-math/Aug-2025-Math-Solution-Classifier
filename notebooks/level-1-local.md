```python
# --- 1.1 Mount Google Drive to access your data ---
from google.colab import drive
drive.mount('/content/drive')
print("Google Drive mounted successfully.")

# --- 1.2. Install Core Libraries (Revised for Compatibility) ---

# Install the other libraries as before
!pip install -Uq transformers
!pip install -Uq peft
!pip install -Uq trl
!pip install -Uq accelerate
!pip install -Uq datasets
!pip install -Uq bitsandbytes

!pip install flash-attn==2.7.4.post1 \
  --extra-index-url https://download.pytorch.org/whl/cu124 \
  --no-build-isolation

# --- 1.3 Unzip Dataset ---
# This assumes the zip file is in the "My Drive" folder
!unzip -q /content/drive/My\ Drive/level-1-binary.zip -d /content/
print("Dataset unzipped to '/content/level-1-binary'.")
```


```python
# --- 2.1 Define Basic Project Parameters ---
class BasicConfig:
    # The Hugging Face Hub identifier for the model we are fine-tuning.
    MODEL_ID = "microsoft/Phi-4-mini-instruct"

    # The local path to the unzipped dataset we prepared earlier.
    DATASET_PATH = "/content/level-1-binary"

    # The directory where all outputs (checkpoints, logs) will be saved.
    OUTPUT_DIR = "/content/solution-verifier-level1"

# --- 2.2 Define the SFT Configuration ---
from trl import SFTConfig
from datasets import load_from_disk

# --- First, calculate the evaluation steps ---
# Load the dataset to get the number of training samples
temp_dataset = load_from_disk(BasicConfig.DATASET_PATH)
num_train_samples = len(temp_dataset['train'])

# Define batching strategy
batch_size = 8 # 8 for A100
gradient_accumulation_steps = 4 # 4 for A100
effective_batch_size = batch_size * gradient_accumulation_steps

# Calculate steps to evaluate twice per epoch
eval_and_save_steps = num_train_samples // (2 * effective_batch_size)
eval_and_save_steps = max(1, eval_and_save_steps) # Ensure at least one step

print(f"--> Evaluation/Saving will happen every {eval_and_save_steps} steps.")

# --- Now, define the SFTConfig ---
sft_config = SFTConfig(
    # --- Core Training ---
    output_dir=BasicConfig.OUTPUT_DIR,
    num_train_epochs=3,
    learning_rate=2e-4,

    # --- Batching ---
    per_device_train_batch_size=batch_size,
    # per_device_eval_batch_size=batch_size * 2,
    gradient_accumulation_steps=gradient_accumulation_steps,
    per_device_eval_batch_size = 1,
    eval_accumulation_steps    = 1,

    # --- Optimizer & Precision ---
    optim="paged_adamw_8bit",
    bf16=True,

    # --- Dataset & Formatting ---
    # dataset_text_field="text",
    max_length=512,
    packing=False, # We are providing a pre-tokenized dataset, so packing must be False.
    assistant_only_loss=False, # We are creating the mask manually, so we disable the trainer's attempt.

    # --- Loss Calculation ---
    # assistant_only_loss=True, # Automatically mask prompt for loss

    # --- Evaluation & Saving ---
    eval_strategy="steps",
    eval_steps=eval_and_save_steps,
    save_strategy="steps",
    save_steps=eval_and_save_steps,
    save_total_limit=3,
    load_best_model_at_end=True,
    metric_for_best_model="accuracy",
    greater_is_better=True,

    # --- Logging ---
    logging_steps=25,
    report_to="none",
)

# --- 4.1 Define 4-bit Quantization Configuration ---
import torch
from transformers import BitsAndBytesConfig

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_quant_type="nf4"
)

# --- 4.3 Load and Configure the Tokenizer ---
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    BasicConfig.MODEL_ID,
    trust_remote_code=True
)

# Set padding token if it's not already set
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# --- 3.1 & 3.2. Tokenize Dataset and Create Manual Assistant Mask ---
from datasets import load_from_disk
import numpy as np

# Load the raw dataset
raw_dataset = load_from_disk(BasicConfig.DATASET_PATH)

# Get the token ID for the assistant tag to find where the response starts
# We use add_special_tokens=False to get the raw token ID
assistant_token_id = tokenizer.convert_tokens_to_ids("<|assistant|>")

def process_and_tokenize(sample):
    """
    1. Formats the sample into a structured list of messages.
    2. Tokenizes the messages using the chat template.
    3. Manually creates an 'assistant_mask'.
    """
    # Create the structured message format
    system_prompt = "Analyze the following mathematical problem and solution to determine if the solution is correct (0) or flawed (1)."
    user_input = f"### Problem:\n{sample['question']}\n\n### Solution:\n{sample['solution']}"
    label = str(sample['label'])
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input},
        {"role": "assistant", "content": label},
    ]

    # Tokenize the entire conversation
    tokenized_output = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=False, # We are providing the full conversation
        return_tensors=None, # Return list of ints
        truncation=True,
        max_length=sft_config.max_length,
    )

    # Find the start of the assistant's response
    # The mask should start *after* the <|assistant|> token
    input_ids_array = np.array(tokenized_output)
    assistant_indices = np.where(input_ids_array == assistant_token_id)[0]

    assistant_mask = np.zeros_like(input_ids_array)
    if len(assistant_indices) > 0:
        # The mask starts one position AFTER the assistant token
        mask_start_index = assistant_indices[0] + 1
        assistant_mask[mask_start_index:] = 1

    return {
        "input_ids": tokenized_output,
        "attention_mask": [1] * len(tokenized_output),
        "assistant_masks": list(assistant_mask),
    }


# Apply the new processing function to the dataset
formatted_dataset = raw_dataset.map(
    process_and_tokenize,
    remove_columns=raw_dataset['train'].column_names
)

print("--- Dataset pre-tokenized with manual assistant masks ---")
print(formatted_dataset)
```


```python
# --- 4.2 Load the 4-bit Quantized Model ---
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained(
    BasicConfig.MODEL_ID,
    quantization_config=quantization_config,
    device_map="auto",
    trust_remote_code=True,
    attn_implementation="flash_attention_2"
)

# --- 4.5 Prepare Quantized Model for Training ---
from peft import prepare_model_for_kbit_training

model = prepare_model_for_kbit_training(model)

# --- 4.6 Configure LoRA Adapters ---
from peft import LoraConfig

lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    lora_dropout=0.05,
    bias="none",
    target_modules="all-linear",
    task_type="CAUSAL_LM",
)

# --- 5.1 Define the Metrics Calculation Function ---
import numpy as np
from transformers import EvalPrediction

def compute_metrics(p: EvalPrediction):
    """
    Computes accuracy on the final, unmasked token of each sequence.
    """
    # The first element of p.predictions is the logits matrix
    logits = p.predictions[0]
    labels = p.label_ids

    # Find the index of the last non-masked token for each sequence.
    # A label of -100 is a masked token, so we find the last position that is not -100.
    last_token_indices = np.array([np.where(row != -100)[0][-1] for row in labels])

    # Extract the logits for the target tokens
    last_token_logits = logits[np.arange(len(last_token_indices)), last_token_indices]

    # Get the predictions by taking the argmax of the logits
    predictions = last_token_logits.argmax(axis=-1)

    # Get the ground truth labels for the same tokens
    ground_truth_labels = labels[np.arange(len(last_token_indices)), last_token_indices]

    # Calculate accuracy
    accuracy = np.mean(predictions == ground_truth_labels)

    return {"accuracy": accuracy}

import torch
from transformers import DataCollatorWithPadding

class SFTCollatorWithMask(DataCollatorWithPadding):
    """
    1. Removes `assistant_masks` before calling tokenizer.pad()
       (so pad() sees only uniform-length keys).
    2. Pads `assistant_masks` to the batch max length.
    3. Builds `labels` where loss is computed only on assistant tokens.
    """

    def __call__(self, features, return_tensors: str = "pt"):
        # ---- separate the masks ------------------------------------------
        masks = [f.pop("assistant_masks") for f in features]   # remove key

        # ---- pad input_ids & attention_mask normally ---------------------
        batch = self.tokenizer.pad(
            features,
            padding=True,
            return_tensors="pt",
        )

        # ---- pad assistant_masks to match new seq length -----------------
        max_len = batch["input_ids"].size(1)
        padded_masks = [
            m + [0] * (max_len - len(m)) if len(m) < max_len else m[:max_len]
            for m in masks
        ]
        batch["assistant_masks"] = torch.tensor(padded_masks, dtype=torch.long)

        # ---- build labels -----------------------------------------------
        labels = batch["input_ids"].clone()
        labels[batch["assistant_masks"] == 0] = -100   # ignore prompt tokens
        batch["labels"] = labels

        return batch


from trl import SFTTrainer

data_collator = SFTCollatorWithMask(tokenizer)

trainer = SFTTrainer(
    model            = model,
    args             = sft_config,          # the TrainingArguments you built
    train_dataset    = formatted_dataset["train"],
    eval_dataset     = formatted_dataset["validation"],
    peft_config      = lora_config,
    data_collator    = data_collator,       # ← our new collator
    compute_metrics  = compute_metrics,
)
```
