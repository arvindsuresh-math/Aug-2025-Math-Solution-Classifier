```python
# --- 1.2: Install Required Libraries ---

!pip install -U transformers==4.49.0
!pip install -Uq peft
!pip install -Uq trl
!pip install -Uq accelerate
!pip install -Uq datasets
!pip install -Uq bitsandbytes

!pip install flash-attn==2.7.4.post1 \
  --extra-index-url https://download.pytorch.org/whl/cu124 \
  --no-build-isolation
```

```python
class Config:
    # Model ID from Hugging Face Hub
    MODEL_ID = "microsoft/Phi-4-mini-instruct"

    # Local path to the unzipped dataset
    DATASET_PATH = '/content/N4_concep.csv'

    # Number of labels for the classification task
    NUM_LABELS = 2
```


```python
# --- 2.2: Load Dataset from Disk ---
from datasets import Dataset, DatasetDict
import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv(Config.DATASET_PATH, index_col=0)

data['label'] = data['error_type'].apply(lambda x: 1 if x == 'conceptual_error' else 0)
data.drop(columns=['error_type'], inplace=True)

data_train, data_test = train_test_split(data, test_size=0.25,shuffle=False)

# Load the dataset using the path defined in our Config
raw_dataset_train = Dataset.from_pandas(data_train)
raw_dataset_test = Dataset.from_pandas(data_test)

# Combine the training and test datasets
raw_dataset = DatasetDict({
    'train': raw_dataset_train,
    'test': raw_dataset_test
})

# Display the structure of the loaded dataset
print("--- Raw Dataset Structure ---")
print(raw_dataset)
```

    --- Raw Dataset Structure ---
    DatasetDict({
        train: Dataset({
            features: ['wrong_answer', 'label', 'question'],
            num_rows: 4232
        })
        test: Dataset({
            features: ['wrong_answer', 'label', 'question'],
            num_rows: 1411
        })
    })


```python
raw_dataset['train'][1]
```




    {'wrong_answer': 'Weng earns 12/60 = $0.2 per minute.\nWorking 50 minutes, she earned 0.2 x 50 = $10.\n#### 10',
     'label': 0,
     'question': 'Weng earns $12 an hour for babysitting. Yesterday, she just did 50 minutes of babysitting. How much did she earn?'}




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

    Tokenizer loaded and configured successfully.



```python
# --- 3.2: Define and Apply Preprocessing ---

def preprocess_function(examples):
    """
    Formats the input text using a prompt template and tokenizes it.
    The 'label' and 'index' columns are passed through untouched.
    """
    # Define the instruction prompt for the model
    system_prompt = "Analyze the following mathematical problems and answers to determine if the solution is correct or incorrect."

    # Create a single formatted input string for each example
    input_texts = [
        f"{system_prompt}\n\n### Problem:\n{q}\n\n### Answer:\n{t}"
        for q, t in zip(examples["question"], examples["wrong_answer"])
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
    remove_columns=["question", "wrong_answer"]
)

# --- Verification of a Single Example ---

# 1. Reconstruct the full prompt for the first training example
first_example_raw = raw_dataset["train"][0]
system_prompt = "Analyze the following mathematical problems and answers to determine if the solution is correct or incorrect."
full_prompt = f"{system_prompt}\n\n### Problem:\n{first_example_raw['question']}\n\n### {first_example_raw['wrong_answer']}"

# 2. Get the tokenized output for the same example
first_example_tokenized = tokenized_dataset["train"][0]["input_ids"]

# 3. Print everything for inspection
print("--- Example of a Single Processed Input ---")
print("\n[Full Prompt String]\n")
print(full_prompt)
print("\n\n[Corresponding Token IDs]\n")
print(first_example_tokenized)
```


    Map:   0%|          | 0/4232 [00:00<?, ? examples/s]



    Map:   0%|          | 0/1411 [00:00<?, ? examples/s]


    --- Example of a Single Processed Input ---
    
    [Full Prompt String]
    
    Analyze the following mathematical problems and answers to determine if the solution is correct or incorrect.
    
    ### Problem:
    Weng earns $12 an hour for babysitting. Yesterday, she just did 50 minutes of babysitting. How much did she earn?
    
    ### Weng earns 12/60 = $0.2 per minute.
    Working 50 minutes, she earned 50 x 50 = $2500.
    #### 2500
    
    
    [Corresponding Token IDs]
    
    [107202, 290, 3992, 58944, 6840, 326, 14716, 316, 11433, 538, 290, 7578, 382, 6145, 503, 25570, 364, 31639, 26113, 734, 54, 882, 112231, 548, 899, 448, 8825, 395, 95717, 6603, 13, 85247, 11, 1770, 1327, 2242, 220, 1434, 5438, 328, 95717, 6603, 13, 3253, 2009, 2242, 1770, 8748, 1715, 31639, 30985, 734, 54, 882, 112231, 220, 899, 14, 1910, 314, 548, 15, 13, 17, 777, 12434, 558, 39580, 220, 1434, 5438, 11, 1770, 22639, 220, 1434, 1215, 220, 1434, 314, 548, 6911, 15, 558, 1509, 220, 6911, 15]



```python
# --- 3.3: Combine Training and Validation Splits ---
from datasets import concatenate_datasets, DatasetDict

final_dataset = DatasetDict({
    "train": tokenized_dataset['train'],
    "test": tokenized_dataset["test"]
})

# Display the structure of the final dataset to be used for training
print("--- Final Dataset for Training and Evaluation ---")
print(final_dataset)
```

    --- Final Dataset for Training and Evaluation ---
    DatasetDict({
        train: Dataset({
            features: ['label', 'input_ids', 'attention_mask'],
            num_rows: 4232
        })
        test: Dataset({
            features: ['label', 'input_ids', 'attention_mask'],
            num_rows: 1411
        })
    })



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

print("SequenceClassifier class defined successfully.")
```

    SequenceClassifier class defined successfully.



```python
# --- 5.1: Define Common Training Arguments ---
from transformers import TrainingArguments

# Define the arguments that will be shared across both training runs.
training_args = TrainingArguments(
    # Base directory for outputs. Specific trainers will use subdirectories.
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

    Common TrainingArguments configured.



```python
# --- 5.2: Define the Evaluation Metric ---
import numpy as np
from transformers.trainer_utils import EvalPrediction

def compute_metrics(p: EvalPrediction):
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

    Metric computation function defined.



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

# #  # Verify that all weights are frozen
# print("Trainable parameters for linear probe model:")
# backbone_probe.base.print_trainable_parameters() # Should show 0 trainable params

# Ensure the model's pad token ID is set correctly
backbone_probe.config.pad_token_id = tokenizer.pad_token_id

print("Backbone for linear probing loaded and all parameters frozen.")
```


    model.safetensors.index.json: 0.00B [00:00, ?B/s]



    Downloading shards:   0%|          | 0/2 [00:00<?, ?it/s]



    model-00001-of-00002.safetensors:   0%|          | 0.00/4.90G [00:00<?, ?B/s]



    model-00002-of-00002.safetensors:   0%|          | 0.00/2.77G [00:00<?, ?B/s]



    Loading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]



    generation_config.json:   0%|          | 0.00/168 [00:00<?, ?B/s]


    Backbone for linear probing loaded and all parameters frozen.



```python
# --- 6.2: Initialize the Linear Probe Trainer ---
from transformers import Trainer, DataCollatorWithPadding
import copy

# Instantiate the model: frozen backbone + trainable head.
model_probe = GPTSequenceClassifier(backbone_probe, Config.NUM_LABELS)

# Verify which parts of the model are trainable.
# We expect to see that only the 'classifier' parameters require gradients.
total_params = 0
trainable_params = 0
print("--- Trainable Status for Linear Probe Model ---")
for name, param in model_probe.named_parameters():
    total_params += param.numel()
    if param.requires_grad:
        trainable_params += param.numel()
        print(f"  [Trainable]: {name}")
print(f"-------------------------------------------------")
print(f"Trainable params: {trainable_params} || All params: {total_params} || Trainable %: {100 * trainable_params / total_params:.4f}")

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

    --- Trainable Status for Linear Probe Model ---
      [Trainable]: classifier.weight
      [Trainable]: classifier.bias
    -------------------------------------------------
    Trainable params: 6146 || All params: 2225415170 || Trainable %: 0.0003
    
    Trainer for linear probing initialized successfully.


    /tmp/ipython-input-191356708.py:29: FutureWarning: `tokenizer` is deprecated and will be removed in version 5.0.0 for `Trainer.__init__`. Use `processing_class` instead.
      trainer_probe = Trainer(



```python
# --- 7.1: Define the LoRA-Enabled Model ---
import torch
from transformers import AutoModelForCausalLM, BitsAndBytesConfig
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

# Verify which parts of the model are trainable.
# We expect to see LoRA adapter weights ('lora_A', 'lora_B') and 'classifier' weights.
total_params = 0
trainable_params = 0
print("--- Trainable Status for LoRA Fine-Tuning Model ---")
for name, param in model_lora.named_parameters():
    total_params += param.numel()
    if param.requires_grad:
        trainable_params += param.numel()
        print(f"  [Trainable]: {name}")
print(f"-------------------------------------------------")
print(f"Trainable params: {trainable_params} || All params: {total_params} || Trainable %: {100 * trainable_params / total_params:.4f}")
```

    Trainable params: 23074818 || All params: 2248483842 || Trainable %: 1.0262



```python
# --- 7.2: Initialize the LoRA Trainer ---
import copy
from transformers import Trainer

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

    Trainer for full LoRA fine-tuning initialized successfully.


    /tmp/ipython-input-1624353024.py:10: FutureWarning: `tokenizer` is deprecated and will be removed in version 5.0.0 for `Trainer.__init__`. Use `processing_class` instead.
      trainer_lora = Trainer(



```python
# --- 7.3: Fine-Tune the LoRA Model ---

print("--- Starting full LoRA fine-tuning ---")
trainer_lora.train()
print("\n--- Full LoRA fine-tuning complete ---")
```

    --- Starting full LoRA fine-tuning ---


    The input hidden states seems to be silently casted in float32, this might be related to the fact you have upcasted embedding or layer norm layers in float32. We will cast back the input in torch.bfloat16.




    <div>

      <progress value='660' max='660' style='width:300px; height:20px; vertical-align: middle;'></progress>
      [660/660 21:52, Epoch 4/5]
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
      <td>25</td>
      <td>2.717500</td>
    </tr>
    <tr>
      <td>50</td>
      <td>2.446700</td>
    </tr>
    <tr>
      <td>75</td>
      <td>2.142000</td>
    </tr>
    <tr>
      <td>100</td>
      <td>1.941900</td>
    </tr>
    <tr>
      <td>125</td>
      <td>1.654800</td>
    </tr>
    <tr>
      <td>150</td>
      <td>1.781500</td>
    </tr>
    <tr>
      <td>175</td>
      <td>1.178600</td>
    </tr>
    <tr>
      <td>200</td>
      <td>1.156200</td>
    </tr>
    <tr>
      <td>225</td>
      <td>1.215100</td>
    </tr>
    <tr>
      <td>250</td>
      <td>0.999000</td>
    </tr>
    <tr>
      <td>275</td>
      <td>0.874900</td>
    </tr>
    <tr>
      <td>300</td>
      <td>0.512000</td>
    </tr>
    <tr>
      <td>325</td>
      <td>0.753400</td>
    </tr>
    <tr>
      <td>350</td>
      <td>0.596700</td>
    </tr>
    <tr>
      <td>375</td>
      <td>0.561000</td>
    </tr>
    <tr>
      <td>400</td>
      <td>0.563600</td>
    </tr>
    <tr>
      <td>425</td>
      <td>0.299200</td>
    </tr>
    <tr>
      <td>450</td>
      <td>0.285900</td>
    </tr>
    <tr>
      <td>475</td>
      <td>0.462200</td>
    </tr>
    <tr>
      <td>500</td>
      <td>0.186400</td>
    </tr>
    <tr>
      <td>525</td>
      <td>0.271400</td>
    </tr>
    <tr>
      <td>550</td>
      <td>0.039600</td>
    </tr>
    <tr>
      <td>575</td>
      <td>0.132400</td>
    </tr>
    <tr>
      <td>600</td>
      <td>0.116800</td>
    </tr>
    <tr>
      <td>625</td>
      <td>0.115300</td>
    </tr>
    <tr>
      <td>650</td>
      <td>0.114500</td>
    </tr>
  </tbody>
</table><p>


    
    --- Full LoRA fine-tuning complete ---



```python
import gc
gc.collect()
torch.cuda.empty_cache()
torch.cuda.ipc_collect()
```


```python
trainer_lora.evaluate()
```



<div>

  <progress value='177' max='177' style='width:300px; height:20px; vertical-align: middle;'></progress>
  [177/177 00:40]
</div>






    {'eval_loss': 0.32724976539611816,
     'eval_accuracy': 0.9312544294826365,
     'eval_runtime': 40.5731,
     'eval_samples_per_second': 34.777,
     'eval_steps_per_second': 4.363,
     'epoch': 4.967863894139887}




```python

```
