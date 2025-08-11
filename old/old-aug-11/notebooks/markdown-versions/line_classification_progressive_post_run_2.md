
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
    DATASET_PATH = "/content/3n_progressive_line_classification_dataset_2.csv"

    # Directory for saving the final model adapter
    OUTPUT_DIR = "/content/line-classifier-output"

    # The head outputs one logit per line for binary (is/is_not_error) classification
    NUM_LABELS = 1
```


```python
# ==============================================================================
# Cell 3: Enhanced Tokenizer Setup with Special Token Support
# ==============================================================================
import pandas as pd
from datasets import Dataset
from transformers import AutoTokenizer

# Initialize tokenizer
tokenizer = AutoTokenizer.from_pretrained(Config.MODEL_ID, trust_remote_code=True)
tokenizer.padding_side = "left"
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Special token for reliable line separation (matching dataset creation approach)
LINE_SEP_TOKEN = "<|LINE_SEP|>"

# Add the special line separator token to the tokenizer
# This avoids inconsistent newline tokenization issues we discovered
special_tokens_dict = {"additional_special_tokens": [LINE_SEP_TOKEN]}
num_added_tokens = tokenizer.add_special_tokens(special_tokens_dict)
print(f"Added {num_added_tokens} special tokens to tokenizer")

# Get the token ID for our special line separator
line_sep_token_id = tokenizer.convert_tokens_to_ids(LINE_SEP_TOKEN)
print(f"Line separator token '{LINE_SEP_TOKEN}' has ID: {line_sep_token_id}")

# Load the CSV dataset (not using load_from_disk for CSV files)
print("Loading flawed-only line classification dataset...")
df = pd.read_csv(Config.DATASET_PATH)
print(f"✅ Dataset loaded successfully: {len(df)} samples")

# Convert to Hugging Face Dataset
raw_dataset = Dataset.from_pandas(df)

print("Tokenizer and raw dataset loaded successfully.")
print(f"Dataset columns: {raw_dataset.column_names}")
print(f"Dataset size: {len(raw_dataset)}")
print(f"Vocabulary size after adding special tokens: {len(tokenizer)}")
```

    Added 1 special tokens to tokenizer
    Line separator token '<|LINE_SEP|>' has ID: 200029
    Loading flawed-only line classification dataset...
    ✅ Dataset loaded successfully: 5093 samples
    Tokenizer and raw dataset loaded successfully.
    Dataset columns: ['text', 'correct_answer', 'line_labels', 'error_type', 'index', 'tier', 'source', 'relative_line_position', 'solution_length', 'first_error_line']
    Dataset size: 5093
    Vocabulary size after adding special tokens: 200030



```python
# ==============================================================================
# Cell 4: UPDATED Preprocessing Function for Special Tokens
# ==============================================================================
def preprocess_for_line_detection(examples):
    """
    Prepares the flawed-only dataset for line-level error detection.

    This function uses the pre-preprocessed text with special tokens,
    finds the special token indices, and uses the pre-computed line_labels.

    Args:
        examples (dict): A batch of examples from the flawed-only dataset.
                         Expected columns: 'text', 'line_labels'

    Returns:
        dict: A dictionary containing the tokenized inputs, attention masks,
              the calculated line-end indices, and the per-line labels.
    """
    # Use the pre-processed text directly (already contains special tokens)
    input_texts = examples["text"]

    tokenized_outputs = tokenizer(
        input_texts,
        truncation=True,
        max_length=512,
        padding=False
    )

    # Find special token indices (instead of newlines)
    all_line_end_indices = []
    for input_ids in tokenized_outputs["input_ids"]:
        indices = [i for i, token_id in enumerate(input_ids) if token_id == line_sep_token_id]
        all_line_end_indices.append(indices)

    tokenized_outputs["line_end_indices"] = all_line_end_indices

    # Use the pre-computed line_labels from the dataset
    # Convert string representation to list if needed
    per_line_labels = []
    for line_labels_raw in examples["line_labels"]:
        if isinstance(line_labels_raw, str):
            # Parse string representation like "[0, 0, 1, 0]"
            import ast
            line_labels = ast.literal_eval(line_labels_raw)
        else:
            line_labels = line_labels_raw
        per_line_labels.append(line_labels)

    tokenized_outputs["labels"] = per_line_labels

    # For metrics computation, also compute first_error_line
    first_error_lines = []
    for line_labels in per_line_labels:
        try:
            first_error_line = line_labels.index(1)  # Find first occurrence of 1
        except ValueError:
            first_error_line = -1  # No error found (shouldn't happen in flawed-only dataset)
        first_error_lines.append(first_error_line)

    tokenized_outputs["first_error_line"] = first_error_lines

    return tokenized_outputs
```


```python
# ==============================================================================
# Cell 5: Apply Preprocessing and Finalize Dataset
# ==============================================================================
import pandas as pd
from datasets import Dataset, DatasetDict

# Split into train/test (80/20 split)
split_dataset = raw_dataset.train_test_split(test_size=0.2, seed=42)

print("Applying preprocessing to the dataset...")
tokenized_dataset = split_dataset.map(
    preprocess_for_line_detection,
    batched=True,
    # Keep all original columns for convenience - Trainer will select what it needs
    remove_columns=None
)

final_dataset = DatasetDict({
    "train": tokenized_dataset["train"],
    "test": tokenized_dataset["test"]
})

print("\n--- Preprocessing for flawed-only line detection complete ---")
print(final_dataset)
print(f"Train samples: {len(final_dataset['train'])}")
print(f"Test samples: {len(final_dataset['test'])}")
```

    Applying preprocessing to the dataset...



    Map:   0%|          | 0/4074 [00:00<?, ? examples/s]



    Map:   0%|          | 0/1019 [00:00<?, ? examples/s]


    
    --- Preprocessing for flawed-only line detection complete ---
    DatasetDict({
        train: Dataset({
            features: ['text', 'correct_answer', 'line_labels', 'error_type', 'index', 'tier', 'source', 'relative_line_position', 'solution_length', 'first_error_line', 'input_ids', 'attention_mask', 'line_end_indices', 'labels'],
            num_rows: 4074
        })
        test: Dataset({
            features: ['text', 'correct_answer', 'line_labels', 'error_type', 'index', 'tier', 'source', 'relative_line_position', 'solution_length', 'first_error_line', 'input_ids', 'attention_mask', 'line_end_indices', 'labels'],
            num_rows: 1019
        })
    })
    Train samples: 4074
    Test samples: 1019



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
    A data collator that handles padding for our line-level task.
    Updated to work with variable-length line_labels from flawed-only dataset.
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
        max_labels = max(len(f["labels"]) for f in features)

        # Ensure line_end_indices and labels have the same max length
        max_length = max(max_lines, max_labels)

        padded_line_indices = []
        padded_labels = []

        for f in features:
            line_indices = f["line_end_indices"]
            labels = f["labels"]

            # Pad line_end_indices
            padded_line_indices.append(
                line_indices + [self.padding_value] * (max_length - len(line_indices))
            )

            # Pad labels
            padded_labels.append(
                labels + [self.padding_value] * (max_length - len(labels))
            )

        batch["line_end_indices"] = torch.tensor(padded_line_indices, dtype=torch.long)
        batch["labels"] = torch.tensor(padded_labels, dtype=torch.float)

        # Keep the computed first_error_line for metrics
        if "first_error_line" in features[0]:
            batch["first_error_line"] = torch.tensor([f["first_error_line"] for f in features], dtype=torch.long)

        return batch
```


```python
# ==============================================================================
# Cell 7: FIXED Custom Model Definition with Proper Dtype Handling
# ==============================================================================
import torch
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

        # CRITICAL FIX: Create classifier with the same dtype as the base model
        # Since we're using 4-bit quantization with bfloat16 compute dtype
        self.classifier = nn.Linear(hidden_size, num_labels, bias=True, dtype=torch.bfloat16)

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

        # DTYPE FIX: Ensure both tensors have the same dtype
        if line_end_hidden_states.dtype != self.classifier.weight.dtype:
            line_end_hidden_states = line_end_hidden_states.to(self.classifier.weight.dtype)

        logits = self.classifier(line_end_hidden_states).squeeze(-1)

        loss = None
        if labels is not None:
            # Mask the logits and labels to compute loss only on valid lines
            valid_logits = logits[valid_indices_mask]
            valid_labels = labels[valid_indices_mask]

            # Ensure labels have the same dtype as logits
            if valid_labels.dtype != valid_logits.dtype:
                valid_labels = valid_labels.to(valid_logits.dtype)

            loss = F.binary_cross_entropy_with_logits(valid_logits, valid_labels)

        return {"loss": loss, "logits": logits}
```


```python
# ==============================================================================
# Cell 8: FIXED Model Initialization with Proper Dtype Management
# ==============================================================================
from transformers import BitsAndBytesConfig
from peft import LoraConfig, get_peft_model
import torch

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

# CRITICAL FIX: Move the entire model to GPU and ensure proper dtype
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

# Ensure classifier is in the right dtype and device
if hasattr(model, 'classifier'):
    model.classifier = model.classifier.to(device=device, dtype=torch.bfloat16)

print(f"🎯 Model moved to device: {device}")
print(f"🔧 Classifier dtype: {model.classifier.weight.dtype}")
print(f"🔧 Classifier device: {model.classifier.weight.device}")

model.base.print_trainable_parameters()
print("\n--- Line detection model ready for training ---")
```


    config.json: 0.00B [00:00, ?B/s]



    configuration_phi3.py: 0.00B [00:00, ?B/s]


    A new version of the following files was downloaded from https://huggingface.co/microsoft/phi-4-mini-instruct:
    - configuration_phi3.py
    . Make sure to double-check they do not contain any added malicious code. To avoid downloading new versions of the code file, you can pin a revision.



    modeling_phi3.py: 0.00B [00:00, ?B/s]


    A new version of the following files was downloaded from https://huggingface.co/microsoft/phi-4-mini-instruct:
    - modeling_phi3.py
    . Make sure to double-check they do not contain any added malicious code. To avoid downloading new versions of the code file, you can pin a revision.



    model.safetensors.index.json: 0.00B [00:00, ?B/s]



    Fetching 2 files:   0%|          | 0/2 [00:00<?, ?it/s]



    model-00001-of-00002.safetensors:   0%|          | 0.00/4.90G [00:00<?, ?B/s]



    model-00002-of-00002.safetensors:   0%|          | 0.00/2.77G [00:00<?, ?B/s]



    Loading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]



    generation_config.json:   0%|          | 0.00/168 [00:00<?, ?B/s]


    🎯 Model moved to device: cuda
    🔧 Classifier dtype: torch.bfloat16
    🔧 Classifier device: cuda:0
    trainable params: 23,068,672 || all params: 3,859,090,432 || trainable%: 0.5978
    
    --- Line detection model ready for training ---



```python
# ==============================================================================
# Cell 9: UPDATED Custom Metrics Function for Progressive Labeling
# ==============================================================================
import numpy as np

def compute_metrics_for_line_detection(eval_pred):
    """
    Calculates metrics for the progressive line detection task.

    With progressive labeling, we measure how well the model captures
    the transition pattern [0,0,1,1...] rather than just finding a peak.

    Args:
        eval_pred: Tuple of (logits, labels) where:
            - logits: Model outputs with shape (batch_size, max_lines)
            - labels: Progressive binary labels with shape (batch_size, max_lines)

    Returns:
        dict: Dictionary containing line-level and sample-level accuracy metrics
    """
    logits, labels = eval_pred

    # Convert logits to binary predictions (use 0 as threshold)
    predictions = (logits > 0).astype(int)

    # Flatten for line-level metrics (each line is a separate prediction)
    flat_predictions = predictions.flatten()
    flat_labels = labels.flatten()

    # Remove padding tokens (assuming -100 is used for padding)
    valid_mask = flat_labels != -100
    valid_predictions = flat_predictions[valid_mask]
    valid_labels = flat_labels[valid_mask]

    # Line-level accuracy: What fraction of individual lines are predicted correctly?
    line_accuracy = (valid_predictions == valid_labels).mean()

    # Sample-level accuracy: What fraction of complete sequences are predicted correctly?
    sample_accuracy = 0
    total_samples = len(predictions)
    first_error_correct = 0
    total_error_samples = 0

    for i in range(len(predictions)):
        sample_preds = predictions[i]
        sample_labels = labels[i]

        # Remove padding
        valid_positions = sample_labels != -100
        if not valid_positions.any():
            continue

        sample_preds = sample_preds[valid_positions]
        sample_labels = sample_labels[valid_positions]

        # Check if entire sequence matches exactly
        if np.array_equal(sample_preds, sample_labels):
            sample_accuracy += 1

        # First error line accuracy: For samples with errors, does the model
        # correctly identify the first line where the error occurs?
        if np.any(sample_labels == 1):  # Sample has errors
            total_error_samples += 1

            # Find first error line in true labels
            true_error_positions = np.where(sample_labels == 1)[0]
            pred_error_positions = np.where(sample_preds == 1)[0]

            if len(true_error_positions) > 0 and len(pred_error_positions) > 0:
                true_first_error = true_error_positions[0]
                pred_first_error = pred_error_positions[0]

                # Check if predicted first error matches true first error
                if pred_first_error == true_first_error:
                    first_error_correct += 1

    sample_accuracy = sample_accuracy / total_samples if total_samples > 0 else 0.0
    first_error_accuracy = first_error_correct / total_error_samples if total_error_samples > 0 else 0.0

    # Class distribution analysis
    total_positions = len(valid_labels)
    positive_positions = (valid_labels == 1).sum()
    negative_positions = (valid_labels == 0).sum()

    return {
        # Main metrics
        "line_accuracy": float(line_accuracy),              # % of individual lines correct
        "sample_accuracy": float(sample_accuracy),          # % of complete sequences correct
        "first_error_accuracy": float(first_error_accuracy), # % of first error lines correct

        # Count metrics for debugging
        "correct_samples": int(sample_accuracy * total_samples),
        "first_error_correct": int(first_error_correct),
        "total_samples": int(total_samples),
        "total_error_samples": int(total_error_samples),
        "total_positions": int(total_positions),
        "positive_positions": int(positive_positions),
        "negative_positions": int(negative_positions),

        # Class balance analysis
        "positive_rate": float(positive_positions / total_positions) if total_positions > 0 else 0.0,
    }
```


```python
# ==============================================================================
# Cell 10: UPDATED Training Setup - Early Stopping & Progressive Labels
# ==============================================================================
from transformers import TrainingArguments, Trainer, EarlyStoppingCallback

# Define training arguments with early stopping and progressive labeling
training_args = TrainingArguments(
    output_dir=Config.OUTPUT_DIR,
    num_train_epochs=6,  # Extended training
    per_device_train_batch_size=8,
    gradient_accumulation_steps=4,  # Effective batch size = 32
    optim="paged_adamw_8bit",
    learning_rate=1e-4,  # Lower learning rate for continued training
    lr_scheduler_type="cosine",
    warmup_ratio=0.1,  # Reduced warmup for continued training
    bf16=True,

    # FREQUENT LOGGING, EVALUATION & SAVING
    logging_strategy="steps",
    logging_steps=25,
    eval_strategy="steps",        # Evaluate every 25 steps
    eval_steps=25,
    save_strategy="steps",       # Save every 25 steps
    save_steps=25,
    save_total_limit=1,          # Keep only the most recent checkpoint

    # EARLY STOPPING CONFIGURATION
    load_best_model_at_end=True,
    metric_for_best_model="first_error_accuracy",  # CHANGED: Use sample accuracy as main metric
    greater_is_better=True,

    # OTHER SETTINGS
    report_to="none",
    save_safetensors=False,
    label_names=["labels"]  # CHANGED: Use progressive binary labels
)

# Instantiate the updated data collator
data_collator = DataCollatorForLineClassification(tokenizer=tokenizer)

# Initialize early stopping callback
early_stopping_callback = EarlyStoppingCallback(
    early_stopping_patience=10,    # Stop after 2 evaluations without improvement
    early_stopping_threshold=0.0  # Any improvement counts
)

# Initialize the Trainer with early stopping
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=final_dataset["train"],
    eval_dataset=final_dataset["test"],
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics_for_line_detection,
    callbacks=[early_stopping_callback]
)

print("--- Enhanced Trainer with Progressive Labeling initialized ---")
print(f"📊 Configuration Summary:")
print(f"   🔄 Evaluation every: {training_args.eval_steps} steps")
print(f"   💾 Saving every: {training_args.save_steps} steps")
print(f"   📈 Logging every: {training_args.logging_steps} steps")
print(f"   📁 Max checkpoints: {training_args.save_total_limit}")
print(f"   📚 Training samples: {len(final_dataset['train'])}")
print(f"   🧪 Evaluation samples: {len(final_dataset['test'])}")
print(f"   🎯 Total epochs: {training_args.num_train_epochs}")
print(f"   🏆 Best metric: {training_args.metric_for_best_model}")
print(f"   🎯 Label format: Progressive binary labels")
```

    --- Enhanced Trainer with Progressive Labeling initialized ---
    📊 Configuration Summary:
       🔄 Evaluation every: 25 steps
       💾 Saving every: 25 steps
       📈 Logging every: 25 steps
       📁 Max checkpoints: 1
       📚 Training samples: 4074
       🧪 Evaluation samples: 1019
       🎯 Total epochs: 6
       🏆 Best metric: first_error_accuracy
       🎯 Label format: Progressive binary labels


    /tmp/ipython-input-11-214991186.py:48: FutureWarning: `tokenizer` is deprecated and will be removed in version 5.0.0 for `Trainer.__init__`. Use `processing_class` instead.
      trainer = Trainer(



```python
trainer.train()
print("Training complete.")
```

    You're using a GPT2TokenizerFast tokenizer. Please note that with a fast tokenizer, using the `__call__` method is faster than using a method to encode the text followed by a call to the `pad` method to get a padded encoding.
    The input hidden states seems to be silently casted in float32, this might be related to the fact you have upcasted embedding or layer norm layers in float32. We will cast back the input in torch.bfloat16.




    <div>

      <progress value='301' max='768' style='width:300px; height:20px; vertical-align: middle;'></progress>
      [301/768 19:27 < 30:23, 0.26 it/s, Epoch 2.35/6]
    </div>
    <table border="1" class="dataframe">
  <thead>
 <tr style="text-align: left;">
      <th>Step</th>
      <th>Training Loss</th>
      <th>Validation Loss</th>
      <th>Line Accuracy</th>
      <th>Sample Accuracy</th>
      <th>First Error Accuracy</th>
      <th>Correct Samples</th>
      <th>First Error Correct</th>
      <th>Total Samples</th>
      <th>Total Error Samples</th>
      <th>Total Positions</th>
      <th>Positive Positions</th>
      <th>Negative Positions</th>
      <th>Positive Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>25</td>
      <td>2.886700</td>
      <td>0.710311</td>
      <td>0.487134</td>
      <td>0.094210</td>
      <td>0.235043</td>
      <td>96</td>
      <td>165</td>
      <td>1019</td>
      <td>702</td>
      <td>4547</td>
      <td>2354</td>
      <td>2193</td>
      <td>0.517704</td>
    </tr>
    <tr>
      <td>50</td>
      <td>2.797600</td>
      <td>0.687931</td>
      <td>0.538377</td>
      <td>0.117763</td>
      <td>0.277778</td>
      <td>120</td>
      <td>195</td>
      <td>1019</td>
      <td>702</td>
      <td>4547</td>
      <td>2354</td>
      <td>2193</td>
      <td>0.517704</td>
    </tr>
    <tr>
      <td>75</td>
      <td>2.804200</td>
      <td>0.694979</td>
      <td>0.533978</td>
      <td>0.194308</td>
      <td>0.388889</td>
      <td>198</td>
      <td>273</td>
      <td>1019</td>
      <td>702</td>
      <td>4547</td>
      <td>2354</td>
      <td>2193</td>
      <td>0.517704</td>
    </tr>
    <tr>
      <td>100</td>
      <td>2.780000</td>
      <td>0.699511</td>
      <td>0.510227</td>
      <td>0.127576</td>
      <td>0.239316</td>
      <td>130</td>
      <td>168</td>
      <td>1019</td>
      <td>702</td>
      <td>4547</td>
      <td>2354</td>
      <td>2193</td>
      <td>0.517704</td>
    </tr>
    <tr>
      <td>125</td>
      <td>2.828300</td>
      <td>0.691449</td>
      <td>0.528260</td>
      <td>0.158979</td>
      <td>0.337607</td>
      <td>162</td>
      <td>237</td>
      <td>1019</td>
      <td>702</td>
      <td>4547</td>
      <td>2354</td>
      <td>2193</td>
      <td>0.517704</td>
    </tr>
    <tr>
      <td>150</td>
      <td>2.738800</td>
      <td>0.685841</td>
      <td>0.532879</td>
      <td>0.114818</td>
      <td>0.266382</td>
      <td>117</td>
      <td>187</td>
      <td>1019</td>
      <td>702</td>
      <td>4547</td>
      <td>2354</td>
      <td>2193</td>
      <td>0.517704</td>
    </tr>
    <tr>
      <td>175</td>
      <td>2.770200</td>
      <td>0.692087</td>
      <td>0.534418</td>
      <td>0.135427</td>
      <td>0.163818</td>
      <td>138</td>
      <td>115</td>
      <td>1019</td>
      <td>702</td>
      <td>4547</td>
      <td>2354</td>
      <td>2193</td>
      <td>0.517704</td>
    </tr>
    <tr>
      <td>200</td>
      <td>2.751300</td>
      <td>0.696518</td>
      <td>0.521003</td>
      <td>0.097154</td>
      <td>0.257835</td>
      <td>99</td>
      <td>181</td>
      <td>1019</td>
      <td>702</td>
      <td>4547</td>
      <td>2354</td>
      <td>2193</td>
      <td>0.517704</td>
    </tr>
    <tr>
      <td>225</td>
      <td>2.782700</td>
      <td>0.686208</td>
      <td>0.535738</td>
      <td>0.140334</td>
      <td>0.339031</td>
      <td>143</td>
      <td>238</td>
      <td>1019</td>
      <td>702</td>
      <td>4547</td>
      <td>2354</td>
      <td>2193</td>
      <td>0.517704</td>
    </tr>
    <tr>
      <td>250</td>
      <td>2.731000</td>
      <td>0.683829</td>
      <td>0.554651</td>
      <td>0.138371</td>
      <td>0.279202</td>
      <td>141</td>
      <td>196</td>
      <td>1019</td>
      <td>702</td>
      <td>4547</td>
      <td>2354</td>
      <td>2193</td>
      <td>0.517704</td>
    </tr>
    <tr>
      <td>275</td>
      <td>2.600400</td>
      <td>0.677811</td>
      <td>0.555091</td>
      <td>0.167812</td>
      <td>0.327635</td>
      <td>171</td>
      <td>230</td>
      <td>1019</td>
      <td>702</td>
      <td>4547</td>
      <td>2354</td>
      <td>2193</td>
      <td>0.517704</td>
    </tr>
  </tbody>
</table><p>
    <div>

      <progress value='6' max='128' style='width:300px; height:20px; vertical-align: middle;'></progress>
      [  6/128 00:01 < 00:32, 3.73 it/s]
    </div>





    <div>

      <progress value='301' max='768' style='width:300px; height:20px; vertical-align: middle;'></progress>
      [301/768 19:27 < 30:23, 0.26 it/s, Epoch 2.35/6]
    </div>
    <table border="1" class="dataframe">
  <thead>
 <tr style="text-align: left;">
      <th>Step</th>
      <th>Training Loss</th>
      <th>Validation Loss</th>
      <th>Line Accuracy</th>
      <th>Sample Accuracy</th>
      <th>First Error Accuracy</th>
      <th>Correct Samples</th>
      <th>First Error Correct</th>
      <th>Total Samples</th>
      <th>Total Error Samples</th>
      <th>Total Positions</th>
      <th>Positive Positions</th>
      <th>Negative Positions</th>
      <th>Positive Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>25</td>
      <td>2.886700</td>
      <td>0.710311</td>
      <td>0.487134</td>
      <td>0.094210</td>
      <td>0.235043</td>
      <td>96</td>
      <td>165</td>
      <td>1019</td>
      <td>702</td>
      <td>4547</td>
      <td>2354</td>
      <td>2193</td>
      <td>0.517704</td>
    </tr>
    <tr>
      <td>50</td>
      <td>2.797600</td>
      <td>0.687931</td>
      <td>0.538377</td>
      <td>0.117763</td>
      <td>0.277778</td>
      <td>120</td>
      <td>195</td>
      <td>1019</td>
      <td>702</td>
      <td>4547</td>
      <td>2354</td>
      <td>2193</td>
      <td>0.517704</td>
    </tr>
    <tr>
      <td>75</td>
      <td>2.804200</td>
      <td>0.694979</td>
      <td>0.533978</td>
      <td>0.194308</td>
      <td>0.388889</td>
      <td>198</td>
      <td>273</td>
      <td>1019</td>
      <td>702</td>
      <td>4547</td>
      <td>2354</td>
      <td>2193</td>
      <td>0.517704</td>
    </tr>
    <tr>
      <td>100</td>
      <td>2.780000</td>
      <td>0.699511</td>
      <td>0.510227</td>
      <td>0.127576</td>
      <td>0.239316</td>
      <td>130</td>
      <td>168</td>
      <td>1019</td>
      <td>702</td>
      <td>4547</td>
      <td>2354</td>
      <td>2193</td>
      <td>0.517704</td>
    </tr>
    <tr>
      <td>125</td>
      <td>2.828300</td>
      <td>0.691449</td>
      <td>0.528260</td>
      <td>0.158979</td>
      <td>0.337607</td>
      <td>162</td>
      <td>237</td>
      <td>1019</td>
      <td>702</td>
      <td>4547</td>
      <td>2354</td>
      <td>2193</td>
      <td>0.517704</td>
    </tr>
    <tr>
      <td>150</td>
      <td>2.738800</td>
      <td>0.685841</td>
      <td>0.532879</td>
      <td>0.114818</td>
      <td>0.266382</td>
      <td>117</td>
      <td>187</td>
      <td>1019</td>
      <td>702</td>
      <td>4547</td>
      <td>2354</td>
      <td>2193</td>
      <td>0.517704</td>
    </tr>
    <tr>
      <td>175</td>
      <td>2.770200</td>
      <td>0.692087</td>
      <td>0.534418</td>
      <td>0.135427</td>
      <td>0.163818</td>
      <td>138</td>
      <td>115</td>
      <td>1019</td>
      <td>702</td>
      <td>4547</td>
      <td>2354</td>
      <td>2193</td>
      <td>0.517704</td>
    </tr>
    <tr>
      <td>200</td>
      <td>2.751300</td>
      <td>0.696518</td>
      <td>0.521003</td>
      <td>0.097154</td>
      <td>0.257835</td>
      <td>99</td>
      <td>181</td>
      <td>1019</td>
      <td>702</td>
      <td>4547</td>
      <td>2354</td>
      <td>2193</td>
      <td>0.517704</td>
    </tr>
    <tr>
      <td>225</td>
      <td>2.782700</td>
      <td>0.686208</td>
      <td>0.535738</td>
      <td>0.140334</td>
      <td>0.339031</td>
      <td>143</td>
      <td>238</td>
      <td>1019</td>
      <td>702</td>
      <td>4547</td>
      <td>2354</td>
      <td>2193</td>
      <td>0.517704</td>
    </tr>
    <tr>
      <td>250</td>
      <td>2.731000</td>
      <td>0.683829</td>
      <td>0.554651</td>
      <td>0.138371</td>
      <td>0.279202</td>
      <td>141</td>
      <td>196</td>
      <td>1019</td>
      <td>702</td>
      <td>4547</td>
      <td>2354</td>
      <td>2193</td>
      <td>0.517704</td>
    </tr>
    <tr>
      <td>275</td>
      <td>2.600400</td>
      <td>0.677811</td>
      <td>0.555091</td>
      <td>0.167812</td>
      <td>0.327635</td>
      <td>171</td>
      <td>230</td>
      <td>1019</td>
      <td>702</td>
      <td>4547</td>
      <td>2354</td>
      <td>2193</td>
      <td>0.517704</td>
    </tr>
  </tbody>
</table><p>
    <div>

      <progress value='19' max='128' style='width:300px; height:20px; vertical-align: middle;'></progress>
      [ 19/128 00:04 < 00:29, 3.70 it/s]
    </div>




```python
# ==============================================================================
# Cell 12: Evaluation and Saving
# ==============================================================================
print("\n--- Evaluating on the test set ---")
test_results = trainer.evaluate()
print("Test set performance:")
print(test_results)

print(f"\nSaving final model adapter to {Config.OUTPUT_DIR}...")
trainer.save_model(Config.OUTPUT_DIR)
print("Model saved successfully.")
```
