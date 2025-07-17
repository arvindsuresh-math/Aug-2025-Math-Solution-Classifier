```python
# Cell 1: Setup and Installations

# 1.1 Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')
print("Google Drive mounted successfully.")

# 1.2 Install required libraries
# Note: TRL is included for consistency with your original script, but is not
# strictly required for this sequence classification task.
!pip install -Uq transformers
!pip install -Uq peft
!pip install -Uq trl
!pip install -Uq accelerate
!pip install -Uq datasets
!pip install -Uq bitsandbytes

# Install Flash Attention 2
!pip install flash-attn==2.7.4.post1 \
  --extra-index-url https://download.pytorch.org/whl/cu124 \
  --no-build-isolation

# 1.3 Unzip the dataset
# Assumes the dataset ZIP file is located in your Google Drive's root directory.
# Adjust the path if it is stored elsewhere.
!unzip -q -o /content/drive/My\ Drive/level-1-binary.zip -d /content/
print("Dataset unzipped to '/content/level-1-binary'.")
```

    Mounted at /content/drive
    Google Drive mounted successfully.
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m363.4/363.4 MB[0m [31m4.3 MB/s[0m eta [36m0:00:00[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m13.8/13.8 MB[0m [31m109.5 MB/s[0m eta [36m0:00:00[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m24.6/24.6 MB[0m [31m98.8 MB/s[0m eta [36m0:00:00[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m883.7/883.7 kB[0m [31m58.8 MB/s[0m eta [36m0:00:00[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m664.8/664.8 MB[0m [31m1.3 MB/s[0m eta [36m0:00:00[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m211.5/211.5 MB[0m [31m9.8 MB/s[0m eta [36m0:00:00[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m56.3/56.3 MB[0m [31m37.2 MB/s[0m eta [36m0:00:00[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m127.9/127.9 MB[0m [31m16.6 MB/s[0m eta [36m0:00:00[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m207.5/207.5 MB[0m [31m2.9 MB/s[0m eta [36m0:00:00[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m21.1/21.1 MB[0m [31m30.3 MB/s[0m eta [36m0:00:00[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m376.2/376.2 kB[0m [31m9.2 MB/s[0m eta [36m0:00:00[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m494.8/494.8 kB[0m [31m28.3 MB/s[0m eta [36m0:00:00[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m193.6/193.6 kB[0m [31m22.7 MB/s[0m eta [36m0:00:00[0m
    [?25h[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
    gcsfs 2025.3.2 requires fsspec==2025.3.2, but you have fsspec 2025.3.0 which is incompatible.[0m[31m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m367.1/367.1 kB[0m [31m7.8 MB/s[0m eta [36m0:00:00[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m72.9/72.9 MB[0m [31m29.8 MB/s[0m eta [36m0:00:00[0m
    [?25hLooking in indexes: https://pypi.org/simple, https://download.pytorch.org/whl/cu124
    Collecting flash-attn==2.7.4.post1
      Downloading flash_attn-2.7.4.post1.tar.gz (6.0 MB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m6.0/6.0 MB[0m [31m56.4 MB/s[0m eta [36m0:00:00[0m
    [?25h  Preparing metadata (setup.py) ... [?25l[?25hdone
    Requirement already satisfied: torch in /usr/local/lib/python3.11/dist-packages (from flash-attn==2.7.4.post1) (2.6.0+cu124)
    Requirement already satisfied: einops in /usr/local/lib/python3.11/dist-packages (from flash-attn==2.7.4.post1) (0.8.1)
    Requirement already satisfied: filelock in /usr/local/lib/python3.11/dist-packages (from torch->flash-attn==2.7.4.post1) (3.18.0)
    Requirement already satisfied: typing-extensions>=4.10.0 in /usr/local/lib/python3.11/dist-packages (from torch->flash-attn==2.7.4.post1) (4.14.1)
    Requirement already satisfied: networkx in /usr/local/lib/python3.11/dist-packages (from torch->flash-attn==2.7.4.post1) (3.5)
    Requirement already satisfied: jinja2 in /usr/local/lib/python3.11/dist-packages (from torch->flash-attn==2.7.4.post1) (3.1.6)
    Requirement already satisfied: fsspec in /usr/local/lib/python3.11/dist-packages (from torch->flash-attn==2.7.4.post1) (2025.3.0)
    Requirement already satisfied: nvidia-cuda-nvrtc-cu12==12.4.127 in /usr/local/lib/python3.11/dist-packages (from torch->flash-attn==2.7.4.post1) (12.4.127)
    Requirement already satisfied: nvidia-cuda-runtime-cu12==12.4.127 in /usr/local/lib/python3.11/dist-packages (from torch->flash-attn==2.7.4.post1) (12.4.127)
    Requirement already satisfied: nvidia-cuda-cupti-cu12==12.4.127 in /usr/local/lib/python3.11/dist-packages (from torch->flash-attn==2.7.4.post1) (12.4.127)
    Requirement already satisfied: nvidia-cudnn-cu12==9.1.0.70 in /usr/local/lib/python3.11/dist-packages (from torch->flash-attn==2.7.4.post1) (9.1.0.70)
    Requirement already satisfied: nvidia-cublas-cu12==12.4.5.8 in /usr/local/lib/python3.11/dist-packages (from torch->flash-attn==2.7.4.post1) (12.4.5.8)
    Requirement already satisfied: nvidia-cufft-cu12==11.2.1.3 in /usr/local/lib/python3.11/dist-packages (from torch->flash-attn==2.7.4.post1) (11.2.1.3)
    Requirement already satisfied: nvidia-curand-cu12==10.3.5.147 in /usr/local/lib/python3.11/dist-packages (from torch->flash-attn==2.7.4.post1) (10.3.5.147)
    Requirement already satisfied: nvidia-cusolver-cu12==11.6.1.9 in /usr/local/lib/python3.11/dist-packages (from torch->flash-attn==2.7.4.post1) (11.6.1.9)
    Requirement already satisfied: nvidia-cusparse-cu12==12.3.1.170 in /usr/local/lib/python3.11/dist-packages (from torch->flash-attn==2.7.4.post1) (12.3.1.170)
    Requirement already satisfied: nvidia-cusparselt-cu12==0.6.2 in /usr/local/lib/python3.11/dist-packages (from torch->flash-attn==2.7.4.post1) (0.6.2)
    Requirement already satisfied: nvidia-nccl-cu12==2.21.5 in /usr/local/lib/python3.11/dist-packages (from torch->flash-attn==2.7.4.post1) (2.21.5)
    Requirement already satisfied: nvidia-nvtx-cu12==12.4.127 in /usr/local/lib/python3.11/dist-packages (from torch->flash-attn==2.7.4.post1) (12.4.127)
    Requirement already satisfied: nvidia-nvjitlink-cu12==12.4.127 in /usr/local/lib/python3.11/dist-packages (from torch->flash-attn==2.7.4.post1) (12.4.127)
    Requirement already satisfied: triton==3.2.0 in /usr/local/lib/python3.11/dist-packages (from torch->flash-attn==2.7.4.post1) (3.2.0)
    Requirement already satisfied: sympy==1.13.1 in /usr/local/lib/python3.11/dist-packages (from torch->flash-attn==2.7.4.post1) (1.13.1)
    Requirement already satisfied: mpmath<1.4,>=1.1.0 in /usr/local/lib/python3.11/dist-packages (from sympy==1.13.1->torch->flash-attn==2.7.4.post1) (1.3.0)
    Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.11/dist-packages (from jinja2->torch->flash-attn==2.7.4.post1) (3.0.2)
    Building wheels for collected packages: flash-attn
      Building wheel for flash-attn (setup.py) ... [?25l[?25hdone
      Created wheel for flash-attn: filename=flash_attn-2.7.4.post1-cp311-cp311-linux_x86_64.whl size=187831595 sha256=58853b28a5a926cae14402bfd8d4d93a45ebf8f9e79533f37ab09d0d77a99c05
      Stored in directory: /root/.cache/pip/wheels/3d/88/d8/284b89f56af7d5bf366b10d6b8e251ac8a7c7bf3f04203fb4f
    Successfully built flash-attn
    Installing collected packages: flash-attn
    Successfully installed flash-attn-2.7.4.post1
    Dataset unzipped to '/content/level-1-binary'.



```python
# Cell 2: Project Configuration

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


```python
# Cell 3: Data Loading and Preprocessing

from datasets import load_from_disk
from transformers import AutoTokenizer

# 3.1 Load the tokenizer needed for preprocessing
# This will be the same tokenizer used for the model later.
tokenizer = AutoTokenizer.from_pretrained(
    Config.MODEL_ID,
    trust_remote_code=True
)

tokenizer.padding_side = "left"      # Flash-Attn requires left padding
# Set a padding token if one is not already defined
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# 3.2 Load the raw dataset from disk
raw_dataset = load_from_disk(Config.DATASET_PATH)

# 3.3 Define the preprocessing function
def preprocess_function(examples):
    """
    Formats the input text and tokenizes it for sequence classification.
    The label is passed through untouched.
    """
    # Create a single input string per example
    # Note: We do not include the label (0 or 1) in the input text itself.
    system_prompt = "Analyze the following mathematical problem and solution to determine if the solution is correct or flawed."
    input_texts = [
        f"{system_prompt}\n\n### Problem:\n{q}\n\n### Solution:\n{s}"
        for q, s in zip(examples["question"], examples["solution"])
    ]

    # Tokenize the texts
    # The tokenizer will return 'input_ids' and 'attention_mask'.
    return tokenizer(
        input_texts,
        truncation=True,
        max_length=512,  # A reasonable max length for these problems
        padding=False    # Padding will be handled by the data collator
    )

# 3.4 Apply the preprocessing function to the dataset
# We use batched=True for efficiency and remove original text columns.
tokenized_dataset = raw_dataset.map(
    preprocess_function,
    batched=True,
    remove_columns=["question", "solution"]
)

# 3.5 Verify the new dataset structure
print("--- Tokenized dataset ---")
print(tokenized_dataset)
print("\nExample record:")
print(tokenized_dataset["train"][0])
```

    /usr/local/lib/python3.11/dist-packages/huggingface_hub/utils/_auth.py:94: UserWarning: 
    The secret `HF_TOKEN` does not exist in your Colab secrets.
    To authenticate with the Hugging Face Hub, create a token in your settings tab (https://huggingface.co/settings/tokens), set it as secret in your Google Colab and restart your session.
    You will be able to reuse this secret in all of your notebooks.
    Please note that authentication is recommended but still optional to access public models or datasets.
      warnings.warn(



    tokenizer_config.json: 0.00B [00:00, ?B/s]



    vocab.json: 0.00B [00:00, ?B/s]



    merges.txt: 0.00B [00:00, ?B/s]



    tokenizer.json:   0%|          | 0.00/15.5M [00:00<?, ?B/s]



    added_tokens.json:   0%|          | 0.00/249 [00:00<?, ?B/s]



    special_tokens_map.json:   0%|          | 0.00/587 [00:00<?, ?B/s]



    Map:   0%|          | 0/3296 [00:00<?, ? examples/s]



    Map:   0%|          | 0/412 [00:00<?, ? examples/s]



    Map:   0%|          | 0/412 [00:00<?, ? examples/s]


    --- Tokenized dataset ---
    DatasetDict({
        train: Dataset({
            features: ['index', 'label', 'input_ids', 'attention_mask'],
            num_rows: 3296
        })
        validation: Dataset({
            features: ['index', 'label', 'input_ids', 'attention_mask'],
            num_rows: 412
        })
        test: Dataset({
            features: ['index', 'label', 'input_ids', 'attention_mask'],
            num_rows: 412
        })
    })
    
    Example record:
    {'index': 1325, 'label': 1, 'input_ids': [107202, 290, 3992, 58944, 4792, 326, 7578, 316, 11433, 538, 290, 7578, 382, 6145, 503, 104041, 364, 31639, 26113, 734, 50, 2146, 22639, 548, 1353, 15, 540, 1101, 2174, 2944, 13, 1328, 2944, 11, 1770, 6100, 261, 220, 702, 4, 9338, 13, 3253, 2009, 3905, 738, 1770, 1520, 306, 3609, 395, 290, 1920, 5503, 1715, 31639, 20858, 734, 2500, 2944, 1770, 738, 8748, 548, 1353, 15, 425, 350, 702, 14, 1353, 8, 314, 548, 5354, 1353, 15, 14793, 702, 14, 1353, 25987, 1353, 3920, 1353, 558, 637, 3609, 11, 1770, 738, 1520, 548, 1353, 15, 659, 548, 1353, 314, 548, 5354, 1353, 15, 10, 1353, 28, 7920, 15, 3920, 7920, 15, 558, 1509, 220, 7920, 15], 'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}



```python
# Cell 3.5: Merge Datasets for Training

from datasets import concatenate_datasets, DatasetDict

# 3.5.1 Combine the 'train' and 'validation' splits
# This creates a larger training set for the model.
full_train_dataset = concatenate_datasets(
    [tokenized_dataset["train"], tokenized_dataset["validation"]]
)

# 3.5.2 Create a new DatasetDict with the merged training set and the original test set
final_dataset = DatasetDict({
    "train": full_train_dataset,
    "test": tokenized_dataset["test"]
})

print("--- Merged dataset for training ---")
```

    --- Merged dataset for training ---



```python
# ────────────────────────────────────────────────────────────────
# Cell 4-5 · Tokenizer, 4-bit backbone → LoRA + custom classifier
# ────────────────────────────────────────────────────────────────
import torch, torch.nn as nn
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import LoraConfig, get_peft_model, TaskType

# ----- Config -----
NUM_LABELS = Config.NUM_LABELS      # e.g. 2
DTYPE       = torch.bfloat16        # A100 native

quant_cfg = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=DTYPE,
)

tokenizer = AutoTokenizer.from_pretrained(Config.MODEL_ID, trust_remote_code=True)
tokenizer.padding_side = "left"      # Flash-Attn requires left padding
tokenizer.pad_token = tokenizer.pad_token or tokenizer.eos_token

# 1. load causal-LM in 4-bit
backbone = AutoModelForCausalLM.from_pretrained(
    Config.MODEL_ID,
    quantization_config=quant_cfg,
    device_map="auto",
    trust_remote_code=True,
    attn_implementation="flash_attention_2",
)
backbone.config.pad_token_id = tokenizer.pad_token_id

# 2. LoRA on all linear layers
lora_cfg = LoraConfig(
    task_type=TaskType.SEQ_CLS,   # still “SEQ_CLS” so PEFT knows to train a head
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    target_modules="all-linear",
)
backbone = get_peft_model(backbone, lora_cfg)

# 3. custom classification wrapper
class GPTSequenceClassifier(nn.Module):
    def __init__(self, base_model, num_labels):
        super().__init__()
        self.base = base_model                       # LoRA-augmented Φ-4-mini
        hidden = base_model.config.hidden_size
        self.classifier = nn.Linear(hidden, num_labels, bias=True)
        self.num_labels = num_labels

    def forward(self, input_ids=None, attention_mask=None, labels=None, **kw):
        outputs = self.base(
            input_ids=input_ids,
            attention_mask=attention_mask,
            output_hidden_states=True,
            **kw,
        )
        last_hidden = outputs.hidden_states[-1]      # (B, L, H)
        pooled      = last_hidden[:, -1, :]          # use last token
        logits      = self.classifier(pooled)        # (B, num_labels)

        loss = None
        if labels is not None:
            loss = nn.functional.cross_entropy(logits, labels)

        return {"loss": loss, "logits": logits} if loss is not None else {"logits": logits}

model = GPTSequenceClassifier(backbone, NUM_LABELS)
# call on the LoRA-augmented backbone instead
backbone.print_trainable_parameters()
print("--- LoRA+classifier model ready ---")
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



    model-00001-of-00002.safetensors:   0%|          | 0.00/4.90G [00:00<?, ?B/s]



    model-00002-of-00002.safetensors:   0%|          | 0.00/2.77G [00:00<?, ?B/s]



    Loading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]



    generation_config.json:   0%|          | 0.00/168 [00:00<?, ?B/s]


    trainable params: 23,068,672 || all params: 3,859,090,432 || trainable%: 0.5978
    --- LoRA+classifier model ready ---



```python
from transformers import TrainingArguments, Trainer, DataCollatorWithPadding

training_args = TrainingArguments(
    output_dir=Config.OUTPUT_DIR,

    # —— Batching ——
    num_train_epochs=3,
    per_device_train_batch_size=8,   # safe default on 4-bit + A100
    gradient_accumulation_steps=4,   # effective 32

    # —— Optimiser / sched ——
    optim="paged_adamw_8bit",
    learning_rate=2e-4,
    lr_scheduler_type="cosine",
    warmup_ratio=0.1,

    # —— Precision / memory ——
    bf16=True,                       # A100 native bf16
    gradient_checkpointing=False,

    # —— Logging / ckpt ——
    logging_strategy="steps",
    logging_steps=25,
    save_strategy="epoch",
    save_total_limit=1,
    report_to="none",
    save_safetensors=False,

    # —— Evaluation ——
    # evaluation_strategy="epoch",
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=final_dataset["train"],
    # eval_dataset=final_dataset["test"],   # drop if you have no split
    tokenizer=tokenizer,
    data_collator=DataCollatorWithPadding(tokenizer=tokenizer),
    compute_metrics=compute_metrics,            # ↳ defined earlier
)

print("--- Trainer initialised ---")
```

    --- Trainer initialised ---


    /tmp/ipython-input-8-1445400942.py:33: FutureWarning: `tokenizer` is deprecated and will be removed in version 5.0.0 for `Trainer.__init__`. Use `processing_class` instead.
      trainer = Trainer(



```python
# Cell 8: Execute Training

print("Starting model training...")
trainer.train()
print("Training complete.")
```

    Starting model training...


    The input hidden states seems to be silently casted in float32, this might be related to the fact you have upcasted embedding or layer norm layers in float32. We will cast back the input in torch.bfloat16.




    <div>

      <progress value='348' max='348' style='width:300px; height:20px; vertical-align: middle;'></progress>
      [348/348 12:24, Epoch 3/3]
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
      <td>2.826000</td>
    </tr>
    <tr>
      <td>50</td>
      <td>2.825100</td>
    </tr>
    <tr>
      <td>75</td>
      <td>2.582200</td>
    </tr>
    <tr>
      <td>100</td>
      <td>2.660400</td>
    </tr>
    <tr>
      <td>125</td>
      <td>2.652700</td>
    </tr>
    <tr>
      <td>150</td>
      <td>2.419000</td>
    </tr>
    <tr>
      <td>175</td>
      <td>2.203500</td>
    </tr>
    <tr>
      <td>200</td>
      <td>1.910300</td>
    </tr>
    <tr>
      <td>225</td>
      <td>1.550600</td>
    </tr>
    <tr>
      <td>250</td>
      <td>1.079600</td>
    </tr>
    <tr>
      <td>275</td>
      <td>1.018500</td>
    </tr>
    <tr>
      <td>300</td>
      <td>0.916300</td>
    </tr>
    <tr>
      <td>325</td>
      <td>0.773900</td>
    </tr>
  </tbody>
</table><p>


    Training complete.



```python
# Cell 9: Final Evaluation and Saving

def compute_metrics_new(p):
    # HF passes either a plain ndarray or a tuple; handle both robustly
    logits = p.predictions[0] if isinstance(p.predictions, (tuple, list)) else p.predictions

    preds  = np.argmax(logits, axis=1)
    labels = p.label_ids
    return {"accuracy": (preds == labels).mean().item()}

trainer.compute_metrics = compute_metrics_new

# 9.1 Evaluate the model on the test set
print("\n--- Evaluating on the test set ---")
test_results = trainer.evaluate(eval_dataset=final_dataset["test"])

# 9.2 Print the evaluation results
print("Test set performance:")
print(test_results)

# 9.3 Save the final trained LoRA adapter
print(f"\nSaving final model adapter to {Config.OUTPUT_DIR}...")
trainer.save_model(Config.OUTPUT_DIR)
print("Model saved successfully.")
```

    
    --- Evaluating on the test set ---




<div>

  <progress value='156' max='52' style='width:300px; height:20px; vertical-align: middle;'></progress>
  [52/52 03:38]
</div>



    Test set performance:
    {'eval_loss': 0.24340982735157013, 'eval_accuracy': 0.9053398058252428, 'eval_runtime': 12.6931, 'eval_samples_per_second': 32.459, 'eval_steps_per_second': 4.097, 'epoch': 3.0}
    
    Saving final model adapter to /content/level1-classifier-output...
    Model saved successfully.



```python
print(final_dataset['test'][0])
```

    {'index': 1417, 'label': 0, 'input_ids': [107202, 290, 3992, 58944, 4792, 326, 7578, 316, 11433, 538, 290, 7578, 382, 6145, 503, 104041, 364, 31639, 26113, 734, 976, 4215, 328, 38927, 326, 23135, 885, 20355, 1954, 382, 220, 22, 13, 38927, 382, 220, 16, 1284, 12787, 1572, 23135, 13, 3253, 2890, 382, 38927, 1715, 31639, 20858, 734, 3335, 1215, 382, 23135, 885, 5744, 11, 1815, 38927, 885, 5744, 382, 1215, 659, 220, 16, 558, 976, 42006, 484, 18627, 290, 4215, 328, 1043, 20355, 382, 1215, 659, 1215, 659, 220, 16, 314, 220, 22, 558, 1582, 48784, 1299, 5941, 11, 290, 42006, 14081, 220, 17, 87, 314, 220, 21, 558, 198140, 11, 290, 1432, 328, 1215, 1118, 18627, 290, 5744, 328, 23135, 382, 220, 21, 14, 17, 28, 5354, 21, 14, 17, 28, 18, 3920, 18, 558, 5808, 51613, 84, 382, 220, 18, 659, 220, 16, 314, 2256, 18, 10, 16, 28, 19, 3920, 19, 2101, 2890, 558, 1509, 220, 19], 'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}



```python
import torch
import numpy as np
import pandas as pd   # only if you want a tidy table

# 1. Forward pass (no grad) over the test set
pred_outputs = trainer.predict(final_dataset["test"])   # returns EvalPrediction

# 2. Extract logits – shape: (num_samples, num_labels)
logits = pred_outputs.predictions if not isinstance(pred_outputs.predictions, (tuple, list)) \
         else pred_outputs.predictions[0]

# 3. Convert to probabilities
probs = torch.softmax(torch.tensor(logits), dim=-1).numpy()  # (N, C) NumPy array

# 4. (optional) wrap in a DataFrame for easy inspection / CSV export
df = pd.DataFrame(
    probs,
    columns=[f"p(class={i})" for i in range(probs.shape[1])],
)

# 5. add auxiliary fields from the dataset
df["index"]      = final_dataset["test"]["index"]   # ← your original sample ID
df["true_label"] = final_dataset["test"]["label"]

# optional: move index to first column
cols = ["index", "true_label"] + [c for c in df.columns if c.startswith("p(")]
df = df[cols]

print(df.head())

# 5. Save if you like
df.to_csv("test_probs.csv", index=False)
```





       index  true_label  p(class=0)  p(class=1)
    0   1417           0    0.979823    0.020177
    1   1179           1    0.396068    0.603932
    2   1299           1    0.029424    0.970576
    3   2527           0    0.952042    0.047958
    4    880           0    0.737631    0.262369



```python
!zip -r level1-classifier-output.zip level1-classifier-output
```

      adding: level1-classifier-output/ (stored 0%)
      adding: level1-classifier-output/merges.txt (deflated 53%)
      adding: level1-classifier-output/training_args.bin (deflated 52%)
      adding: level1-classifier-output/checkpoint-348/ (stored 0%)
      adding: level1-classifier-output/checkpoint-348/merges.txt (deflated 53%)
      adding: level1-classifier-output/checkpoint-348/training_args.bin (deflated 52%)
      adding: level1-classifier-output/checkpoint-348/optimizer.pt (deflated 10%)
      adding: level1-classifier-output/checkpoint-348/pytorch_model.bin (deflated 14%)
      adding: level1-classifier-output/checkpoint-348/scheduler.pt (deflated 56%)
      adding: level1-classifier-output/checkpoint-348/rng_state.pth (deflated 25%)
      adding: level1-classifier-output/checkpoint-348/vocab.json (deflated 58%)
      adding: level1-classifier-output/checkpoint-348/tokenizer.json (deflated 79%)
      adding: level1-classifier-output/checkpoint-348/tokenizer_config.json (deflated 86%)
      adding: level1-classifier-output/checkpoint-348/special_tokens_map.json (deflated 75%)
      adding: level1-classifier-output/checkpoint-348/added_tokens.json (deflated 55%)
      adding: level1-classifier-output/checkpoint-348/chat_template.jinja (deflated 59%)
      adding: level1-classifier-output/checkpoint-348/trainer_state.json (deflated 69%)
      adding: level1-classifier-output/pytorch_model.bin (deflated 14%)
      adding: level1-classifier-output/vocab.json (deflated 58%)
      adding: level1-classifier-output/tokenizer.json (deflated 79%)
      adding: level1-classifier-output/tokenizer_config.json (deflated 86%)
      adding: level1-classifier-output/special_tokens_map.json (deflated 75%)
      adding: level1-classifier-output/added_tokens.json (deflated 55%)
      adding: level1-classifier-output/chat_template.jinja (deflated 59%)



```python
from google.colab import files
files.download("level1-classifier-output.zip")
```


    <IPython.core.display.Javascript object>



    <IPython.core.display.Javascript object>



```python
!cp -r level1-classifier-output.zip /content/drive/MyDrive/
```


```python

```
