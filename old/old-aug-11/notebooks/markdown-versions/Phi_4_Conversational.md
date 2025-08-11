To run this, press "*Runtime*" and press "*Run all*" on a **free** Tesla T4 Google Colab instance!
<div class="align-center">
<a href="https://unsloth.ai/"><img src="https://github.com/unslothai/unsloth/raw/main/images/unsloth%20new%20logo.png" width="115"></a>
<a href="https://discord.gg/unsloth"><img src="https://github.com/unslothai/unsloth/raw/main/images/Discord button.png" width="145"></a>
<a href="https://docs.unsloth.ai/"><img src="https://github.com/unslothai/unsloth/blob/main/images/documentation%20green%20button.png?raw=true" width="125"></a></a> Join Discord if you need help + ⭐ <i>Star us on <a href="https://github.com/unslothai/unsloth">Github</a> </i> ⭐
</div>

To install Unsloth on your own computer, follow the installation instructions on our Github page [here](https://docs.unsloth.ai/get-started/installing-+-updating).

You will learn how to do [data prep](#Data), how to [train](#Train), how to [run the model](#Inference), & [how to save it](#Save)


### News

Unsloth now supports Text-to-Speech (TTS) models. Read our [guide here](https://docs.unsloth.ai/basics/text-to-speech-tts-fine-tuning).

Read our **[Gemma 3N Guide](https://docs.unsloth.ai/basics/gemma-3n-how-to-run-and-fine-tune)** and check out our new **[Dynamic 2.0](https://docs.unsloth.ai/basics/unsloth-dynamic-2.0-ggufs)** quants which outperforms other quantization methods!

Visit our docs for all our [model uploads](https://docs.unsloth.ai/get-started/all-our-models) and [notebooks](https://docs.unsloth.ai/get-started/unsloth-notebooks).


### Installation


```python
%%capture
import os
if "COLAB_" not in "".join(os.environ.keys()):
    !pip install unsloth
else:
    # Do this only in Colab notebooks! Otherwise use pip install unsloth
    !pip install --no-deps bitsandbytes accelerate xformers==0.0.29.post3 peft trl triton cut_cross_entropy unsloth_zoo
    !pip install sentencepiece protobuf "datasets>=3.4.1,<4.0.0" huggingface_hub hf_transfer
    !pip install --no-deps unsloth
```

### Unsloth


```python
from unsloth import FastLanguageModel  # FastVisionModel for LLMs
import torch
max_seq_length = 2048  # Choose any! We auto support RoPE Scaling internally!
load_in_4bit = True  # Use 4bit quantization to reduce memory usage. Can be False.

# 4bit pre quantized models we support for 4x faster downloading + no OOMs.
fourbit_models = [
    "unsloth/Meta-Llama-3.1-8B-bnb-4bit",  # Llama-3.1 2x faster
    "unsloth/Mistral-Small-Instruct-2409",  # Mistral 22b 2x faster!
    "unsloth/Phi-4",  # Phi-4 2x faster!
    "unsloth/Phi-4-unsloth-bnb-4bit",  # Phi-4 Unsloth Dynamic 4-bit Quant
    "unsloth/gemma-2-9b-bnb-4bit",  # Gemma 2x faster!
    "unsloth/Qwen2.5-7B-Instruct-bnb-4bit"  # Qwen 2.5 2x faster!
    "unsloth/Llama-3.2-1B-bnb-4bit",  # NEW! Llama 3.2 models
    "unsloth/Llama-3.2-1B-Instruct-bnb-4bit",
    "unsloth/Llama-3.2-3B-bnb-4bit",
    "unsloth/Llama-3.2-3B-Instruct-bnb-4bit",
]  # More models at https://docs.unsloth.ai/get-started/all-our-models

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/Phi-4",
    max_seq_length = max_seq_length,
    load_in_4bit = load_in_4bit,
    # token = "hf_...", # use one if using gated models like meta-llama/Llama-2-7b-hf
)
```

    🦥 Unsloth: Will patch your computer to enable 2x faster free finetuning.
    🦥 Unsloth Zoo will now patch everything to make training faster!
    ==((====))==  Unsloth 2025.1.5: Fast Llama patching. Transformers: 4.47.1.
       \\   /|    GPU: Tesla T4. Max memory: 14.748 GB. Platform: Linux.
    O^O/ \_/ \    Torch: 2.5.1+cu121. CUDA: 7.5. CUDA Toolkit: 12.1. Triton: 3.1.0
    \        /    Bfloat16 = FALSE. FA [Xformers = 0.0.29.post1. FA2 = False]
     "-____-"     Free Apache license: http://github.com/unslothai/unsloth
    Unsloth: Fast downloading is enabled - ignore downloading bars which are red colored!



    model.safetensors.index.json:   0%|          | 0.00/160k [00:00<?, ?B/s]



    Downloading shards:   0%|          | 0/3 [00:00<?, ?it/s]



    model-00001-of-00003.safetensors:   0%|          | 0.00/4.97G [00:00<?, ?B/s]



    model-00002-of-00003.safetensors:   0%|          | 0.00/4.39G [00:00<?, ?B/s]



    model-00003-of-00003.safetensors:   0%|          | 0.00/1.03G [00:00<?, ?B/s]



    Loading checkpoint shards:   0%|          | 0/3 [00:00<?, ?it/s]



    generation_config.json:   0%|          | 0.00/170 [00:00<?, ?B/s]



    tokenizer_config.json:   0%|          | 0.00/18.0k [00:00<?, ?B/s]



    vocab.json:   0%|          | 0.00/1.61M [00:00<?, ?B/s]



    merges.txt:   0%|          | 0.00/917k [00:00<?, ?B/s]



    special_tokens_map.json:   0%|          | 0.00/570 [00:00<?, ?B/s]



    tokenizer.json:   0%|          | 0.00/7.15M [00:00<?, ?B/s]


We now add LoRA adapters for parameter efficient finetuning - this allows us to only efficiently train 1% of all parameters.


```python
model = FastLanguageModel.get_peft_model(
    model,
    r = 16, # Choose any number > 0 ! Suggested 8, 16, 32, 64, 128
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj",],
    lora_alpha = 16,
    lora_dropout = 0, # Supports any, but = 0 is optimized
    bias = "none",    # Supports any, but = "none" is optimized
    # [NEW] "unsloth" uses 30% less VRAM, fits 2x larger batch sizes!
    use_gradient_checkpointing = "unsloth", # True or "unsloth" for very long context
    random_state = 3407,
    use_rslora = False,  # We support rank stabilized LoRA
    loftq_config = None, # And LoftQ
)
```

    Unsloth 2025.1.5 patched 40 layers with 40 QKV layers, 40 O layers and 40 MLP layers.


<a name="Data"></a>
### Data Prep
We now use the `Phi-4` format for conversation style finetunes. We use [Maxime Labonne's FineTome-100k](https://huggingface.co/datasets/mlabonne/FineTome-100k) dataset in ShareGPT style. But we convert it to HuggingFace's normal multiturn format `("role", "content")` instead of `("from", "value")`/ Phi-4 renders multi turn conversations like below:

```
<|im_start|>user<|im_sep|>Hello!<|im_end|>
<|im_start|>assistant<|im_sep|>Hi! How can I help?<|im_end|>
<|im_start|>user<|im_sep|>What is 2+2?<|im_end|>
```

We use our `get_chat_template` function to get the correct chat template. We support `zephyr, chatml, mistral, llama, alpaca, vicuna, vicuna_old, phi3, phi4, llama3` and more.


```python
from unsloth.chat_templates import get_chat_template

tokenizer = get_chat_template(
    tokenizer,
    chat_template = "phi-4",
)

def formatting_prompts_func(examples):
    convos = examples["conversations"]
    texts = [
        tokenizer.apply_chat_template(
            convo, tokenize = False, add_generation_prompt = False
        )
        for convo in convos
    ]
    return { "text" : texts, }
pass

from datasets import load_dataset
dataset = load_dataset("mlabonne/FineTome-100k", split = "train")
```


    README.md:   0%|          | 0.00/982 [00:00<?, ?B/s]



    train-00000-of-00001.parquet:   0%|          | 0.00/117M [00:00<?, ?B/s]



    Generating train split:   0%|          | 0/100000 [00:00<?, ? examples/s]


We now use `standardize_sharegpt` to convert ShareGPT style datasets into HuggingFace's generic format. This changes the dataset from looking like:
```
{"from": "system", "value": "You are an assistant"}
{"from": "human", "value": "What is 2+2?"}
{"from": "gpt", "value": "It's 4."}
```
to
```
{"role": "system", "content": "You are an assistant"}
{"role": "user", "content": "What is 2+2?"}
{"role": "assistant", "content": "It's 4."}
```


```python
from unsloth.chat_templates import standardize_sharegpt

dataset = standardize_sharegpt(dataset)
dataset = dataset.map(
    formatting_prompts_func,
    batched=True,
)
```


    Standardizing format:   0%|          | 0/100000 [00:00<?, ? examples/s]



    Map:   0%|          | 0/100000 [00:00<?, ? examples/s]


We look at how the conversations are structured for item 5:


```python
dataset[5]["conversations"]
```




    [{'content': 'How do astronomers determine the original wavelength of light emitted by a celestial body at rest, which is necessary for measuring its speed using the Doppler effect?',
      'role': 'user'},
     {'content': 'Astronomers make use of the unique spectral fingerprints of elements found in stars. These elements emit and absorb light at specific, known wavelengths, forming an absorption spectrum. By analyzing the light received from distant stars and comparing it to the laboratory-measured spectra of these elements, astronomers can identify the shifts in these wavelengths due to the Doppler effect. The observed shift tells them the extent to which the light has been redshifted or blueshifted, thereby allowing them to calculate the speed of the star along the line of sight relative to Earth.',
      'role': 'assistant'}]



And we see how the chat template transformed these conversations.


```python
dataset[5]["text"]
```




    '<|im_start|>user<|im_sep|>How do astronomers determine the original wavelength of light emitted by a celestial body at rest, which is necessary for measuring its speed using the Doppler effect?<|im_end|><|im_start|>assistant<|im_sep|>Astronomers make use of the unique spectral fingerprints of elements found in stars. These elements emit and absorb light at specific, known wavelengths, forming an absorption spectrum. By analyzing the light received from distant stars and comparing it to the laboratory-measured spectra of these elements, astronomers can identify the shifts in these wavelengths due to the Doppler effect. The observed shift tells them the extent to which the light has been redshifted or blueshifted, thereby allowing them to calculate the speed of the star along the line of sight relative to Earth.<|im_end|>'



<a name="Train"></a>
### Train the model
Now let's use Huggingface TRL's `SFTTrainer`! More docs here: [TRL SFT docs](https://huggingface.co/docs/trl/sft_trainer). We do 60 steps to speed things up, but you can set `num_train_epochs=1` for a full run, and turn off `max_steps=None`. We also support TRL's `DPOTrainer`!


```python
from trl import SFTConfig, SFTTrainer
from transformers import DataCollatorForSeq2Seq
trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    dataset_text_field = "text",
    max_seq_length = max_seq_length,
    data_collator = DataCollatorForSeq2Seq(tokenizer = tokenizer),
    packing = False, # Can make training 5x faster for short sequences.
    args = SFTConfig(
        per_device_train_batch_size = 2,
        gradient_accumulation_steps = 4,
        warmup_steps = 5,
        # num_train_epochs = 1, # Set this for 1 full training run.
        max_steps = 30,
        learning_rate = 2e-4,
        logging_steps = 1,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 3407,
        output_dir = "outputs",
        report_to = "none", # Use this for WandB etc
    ),
)
```


    Map (num_proc=2):   0%|          | 0/100000 [00:00<?, ? examples/s]


We also use Unsloth's `train_on_completions` method to only train on the assistant outputs and ignore the loss on the user's inputs.


```python
from unsloth.chat_templates import train_on_responses_only

trainer = train_on_responses_only(
    trainer,
    instruction_part="<|im_start|>user<|im_sep|>",
    response_part="<|im_start|>assistant<|im_sep|>",
)
```


    Map:   0%|          | 0/100000 [00:00<?, ? examples/s]


We verify masking is actually done:


```python
tokenizer.decode(trainer.train_dataset[5]["input_ids"])
```




    '<|im_start|>user<|im_sep|>How do astronomers determine the original wavelength of light emitted by a celestial body at rest, which is necessary for measuring its speed using the Doppler effect?<|im_end|><|im_start|>assistant<|im_sep|>Astronomers make use of the unique spectral fingerprints of elements found in stars. These elements emit and absorb light at specific, known wavelengths, forming an absorption spectrum. By analyzing the light received from distant stars and comparing it to the laboratory-measured spectra of these elements, astronomers can identify the shifts in these wavelengths due to the Doppler effect. The observed shift tells them the extent to which the light has been redshifted or blueshifted, thereby allowing them to calculate the speed of the star along the line of sight relative to Earth.<|im_end|>'




```python
space = tokenizer(" ", add_special_tokens = False).input_ids[0]
tokenizer.decode([space if x == -100 else x for x in trainer.train_dataset[5]["labels"]])
```




    '                                     Astronomers make use of the unique spectral fingerprints of elements found in stars. These elements emit and absorb light at specific, known wavelengths, forming an absorption spectrum. By analyzing the light received from distant stars and comparing it to the laboratory-measured spectra of these elements, astronomers can identify the shifts in these wavelengths due to the Doppler effect. The observed shift tells them the extent to which the light has been redshifted or blueshifted, thereby allowing them to calculate the speed of the star along the line of sight relative to Earth.<|im_end|>'



We can see the System and Instruction prompts are successfully masked!


```python
# @title Show current memory stats
gpu_stats = torch.cuda.get_device_properties(0)
start_gpu_memory = round(torch.cuda.max_memory_reserved() / 1024 / 1024 / 1024, 3)
max_memory = round(gpu_stats.total_memory / 1024 / 1024 / 1024, 3)
print(f"GPU = {gpu_stats.name}. Max memory = {max_memory} GB.")
print(f"{start_gpu_memory} GB of memory reserved.")
```

    GPU = Tesla T4. Max memory = 14.748 GB.
    10.043 GB of memory reserved.



```python
trainer_stats = trainer.train()
```

    ==((====))==  Unsloth - 2x faster free finetuning | Num GPUs = 1
       \\   /|    Num examples = 100,000 | Num Epochs = 1
    O^O/ \_/ \    Batch size per device = 2 | Gradient Accumulation steps = 4
    \        /    Total batch size = 8 | Total steps = 30
     "-____-"     Number of trainable parameters = 65,536,000




    <div>

      <progress value='30' max='30' style='width:300px; height:20px; vertical-align: middle;'></progress>
      [30/30 15:11, Epoch 0/1]
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
      <td>0.746700</td>
    </tr>
    <tr>
      <td>2</td>
      <td>0.660800</td>
    </tr>
    <tr>
      <td>3</td>
      <td>1.035700</td>
    </tr>
    <tr>
      <td>4</td>
      <td>0.767600</td>
    </tr>
    <tr>
      <td>5</td>
      <td>0.693200</td>
    </tr>
    <tr>
      <td>6</td>
      <td>0.818100</td>
    </tr>
    <tr>
      <td>7</td>
      <td>0.464400</td>
    </tr>
    <tr>
      <td>8</td>
      <td>0.831800</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.600800</td>
    </tr>
    <tr>
      <td>10</td>
      <td>0.525800</td>
    </tr>
    <tr>
      <td>11</td>
      <td>0.700200</td>
    </tr>
    <tr>
      <td>12</td>
      <td>0.760500</td>
    </tr>
    <tr>
      <td>13</td>
      <td>0.774900</td>
    </tr>
    <tr>
      <td>14</td>
      <td>0.452600</td>
    </tr>
    <tr>
      <td>15</td>
      <td>0.634000</td>
    </tr>
    <tr>
      <td>16</td>
      <td>0.395300</td>
    </tr>
    <tr>
      <td>17</td>
      <td>0.783800</td>
    </tr>
    <tr>
      <td>18</td>
      <td>0.656200</td>
    </tr>
    <tr>
      <td>19</td>
      <td>0.605400</td>
    </tr>
    <tr>
      <td>20</td>
      <td>0.770700</td>
    </tr>
    <tr>
      <td>21</td>
      <td>0.732600</td>
    </tr>
    <tr>
      <td>22</td>
      <td>0.535400</td>
    </tr>
    <tr>
      <td>23</td>
      <td>0.910900</td>
    </tr>
    <tr>
      <td>24</td>
      <td>0.721200</td>
    </tr>
    <tr>
      <td>25</td>
      <td>0.500100</td>
    </tr>
    <tr>
      <td>26</td>
      <td>0.590200</td>
    </tr>
    <tr>
      <td>27</td>
      <td>0.658900</td>
    </tr>
    <tr>
      <td>28</td>
      <td>0.657500</td>
    </tr>
    <tr>
      <td>29</td>
      <td>0.698500</td>
    </tr>
    <tr>
      <td>30</td>
      <td>0.770000</td>
    </tr>
  </tbody>
</table><p>



```python
# @title Show final memory and time stats
used_memory = round(torch.cuda.max_memory_reserved() / 1024 / 1024 / 1024, 3)
used_memory_for_lora = round(used_memory - start_gpu_memory, 3)
used_percentage = round(used_memory / max_memory * 100, 3)
lora_percentage = round(used_memory_for_lora / max_memory * 100, 3)
print(f"{trainer_stats.metrics['train_runtime']} seconds used for training.")
print(
    f"{round(trainer_stats.metrics['train_runtime']/60, 2)} minutes used for training."
)
print(f"Peak reserved memory = {used_memory} GB.")
print(f"Peak reserved memory for training = {used_memory_for_lora} GB.")
print(f"Peak reserved memory % of max memory = {used_percentage} %.")
print(f"Peak reserved memory for training % of max memory = {lora_percentage} %.")
```

    959.8611 seconds used for training.
    16.0 minutes used for training.
    Peak reserved memory = 12.361 GB.
    Peak reserved memory for training = 2.318 GB.
    Peak reserved memory % of max memory = 83.815 %.
    Peak reserved memory for training % of max memory = 15.717 %.


<a name="Inference"></a>
### Inference
Let's run the model! You can change the instruction and input - leave the output blank!



We use `min_p = 0.1` and `temperature = 1.5`.


```python
from unsloth.chat_templates import get_chat_template

tokenizer = get_chat_template(
    tokenizer,
    chat_template = "phi-4",
)
FastLanguageModel.for_inference(model) # Enable native 2x faster inference

messages = [
    {"role": "user", "content": "Continue the fibonnaci sequence: 1, 1, 2, 3, 5, 8,"},
]
inputs = tokenizer.apply_chat_template(
    messages,
    tokenize = True,
    add_generation_prompt = True, # Must add for generation
    return_tensors = "pt",
).to("cuda")

outputs = model.generate(
    input_ids = inputs, max_new_tokens = 64, use_cache = True, temperature = 1.5, min_p = 0.1
)
tokenizer.batch_decode(outputs)
```

    The attention mask is not set and cannot be inferred from input because pad token is same as eos token. As a consequence, you may observe unexpected behavior. Please pass your input's `attention_mask` to obtain reliable results.





    ['<|im_start|>user<|im_sep|>Continue the fibonnaci sequence: 1, 1, 2, 3, 5, 8,<|im_end|><|im_start|>assistant<|im_sep|>The next number in the Fibonacci sequence is 13. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. In this case, the sequence starts with 1 and 1, and each subsequent number is the sum of the']



 You can also use a `TextStreamer` for continuous inference - so you can see the generation token by token, instead of waiting the whole time!


```python
FastLanguageModel.for_inference(model) # Enable native 2x faster inference

messages = [
    {"role": "user", "content": "Continue the fibonnaci sequence: 1, 1, 2, 3, 5, 8,"},
]
inputs = tokenizer.apply_chat_template(
    messages,
    tokenize = True,
    add_generation_prompt = True, # Must add for generation
    return_tensors = "pt",
).to("cuda")

from transformers import TextStreamer
text_streamer = TextStreamer(tokenizer, skip_prompt = True)
_ = model.generate(
    input_ids = inputs, streamer = text_streamer, max_new_tokens = 128,
    use_cache = True, temperature = 1.5, min_p = 0.1
)
```

    The next number in the Fibonacci sequence is 13. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. In this case, the sequence starts with 1 and 1, and each subsequent number is the sum of the two preceding numbers. So, the next number after 8 is 13, which is the sum of 5 and 8.<|im_end|>


<a name="Save"></a>
### Saving, loading finetuned models
To save the final model as LoRA adapters, either use Huggingface's `push_to_hub` for an online save or `save_pretrained` for a local save.

**[NOTE]** This ONLY saves the LoRA adapters, and not the full model. To save to 16bit or GGUF, scroll down!


```python
model.save_pretrained("lora_model")  # Local saving
tokenizer.save_pretrained("lora_model")
# model.push_to_hub("your_name/lora_model", token = "...") # Online saving
# tokenizer.push_to_hub("your_name/lora_model", token = "...") # Online saving
```




    ('lora_model/tokenizer_config.json',
     'lora_model/special_tokens_map.json',
     'lora_model/vocab.json',
     'lora_model/merges.txt',
     'lora_model/added_tokens.json',
     'lora_model/tokenizer.json')



Now if you want to load the LoRA adapters we just saved for inference, set `False` to `True`:


```python
if False:
    from unsloth import FastLanguageModel
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name = "lora_model", # YOUR MODEL YOU USED FOR TRAINING
        max_seq_length = max_seq_length,
        dtype = dtype,
        load_in_4bit = load_in_4bit,
    )
    FastLanguageModel.for_inference(model) # Enable native 2x faster inference

messages = [
    {"role": "user", "content": "Describe a tall tower in the capital of France."},
]
inputs = tokenizer.apply_chat_template(
    messages,
    tokenize = True,
    add_generation_prompt = True, # Must add for generation
    return_tensors = "pt",
).to("cuda")

from transformers import TextStreamer
text_streamer = TextStreamer(tokenizer, skip_prompt = True)
_ = model.generate(
    input_ids = inputs, streamer = text_streamer, max_new_tokens = 128,
    use_cache = True, temperature = 1.5, min_p = 0.1
)
```

    The Eiffel Tower is a tall tower located in the capital of France, Paris. It stands at a height of 324 meters (1,063 feet) and was completed in 1889. The tower was designed by Gustave Eiffel and his team for the 1889 Exposition Universelle (World's Fair) to celebrate the 100th anniversary of the French Revolution. It is made of wrought iron and consists of three levels that are accessible to visitors. The Eiffel Tower is one of the most recognizable landmarks in the world and attracts millions of tourists each year.<|im_end|>


You can also use Hugging Face's `AutoModelForPeftCausalLM`. Only use this if you do not have `unsloth` installed. It can be hopelessly slow, since `4bit` model downloading is not supported, and Unsloth's **inference is 2x faster**.


```python
if False:
    # I highly do NOT suggest - use Unsloth if possible
    from peft import AutoPeftModelForCausalLM
    from transformers import AutoTokenizer

    model = AutoPeftModelForCausalLM.from_pretrained(
        "lora_model",  # YOUR MODEL YOU USED FOR TRAINING
        load_in_4bit=load_in_4bit,
    )
    tokenizer = AutoTokenizer.from_pretrained("lora_model")
```

### Saving to float16 for VLLM

We also support saving to `float16` directly. Select `merged_16bit` for float16 or `merged_4bit` for int4. We also allow `lora` adapters as a fallback. Use `push_to_hub_merged` to upload to your Hugging Face account! You can go to https://huggingface.co/settings/tokens for your personal tokens.


```python
from google.colab import userdata
# Merge to 16bit
if False: model.save_pretrained_merged("model", tokenizer, save_method = "merged_16bit",)
if False: model.push_to_hub_merged("hf/model", tokenizer, save_method = "merged_16bit", token = "")

# Merge to 4bit
if False: model.save_pretrained_merged("model", tokenizer, save_method = "merged_4bit",)
if False: model.push_to_hub_merged("hf/model", tokenizer, save_method = "merged_4bit", token = "")

# Just LoRA adapters
if False:
    model.save_pretrained("model")
    tokenizer.save_pretrained("model")
if False:
    model.push_to_hub("hf/model", token = "")
    tokenizer.push_to_hub("hf/model", token = "")

```

### GGUF / llama.cpp Conversion
To save to `GGUF` / `llama.cpp`, we support it natively now! We clone `llama.cpp` and we default save it to `q8_0`. We allow all methods like `q4_k_m`. Use `save_pretrained_gguf` for local saving and `push_to_hub_gguf` for uploading to HF.

Some supported quant methods (full list in our [Docs](https://docs.unsloth.ai/basics/saving-and-using-models/saving-to-gguf)):
* `q8_0` - Fast conversion. High resource use, but generally acceptable.
* `q4_k_m` - Recommended. Uses Q6_K for half of the attention.wv and feed_forward.w2 tensors, else Q4_K.
* `q5_k_m` - Recommended. Uses Q6_K for half of the attention.wv and feed_forward.w2 tensors, else Q5_K.

[**NEW**] To finetune and auto export to Ollama, try our [Ollama notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3_(8B)-Ollama.ipynb)


```python
# Save to 8bit Q8_0
if False: model.save_pretrained_gguf("model", tokenizer,)
# Remember to go to https://huggingface.co/settings/tokens for a token!
# And change hf to your username!
if False: model.push_to_hub_gguf("hf/model", tokenizer, quantization_method = "q4_k_m", token = "")

# Save to 16bit GGUF
if False: model.save_pretrained_gguf("model", tokenizer, quantization_method = "f16")
if False: model.push_to_hub_gguf("hf/model", tokenizer, quantization_method = "f16", token = "")

# Save to q4_k_m GGUF
if False: model.save_pretrained_gguf("model", tokenizer, quantization_method = "q4_k_m")
if False: model.push_to_hub_gguf("hf/model", tokenizer, quantization_method = "q4_k_m", token = "")

# Save to multiple GGUF options - much faster if you want multiple!
if False:
    model.push_to_hub_gguf(
        "hf/model", # Change hf to your username!
        tokenizer,
        quantization_method = ["q4_k_m", "q8_0", "q5_k_m",],
        token = "", # Get a token at https://huggingface.co/settings/tokens
    )
```

Now, use the `model-unsloth.gguf` file or `model-unsloth-Q4_K_M.gguf` file in llama.cpp or a UI based system like Jan or Open WebUI. You can install Jan [here](https://github.com/janhq/jan) and Open WebUI [here](https://github.com/open-webui/open-webui)

And we're done! If you have any questions on Unsloth, we have a [Discord](https://discord.gg/unsloth) channel! If you find any bugs or want to keep updated with the latest LLM stuff, or need help, join projects etc, feel free to join our Discord!

Some other links:
1. Train your own reasoning model - Llama GRPO notebook [Free Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.1_(8B)-GRPO.ipynb)
2. Saving finetunes to Ollama. [Free notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3_(8B)-Ollama.ipynb)
3. Llama 3.2 Vision finetuning - Radiography use case. [Free Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.2_(11B)-Vision.ipynb)
6. See notebooks for DPO, ORPO, Continued pretraining, conversational finetuning and more on our [documentation](https://docs.unsloth.ai/get-started/unsloth-notebooks)!

<div class="align-center">
  <a href="https://unsloth.ai"><img src="https://github.com/unslothai/unsloth/raw/main/images/unsloth%20new%20logo.png" width="115"></a>
  <a href="https://discord.gg/unsloth"><img src="https://github.com/unslothai/unsloth/raw/main/images/Discord.png" width="145"></a>
  <a href="https://docs.unsloth.ai/"><img src="https://github.com/unslothai/unsloth/blob/main/images/documentation%20green%20button.png?raw=true" width="125"></a>

  Join Discord if you need help + ⭐️ <i>Star us on <a href="https://github.com/unslothai/unsloth">Github</a> </i> ⭐️
</div>


---
description: >-
  Learn to run & fine-tune Phi-4 reasoning models locally with Unsloth + our
  Dynamic 2.0 quants
---

# Phi-4 Reasoning: How to Run & Fine-tune

Microsoft's new Phi-4 reasoning models are now supported in Unsloth. The 'plus' variant performs on par with OpenAI's o1-mini, o3-mini and Sonnet 3.7. The 'plus' and standard reasoning models are 14B parameters while the 'mini' has 4B parameters.\
\
All Phi-4 reasoning uploads use our [Unsloth Dynamic 2.0](../unsloth-dynamic-2.0-ggufs) methodology.

#### **Phi-4 reasoning - Unsloth Dynamic 2.0 uploads:**

| Dynamic 2.0 GGUF (to run)                                                                                                                                                                                                                                                                                                      | Dynamic 4-bit Safetensor (to finetune/deploy)                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li><a href="https://huggingface.co/unsloth/Phi-4-reasoning-plus-GGUF/">Reasoning-plus</a> (14B)</li></ul><ul><li><a href="https://huggingface.co/unsloth/Phi-4-reasoning-GGUF">Reasoning</a> (14B)</li></ul><ul><li><a href="https://huggingface.co/unsloth/Phi-4-mini-reasoning-GGUF/">Mini-reasoning</a> (4B)</li></ul> | <ul><li><a href="https://huggingface.co/unsloth/Phi-4-reasoning-plus-unsloth-bnb-4bit">Reasoning-plus</a></li></ul><ul><li><a href="https://huggingface.co/unsloth/phi-4-reasoning-unsloth-bnb-4bit">Reasoning</a></li></ul><ul><li><a href="https://huggingface.co/unsloth/Phi-4-mini-reasoning-unsloth-bnb-4bit">Mini-reasoning</a></li></ul> |

## 🖥️ **Running Phi-4 reasoning**

### :gear: Official Recommended Settings

According to Microsoft, these are the recommended settings for inference:

* <mark style="background-color:blue;">**Temperature = 0.8**</mark>
* Top\_P = 0.95

### **Phi-4 reasoning Chat templates**

Please ensure you use the correct chat template as the 'mini' variant has a different one.

#### **Phi-4-mini:**

{% code overflow="wrap" %}
```
<|system|>Your name is Phi, an AI math expert developed by Microsoft.<|end|><|user|>How to solve 3*x^2+4*x+5=1?<|end|><|assistant|>
```
{% endcode %}

#### **Phi-4-reasoning and Phi-4-reasoning-plus:**

This format is used for general conversation and instructions:

{% code overflow="wrap" %}
```
<|im_start|>system<|im_sep|>You are Phi, a language model trained by Microsoft to help users. Your role as an assistant involves thoroughly exploring questions through a systematic thinking process before providing the final precise and accurate solutions. This requires engaging in a comprehensive cycle of analysis, summarizing, exploration, reassessment, reflection, backtracing, and iteration to develop well-considered thinking process. Please structure your response into two main sections: Thought and Solution using the specified format: <think> {Thought section} </think> {Solution section}. In the Thought section, detail your reasoning process in steps. Each step should include detailed considerations such as analysing questions, summarizing relevant findings, brainstorming new ideas, verifying the accuracy of the current steps, refining any errors, and revisiting previous steps. In the Solution section, based on various attempts, explorations, and reflections from the Thought section, systematically present the final solution that you deem correct. The Solution section should be logical, accurate, and concise and detail necessary steps needed to reach the conclusion. Now, try to solve the following question through the above guidelines:<|im_end|><|im_start|>user<|im_sep|>What is 1+1?<|im_end|><|im_start|>assistant<|im_sep|>
```
{% endcode %}

{% hint style="info" %}
Yes, the chat template/prompt format is this long!
{% endhint %}

### 🦙 Ollama: Run Phi-4 reasoning Tutorial

1. Install `ollama` if you haven't already!

```bash
apt-get update
apt-get install pciutils -y
curl -fsSL https://ollama.com/install.sh | sh
```

2. Run the model! Note you can call `ollama serve`in another terminal if it fails. We include all our fixes and suggested parameters (temperature etc) in `params` in our Hugging Face upload.

```bash
ollama run hf.co/unsloth/Phi-4-mini-reasoning-GGUF:Q4_K_XL
```

### 📖 Llama.cpp: Run Phi-4 reasoning Tutorial

{% hint style="warning" %}
You must use `--jinja` in llama.cpp to enable reasoning for the models, expect for the 'mini' variant. Otherwise no token will be provided.
{% endhint %}

1. Obtain the latest `llama.cpp` on [GitHub here](https://github.com/ggml-org/llama.cpp). You can follow the build instructions below as well. Change `-DGGML_CUDA=ON` to `-DGGML_CUDA=OFF` if you don't have a GPU or just want CPU inference.

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

2. Download the model via (after installing `pip install huggingface_hub hf_transfer` ). You can choose Q4\_K\_M, or other quantized versions.

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/Phi-4-mini-reasoning-GGUF",
    local_dir = "unsloth/Phi-4-mini-reasoning-GGUF",
    allow_patterns = ["*UD-Q4_K_XL*"],
)
```

3. Run the model in conversational mode in llama.cpp. You must use `--jinja` in llama.cpp to enable reasoning for the models. This is however not needed if you're using the 'mini' variant.&#x20;

```
./llama.cpp/llama-cli \
    --model unsloth/Phi-4-mini-reasoning-GGUF/Phi-4-mini-reasoning-UD-Q4_K_XL.gguf \
    --threads -1 \
    --n-gpu-layers 99 \
    --prio 3 \
    --temp 0.8 \
    --top-p 0.95 \
    --jinja \
    --min_p 0.00 \
    --ctx-size 32768 \
    --seed 3407
```

## 🦥 Fine-tuning Phi-4 with Unsloth

[Phi-4 fine-tuning](https://unsloth.ai/blog/phi4) for the models are also now supported in Unsloth. To fine-tune for free on Google Colab, just change the `model_name` of 'unsloth/Phi-4' to 'unsloth/Phi-4-mini-reasoning' etc.

* [Phi-4 (14B) fine-tuning notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Phi_4-Conversational.ipynb)



```python

```
