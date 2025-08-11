# Level 1 Fine-Tuning: Binary Classification of Solution Correctness

## 1. Environment Setup

### 1.1 Mount google drive
This notebook fine-tunes the `microsoft/Phi-4-mini-instruct` model for a binary sequence classification task. The goal is to train the model to distinguish between "Correct" (Label 0) and "Flawed" (Label 1) mathematical solutions.

We begin by setting up the necessary environment in Google Colab. This includes mounting Google Drive for persistent storage, installing the required Python libraries for model training and data handling, and preparing our dataset.


```python
# --- 1.1: Mount Google Drive ---
from google.colab import drive
drive.mount('/content/drive')
```

### 1.2 Library Installation

Next, we install the core libraries from the Hugging Face ecosystem and other tools required for efficient model training.

-   **`transformers`**: The primary library for interacting with Hugging Face models and tokenizers.
-   **`peft` (Parameter-Efficient Fine-Tuning)**: A library that enables techniques like LoRA (Low-Rank Adaptation), which allows us to fine-tune large models by training only a small number of new parameters ("adapters"). This dramatically reduces memory and computational requirements.
-   **`accelerate`**: Simplifies running PyTorch training loops on any distributed hardware (e.g., single GPU, multiple GPUs, TPUs) with minimal code changes.
-   **`bitsandbytes`**: Enables model quantization, a technique to load the model with lower precision (e.g., in 4-bit instead of 32-bit). This is essential for fitting a large model into the VRAM of a single GPU.
-   **`datasets`**: Provides a highly efficient and easy-to-use framework for loading and preprocessing the data.
-   **`trl`**: The Transformer Reinforcement Learning library, often used for more advanced fine-tuning like DPO. While not strictly necessary for our simple classification task, we include it for consistency with more advanced project goals.


```python
# --- 1.2: Install Required Libraries ---

!pip install -Uq transformers
!pip install -Uq peft
!pip install -Uq trl
!pip install -Uq accelerate
!pip install -Uq datasets
!pip install -Uq bitsandbytes

!pip install flash-attn==2.7.4.post1 \
  --extra-index-url https://download.pytorch.org/whl/cu124 \
  --no-build-isolation
```

## 2. Project Configuration

### 2.1 Define Core Parameters

To maintain a clean and organized notebook, we define all key parameters and hyperparameters in a central `Config` class. This practice makes it easy to modify experiment settings without searching through the entire codebase.

-   **`MODEL_ID`**: The identifier for the pre-trained model we will fine-tune, hosted on the Hugging Face Hub. We use `microsoft/Phi-4-mini-instruct`, a powerful small language model.
-   **`DATASET_PATH`**: The local path in the Colab environment where the unzipped dataset from step 1.3 is located.
-   **`OUTPUT_DIR`**: The directory where the results of our training, specifically the final LoRA adapter, will be saved.
-   **`NUM_LABELS`**: The number of output classes for our classification task. For Level 1, this is `2` ("Correct" and "Flawed").


```python
# --- 2.1: Define Project Configuration ---

class Config:
    # Model ID from Hugging Face Hub
    MODEL_ID = "microsoft/Phi-4-mini-instruct"

    # Local path to the unzipped dataset
    DATASET_PATH = "/content/level-1-binary"

    # Directory for saving the final model adapter
    OUTPUT_DIR = "/content/level1-classifier-output"

    # Number of labels for the classification task
    NUM_LABELS = 2
```

### 2.2 Load Dataset from Disk

With our configuration defined, the first step in our data pipeline is to load the raw dataset from the local directory where it was unzipped. We use the `load_from_disk` function from the `datasets` library, which is highly efficient for loading datasets saved in the Apache Arrow format.

The function will return a `DatasetDict` object, a dictionary-like structure that typically contains our predefined data splits: `train`, `validation`, and `test`. We will print this object to verify its contents and structure.


```python
# --- 2.2: Load Dataset from Disk ---
from datasets import load_from_disk

# Load the dataset using the path defined in our Config
raw_dataset = load_from_disk(Config.DATASET_PATH)

# Display the structure of the loaded dataset
print("--- Raw Dataset Structure ---")
print(raw_dataset)
```

## 3. Data Preprocessing

### 3.1 Load and Configure the Tokenizer

Before the model can process our text, we must convert it into a sequence of numerical IDs through a process called **tokenization**. Each model has its own specific tokenizer, which was trained alongside it. It is essential to use the exact same tokenizer as the base model (`Phi-4-mini-instruct` in our case) to ensure the input is interpreted correctly.

We perform two key configuration steps:
1.  **`padding_side = "left"`**: For causal language models like Phi-4, it is standard practice to pad on the left. This is particularly important when using optimizations like Flash Attention. It ensures that the actual content tokens, which the model uses for prediction, are aligned to the right, simplifying the internal logic for tasks like sequence classification where we often look at the final token's representation.
2.  **`pad_token`**: We ensure a padding token is defined. If the tokenizer doesn't have a pre-defined `pad_token`, we set it to the `eos_token` (End of Sequence). The model will use this token's ID to fill shorter sequences in a batch up to the length of the longest sequence in the batch (necessary for processing samples in the batch in parallel).


```python
# --- 3.1: Load and Configure the Tokenizer ---
from transformers import AutoTokenizer

# Load the tokenizer associated with the specified model
tokenizer = AutoTokenizer.from_pretrained(
    Config.MODEL_ID,
    trust_remote_code=True
)

# Configure tokenizer padding for a causal language model
tokenizer.padding_side = "left"
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

print("Tokenizer loaded and configured successfully.")
```

### 3.2 Create and Apply the Preprocessing Function

Now, we define a function that will format our `question` and `solution` text into a single, structured input string based on a prompt template. This template provides clear context to the instruction-tuned model, telling it what task to perform. The template is as follows:

```text
Analyze the following mathematical problem and solution to determine if the solution is correct or flawed.

###
Problem:
{question}

###
Solution:
{solution}

```


This formatted string is then tokenized. We apply this function across our entire dataset using the `.map()` method, which is highly efficient.

-   **`truncation=True`**: If a formatted input exceeds the `max_length`, it will be cut short.
-   **`max_length=512`**: A reasonable maximum sequence length for this task, balancing context preservation with memory constraints.
-   **`padding=False`**: We do *not* pad the sequences at this stage. Padding is applied dynamically on a per-batch basis by a `DataCollator` during training. This is more efficient as it avoids padding every sample in the dataset to a global maximum length.
-   **`remove_columns`**: We discard the original text columns (`question`, `solution`) as they are no longer needed after tokenization.


```python
# --- 3.2: Define and Apply Preprocessing ---

def preprocess_function(examples):
    """
    Formats the input text using a prompt template and tokenizes it.
    The 'label' and 'index' columns are passed through untouched.
    """
    # Define the instruction prompt for the model
    system_prompt = "Analyze the following mathematical problem and solution to determine if the solution is correct or flawed."

    # Create a single formatted input string for each example
    input_texts = [
        f"{system_prompt}\n\n### Problem:\n{q}\n\n### Solution:\n{s}"
        for q, s in zip(examples["question"], examples["solution"])
    ]

    # Tokenize the formatted text
    return tokenizer(
        input_texts,
        truncation=True,
        max_length=512,
        padding=False
    )

# Apply the function to all splits of the dataset
tokenized_dataset = raw_dataset.map(
    preprocess_function,
    batched=True,  # Process examples in batches for speed
    remove_columns=["question", "solution"]
)

# --- Verification of a Single Example ---

# 1. Reconstruct the full prompt for the first training example
first_example_raw = raw_dataset["train"][0]
system_prompt = "Analyze the following mathematical problem and solution to determine if the solution is correct or flawed."
full_prompt = f"{system_prompt}\n\n### Problem:\n{first_example_raw['question']}\n\n### Solution:\n{first_example_raw['solution']}"

# 2. Get the tokenized output for the same example
first_example_tokenized = tokenized_dataset["train"][0]["input_ids"]

# 3. Print everything for inspection
print("--- Example of a Single Processed Input ---")
print("\n[Full Prompt String]\n")
print(full_prompt)
print("\n\n[Corresponding Token IDs]\n")
print(first_example_tokenized)
```

### 3.3 Combine Training and Validation Splits

For this initial experiment, we will not perform evaluation during the training process (`eval_strategy="epoch"` is disabled). Instead, we will use a final, single evaluation on the hold-out `test` set to judge the model's performance.

Given this approach, we can maximize the amount of data the model trains on by combining the original `train` and `validation` splits into a single, larger training set. This is a pragmatic strategy when compute resources are limited and the primary goal is to train a prototype, rather than to perform extensive hyperparameter tuning using a validation set.

We use the `concatenate_datasets` function to merge the two splits and then create a new `DatasetDict` that will contain our final `train` and `test` sets to be used by the `Trainer`.


```python
# --- 3.3: Combine Training and Validation Splits ---
from datasets import concatenate_datasets, DatasetDict

# Combine the 'train' and 'validation' splits from the tokenized dataset
full_train_dataset = concatenate_datasets(
    [tokenized_dataset["train"], tokenized_dataset["validation"]]
)

# Create a new DatasetDict with the merged training set and the original test set
final_dataset = DatasetDict({
    "train": full_train_dataset,
    "test": tokenized_dataset["test"]
})

# Display the structure of the final dataset to be used for training
print("--- Final Dataset for Training and Evaluation ---")
print(final_dataset)
```

## 4. Model Architecture Definition

Before we conduct our experiments, we need to define the architectural components that will be used in both the linear probe baseline and the full LoRA fine-tuning. The central piece is a custom PyTorch module that wraps the LLM backbone and attaches a classification head to it.

### 4.1 Define the Custom Classifier Class

We will create a class called `GPTSequenceClassifier` that inherits from `torch.nn.Module`. This class is designed to be flexible and can accept any Hugging Face model as its `base_model`. Its primary responsibilities are:

1.  To hold the base LLM (the "backbone") and the final classification layer (the "head").
2.  To define the data flow in its `forward` method, which takes tokenized inputs and produces the final class logits.

By defining this class once, we can reuse it consistently across both of our upcoming experiments, ensuring a fair and direct comparison.

---
#### The `forward` Method: A Detailed Walkthrough

The `forward` method defines the precise data flow for a single prediction. Let's break it down step-by-step:

**1. Get Hidden States from the Backbone**

The process begins by passing the tokenized input through the `base_model` (our backbone).
-   The backbone's output, which we call `outputs`, is **not** a single tensor. It is a special container object from the Hugging Face library that holds various potential outputs.
-   Because we pass `output_hidden_states=True` to the backbone, this `outputs` object contains a tuple called `hidden_states`. This tuple holds the output tensor from *every single layer* of the transformer.
-   We extract the output from the **final layer** using `outputs.hidden_states[-1]`. This gives us the most contextually rich representation of the input tokens.

The resulting tensor, `last_hidden_state`, has a shape of `(batch_size, sequence_length, hidden_size)`. It's crucial to understand this shape:
-   A transformer is a **sequence-to-sequence** processor. For every token we provide in the input sequence, it produces a corresponding output vector.
-   **`hidden_size`** is the dimensionality of these vectors (for `microsoft/Phi-4-mini-instruct`, this is 3072). It is the fundamental "width" of the model's internal representations. The `self.classifier` is designed to take a vector of this size as input.

**2. Pooling: From a Sequence to a Single Vector**

Our goal is classification, so we need a single vector to represent the entire input sequence, not a sequence of vectors. This reduction process is called **pooling**.
-   We use **last-token pooling**, a common and effective strategy for causal models. We simply select the hidden state vector corresponding to the very last token of each sequence: `last_hidden_state[:, -1, :]`.
-   The rationale is that a causal (decoder-only) model is trained to predict the next token. Therefore, the hidden state of the final token has, by necessity, attended to all preceding tokens and implicitly contains a summary of the entire sequence's meaning.
-   This step reduces the tensor's shape from `(batch_size, sequence_length, hidden_size)` to `(batch_size, hidden_size)`.

**3. Classification: Generating Logits**

The pooled vector for each sample, which now represents the entire input, is passed through our new, trainable `nn.Linear` classifier.
-   This layer performs a simple matrix multiplication, projecting the `hidden_size` dimension down to our `NUM_LABELS` (2 in this case).
-   The output of this layer is the final `logits` tensor of shape `(batch_size, NUM_LABELS)`. Each row contains the raw, unnormalized scores for the "Correct" and "Flawed" classes for one sample in the batch.

**4. Loss Calculation (During Training)**

This step only occurs when `labels` are provided to the `forward` method (i.e., during a training step).
-   We use **`nn.functional.cross_entropy`**, the standard loss function for multi-class classification tasks.
-   This function compares the predicted `logits` with the true `labels` to compute a single scalar `loss` value. It expects its inputs to have specific shapes:
    -   `logits`: A 2D tensor of shape `(N, C)`, where `N` is the batch size and `C` is the number of classes.
    -   `labels`: A 1D tensor of shape `(N)`.
-   This `loss` value is what the `Trainer` uses to compute gradients and update the model's trainable weights via backpropagation.


```python
# --- 4.1: Define the Custom Classifier Class ---
import torch.nn as nn

class GPTSequenceClassifier(nn.Module):
    """
    A custom wrapper class for sequence classification using an LLM backbone.
    """
    def __init__(self, base_model, num_labels):
        super().__init__()
        self.base = base_model
        hidden_size = base_model.config.hidden_size
        self.classifier = nn.Linear(hidden_size, num_labels, bias=True)
        self.num_labels = num_labels

    def forward(self, input_ids=None, attention_mask=None, labels=None, **kwargs):
        # 1. Get hidden states from the backbone
        outputs = self.base(
            input_ids=input_ids,
            attention_mask=attention_mask,
            output_hidden_states=True,
            **kwargs,
            )
        
        # 2. Perform last-token pooling
        last_hidden_state = outputs.hidden_states[-1]
        pooled_output = last_hidden_state[:, -1, :]
        
        # 3. Pass the pooled output through the classifier to get logits
        logits = self.classifier(pooled_output)

        # 4. Calculate loss if labels are provided (i.e., during training)
        loss = None
        if labels is not None:
            loss = nn.functional.cross_entropy(logits.view(-1, self.num_labels), labels.view(-1))
        
        # Return a dictionary compatible with the Hugging Face Trainer
        return {"loss": loss, "logits": logits} if loss is not None else {"logits": logits}

print("GPTSequenceClassifier class defined successfully.")
```

## 5. Common Training Components

To ensure that our comparison between the linear probe and the full LoRA fine-tuning is fair and consistent, we will define a single, shared set of training configurations. This includes the `TrainingArguments` that control the training loop and the `compute_metrics` function for evaluation.

### 5.1 Define Training Arguments

The Hugging Face `Trainer` is configured through a `TrainingArguments` object, which encapsulates all the hyperparameters and settings for the training run. By defining this once, we guarantee that both experiments use the same learning rate, batch size, optimizer, etc., making the final results directly comparable.

Let's break down the key arguments:

---
#### Batching & Epochs

-   **`num_train_epochs`**: The total number of times the training loop will iterate over the entire training dataset.
-   **`per_device_train_batch_size`**: The number of samples processed by the GPU in a single forward/backward pass.
-   **`gradient_accumulation_steps`**: A crucial technique to simulate a larger effective batch size (`8 × 4 = 32` in our case) without increasing VRAM usage.

---
#### Optimizer & Learning Rate Schedule

-   **`optim="paged_adamw_8bit"`**: A memory-efficient variant of the AdamW optimizer that reduces VRAM consumption.
-   **`learning_rate`**: The initial learning rate for the optimizer.
-   **`lr_scheduler_type="cosine"`**: A scheduler that smoothly anneals the learning rate down towards zero over the course of training, helping the model converge more effectively.
-   **`warmup_ratio`**: A warmup phase where the learning rate gradually increases over the first 10% of training steps to prevent initial instability.

---
#### Precision & Memory Management

-   **`bf16=True`**: Enables automatic mixed-precision training using the `bfloat16` format, which is natively accelerated on modern GPUs (like the A100) to speed up computations and reduce memory.
-   **`gradient_checkpointing=False`**: This memory-saving technique is disabled here to prioritize speed, as our other optimizations (4-bit quantization, LoRA) are sufficient.

---
#### Logging & Checkpointing

-   **`logging_strategy` / `logging_steps`**: Controls how often training metrics are printed.
-   **`save_strategy` / `save_total_limit`**: Defines the checkpointing strategy. We will save the model adapter at the end of each epoch and keep only the single most recent checkpoint.
-   **`output_dir`**: This will serve as a base directory. When we initialize the `Trainer` for each experiment, we will point each one to a unique subdirectory to keep the results and checkpoints separate.


```python
# --- 5.1: Define Common Training Arguments ---
from transformers import TrainingArguments

# Define the arguments that will be shared across both training runs.
training_args = TrainingArguments(
    # Base directory for outputs. Specific trainers will use subdirectories.
    output_dir="/content/training_output",

    # --- Batching & Epochs ---
    num_train_epochs=3,
    per_device_train_batch_size=8,
    gradient_accumulation_steps=4,

    # --- Optimizer & Learning Rate Schedule ---
    optim="paged_adamw_8bit",
    learning_rate=2e-4,
    lr_scheduler_type="cosine",
    warmup_ratio=0.1,

    # --- Precision & Memory ---
    bf16=True,
    gradient_checkpointing=False,

    # --- Logging & Checkpointing ---
    logging_strategy="steps",
    logging_steps=25,
    save_strategy="epoch",
    save_total_limit=1,
    report_to="none",
    save_safetensors=False,
)

print("Common TrainingArguments configured.")
```

### 5.2 Define the Evaluation Metric

Both the linear probe and the full LoRA fine-tuning will be evaluated using the same metric: **accuracy**. To implement this, we define a single `compute_metrics` function that will be passed to both `Trainer` instances.

This function receives an `EvalPrediction` object (`p`) from the `Trainer` during the evaluation phase. This object conveniently packages the model's outputs:
-   `p.predictions`: A NumPy array containing the raw `logits` produced by the model.
-   `p.label_ids`: A NumPy array containing the ground-truth labels.

Our function performs three simple steps:
1.  Extracts the logits.
2.  Converts the raw logits into final class predictions (0 or 1) using `np.argmax`.
3.  Calculates accuracy by comparing the predictions with the true labels and returns the result in a dictionary, as required by the `Trainer`.


```python
# --- 5.2: Define the Evaluation Metric ---
import numpy as np

def compute_metrics(p: 'EvalPrediction'):
    """
    Computes accuracy for a sequence classification task. Accepts an EvalPrediction object `p` which contains the model's predictions and true labels. Returns a dictionary mapping `"accuracy"` to its value.
    """
    logits = p.predictions[0] if isinstance(p.predictions, (tuple, list)) else p.predictions
    preds = np.argmax(logits, axis=1)
    labels = p.label_ids
    accuracy = (preds == labels).mean().item()
    return {"accuracy": accuracy}

print("Metric computation function defined.")
```

## 6. Experiment 1: Linear Probe Baseline

Our first experiment aims to establish a strong, informative baseline. Instead of just measuring the performance of a randomly initialized model, we will perform **linear probing**.

**The Concept:** Linear probing answers the question, *"How good are the off-the-shelf representations from the pre-trained `Phi-4-mini` model for our specific task?"*

To find out, we will:
1.  Load the pre-trained backbone and **freeze it completely**, ensuring that none of its 4.2 billion parameters can be updated.
2.  Attach a new, trainable classification head on top.
3.  Train **only the classification head**.

The resulting accuracy will tell us how "linearly separable" our classes ("Correct" vs. "Flawed") are using the fixed features provided by the base model. This is a much more powerful baseline than random chance and provides a true measure of the base model's zero-shot understanding of our task's domain.

### 6.1 Define and Freeze the Backbone for Probing

Our first step is to prepare the model for this experiment. We load a fresh instance of the `microsoft/Phi-4-mini-instruct` model using 4-bit quantization for memory efficiency.

The most critical step here is to manually iterate through every parameter in the loaded backbone and set its `requires_grad` attribute to `False`. This explicitly tells the PyTorch autograd engine not to compute gradients for these parameters, effectively freezing them and ensuring they will not be modified by the optimizer during training.


```python
# --- 6.1: Define and Freeze the Backbone for Probing ---
import torch
from transformers import AutoModelForCausalLM, BitsAndBytesConfig

# Define the data type and quantization configuration
DTYPE = torch.bfloat16
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=DTYPE,
)

# Load a fresh instance of the base model
backbone_probe = AutoModelForCausalLM.from_pretrained(
    Config.MODEL_ID,
    quantization_config=quantization_config,
    device_map="auto",
    trust_remote_code=True,
    attn_implementation="flash_attention_2",
)

# --- CRITICAL STEP: Freeze all parameters in the backbone ---
for param in backbone_probe.parameters():
    param.requires_grad = False

# Ensure the model's pad token ID is set correctly
backbone_probe.config.pad_token_id = tokenizer.pad_token_id

print("Backbone for linear probing loaded and all parameters frozen.")
```

### 6.2 Initialize the Linear Probe Trainer

Now that we have our frozen backbone, we can assemble the complete model for our linear probing experiment. We do this by passing the frozen `backbone_probe` to our `GPTSequenceClassifier` class.

This creates a model where:
-   The `base` component (the entire `Phi-4-mini` model) is frozen and its weights will not change.
-   The `classifier` component (the `nn.Linear` head) is randomly initialized and, by default, its parameters have `requires_grad=True`, meaning they are trainable.

We then instantiate a new `Trainer` specifically for this experiment (`trainer_probe`). We pass it our shared `training_args` and `compute_metrics` function, but we make sure to give it a unique `output_dir` to prevent its checkpoints and results from overwriting our main experiment later on.


```python
# --- 6.2: Initialize the Linear Probe Trainer ---
from transformers import Trainer, DataCollatorWithPadding
import copy

# Instantiate the model: frozen backbone + trainable head.
model_probe = GPTSequenceClassifier(backbone_probe, Config.NUM_LABELS)

# Verify that only the classifier's weights are trainable
print("Trainable parameters for linear probe model:")
model_probe.base.print_trainable_parameters() # Should show 0 trainable params

# Create a copy of the shared training args to modify the output directory
probe_training_args = copy.deepcopy(training_args)
probe_training_args.output_dir = "/content/training_output/linear_probe"

# The data collator will dynamically pad inputs in each batch.
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

# Instantiate a dedicated Trainer for the linear probe experiment.
trainer_probe = Trainer(
    model=model_probe,
    args=probe_training_args,
    train_dataset=final_dataset["train"],
    eval_dataset=final_dataset["test"],
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
)

print("\nTrainer for linear probing initialized successfully.")
```

### 6.3 Train the Classifier Head (Linear Probe)

With the `trainer_probe` fully configured, we can now start the training process. By calling `trainer_probe.train()`, we begin the training loop.

Crucially, because we have frozen the entire backbone, the optimizer will **only** see and update the parameters of the randomly initialized classification head. The training process will be very fast and memory-efficient as it is only optimizing a tiny number of parameters (~6k) relative to the full model size.

The goal of this training run is to find the best possible linear mapping from the fixed `Phi-4-mini` representations to our "Correct" / "Flawed" labels.


```python
# --- 6.3: Train the Classifier Head (Linear Probe) ---

print("--- Starting training for the linear probe baseline ---")
trainer_probe.train()
print("\n--- Linear probe training complete ---")
```

### 6.4 Evaluate the Linear Probe Baseline

After the head-only training is complete, we immediately evaluate the model's performance on the hold-out test set. We call `trainer_probe.evaluate()` to run inference and compute our accuracy metric.

The resulting accuracy is our **linear probe baseline**. This number is highly informative: it represents the best performance achievable on our task using only a simple linear classifier on top of the fixed, pre-trained `Phi-4-mini` representations. Any improvement we see in our next experiment can be directly attributed to the fine-tuning of the model's internal representations via LoRA.


```python
# --- 6.4: Evaluate the Linear Probe Baseline ---

print("--- Evaluating the linear probe model on the test set ---")
probe_results = trainer_probe.evaluate()

print("\n--- Linear Probe Baseline Performance ---")
print(probe_results)
```

### 6.5 Save Baseline Model Predictions

While the aggregate accuracy score from `.evaluate()` is a good summary, it's often more insightful to analyze the model's predictions on a sample-by-sample basis. To do this, we use `trainer.predict()` to get the raw logits for every sample in the test set.

We then convert these logits into probabilities using the softmax function. Finally, we compile these probabilities, along with the true labels and problem indices, into a pandas DataFrame and save it as a CSV file. This file will allow us to later inspect specific cases where the baseline model was confident or uncertain, correct or incorrect.


```python
# --- 6.5: Save Baseline Model Predictions ---
import torch
import pandas as pd

print("--- Generating and saving baseline model predictions for the test set ---")

# 1. Get prediction outputs from the trainer
pred_outputs_probe = trainer_probe.predict(final_dataset["test"])

# 2. Extract logits
logits_probe = pred_outputs_probe.predictions[0] if isinstance(pred_outputs_probe.predictions, tuple) else pred_outputs_probe.predictions

# 3. Convert logits to probabilities
probs_probe = torch.softmax(torch.tensor(logits_probe), dim=-1).numpy()

# 4. Create a DataFrame for analysis
df_probe = pd.DataFrame(probs_probe, columns=[f"p(class={i})" for i in range(Config.NUM_LABELS)])
df_probe["index"] = final_dataset["test"]["index"]
df_probe["true_label"] = final_dataset["test"]["label"]

# Reorder columns for clarity
cols = ["index", "true_label"] + [c for c in df_probe.columns if c.startswith("p(")]
df_probe = df_probe[cols]

# 5. Save to CSV
output_path = "/content/probe_baseline_predictions.csv"
df_probe.to_csv(output_path, index=False)

print(f"\nBaseline predictions saved to {output_path}")
print(df_probe.head())
```

## 7. Experiment 2: Full LoRA Fine-Tuning

Having established our linear probe baseline, we now proceed to the main experiment. The goal is to measure the performance gain achieved by fine-tuning the model's internal representations using Parameter-Efficient Fine-Tuning (PEFT) with LoRA.

In this experiment, we will train the system end-to-end. Both the LoRA adapters injected into the backbone and the final classification head will be trained simultaneously. This allows for **co-adaptation**: the backbone learns to produce feature representations that are better suited for our specific task, and the classifier head learns to optimally separate these new, improved representations.

### 7.1 Define the LoRA-Enabled Model

The first step is to construct the model. This involves three stages:
1.  **Load a fresh instance** of the `microsoft/Phi-4-mini-instruct` backbone, again using 4-bit quantization.
2.  **Define the `LoraConfig`**, specifying the parameters for our adapters (e.g., rank, alpha). For a detailed explanation of LoRA, refer back to the extended discussions in sections 4.2 and beyond.
3.  **Apply LoRA** by wrapping the backbone with `get_peft_model`. This injects the trainable adapters into the frozen layers of the base model.
4.  **Wrap the resulting `lora_backbone`** with our `GPTSequenceClassifier` to attach a new, randomly initialized (and trainable) classification head.


```python
# --- 7.1: Define the LoRA-Enabled Model ---
from peft import LoraConfig, get_peft_model, TaskType

# Load a fresh instance of the base model for this experiment
backbone_lora = AutoModelForCausalLM.from_pretrained(
    Config.MODEL_ID,
    quantization_config=quantization_config, # Defined in 6.1
    device_map="auto",
    trust_remote_code=True,
    attn_implementation="flash_attention_2",
)
backbone_lora.config.pad_token_id = tokenizer.pad_token_id

# Define the configuration for the LoRA adapters
lora_config = LoraConfig(
    task_type=TaskType.SEQ_CLS,
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    target_modules="all-linear",
)

# Apply the LoRA configuration to the backbone
lora_backbone = get_peft_model(backbone_lora, lora_config)

# Instantiate the new model with the LoRA backbone
model_lora = GPTSequenceClassifier(lora_backbone, Config.NUM_LABELS)

# Verify the number of trainable parameters. This should now include
# both the LoRA adapters and the classifier head.
print("Trainable parameters for full LoRA fine-tuning model:")
model_lora.base.print_trainable_parameters()
```

### 7.2 Initialize the LoRA Trainer

We now set up a new `Trainer` instance specifically for this full fine-tuning experiment. As before, we use our shared `training_args` and `compute_metrics` function to ensure a fair comparison with the baseline.

The `Trainer` will be responsible for orchestrating the training loop, feeding batches of data to `model_lora`, calculating the loss, and backpropagating the error signal to update the trainable parameters—which in this case, are both the LoRA adapters and the weights of the classification head. We again assign a unique output directory to keep its results separate.


```python
# --- 7.2: Initialize the LoRA Trainer ---
import copy

# Create a copy of the shared training args to modify the output directory
lora_training_args = copy.deepcopy(training_args)
lora_training_args.output_dir = "/content/training_output/lora_finetune"

# Instantiate a new Trainer for the full fine-tuning experiment.
trainer_lora = Trainer(
    model=model_lora,
    args=lora_training_args,
    train_dataset=final_dataset["train"],
    eval_dataset=final_dataset["test"],
    tokenizer=tokenizer,
    data_collator=data_collator,      # Defined in 6.2
    compute_metrics=compute_metrics,  # Defined in 5.2
)

print("Trainer for full LoRA fine-tuning initialized successfully.")
```

### 7.3 Fine-Tune the LoRA Model

We now execute `trainer_lora.train()` to begin the full fine-tuning process. During this phase, the `Trainer` will update both the LoRA adapter weights within the backbone and the weights of the final classification head.

This co-adaptation process allows the model to learn task-specific features, pushing the vector representations for "Correct" and "Flawed" solutions into more easily separable regions of the embedding space, while the classifier head simultaneously learns the optimal boundary for these new, improved representations.


```python
# --- 7.3: Fine-Tune the LoRA Model ---

print("--- Starting full LoRA fine-tuning ---")
trainer_lora.train()
print("\n--- Full LoRA fine-tuning complete ---")
```

### 7.4 Evaluate the Fine-Tuned LoRA Model

With the full fine-tuning complete, we perform our final evaluation. We call `trainer_lora.evaluate()` on the hold-out test set to get the final performance metrics for our specialized model.

This result represents the peak performance of our system after adapting the model's internal representations via LoRA. The key step will be to compare this result directly against the linear probe baseline established in Experiment 1 to quantify the effectiveness of our fine-tuning strategy.


```python
# --- 7.4: Evaluate the Fine-Tuned LoRA Model ---

print("--- Evaluating the fine-tuned LoRA model on the test set ---")
lora_results = trainer_lora.evaluate()

print("\n--- LoRA Fine-Tuned Performance ---")
print(lora_results)
```

### 7.5 Save Fine-Tuned Model Predictions

We repeat the same prediction-saving process for our fully fine-tuned LoRA model. This will generate a second CSV file containing the predictions from `model_lora`.

Having both `probe_baseline_predictions.csv` and `lora_finetuned_predictions.csv` will allow for a powerful side-by-side comparison. We can analyze how fine-tuning not only changed the final prediction for a given problem but also how it shifted the model's confidence (i.e., the predicted probabilities).


```python
# --- 7.5: Save Fine-Tuned Model Predictions ---
import torch
import pandas as pd

print("--- Generating and saving fine-tuned model predictions for the test set ---")

# 1. Get prediction outputs from the trainer
pred_outputs_lora = trainer_lora.predict(final_dataset["test"])

# 2. Extract logits
logits_lora = pred_outputs_lora.predictions[0] if isinstance(pred_outputs_lora.predictions, tuple) else pred_outputs_lora.predictions

# 3. Convert logits to probabilities
probs_lora = torch.softmax(torch.tensor(logits_lora), dim=-1).numpy()

# 4. Create a DataFrame for analysis
df_lora = pd.DataFrame(probs_lora, columns=[f"p(class={i})" for i in range(Config.NUM_LABELS)])
df_lora["index"] = final_dataset["test"]["index"]
df_lora["true_label"] = final_dataset["test"]["label"]

# Reorder columns for clarity
cols = ["index", "true_label"] + [c for c in df_lora.columns if c.startswith("p(")]
df_lora = df_lora[cols]

# 5. Save to CSV
output_path = "/content/lora_finetuned_predictions.csv"
df_lora.to_csv(output_path, index=False)

print(f"\nFine-tuned predictions saved to {output_path}")
print(df_lora.head())
```

## 8. Saving Final Model Artifacts

With both experiments complete and the prediction data saved for offline analysis, the final step is to save the trained components from both the linear probe and the LoRA fine-tuning experiments. These artifacts are all we need to reload the models for future inference or analysis without having to retrain them.

### 8.1 Save the Linear Probe Model

First, we save the model from our baseline experiment. Calling `trainer_probe.save_model()` will save the state dictionary of the `GPTSequenceClassifier` used in the probe. The most important component in this save is the set of weights for the **trained classifier head**, as the backbone itself was frozen and remains identical to the original pre-trained model.


```python
# --- 8.1: Save the Linear Probe Model ---

# The output directory is already defined in the trainer's arguments
output_dir_probe = trainer_probe.args.output_dir

print(f"--- Saving the linear probe model to {output_dir_probe} ---")

# Save the model state, which primarily contains the trained classifier head
trainer_probe.save_model(output_dir_probe)

print("\nLinear probe model saved successfully.")
```

### 8.2 Save the Fine-Tuned LoRA Model

Next, we save the model from our main fine-tuning experiment. This is the most important artifact. `trainer_lora.save_model()` will save several critical components:

1.  **The LoRA Adapter Weights**: A file (`adapter_model.bin`) containing the weights for all trained LoRA layers.
2.  **The LoRA Configuration**: A file (`adapter_config.json`) storing the LoRA settings (e.g., `r`, `lora_alpha`).
3.  **The Full Model State**: A file (`pytorch_model.bin`) containing the weights for our **trained classification head**.
4.  **The Tokenizer**: All necessary tokenizer files for perfect replication.


```python
# --- 8.2: Save the Fine-Tuned LoRA Model ---

# The output directory is already defined in the trainer's arguments
output_dir_lora = trainer_lora.args.output_dir

print(f"--- Saving the final fine-tuned model to {output_dir_lora} ---")

# Save the LoRA adapters, the classification head, and the tokenizer
trainer_lora.save_model(output_dir_lora)

print("\nFine-tuned LoRA model saved successfully.")
```

### 8.3 Package All Artifacts for Download

To make it easy to download everything from Google Colab, we will package the entire parent `training_output` directory, which contains the subdirectories for both `linear_probe` and `lora_finetune`, into a single `.zip` file. This single archive will contain all the necessary components to reload and analyze both trained models.


```python
# --- 8.3: Package All Artifacts into a ZIP file ---

# The name for the final output zip file
zip_filename = "level1_all_model_artifacts.zip"

# The parent directory containing both experiment outputs
parent_directory_to_zip = training_args.output_dir # This was "/content/training_output"

# Use the zip shell command to create the archive.
# The -r flag ensures it recursively includes all subdirectories.
!zip -r {zip_filename} {parent_directory_to_zip}

print(f"\nSuccessfully created {zip_filename} containing all model artifacts.")
```

### 8.4 Download the Final Model Package

Finally, we use Colab's `files.download()` utility to trigger a browser download of the `.zip` file we just created. This allows us to easily save the complete set of trained artifacts from both experiments to our local machine for storage and offline analysis.


```python
# --- 8.3: Download the Final Model ZIP ---
from google.colab import files
files.download(zip_filename)
```
