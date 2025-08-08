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
# 1.2 Install required libraries
# Note: TRL is included for consistency with your original script, but is not
# strictly required for this sequence classification task.
!pip install -U transformers==4.53.2
!pip install -U peft
!pip install -U trl
!pip install -U accelerate
!pip install -U datasets
!pip install -U bitsandbytes

# Install Flash Attention 2
!pip install flash-attn==2.7.4.post1 \
  --extra-index-url https://download.pytorch.org/whl/cu124 \
  --no-build-isolation
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
    DATASET_PATH = "/content/flawed_only_line_classification_dataset.csv"

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


    tokenizer_config.json: 0.00B [00:00, ?B/s]



    vocab.json: 0.00B [00:00, ?B/s]



    merges.txt: 0.00B [00:00, ?B/s]



    tokenizer.json:   0%|          | 0.00/15.5M [00:00<?, ?B/s]



    added_tokens.json:   0%|          | 0.00/249 [00:00<?, ?B/s]



    special_tokens_map.json:   0%|          | 0.00/587 [00:00<?, ?B/s]


    Added 1 special tokens to tokenizer
    Line separator token '<|LINE_SEP|>' has ID: 200029
    Loading flawed-only line classification dataset...
    ✅ Dataset loaded successfully: 3487 samples
    Tokenizer and raw dataset loaded successfully.
    Dataset columns: ['text', 'correct_answer', 'line_labels', 'error_type', 'index', 'tier', 'source', 'relative_line_position', 'solution_length']
    Dataset size: 3487
    Vocabulary size after adding special tokens: 200030



```python
row = df.iloc[0]
print(row.to_dict())
```

    {'text': 'Analyze the following mathematical problem and solution to identify the line containing the error.\n\n### Problem:\nWeng earns $12 an hour for babysitting. Yesterday, she just did 50 minutes of babysitting. How much did she earn?\n\n### Solution:\nWeng earns 12/60 = $0.2 per minute.<|LINE_SEP|>Working 50 minutes, she earned 50 x 50 = $2500.<|LINE_SEP|>#### 2500<|LINE_SEP|>', 'correct_answer': 'Weng earns 12/60 = $0.2 per minute.\nWorking 50 minutes, she earned 0.2 x 50 = $10.\n#### 10', 'line_labels': '[0, 1, 0]', 'error_type': 'conceptual_error', 'index': 1, 'tier': 'tier4', 'source': 'programmatic', 'relative_line_position': 0.5, 'solution_length': 3}



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



    Map:   0%|          | 0/2789 [00:00<?, ? examples/s]



    Map:   0%|          | 0/698 [00:00<?, ? examples/s]


    
    --- Preprocessing for flawed-only line detection complete ---
    DatasetDict({
        train: Dataset({
            features: ['text', 'correct_answer', 'line_labels', 'error_type', 'index', 'tier', 'source', 'relative_line_position', 'solution_length', 'input_ids', 'attention_mask', 'line_end_indices', 'labels', 'first_error_line'],
            num_rows: 2789
        })
        test: Dataset({
            features: ['text', 'correct_answer', 'line_labels', 'error_type', 'index', 'tier', 'source', 'relative_line_position', 'solution_length', 'input_ids', 'attention_mask', 'line_end_indices', 'labels', 'first_error_line'],
            num_rows: 698
        })
    })
    Train samples: 2789
    Test samples: 698



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


    Loading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]


    🎯 Model moved to device: cuda
    🔧 Classifier dtype: torch.bfloat16
    🔧 Classifier device: cuda:0
    trainable params: 23,068,672 || all params: 3,859,090,432 || trainable%: 0.5978
    
    --- Line detection model ready for training ---



```python
# ==============================================================================
# UPDATED: A100-Optimized Testing Functions with Fixed Device Handling
# ==============================================================================
import torch
import time
import psutil

def test_model_forward_pass_a100(model, data_collator, processed_dataset, device='cuda'):
    """Test model forward pass optimized for A100 GPU with proper device handling"""
    print("\n🧪 TEST 6: Model Forward Pass Validation (A100 GPU)")
    print("=" * 60)

    # GPU info
    if torch.cuda.is_available():
        gpu_name = torch.cuda.get_device_name(0)
        total_memory = torch.cuda.get_device_properties(0).total_memory / 1e9
        print(f"🚀 GPU: {gpu_name}")
        print(f"💾 Total GPU Memory: {total_memory:.1f} GB")
        print(f"📍 Using device: {device}")

        # Clear GPU cache
        torch.cuda.empty_cache()
        print(f"🧹 Cleared GPU cache")

    try:
        # Ensure model is on correct device
        model = model.to(device)
        print(f"✅ Model moved to {device}")

        # Create a small batch
        batch_samples = [processed_dataset[i] for i in range(min(2, len(processed_dataset)))]
        batch = data_collator(batch_samples)

        # Move batch to device
        batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in batch.items()}

        print(f"🚀 Testing forward pass with batch size: {batch['input_ids'].shape[0]}")
        print(f"📊 Input sequence length: {batch['input_ids'].shape[1]}")

        # Verify all tensors are on the same device
        print(f"🔍 Device verification:")
        for key, tensor in batch.items():
            if isinstance(tensor, torch.Tensor):
                print(f"   {key}: {tensor.device}")

        # Check model device
        print(f"   model.classifier: {next(model.classifier.parameters()).device}")
        print(f"   model.base device_map: {getattr(model.base, 'hf_device_map', 'Not set')}")

        # Model forward pass with timing
        model.eval()
        start_time = time.time()

        with torch.no_grad():
            outputs = model(**batch)

        end_time = time.time()

        print(f"✅ Forward pass successful")
        print(f"⏱️ Forward pass time: {(end_time - start_time)*1000:.1f}ms")
        print(f"📤 Output keys: {list(outputs.keys())}")

        # Check output shapes and values
        if 'logits' in outputs:
            logits = outputs['logits']
            print(f"   Logits shape: {logits.shape}")
            print(f"   Logits dtype: {logits.dtype}")
            print(f"   Logits device: {logits.device}")
            print(f"   Logits range: [{logits.min().item():.3f}, {logits.max().item():.3f}]")

        if 'loss' in outputs and outputs['loss'] is not None:
            loss = outputs['loss']
            print(f"   Loss: {loss.item():.4f}")
            print(f"   Loss device: {loss.device}")

        # GPU memory usage
        if torch.cuda.is_available():
            memory_used = torch.cuda.memory_allocated(0) / 1e9
            memory_cached = torch.cuda.memory_reserved(0) / 1e9
            print(f"💾 GPU Memory Used: {memory_used:.2f} GB")
            print(f"💾 GPU Memory Cached: {memory_cached:.2f} GB")

        return True

    except Exception as e:
        print(f"❌ Model forward pass failed: {e}")
        print(f"🔍 Detailed error:")
        import traceback
        traceback.print_exc()
        return False


def test_model_inference_colab_a100(model, tokenizer, processed_dataset, device='cuda'):
    """Test complete inference pipeline optimized for Colab A100"""
    print("\n🧪 INFERENCE TEST: Complete Pipeline (A100 GPU)")
    print("=" * 60)

    try:
        # Ensure model is on correct device
        model = model.to(device)

        print(f"📝 Testing complete inference pipeline")
        print(f"🎯 Device: {device}")

        # Get a sample
        sample = processed_dataset[0]
        print(f"📋 Testing with sample 0")
        print(f"   📏 Input length: {len(sample['input_ids'])} tokens")
        print(f"   📍 Number of lines: {len(sample['line_end_indices'])}")
        print(f"   🏷️ True labels: {sample['labels']}")
        print(f"   🎯 True first error line: {sample['first_error_line']}")

        # Create data collator and process single sample
        data_collator = DataCollatorForLineClassification(tokenizer=tokenizer)
        batch = data_collator([sample])

        # Move to device
        batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in batch.items()}

        # Inference
        model.eval()
        with torch.no_grad():
            outputs = model(**batch)

        # Process results
        logits = outputs['logits'][0]  # Remove batch dimension

        # Apply sigmoid to get probabilities
        probabilities = torch.sigmoid(logits)

        # Find predicted error line
        predicted_error_line = torch.argmax(probabilities).item()
        confidence = probabilities[predicted_error_line].item()

        print(f"\n📊 INFERENCE RESULTS:")
        print(f"   🎯 Predicted error line: {predicted_error_line}")
        print(f"   🎯 True error line: {sample['first_error_line']}")
        print(f"   📈 Confidence: {confidence:.3f}")
        print(f"   ✅ Correct: {'Yes' if predicted_error_line == sample['first_error_line'] else 'No'}")

        # Show per-line probabilities
        valid_lines = len(sample['line_end_indices'])
        print(f"\n📋 Per-line probabilities:")
        for i in range(min(valid_lines, len(probabilities))):
            prob = probabilities[i].item()
            is_true_error = (i == sample['first_error_line'])
            marker = "🎯" if is_true_error else "  "
            print(f"   {marker} Line {i}: {prob:.3f}")

        return True

    except Exception as e:
        print(f"❌ Inference test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_gpu_performance_a100(model, data_collator, processed_dataset, device='cuda'):
    """Test GPU performance with different batch sizes on A100"""
    print("\n🧪 GPU PERFORMANCE TEST (A100)")
    print("=" * 60)

    if not torch.cuda.is_available():
        print("⚠️ CUDA not available - cannot run GPU performance test")
        return False

    try:
        # Ensure model is on GPU
        model = model.to(device)
        model.eval()

        batch_sizes = [1, 2, 4, 8]
        performance_results = []

        for batch_size in batch_sizes:
            if batch_size > len(processed_dataset):
                continue

            print(f"\n🔬 Testing batch size: {batch_size}")

            # Create batch
            batch_samples = [processed_dataset[i] for i in range(batch_size)]
            batch = data_collator(batch_samples)
            batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in batch.items()}

            # Clear cache and measure memory
            torch.cuda.empty_cache()
            torch.cuda.synchronize()

            memory_before = torch.cuda.memory_allocated(0) / 1e9

            # Time forward pass
            times = []
            for _ in range(5):  # Average over 5 runs
                torch.cuda.synchronize()
                start_time = time.time()

                with torch.no_grad():
                    outputs = model(**batch)

                torch.cuda.synchronize()
                end_time = time.time()
                times.append(end_time - start_time)

            memory_after = torch.cuda.memory_allocated(0) / 1e9
            memory_used = memory_after - memory_before

            avg_time = sum(times) / len(times)
            throughput = batch_size / avg_time

            result = {
                'batch_size': batch_size,
                'avg_time_ms': avg_time * 1000,
                'throughput_samples_per_sec': throughput,
                'memory_used_gb': memory_used,
                'sequence_length': batch['input_ids'].shape[1]
            }
            performance_results.append(result)

            print(f"   ⏱️ Avg time: {avg_time*1000:.1f}ms")
            print(f"   🚀 Throughput: {throughput:.1f} samples/sec")
            print(f"   💾 Memory used: {memory_used:.3f} GB")

        # Find optimal batch size
        optimal_batch = max(performance_results, key=lambda x: x['throughput_samples_per_sec'])

        print(f"\n🏆 OPTIMAL CONFIGURATION:")
        print(f"   Batch size: {optimal_batch['batch_size']}")
        print(f"   Throughput: {optimal_batch['throughput_samples_per_sec']:.1f} samples/sec")
        print(f"   Time per batch: {optimal_batch['avg_time_ms']:.1f}ms")
        print(f"   Memory usage: {optimal_batch['memory_used_gb']:.3f} GB")

        return performance_results

    except Exception as e:
        print(f"❌ GPU performance test failed: {e}")
        import traceback
        traceback.print_exc()
        return False
```


```python
test_df = df.sample(5, random_state=42)
test_dataset = Dataset.from_pandas(test_df)
processed_test_dataset = test_dataset.map(preprocess_for_line_detection, batched=True)

# Recreate the data collator and test the model forward pass
data_collator = DataCollatorForLineClassification(tokenizer=tokenizer)

# Test the model forward pass (optimized for A100)
test_result = test_model_forward_pass(model, data_collator, processed_test_dataset, device='cuda:0')

# Test complete inference pipeline
inference_result = test_model_inference_colab(model, tokenizer, data_collator, processed_test_dataset, device='cuda:0')

# Test performance characteristics
perf_result = test_gpu_performance(model, data_collator, processed_test_dataset, device='cuda:0')
```


    Map:   0%|          | 0/5 [00:00<?, ? examples/s]


    
    🧪 TEST 6: Model Forward Pass Validation (A100 GPU)
    ============================================================
    🚀 GPU: NVIDIA A100-SXM4-40GB
    💾 Total GPU Memory: 42.5 GB
    📍 Using device: cuda:0
    🧹 Cleared GPU cache
    🚀 Testing forward pass with batch size: 2
    📊 Input sequence length: 317
    💾 GPU memory allocated before: 8090.5 MB
    💾 GPU memory allocated after: 8090.5 MB
    📈 Memory increase: 0.0 MB
    ✅ Forward pass successful
    📤 Output keys: ['loss', 'logits']
       📊 Logits shape: torch.Size([2, 7])
       🔢 Logits dtype: torch.bfloat16
       📈 Logits range: [-0.547, 1.570]
       🎯 Logits device: cuda:0
       💥 Loss: 0.7500
       🎯 Loss device: cuda:0
       🔮 Predicted error lines: [0, 5]
       ✅ True error lines: [6, 0]
       🎯 Batch accuracy: 0.000
    🧹 Cleared GPU cache after test
    
    🧪 INFERENCE TEST: Complete Pipeline (A100 GPU)
    ============================================================
    📝 Testing complete inference pipeline
    🎯 Device: cuda:0
    📋 Testing with sample 0
       📏 Input length: 317 tokens
       📍 Number of lines: 7
       🏷️ True labels: [0, 0, 0, 0, 0, 0, 1]
       🎯 True first error line: 6
    
    📊 INFERENCE RESULTS:
       🔮 Predicted error line: 0
       ✅ True error line: 6
       🎯 Correct: ❌
    
    📈 Line-by-line confidence scores:
       🔥 Line 0: 0.445   
          Line 1: 0.079   
          Line 2: 0.092   
          Line 3: 0.088   
          Line 4: 0.076   
          Line 5: 0.100   
          Line 6: 0.119 ✅
    
    🧪 GPU PERFORMANCE TEST (A100)
    ============================================================
    🏃‍♂️ Testing different batch sizes...
       Batch  1: 0.110s | 9.1 samples/s | 8091MB
       Batch  2: 0.126s | 15.8 samples/s | 8091MB
       Batch  4: 0.165s | 24.3 samples/s | 8091MB
    ✅ Performance test completed



```python
# ==============================================================================
# Cell 9: Custom Metrics Function
# ==============================================================================
import numpy as np

def compute_metrics_for_line_detection(eval_pred):
    """
    Calculates accuracy for the flawed-only line detection task.

    Since all samples have exactly one error line, we compare the predicted
    error line (argmax of logits) to the true error line index.
    """
    logits, true_error_lines = eval_pred

    # Find the predicted line index by taking the argmax over the line logits
    predicted_error_lines = np.argmax(logits, axis=1)

    # Calculate accuracy
    accuracy = (predicted_error_lines == true_error_lines).mean()

    # Additional metrics for better evaluation
    total_samples = len(true_error_lines)
    correct_predictions = (predicted_error_lines == true_error_lines).sum()

    return {
        "line_accuracy": accuracy,
        "correct_predictions": correct_predictions,
        "total_samples": total_samples
    }
```

```python
# ==============================================================================
# Cell 10: UPDATED Training Setup - Early Stopping & Optimized Checkpoints
# ==============================================================================
from transformers import TrainingArguments, Trainer, EarlyStoppingCallback

# Define training arguments with early stopping and frequent evaluation
training_args_2 = TrainingArguments(
    output_dir=Config.OUTPUT_DIR,
    num_train_epochs=6,  # Extended training
    per_device_train_batch_size=4,
    gradient_accumulation_steps=8,  # Effective batch size = 32
    optim="paged_adamw_8bit",
    learning_rate=1e-4,  # Lower learning rate for continued training
    lr_scheduler_type="cosine",
    warmup_ratio=0.05,  # Reduced warmup for continued training
    bf16=True,

    # FREQUENT LOGGING, EVALUATION & SAVING
    logging_strategy="steps",
    logging_steps=25,
    eval_strategy="steps",        # Evaluate every 25 steps
    eval_steps=25,
    save_strategy="steps",       # Save every 25 steps
    save_steps=25,
    save_total_limit=2,          # Keep only 2 most recent checkpoints

    # EARLY STOPPING CONFIGURATION
    load_best_model_at_end=True,
    metric_for_best_model="line_accuracy",
    greater_is_better=True,

    # OTHER SETTINGS
    report_to="none",
    save_safetensors=False,
    label_names=["first_error_line"]
)

# Instantiate the updated data collator
data_collator_2 = DataCollatorForLineClassification(tokenizer=tokenizer)

# Initialize early stopping callback
early_stopping_callback = EarlyStoppingCallback(
    early_stopping_patience=2,    # Stop after 2 evaluations (2 * 25 = 50 steps) without improvement
    early_stopping_threshold=0.0  # Any improvement counts (even tiny ones)
)

# Initialize the Trainer with early stopping
trainer_2 = Trainer(
    model=model,
    args=training_args_2,
    train_dataset=final_dataset["train"],
    eval_dataset=final_dataset["test"],
    tokenizer=tokenizer,
    data_collator=data_collator_2,
    compute_metrics=compute_metrics_for_line_detection,
    callbacks=[early_stopping_callback]  # Add early stopping callback
)

print("--- Enhanced Trainer with Early Stopping initialized ---")
print(f"📊 Configuration Summary:")
print(f"   🔄 Evaluation every: {training_args.eval_steps} steps")
print(f"   💾 Saving every: {training_args.save_steps} steps")
print(f"   📈 Logging every: {training_args.logging_steps} steps")
# print(f"   🛑 Early stopping: {early_stopping_callback.early_stopping_patience * training_args.eval_steps} steps without improvement")
print(f"   📁 Max checkpoints: {training_args.save_total_limit}")
print(f"   📚 Training samples: {len(final_dataset['train'])}")
print(f"   🧪 Evaluation samples: {len(final_dataset['test'])}")
print(f"   🎯 Total epochs: {training_args.num_train_epochs}")
print(f"   🏆 Best metric: {training_args.metric_for_best_model}")
```

    --- Enhanced Trainer with Early Stopping initialized ---
    📊 Configuration Summary:
       🔄 Evaluation every: None steps
       💾 Saving every: 500 steps
       📈 Logging every: 25 steps


    /tmp/ipython-input-33-900272129.py:48: FutureWarning: `tokenizer` is deprecated and will be removed in version 5.0.0 for `Trainer.__init__`. Use `processing_class` instead.
      trainer_2 = Trainer(



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    /tmp/ipython-input-33-900272129.py in <cell line: 0>()
         62 print(f"   💾 Saving every: {training_args.save_steps} steps")
         63 print(f"   📈 Logging every: {training_args.logging_steps} steps")
    ---> 64 print(f"   🛑 Early stopping: {early_stopping_callback.early_stopping_patience * training_args.eval_steps} steps without improvement")
         65 print(f"   📁 Max checkpoints: {training_args.save_total_limit}")
         66 print(f"   📚 Training samples: {len(final_dataset['train'])}")


    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'



```python
trainer_2.train()
print("Training complete.")
```



    <div>

      <progress value='125' max='528' style='width:300px; height:20px; vertical-align: middle;'></progress>
      [125/528 08:00 < 26:13, 0.26 it/s, Epoch 1/6]
    </div>
    <table border="1" class="dataframe">
  <thead>
 <tr style="text-align: left;">
      <th>Step</th>
      <th>Training Loss</th>
      <th>Validation Loss</th>
      <th>Line Accuracy</th>
      <th>Correct Predictions</th>
      <th>Total Samples</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>25</td>
      <td>3.336100</td>
      <td>0.485392</td>
      <td>0.348138</td>
      <td>243</td>
      <td>698</td>
    </tr>
    <tr>
      <td>50</td>
      <td>3.416800</td>
      <td>0.482614</td>
      <td>0.355301</td>
      <td>248</td>
      <td>698</td>
    </tr>
    <tr>
      <td>75</td>
      <td>3.393700</td>
      <td>0.491674</td>
      <td>0.381089</td>
      <td>266</td>
      <td>698</td>
    </tr>
    <tr>
      <td>100</td>
      <td>3.172100</td>
      <td>0.487001</td>
      <td>0.355301</td>
      <td>248</td>
      <td>698</td>
    </tr>
    <tr>
      <td>125</td>
      <td>3.255500</td>
      <td>0.483073</td>
      <td>0.365330</td>
      <td>255</td>
      <td>698</td>
    </tr>
  </tbody>
</table><p>


    There were unexpected keys in the checkpoint model loaded: ['base.base_model.model.model.layers.0.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.0.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.0.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.0.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.0.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.0.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.0.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.0.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.0.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.0.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.0.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.0.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.1.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.1.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.1.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.1.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.1.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.1.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.1.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.1.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.1.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.1.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.1.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.1.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.2.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.2.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.2.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.2.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.2.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.2.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.2.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.2.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.2.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.2.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.2.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.2.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.3.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.3.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.3.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.3.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.3.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.3.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.3.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.3.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.3.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.3.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.3.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.3.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.4.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.4.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.4.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.4.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.4.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.4.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.4.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.4.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.4.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.4.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.4.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.4.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.5.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.5.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.5.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.5.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.5.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.5.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.5.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.5.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.5.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.5.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.5.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.5.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.6.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.6.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.6.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.6.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.6.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.6.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.6.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.6.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.6.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.6.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.6.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.6.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.7.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.7.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.7.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.7.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.7.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.7.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.7.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.7.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.7.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.7.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.7.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.7.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.8.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.8.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.8.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.8.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.8.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.8.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.8.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.8.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.8.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.8.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.8.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.8.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.9.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.9.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.9.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.9.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.9.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.9.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.9.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.9.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.9.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.9.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.9.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.9.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.10.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.10.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.10.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.10.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.10.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.10.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.10.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.10.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.10.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.10.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.10.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.10.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.11.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.11.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.11.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.11.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.11.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.11.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.11.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.11.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.11.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.11.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.11.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.11.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.12.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.12.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.12.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.12.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.12.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.12.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.12.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.12.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.12.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.12.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.12.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.12.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.13.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.13.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.13.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.13.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.13.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.13.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.13.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.13.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.13.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.13.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.13.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.13.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.14.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.14.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.14.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.14.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.14.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.14.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.14.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.14.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.14.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.14.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.14.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.14.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.15.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.15.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.15.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.15.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.15.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.15.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.15.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.15.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.15.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.15.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.15.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.15.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.16.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.16.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.16.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.16.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.16.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.16.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.16.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.16.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.16.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.16.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.16.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.16.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.17.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.17.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.17.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.17.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.17.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.17.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.17.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.17.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.17.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.17.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.17.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.17.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.18.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.18.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.18.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.18.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.18.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.18.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.18.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.18.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.18.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.18.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.18.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.18.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.19.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.19.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.19.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.19.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.19.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.19.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.19.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.19.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.19.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.19.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.19.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.19.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.20.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.20.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.20.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.20.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.20.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.20.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.20.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.20.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.20.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.20.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.20.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.20.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.21.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.21.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.21.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.21.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.21.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.21.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.21.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.21.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.21.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.21.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.21.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.21.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.22.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.22.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.22.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.22.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.22.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.22.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.22.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.22.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.22.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.22.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.22.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.22.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.23.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.23.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.23.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.23.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.23.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.23.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.23.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.23.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.23.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.23.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.23.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.23.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.24.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.24.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.24.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.24.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.24.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.24.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.24.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.24.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.24.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.24.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.24.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.24.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.25.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.25.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.25.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.25.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.25.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.25.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.25.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.25.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.25.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.25.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.25.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.25.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.26.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.26.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.26.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.26.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.26.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.26.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.26.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.26.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.26.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.26.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.26.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.26.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.27.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.27.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.27.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.27.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.27.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.27.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.27.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.27.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.27.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.27.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.27.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.27.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.28.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.28.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.28.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.28.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.28.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.28.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.28.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.28.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.28.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.28.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.28.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.28.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.29.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.29.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.29.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.29.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.29.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.29.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.29.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.29.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.29.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.29.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.29.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.29.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.30.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.30.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.30.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.30.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.30.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.30.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.30.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.30.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.30.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.30.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.30.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.30.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.31.self_attn.o_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.31.self_attn.o_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.31.self_attn.o_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.31.self_attn.qkv_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.31.self_attn.qkv_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.31.self_attn.qkv_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.31.mlp.gate_up_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.31.mlp.gate_up_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.31.mlp.gate_up_proj.base_layer.weight.quant_state.bitsandbytes__nf4', 'base.base_model.model.model.layers.31.mlp.down_proj.base_layer.weight.absmax', 'base.base_model.model.model.layers.31.mlp.down_proj.base_layer.weight.quant_map', 'base.base_model.model.model.layers.31.mlp.down_proj.base_layer.weight.quant_state.bitsandbytes__nf4'].


    Training complete.



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


```python
# # ==============================================================================
# # TESTING SUITE: Comprehensive Pipeline Validation
# # ==============================================================================

# def run_comprehensive_test_suite():
#     """Run all tests in sequence"""
#     print("🚀 RUNNING COMPREHENSIVE TEST SUITE")
#     print("=" * 80)

#     # Load dataset first
#     dataset_path = Config.DATASET_PATH
#     df = pd.read_csv(dataset_path)

#     # Initialize tokenizer
#     tokenizer = AutoTokenizer.from_pretrained(Config.MODEL_ID, trust_remote_code=True)
#     if tokenizer.pad_token is None:
#         tokenizer.pad_token = tokenizer.eos_token

#     # Initialize data collator
#     data_collator = DataCollatorForLineClassification(tokenizer=tokenizer)

#     test_results = {}

#     # Run tests
#     test_results['dataset_loading'] = test_dataset_loading_and_format()
#     test_results['line_labels'] = test_line_labels_validation(df)

#     # Prepare sample texts for tokenization test
#     sample_texts = [
#         f"Problem: {row['question']}\n\nSolution: {row['solution']}"
#         for _, row in df.sample(3, random_state=42).iterrows()
#     ]
#     test_results['tokenization'] = test_tokenization_and_line_detection(tokenizer, sample_texts)

#     test_results['preprocessing'] = test_preprocessing_function(df, tokenizer)

#     # Create processed dataset for remaining tests
#     small_df = df.sample(5, random_state=42)
#     small_dataset = Dataset.from_pandas(small_df)
#     processed_dataset = small_dataset.map(preprocess_for_line_detection, batched=True)

#     test_results['data_collator'] = test_data_collator(data_collator, processed_dataset)

#     # Skip model tests for now (will be added when model is loaded)
#     test_results['solution_alignment'] = test_solution_line_alignment(df)

#     # Print summary
#     print("\n" + "=" * 80)
#     print("🏁 TEST SUITE SUMMARY")
#     print("=" * 80)

#     for test_name, result in test_results.items():
#         status = "✅ PASS" if result else "❌ FAIL"
#         print(f"{status} {test_name}")

#     overall_success = all(test_results.values())
#     print(f"\n🎯 Overall Status: {'✅ ALL TESTS PASSED' if overall_success else '❌ SOME TESTS FAILED'}")

#     return test_results

```
