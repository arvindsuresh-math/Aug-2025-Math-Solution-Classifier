### ## Experiment 2: Per-Line Error Detection

This notebook refines our approach to error detection. Instead of simply classifying a solution as `correct` or `incorrect`, the goal is to pinpoint the **exact line** where the first logical error occurs.

### ### Previous Strategy: Sequence Classification

Our initial method treated the task as a standard binary sequence classification problem.

* **Process**: The model processed the entire `problem + solution` text and used the hidden state of the **final token** as a representation of the whole sequence. A classifier head then predicted one of two labels: `0` (correct) or `1` (incorrect).
* **Limitation**: This approach tells us *if* a solution is flawed, but provides no information about *where* the error is.

### ### New Strategy: Per-Line Classification

The new strategy re-frames the problem as a **sequence labeling** task, enabling a more granular analysis.

* **Process**:
    1.  The model processes the full `problem + solution` text in a single forward pass.
    2.  We identify and select the hidden state at the end of **each line** (specifically, at each `\n` token).
    3.  A single, shared classifier head is applied in parallel to each of these selected hidden states.
    4.  This yields a sequence of logits, one for each line. Each logit represents the model's confidence that its corresponding line contains the first error.
    5.  The model is trained using a per-line binary loss, learning to output a high value for the single correct error line and low values for all other lines.

### ### Key Differences

| Feature | Previous Strategy (Sequence Classification) | New Strategy (Per-Line Classification) |
| :--- | :--- | :--- |
| **Goal** | Is the solution correct or incorrect? | Which line contains the first error? |
| **Output** | A single prediction for the entire solution. | A prediction *for each line* of the solution. |
| **Model Input** | Hidden state of the **final token**. | Hidden states of **all line-end tokens**. |
| **Label Format** | A single integer (`0` or `1`). | A sequence of binary labels (`[0, 0, 1, 0, ...]`). |
| **Advantage**| Simple to implement. | Provides granular, interpretable feedback. |

> **Note**: This advanced strategy requires a dataset with line-level labels. The code assumes your dataset contains a `first_error_line` column indicating the index of the first incorrect line, or `-1` if the solution is correct.


```python
# ==============================================================================
# Cell 1: Setup and Installations
# (No changes from your original script)
# ==============================================================================
from google.colab import drive
drive.mount('/content/drive')

!pip install -Uq transformers peft trl accelerate datasets bitsandbytes
!pip install flash-attn --no-build-isolation

!unzip -q -o /content/drive/My\ Drive/level-1-binary.zip -d /content/
```


```python
# ==============================================================================
# Cell 2: Project Configuration
# ==============================================================================
class Config:
    """
    Holds all static configuration for the project.
    """
    # Model ID from Hugging Face Hub
    MODEL_ID = "microsoft/phi-4-mini-instruct"

    # Local path to the unzipped dataset
    DATASET_PATH = "/content/level-1-binary"

    # Directory for saving the final model adapter
    OUTPUT_DIR = "/content/level1-line-classifier-output"

    # The head outputs one logit per line for binary (is/is_not_error) classification
    NUM_LABELS = 1
```


```python
# ==============================================================================
# Cell 3: Tokenizer and Dataset Loading
# ==============================================================================
from datasets import load_from_disk
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(Config.MODEL_ID, trust_remote_code=True)
tokenizer.padding_side = "left"
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Find the ID for the newline token, which we'll use to locate line breaks
newline_token_id = tokenizer.encode("\n", add_special_tokens=False)[0]

# Load the raw dataset from disk
raw_dataset = load_from_disk(Config.DATASET_PATH)

print("Tokenizer and raw dataset loaded successfully.")
```


```python
# ==============================================================================
# Cell 4: Preprocessing Function Definition
# ==============================================================================
def preprocess_for_line_detection(examples):
    """
    Prepares the dataset for line-level error detection.

    This function formats the input text, tokenizes it, finds the indices
    of all line-endings, and creates a per-line binary label sequence.

    Args:
        examples (dict): A batch of examples from the Hugging Face dataset.
                         It's expected to have 'question', 'solution', and
                         'first_error_line' columns.

    Returns:
        dict: A dictionary containing the tokenized inputs, attention masks,
              the calculated line-end indices, and the per-line labels.
    """
    system_prompt = "Analyze the following mathematical problem and solution to determine if the solution is correct or flawed."
    input_texts = [
        f"{system_prompt}\n\n### Problem:\n{q}\n\n### Solution:\n{s}"
        for q, s in zip(examples["question"], examples["solution"])
    ]
    
    tokenized_outputs = tokenizer(
        input_texts,
        truncation=True,
        max_length=512,
        padding=False
    )

    all_line_end_indices = []
    for input_ids in tokenized_outputs["input_ids"]:
        indices = [i for i, token_id in enumerate(input_ids) if token_id == newline_token_id]
        all_line_end_indices.append(indices)
    
    tokenized_outputs["line_end_indices"] = all_line_end_indices

    per_line_labels = []
    # This assumes your dataset has a 'first_error_line' column.
    for i, error_line in enumerate(examples["first_error_line"]):
        num_lines = len(all_line_end_indices[i])
        labels = [0] * num_lines
        if error_line != -1 and error_line < num_lines:
            labels[error_line] = 1
        per_line_labels.append(labels)
    
    tokenized_outputs["labels"] = per_line_labels
    
    return tokenized_outputs
```


```python
# ==============================================================================
# Cell 4: Preprocessing Function Definition
# ==============================================================================
def preprocess_for_line_detection(examples):
    """
    Prepares the dataset for line-level error detection.

    This function formats the input text, tokenizes it, finds the indices
    of all line-endings, and creates a per-line binary label sequence.

    Args:
        examples (dict): A batch of examples from the Hugging Face dataset.
                         It's expected to have 'question', 'solution', and
                         'first_error_line' columns.

    Returns:
        dict: A dictionary containing the tokenized inputs, attention masks,
              the calculated line-end indices, and the per-line labels.
    """
    system_prompt = "Analyze the following mathematical problem and solution to determine if the solution is correct or flawed."
    input_texts = [
        f"{system_prompt}\n\n### Problem:\n{q}\n\n### Solution:\n{s}"
        for q, s in zip(examples["question"], examples["solution"])
    ]
    
    tokenized_outputs = tokenizer(
        input_texts,
        truncation=True,
        max_length=512,
        padding=False
    )

    all_line_end_indices = []
    for input_ids in tokenized_outputs["input_ids"]:
        indices = [i for i, token_id in enumerate(input_ids) if token_id == newline_token_id]
        all_line_end_indices.append(indices)
    
    tokenized_outputs["line_end_indices"] = all_line_end_indices

    per_line_labels = []
    # This assumes your dataset has a 'first_error_line' column.
    for i, error_line in enumerate(examples["first_error_line"]):
        num_lines = len(all_line_end_indices[i])
        labels = [0] * num_lines
        if error_line != -1 and error_line < num_lines:
            labels[error_line] = 1
        per_line_labels.append(labels)
    
    tokenized_outputs["labels"] = per_line_labels
    
    return tokenized_outputs
```


```python
# ==============================================================================
# Cell 5: Apply Preprocessing and Finalize Dataset
# ==============================================================================
from datasets import concatenate_datasets, DatasetDict

print("Applying preprocessing to the dataset...")
tokenized_dataset = raw_dataset.map(
    preprocess_for_line_detection,
    batched=True,
    # Keep `first_error_line` for metrics, remove the original binary `label`
    remove_columns=["question", "solution", "label"]
)

# Merge train and validation splits for a larger training set
full_train_dataset = concatenate_datasets(
    [tokenized_dataset["train"], tokenized_dataset["validation"]]
)
final_dataset = DatasetDict({
    "train": full_train_dataset,
    "test": tokenized_dataset["test"]
})

print("\n--- Preprocessing for line detection complete ---")
print(final_dataset)
```


```python
# ==============================================================================
# Cell 6: Custom Data Collator
# ==============================================================================
import torch
from dataclasses import dataclass
from transformers import AutoTokenizer

@dataclass
class DataCollatorForLineClassification:
    """
    A data collator that handles padding for our custom line-level task.

    It pads `input_ids`, `attention_mask`, `line_end_indices`, and `labels`
    to the maximum length in each batch.
    """
    tokenizer: AutoTokenizer
    padding_value: int = -100  # Standard value to ignore in loss functions

    def __call__(self, features):
        batch = {}
        
        # Use the tokenizer's default padding for inputs and attention mask
        padded_inputs = self.tokenizer.pad(
            [{"input_ids": f["input_ids"], "attention_mask": f["attention_mask"]} for f in features],
            return_tensors="pt"
        )
        batch["input_ids"] = padded_inputs["input_ids"]
        batch["attention_mask"] = padded_inputs["attention_mask"]
        
        # Manually pad our custom fields
        max_lines = max(len(f["line_end_indices"]) for f in features)
        
        padded_line_indices = []
        padded_labels = []
        
        for f in features:
            line_indices = f["line_end_indices"]
            labels = f["labels"]
            
            padded_line_indices.append(line_indices + [self.padding_value] * (max_lines - len(line_indices)))
            padded_labels.append(labels + [self.padding_value] * (max_lines - len(labels)))

        batch["line_end_indices"] = torch.tensor(padded_line_indices, dtype=torch.long)
        batch["labels"] = torch.tensor(padded_labels, dtype=torch.float)
        
        # Keep the original `first_error_line` index for the metrics calculation
        if "first_error_line" in features[0]:
            batch["first_error_line"] = torch.tensor([f["first_error_line"] for f in features], dtype=torch.long)

        return batch
```


```python
# ==============================================================================
# Cell 7: Custom Model Definition
# ==============================================================================
import torch.nn as nn
import torch.nn.functional as F
from transformers import AutoModelForCausalLM
from peft import PeftModel

class GPTLineErrorDetector(nn.Module):
    """
    A custom model wrapper for line-level error detection.

    This model uses a pre-trained transformer backbone and applies a shared
    linear classifier head to the hidden state of each line-ending token.
    """
    def __init__(self, base_model: PeftModel, num_labels: int):
        super().__init__()
        self.base = base_model
        hidden_size = base_model.config.hidden_size
        self.classifier = nn.Linear(hidden_size, num_labels, bias=True)

    def forward(self, input_ids=None, attention_mask=None, line_end_indices=None, labels=None, **kw):
        """
        Defines the forward pass of the model.

        Args:
            input_ids (torch.Tensor): Padded token IDs for the batch.
            attention_mask (torch.Tensor): Attention mask for the batch.
            line_end_indices (torch.Tensor): Padded indices of line-end tokens.
            labels (torch.Tensor): Padded per-line binary labels.

        Returns:
            dict: A dictionary containing the loss (if labels are provided)
                  and the logits for each line.
        """
        outputs = self.base(
            input_ids=input_ids,
            attention_mask=attention_mask,
            output_hidden_states=True,
        )
        last_hidden_state = outputs.hidden_states[-1]

        batch_size, max_lines = line_end_indices.shape
        hidden_dim = last_hidden_state.shape[-1]
        
        # Create a mask to avoid gathering from padded indices (-100)
        valid_indices_mask = (line_end_indices != -100)
        clamped_indices = line_end_indices.clamp(min=0)
        
        expanded_indices = clamped_indices.unsqueeze(-1).expand(batch_size, max_lines, hidden_dim)
        line_end_hidden_states = torch.gather(last_hidden_state, 1, expanded_indices)

        logits = self.classifier(line_end_hidden_states).squeeze(-1)

        loss = None
        if labels is not None:
            # Mask the logits and labels to compute loss only on valid lines
            valid_logits = logits[valid_indices_mask]
            valid_labels = labels[valid_indices_mask]
            loss = F.binary_cross_entropy_with_logits(valid_logits, valid_labels)

        return {"loss": loss, "logits": logits}
```


```python
# ==============================================================================
# Cell 8: Model Initialization
# ==============================================================================
from transformers import BitsAndBytesConfig
from peft import LoraConfig, get_peft_model

# Configuration for 4-bit quantization
quant_cfg = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

# Configuration for LoRA adapters
lora_cfg = LoraConfig(
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    target_modules="all-linear"
)

# Load the base model with quantization
backbone = AutoModelForCausalLM.from_pretrained(
    Config.MODEL_ID,
    quantization_config=quant_cfg,
    device_map="auto",
    trust_remote_code=True,
    attn_implementation="flash_attention_2",
)
backbone.config.pad_token_id = tokenizer.pad_token_id

# Apply LoRA adapters to the base model
peft_backbone = get_peft_model(backbone, lora_cfg)

# Create the final custom model
model = GPTLineErrorDetector(peft_backbone, Config.NUM_LABELS)

model.base.print_trainable_parameters()
print("\n--- Line detection model ready for training ---")
```


```python
# ==============================================================================
# Cell 9: Custom Metrics Function
# ==============================================================================
import numpy as np

def compute_metrics_for_line_detection(eval_pred):
    """
    Calculates accuracy for the line detection task.

    Compares the predicted error line (argmax of logits) to the true
    error line index.
    """
    logits, true_error_lines = eval_pred
    
    # Find the predicted line index by taking the argmax over the line logits
    predicted_error_lines = np.argmax(logits, axis=1)
    
    accuracy = (predicted_error_lines == true_error_lines).mean()
    
    return {"line_accuracy": accuracy}
```


```python
# ==============================================================================
# Cell 10: Training Setup
# ==============================================================================
from transformers import TrainingArguments, Trainer

# Define training arguments
training_args = TrainingArguments(
    output_dir=Config.OUTPUT_DIR,
    num_train_epochs=3,
    # May need to reduce batch size from original script due to memory usage
    per_device_train_batch_size=4,
    gradient_accumulation_steps=8, # Effective batch size = 32
    optim="paged_adamw_8bit",
    learning_rate=2e-4,
    lr_scheduler_type="cosine",
    warmup_ratio=0.1,
    bf16=True,
    logging_strategy="steps",
    logging_steps=25,
    save_strategy="epoch",
    save_total_limit=1,
    report_to="none",
    save_safetensors=False,
    # Tell Trainer which column contains the labels for metrics
    label_names=["first_error_line"] 
)

# Instantiate the custom data collator
data_collator = DataCollatorForLineClassification(tokenizer=tokenizer)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=final_dataset["train"],
    eval_dataset=final_dataset["test"],
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics_for_line_detection,
)

print("--- Trainer initialised with custom line detection components ---")
```


```python
# ==============================================================================
# Cell 11: Execute Training
# ==============================================================================
print("Starting model training...")
# trainer.train()
print("Training complete.")
```


```python
# ==============================================================================
# Cell 12: Evaluation and Saving
# ==============================================================================
print("\n--- Evaluating on the test set ---")
# test_results = trainer.evaluate()
# print("Test set performance:")
# print(test_results)

print(f"\nSaving final model adapter to {Config.OUTPUT_DIR}...")
# trainer.save_model(Config.OUTPUT_DIR)
print("Model saved successfully.")
```
