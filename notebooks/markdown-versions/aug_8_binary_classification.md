```python
# Cell 1: Installations
!pip install -U transformers==4.53.2
!pip install -U peft
!pip install -U trl==0.20.0
!pip install -U accelerate
!pip install -U datasets
!pip install -U bitsandbytes

!pip install flash-attn==2.7.4.post1 \
  --extra-index-url https://download.pytorch.org/whl/cu124 \
  --no-build-isolation
```

```python
# Cell 2: Configuration
class Config:
    # Model ID from Hugging Face Hub
    MODEL_ID = "microsoft/Phi-4-mini-instruct"

    # Local path to the unzipped dataset
    DATASET_PATH = '/content/error_detection_dataset.csv'

    # Number of labels for the classification task
    NUM_LABELS = 2
```


```python
# ==============================================================================
# Cell 3: Data Loading and Preprocessing (Updated)
# ==============================================================================
import pandas as pd
import numpy as np
from datasets import Dataset, DatasetDict
from transformers import AutoTokenizer

# --- 3.1: Load Raw Data from CSV ---
df = pd.read_csv(Config.DATASET_PATH)

# --- 3.2: Create 'solution' and 'label' columns based on error_type ---
# If error_type is 'correct', use the correct_answer, otherwise use wrong_answer.
df['solution'] = np.where(df['error_type'] == 'correct', df['correct_answer'], df['wrong_answer'])

# The label is 1 (flawed) if the error_type is NOT 'correct', otherwise 0.
df['label'] = (df['error_type'] != 'correct').astype(int)

# --- 3.3: Split DataFrame using the 'split' column ---
train_df = df[df['split'] == 'train'].copy()
test_df = df[df['split'] == 'test'].copy()

# --- 3.4: Select final columns and convert to Hugging Face Dataset ---
# We keep 'index' for final referencing.
cols_to_keep = ['index', 'question', 'solution', 'label']
raw_dataset = DatasetDict({
    "train": Dataset.from_pandas(train_df[cols_to_keep]),
    "test": Dataset.from_pandas(test_df[cols_to_keep])
})

print("--- Raw Dataset Structure ---")
print(raw_dataset)
```

    --- Raw Dataset Structure ---
    DatasetDict({
        train: Dataset({
            features: ['index', 'question', 'solution', 'label', '__index_level_0__'],
            num_rows: 4853
        })
        test: Dataset({
            features: ['index', 'question', 'solution', 'label', '__index_level_0__'],
            num_rows: 1214
        })
    })



```python
# Cell 4: Load and Configure Tokenizer
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    Config.MODEL_ID,
    trust_remote_code=True
)

tokenizer.padding_side = "left"
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

print("Tokenizer loaded and configured successfully.")
```


    tokenizer_config.json: 0.00B [00:00, ?B/s]



    vocab.json: 0.00B [00:00, ?B/s]



    merges.txt: 0.00B [00:00, ?B/s]



    tokenizer.json:   0%|          | 0.00/15.5M [00:00<?, ?B/s]



    added_tokens.json:   0%|          | 0.00/249 [00:00<?, ?B/s]



    special_tokens_map.json:   0%|          | 0.00/587 [00:00<?, ?B/s]


    Tokenizer loaded and configured successfully.



```python
SYSTEM_PROMPT = \
"""You are a mathematics tutor.
You will be given a math word problem and a solution written by a student.
Carefully analyze the problem and solution LINE-BY-LINE and determine whether there are any errors in the solution."""
```


```python
# Cell 5: Define and Apply Preprocessing
def preprocess_function(examples):
    """Formats the input text and tokenizes it for sequence classification."""
    input_texts = [
        f"{SYSTEM_PROMPT}\n\n### Problem:\n{q}\n\n### Solution:\n{s}"
        for q, s in zip(examples["question"], examples["solution"])
    ]
    return tokenizer(
        input_texts,
        truncation=True,
        max_length=512,
        padding=False
    )

tokenized_dataset = raw_dataset.map(
    preprocess_function,
    batched=True,
    remove_columns=["question", "solution"] # Keep 'index' and 'label'
)

final_dataset = tokenized_dataset

print("\n--- Final Tokenized Dataset ---")
print(final_dataset)
```


    Map:   0%|          | 0/4853 [00:00<?, ? examples/s]



    Map:   0%|          | 0/1214 [00:00<?, ? examples/s]


    
    --- Final Tokenized Dataset ---
    DatasetDict({
        train: Dataset({
            features: ['index', 'label', '__index_level_0__', 'input_ids', 'attention_mask'],
            num_rows: 4853
        })
        test: Dataset({
            features: ['index', 'label', '__index_level_0__', 'input_ids', 'attention_mask'],
            num_rows: 1214
        })
    })



```python
# Cell 6: Display a Complete Formatted Prompt for Inspection
first_example_raw = raw_dataset["train"][0]

# Reconstruct the full prompt string
full_prompt = f"{SYSTEM_PROMPT}\n\n### Problem:\n{first_example_raw['question']}\n\n### Answer:\n{first_example_raw['solution']}"

print("--- Example of a Single Formatted Prompt ---")
print(full_prompt)
```

    --- Example of a Single Formatted Prompt ---
    You are a mathematics tutor. 
    You will be given a math word problem and a solution written by a student. 
    Carefully analyze the problem and solution LINE-BY-LINE and determine whether there are any errors in the solution.
    
    ### Problem:
    Stephen has 110 ants in his ant farm.  Half of the ants are worker ants, 20 percent of the worker ants are male.  How many female worker ants are there?
    
    ### Answer:
    Worker ants:110*2=220 ants
    Male worker ants:220(0.2)=44
    Female worker ants:220-44=176 ants
    FINAL ANSWER: 176



```python
# Cell 7: Define the Custom Classifier Class
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
        outputs = self.base(
            input_ids=input_ids,
            attention_mask=attention_mask,
            output_hidden_states=True,
            **kwargs,
        )
        last_hidden_state = outputs.hidden_states[-1]
        pooled_output = last_hidden_state[:, -1, :]
        logits = self.classifier(pooled_output)

        loss = None
        if labels is not None:
            loss = nn.functional.cross_entropy(logits.view(-1, self.num_labels), labels.view(-1))

        return {"loss": loss, "logits": logits} if loss is not None else {"logits": logits}
```


```python
# ==============================================================================
# Cell 8: Define Enhanced Training Arguments
# ==============================================================================
from transformers import TrainingArguments

# Define the arguments, now including frequent evaluation and early stopping logic.
training_args = TrainingArguments(
    # Base directory for outputs.
    output_dir="/content/training_output",

    # --- Batching & Epochs ---
    num_train_epochs=5,
    per_device_train_batch_size=8,
    gradient_accumulation_steps=4,

    # --- Optimizer & Learning Rate Schedule ---
    optim="paged_adamw_8bit",
    learning_rate=1e-4,
    lr_scheduler_type="cosine",
    warmup_ratio=0.1,

    # --- Precision & Memory ---
    bf16=True,
    gradient_checkpointing=False,

    # --- Logging, Evaluation & Checkpointing (ENHANCED) ---
    logging_strategy="steps",
    logging_steps=25,
    eval_strategy="steps",        # ADDED: Evaluate every 25 steps
    eval_steps=25,                # ADDED: Evaluation frequency
    save_strategy="steps",        # CHANGED: Save checkpoints at the same frequency as evaluation
    save_steps=25,                # ADDED: Save frequency
    save_total_limit=1,
    report_to="none",
    save_safetensors=False,

    # --- Early Stopping Configuration (ENHANCED) ---
    load_best_model_at_end=True,         # ADDED: Load the best model found during training at the end
    metric_for_best_model="accuracy",    # ADDED: Use 'accuracy' to determine the best model
    greater_is_better=True,              # ADDED: Higher accuracy is better
)

print("Enhanced TrainingArguments configured with early stopping.")
```

    Enhanced TrainingArguments configured with early stopping.



```python
# Cell 9: Define the Evaluation Metric
import numpy as np
from transformers.trainer_utils import EvalPrediction

def compute_metrics(p: EvalPrediction):
    """
    Computes accuracy for a sequence classification task.
    """
    logits = p.predictions[0] if isinstance(p.predictions, (tuple, list)) else p.predictions
    preds = np.argmax(logits, axis=1)
    labels = p.label_ids
    accuracy = (preds == labels).mean().item()
    return {"accuracy": accuracy}
```


```python
# Cell 10: Define and Initialize the LoRA-Enabled Model
import torch
from transformers import AutoModelForCausalLM, BitsAndBytesConfig
from peft import LoraConfig, get_peft_model, TaskType

DTYPE = torch.bfloat16
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=DTYPE,
)

backbone_lora = AutoModelForCausalLM.from_pretrained(
    Config.MODEL_ID,
    quantization_config=quantization_config,
    device_map="auto",
    trust_remote_code=True,
    attn_implementation="flash_attention_2",
)
backbone_lora.config.pad_token_id = tokenizer.pad_token_id

lora_config = LoraConfig(
    task_type=TaskType.SEQ_CLS,
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    target_modules="all-linear",
)

lora_backbone = get_peft_model(backbone_lora, lora_config)
model_lora = GPTSequenceClassifier(lora_backbone, Config.NUM_LABELS)

print("--- Trainable Status for LoRA Fine-Tuning Model ---")
model_lora.base.print_trainable_parameters()
```


    config.json: 0.00B [00:00, ?B/s]



    configuration_phi3.py: 0.00B [00:00, ?B/s]


    A new version of the following files was downloaded from https://huggingface.co/microsoft/Phi-4-mini-instruct:
    - configuration_phi3.py
    . Make sure to double-check they do not contain any added malicious code. To avoid downloading new versions of the code file, you can pin a revision.



    modeling_phi3.py: 0.00B [00:00, ?B/s]


    A new version of the following files was downloaded from https://huggingface.co/microsoft/Phi-4-mini-instruct:
    - modeling_phi3.py
    . Make sure to double-check they do not contain any added malicious code. To avoid downloading new versions of the code file, you can pin a revision.



    model.safetensors.index.json: 0.00B [00:00, ?B/s]



    Fetching 2 files:   0%|          | 0/2 [00:00<?, ?it/s]



    model-00002-of-00002.safetensors:   0%|          | 0.00/2.77G [00:00<?, ?B/s]



    model-00001-of-00002.safetensors:   0%|          | 0.00/4.90G [00:00<?, ?B/s]



    Loading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]



    generation_config.json:   0%|          | 0.00/168 [00:00<?, ?B/s]


    --- Trainable Status for LoRA Fine-Tuning Model ---
    trainable params: 23,068,672 || all params: 3,859,090,432 || trainable%: 0.5978



```python
# ==============================================================================
# Cell 11: Initialize the LoRA Trainer with Early Stopping
# ==============================================================================
import copy
from transformers import Trainer, DataCollatorWithPadding, EarlyStoppingCallback

data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

# Create a copy of the training args to set a specific output directory
lora_training_args = copy.deepcopy(training_args)
lora_training_args.output_dir = "/content/training_output/lora_finetune"

# Initialize the early stopping callback
early_stopping_callback = EarlyStoppingCallback(
    early_stopping_patience=10,  # Stop if the 'accuracy' metric does not improve for 10 evaluations
    early_stopping_threshold=0.0   # Any improvement is considered significant
)

# Instantiate a new Trainer for the fine-tuning experiment.
trainer_lora = Trainer(
    model=model_lora,
    args=lora_training_args,
    train_dataset=final_dataset["train"],
    eval_dataset=final_dataset["test"],
    processing_class=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
    callbacks=[early_stopping_callback]  # ADDED: Include the callback here
)

print("Trainer for full LoRA fine-tuning initialized with Early Stopping.")
```

    Trainer for full LoRA fine-tuning initialized with Early Stopping.



```python
# Cell 12: Fine-Tune the LoRA Model
print("--- Starting full LoRA fine-tuning ---")
trainer_lora.train()
print("\n--- Full LoRA fine-tuning complete ---")
```

    --- Starting full LoRA fine-tuning ---


    The input hidden states seems to be silently casted in float32, this might be related to the fact you have upcasted embedding or layer norm layers in float32. We will cast back the input in torch.bfloat16.




    <div>

      <progress value='760' max='760' style='width:300px; height:20px; vertical-align: middle;'></progress>
      [760/760 1:05:18, Epoch 5/5]
    </div>
    <table border="1" class="dataframe">
  <thead>
 <tr style="text-align: left;">
      <th>Step</th>
      <th>Training Loss</th>
      <th>Validation Loss</th>
      <th>Accuracy</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>25</td>
      <td>2.592300</td>
      <td>0.656590</td>
      <td>0.670511</td>
    </tr>
    <tr>
      <td>50</td>
      <td>2.544900</td>
      <td>0.615223</td>
      <td>0.668863</td>
    </tr>
    <tr>
      <td>75</td>
      <td>2.501000</td>
      <td>0.630228</td>
      <td>0.584020</td>
    </tr>
    <tr>
      <td>100</td>
      <td>2.378100</td>
      <td>0.547597</td>
      <td>0.687809</td>
    </tr>
    <tr>
      <td>125</td>
      <td>1.990700</td>
      <td>0.427423</td>
      <td>0.817957</td>
    </tr>
    <tr>
      <td>150</td>
      <td>1.469200</td>
      <td>0.359185</td>
      <td>0.850082</td>
    </tr>
    <tr>
      <td>175</td>
      <td>0.995200</td>
      <td>0.393971</td>
      <td>0.870675</td>
    </tr>
    <tr>
      <td>200</td>
      <td>0.876000</td>
      <td>0.253154</td>
      <td>0.903624</td>
    </tr>
    <tr>
      <td>225</td>
      <td>0.909000</td>
      <td>0.307702</td>
      <td>0.870675</td>
    </tr>
    <tr>
      <td>250</td>
      <td>0.756500</td>
      <td>0.264172</td>
      <td>0.898682</td>
    </tr>
    <tr>
      <td>275</td>
      <td>0.876700</td>
      <td>0.242020</td>
      <td>0.910214</td>
    </tr>
    <tr>
      <td>300</td>
      <td>0.803000</td>
      <td>0.237435</td>
      <td>0.904448</td>
    </tr>
    <tr>
      <td>325</td>
      <td>0.307100</td>
      <td>0.325684</td>
      <td>0.913509</td>
    </tr>
    <tr>
      <td>350</td>
      <td>0.474200</td>
      <td>0.356185</td>
      <td>0.914333</td>
    </tr>
    <tr>
      <td>375</td>
      <td>0.369100</td>
      <td>0.432317</td>
      <td>0.920099</td>
    </tr>
    <tr>
      <td>400</td>
      <td>0.474100</td>
      <td>0.331634</td>
      <td>0.915157</td>
    </tr>
    <tr>
      <td>425</td>
      <td>0.372000</td>
      <td>0.287010</td>
      <td>0.920099</td>
    </tr>
    <tr>
      <td>450</td>
      <td>0.407000</td>
      <td>0.274792</td>
      <td>0.917628</td>
    </tr>
    <tr>
      <td>475</td>
      <td>0.109400</td>
      <td>0.351322</td>
      <td>0.922570</td>
    </tr>
    <tr>
      <td>500</td>
      <td>0.102400</td>
      <td>0.406346</td>
      <td>0.920923</td>
    </tr>
    <tr>
      <td>525</td>
      <td>0.232100</td>
      <td>0.411448</td>
      <td>0.921746</td>
    </tr>
    <tr>
      <td>550</td>
      <td>0.115700</td>
      <td>0.487955</td>
      <td>0.920099</td>
    </tr>
    <tr>
      <td>575</td>
      <td>0.127100</td>
      <td>0.461272</td>
      <td>0.920099</td>
    </tr>
    <tr>
      <td>600</td>
      <td>0.124600</td>
      <td>0.484073</td>
      <td>0.920099</td>
    </tr>
    <tr>
      <td>625</td>
      <td>0.038200</td>
      <td>0.474683</td>
      <td>0.923394</td>
    </tr>
    <tr>
      <td>650</td>
      <td>0.000500</td>
      <td>0.464535</td>
      <td>0.920923</td>
    </tr>
    <tr>
      <td>675</td>
      <td>0.016600</td>
      <td>0.465737</td>
      <td>0.923394</td>
    </tr>
    <tr>
      <td>700</td>
      <td>0.048600</td>
      <td>0.461123</td>
      <td>0.921746</td>
    </tr>
    <tr>
      <td>725</td>
      <td>0.114100</td>
      <td>0.465109</td>
      <td>0.921746</td>
    </tr>
    <tr>
      <td>750</td>
      <td>0.050000</td>
      <td>0.462874</td>
      <td>0.921746</td>
    </tr>
  </tbody>
</table><p>

```python
# ==============================================================================
# Cell 13: Final Evaluation and Detailed Results Generation (Updated)
# ==============================================================================
import torch
import numpy as np
import pandas as pd

print("--- Generating predictions for the test set to create a detailed results DataFrame ---")

# 1. Run inference on the test set
pred_outputs = trainer_lora.predict(final_dataset["test"])

# 2. Extract logits and true labels
logits = pred_outputs.predictions[0] if isinstance(pred_outputs.predictions, (tuple, list)) else pred_outputs.predictions
true_labels = pred_outputs.label_ids

# 3. Calculate probabilities, predicted labels, and confidence scores
probs = torch.softmax(torch.tensor(logits), dim=-1).numpy()
predicted_labels = np.argmax(probs, axis=1)
predicted_probas = np.max(probs, axis=1)

# 4. Determine if each prediction was correct
is_correct = (predicted_labels == true_labels)

# 5. Assemble the final DataFrame with the 'index' column included
results_df = pd.DataFrame({
    'index': final_dataset["test"]["index"],  # UPDATED: Source index directly from the dataset
    'true_label': true_labels,
    'predicted_label': predicted_labels,
    'predicted_proba': predicted_probas,
    'is_correct': is_correct
})

# 6. Save the detailed results to a CSV file
output_csv_path = "/content/final_evaluation_results.csv"
results_df.to_csv(output_csv_path, index=False)

# 7. Print a summary for quick inspection
print(f"\n✅ Final evaluation results saved to {output_csv_path}")
print("--- Final Evaluation DataFrame Head ---")
print(results_df.head())

final_accuracy = results_df['is_correct'].mean()
print(f"\nFinal Test Accuracy: {final_accuracy:.4f}")
```

    --- Generating predictions for the test set to create a detailed results DataFrame ---






    
    ✅ Final evaluation results saved to /content/final_evaluation_results.csv
    --- Final Evaluation DataFrame Head ---
       index  true_label  predicted_label  predicted_proba  is_correct
    0   5091           1                1         0.999987        True
    1   1925           1                1         0.999960        True
    2   1193           1                1         0.999910        True
    3   6695           1                1         1.000000        True
    4   4633           1                1         0.999994        True
    
    Final Test Accuracy: 0.9234



```python
# Cell 14: Push Fine-Tuned Model and Classifier Head to Hugging Face Hub
import torch
from huggingface_hub import HfApi, HfFolder, create_repo

# --- Configuration ---
# IMPORTANT: Replace with your Hugging Face username and desired repo name
hf_username = "arvindsuresh-math"
hf_repo_name = "phi-4-error-binary-classifier"
local_save_path = f"/content/{hf_repo_name}"

# --- Save all necessary components locally ---
print(f"Saving components to local directory: {local_save_path}")

# 1. Save the LoRa adapter weights for the backbone model
model_lora.base.save_pretrained(local_save_path)

# 2. Save the state dictionary of the custom classifier head
classifier_head_path = f"{local_save_path}/classifier_head.pth"
torch.save(model_lora.classifier.state_dict(), classifier_head_path)

# 3. Save the tokenizer to bundle it with the model
tokenizer.save_pretrained(local_save_path)

print("All components saved locally.")

# --- Push all files to the Hugging Face Hub ---
print(f"Uploading files to HF Hub repository: {hf_username}/{hf_repo_name}")
api = HfApi()

# Create the repository on the Hub (if it doesn't already exist)
create_repo(
    repo_id=f"{hf_username}/{hf_repo_name}",
    exist_ok=True,
    token=HfFolder.get_token(),
)

# Upload the entire folder's contents
api.upload_folder(
    folder_path=local_save_path,
    repo_id=f"{hf_username}/{hf_repo_name}",
    commit_message="Upload fine-tuned LoRa adapters and classifier head",
    token=HfFolder.get_token(),
)

print(f"\n✅ Successfully pushed all components to: https://huggingface.co/{hf_username}/{hf_repo_name}")
```

    Saving components to local directory: /content/phi-4-error-binary-classifier
    All components saved locally.
    Uploading files to HF Hub repository: arvindsuresh-math/phi-4-error-binary-classifier



    Processing Files (0 / 0)                : |          |  0.00B /  0.00B            



    New Data Upload                         : |          |  0.00B /  0.00B            



      ...or-binary-classifier/tokenizer.json: 100%|##########| 15.5MB / 15.5MB            



      ...lassifier/adapter_model.safetensors:   1%|          |  557kB / 92.3MB            



      ...nary-classifier/classifier_head.pth:   2%|2         |   577B / 26.1kB            


    
    ✅ Successfully pushed all components to: https://huggingface.co/arvindsuresh-math/phi-4-error-binary-classifier



```python
backbone_lora.get_memory_footprint()
```




    2932480192




```python

```
