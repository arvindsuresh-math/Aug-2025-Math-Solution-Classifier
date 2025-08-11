# Hugging Face Model Page: <https://huggingface.co/docs/trl/en/sft_trainer>

## Quickstart

If you have a dataset hosted on the 🤗 Hub, you can easily fine-tune your SFT model using [SFTTrainer](/docs/trl/v0.19.1/en/sft_trainer#trl.SFTTrainer) from TRL. Let us assume your dataset is `imdb`, the text you want to predict is inside the `text` field of the dataset, and you want to fine-tune the `facebook/opt-350m` model. The following code-snippet takes care of all the data pre-processing and training for you:

```python
    from datasets import load_dataset
    from trl import SFTConfig, SFTTrainer
    
    dataset = load_dataset("stanfordnlp/imdb", split="train")
    
    training_args = SFTConfig(
        max_length=512,
        output_dir="/tmp",
    )
    trainer = SFTTrainer(
        "facebook/opt-350m",
        train_dataset=dataset,
        args=training_args,
    )
    trainer.train()
```

Make sure to pass the correct value for `max_length` as the default value will be set to `min(tokenizer.model_max_length, 1024)`.

You can also construct a model outside of the trainer and pass it as follows:

```python
    from transformers import AutoModelForCausalLM
    from datasets import load_dataset
    from trl import SFTConfig, SFTTrainer
    
    dataset = load_dataset("stanfordnlp/imdb", split="train")
    
    model = AutoModelForCausalLM.from_pretrained("facebook/opt-350m")
    
    training_args = SFTConfig(output_dir="/tmp")
    
    trainer = SFTTrainer(
        model,
        train_dataset=dataset,
        args=training_args,
    )
    
    trainer.train()
```

The above snippets will use the default training arguments from the [SFTConfig](/docs/trl/v0.19.1/en/sft_trainer#trl.SFTConfig) class. If you want to modify the defaults, pass in your modification to the `SFTConfig` constructor and pass it to the trainer via the `args` argument.

## Advanced usage

### Train on assistant messages only

To train on assistant messages only, use a [conversational](dataset_formats#conversational) [language modeling](dataset_formats#language_modeling) dataset and set `assistant_only_loss=True` in the [SFTConfig](/docs/trl/v0.19.1/en/sft_trainer#trl.SFTConfig). This setting ensures that loss is computed **only** on the assistant responses, ignoring user and system and user messages.

### Train on completions only

To train on completions only, simply use a [prompt-completion](dataset_formats#prompt-completion) dataset. In this mode, loss is computed solely on the completion part.

If you’d like to compute loss on both the prompt **and** the completion while still using a prompt-completion dataset, set `completion_only_loss=False` in the [SFTConfig](/docs/trl/v0.19.1/en/sft_trainer#trl.SFTConfig). This is equivalent to [converting the dataset to a language modeling](dataset_formats#from-prompt-completion-to-language-modeling-dataset) format.

### Add Special Tokens for Chat Format

Adding special tokens to a language model is crucial for training chat models. These tokens are added between the different roles in a conversation, such as the user, assistant, and system, and help the model recognize the structure and flow of a conversation. This setup is essential for enabling the model to generate coherent and contextually appropriate responses in a chat environment. The [clone_chat_template()](/docs/trl/v0.19.1/en/model_utils#trl.clone_chat_template) function is a useful utility to prepare a model and tokenizer for conversational AI tasks. This function:

* Adds special tokens to the tokenizer, e.g., `<|im_start|>` and `<|im_end|>`, to indicate the start and end of a conversation.
* Resizes the model’s embedding layer to accommodate the new tokens.
* Sets the `chat_template` of the tokenizer, which is used to format the input data into a chat-like format.
* _optionally_ you can pass `resize_to_multiple_of` to resize the embedding layer to a multiple of the `resize_to_multiple_of` argument, e.g., `64`. If you want to see more formats being supported in the future, please open a GitHub issue on [trl](https://github.com/huggingface/trl)

```python
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from trl import clone_chat_template
    
    # Load model and tokenizer
    model = AutoModelForCausalLM.from_pretrained("facebook/opt-350m")
    tokenizer = AutoTokenizer.from_pretrained("facebook/opt-350m")
    
    # Set up the chat format
    model, tokenizer = clone_chat_template(model, tokenizer, "Qwen/Qwen3-0.6B")
```

With our model and tokenizer set up, we can now fine-tune our model on a conversational dataset. Below is an example of how a dataset can be formatted for fine-tuning.

### Dataset format support

The [SFTTrainer](/docs/trl/v0.19.1/en/sft_trainer#trl.SFTTrainer) supports popular dataset formats. This allows you to pass the dataset to the trainer without any pre-processing directly. The following formats are supported:

* conversational format

    {"messages": [{"role": "system", "content": "You are helpful"}, {"role": "user", "content": "What's the capital of France?"}, {"role": "assistant", "content": "..."}]}
    {"messages": [{"role": "system", "content": "You are helpful"}, {"role": "user", "content": "Who wrote 'Romeo and Juliet'?"}, {"role": "assistant", "content": "..."}]}
    {"messages": [{"role": "system", "content": "You are helpful"}, {"role": "user", "content": "How far is the Moon from Earth?"}, {"role": "assistant", "content": "..."}]}

* instruction format

    {"prompt": "<prompt text>", "completion": "<ideal generated text>"}
    {"prompt": "<prompt text>", "completion": "<ideal generated text>"}
    {"prompt": "<prompt text>", "completion": "<ideal generated text>"}

If your dataset uses one of the above formats, you can directly pass it to the trainer without pre-processing. The [SFTTrainer](/docs/trl/v0.19.1/en/sft_trainer#trl.SFTTrainer) will then format the dataset for you using the defined format from the model’s tokenizer with the [apply_chat_template](https://huggingface.co/docs/transformers/main/en/chat_templating#templates-for-chat-models) method.

```python
    from datasets import load_dataset
    from trl import SFTConfig, SFTTrainer
    
    ...
    
    # load jsonl dataset
    dataset = load_dataset("json", data_files="path/to/dataset.jsonl", split="train")
    # load dataset from the HuggingFace Hub
    dataset = load_dataset("philschmid/dolly-15k-oai-style", split="train")
    
    ...
    
    training_args = SFTConfig(packing=True)
    trainer = SFTTrainer(
        "facebook/opt-350m",
        args=training_args,
        train_dataset=dataset,
    )
```

If the dataset is not in one of those formats, you can either preprocess the dataset to match the formatting or pass a formatting function to the SFTTrainer to do it for you. Let’s have a look.

### Format your input prompts

For instruction fine-tuning, it is quite common to have two columns inside the dataset: one for the prompt & the other for the response. This allows people to format examples like [Stanford-Alpaca](https://github.com/tatsu-lab/stanford_alpaca) did as follows:

    Below is an instruction ...
    
    ### Instruction
    {prompt}
    
    ### Response:
    {completion}

Let us assume your dataset has two fields, `question` and `answer`. Therefore you can just run:

```python
    ...
    def formatting_prompts_func(example):
        return f"### Question: {example['question']}\n ### Answer: {example['answer']}"
    
    
    trainer = SFTTrainer(
        model,
        args=training_args,
        train_dataset=dataset,
        formatting_func=formatting_prompt_func,
    )
    
    trainer.train()
```

To properly format your input, make sure to process all the examples by looping over them and returning a list of processed text. Check out a full example of how to use SFTTrainer on the alpaca dataset [here](https://github.com/huggingface/trl/pull/444#issue-1760952763)

## Tool Calling with SFT

The SFT trainer fully supports fine-tuning models with _tool calling_ capabilities. In this case, each dataset example should include:

* The conversation messages, including any tool calls (`tool_calls`) and tool responses (`tool` role messages)
* The list of available tools in the `tools` column, typically provided as JSON schemas

For details on the expected dataset structure, see the [Dataset Format — Tool Calling](dataset_formats#tool-calling) section.

### Packing dataset

[SFTTrainer](/docs/trl/v0.19.1/en/sft_trainer#trl.SFTTrainer) supports _example packing_ , where multiple short examples are packed in the same input sequence to increase training efficiency. To enable the usage of this dataset class, simply pass `packing=True` to the [SFTConfig](/docs/trl/v0.19.1/en/sft_trainer#trl.SFTConfig) constructor.

```python
    ...
    training_args = SFTConfig(packing=True)
    
    trainer = SFTTrainer(
        "facebook/opt-350m",
        train_dataset=dataset,
        args=training_args
    )
    
    trainer.train()
```

Note that if you use a packed dataset and if you pass `max_steps` in the training arguments, you will probably train your models for more than a few epochs, depending on the way you have configured the packed dataset and the training protocol. Double-check that you know and understand what you are doing. If you don’t want to pack your `eval_dataset`, you can pass `eval_packing=False` to the `SFTConfig` init method.

#### Customize your prompts using packed dataset

If your dataset has several fields that you want to combine, for example, if the dataset has `question` and `answer` fields and you want to combine them, you can pass a formatting function to the trainer that will take care of that. For example:

```python
    def formatting_func(example):
        text = f"### Question: {example['question']}\n ### Answer: {example['answer']}"
        return text
    
    training_args = SFTConfig(packing=True)
    trainer = SFTTrainer(
        "facebook/opt-350m",
        train_dataset=dataset,
        args=training_args,
        formatting_func=formatting_func
    )
    
    trainer.train()
```

### Control over the pretrained model

You can directly pass the kwargs of the `from_pretrained()` method to the [SFTConfig](/docs/trl/v0.19.1/en/sft_trainer#trl.SFTConfig). For example, if you want to load a model in a different precision, analogous to

```python
    model = AutoModelForCausalLM.from_pretrained("facebook/opt-350m", torch_dtype=torch.bfloat16)
    
    ...
    
    training_args = SFTConfig(
        model_init_kwargs={
            "torch_dtype": "bfloat16",
        },
        output_dir="/tmp",
    )
    trainer = SFTTrainer(
        "facebook/opt-350m",
        train_dataset=dataset,
        args=training_args,
    )
    
    trainer.train()
```

Note that all keyword arguments of `from_pretrained()` are supported.

### Training adapters

We also support tight integration with 🤗 PEFT library so that any user can conveniently train adapters and share them on the Hub instead of training the entire model.

```python
    from datasets import load_dataset
    from trl import SFTConfig, SFTTrainer
    from peft import LoraConfig
    
    dataset = load_dataset("trl-lib/Capybara", split="train")
    
    peft_config = LoraConfig(
        r=16,
        lora_alpha=32,
        lora_dropout=0.05,
        target_modules="all-linear",
        modules_to_save=["lm_head", "embed_token"],
        task_type="CAUSAL_LM",
    )
    
    trainer = SFTTrainer(
        "Qwen/Qwen2.5-0.5B",
        train_dataset=dataset,
        args=SFTConfig(output_dir="Qwen2.5-0.5B-SFT"),
        peft_config=peft_config
    )
    
    trainer.train()
```

You can also continue training your `PeftModel`. For that, first load a `PeftModel` outside `SFTTrainer` and pass it directly to the trainer without the `peft_config` argument being passed.

### Training adapters with base 8 bit models

For that, you need to first load your 8 bit model outside the Trainer and pass a `PeftConfig` to the trainer. For example:

```python
    ...
    
    peft_config = LoraConfig(
        r=16,
        lora_alpha=32,
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )
    
    model = AutoModelForCausalLM.from_pretrained(
        "EleutherAI/gpt-neo-125m",
        load_in_8bit=True,
        device_map="auto",
    )
    
    trainer = SFTTrainer(
        model,
        train_dataset=dataset,
        args=SFTConfig(),
        peft_config=peft_config,
    )
    
    trainer.train()
```

### Using the model creation utility

We included a utility function to create your model.

Parameters

* **model_name_or_path** (`str` or `None`, _optional_ , defaults to `None`) — Model checkpoint for weights initialization.
* **model_revision** (`str`, _optional_ , defaults to `"main"`) — Specific model version to use. It can be a branch name, a tag name, or a commit id.
* **torch_dtype** (`Literal["auto", "bfloat16", "float16", "float32"]` or `None`, _optional_ , defaults to `None`) — Override the default `torch.dtype` and load the model under this dtype. Possible values are
  * `"bfloat16"`: `torch.bfloat16`
  * `"float16"`: `torch.float16`
  * `"float32"`: `torch.float32`
  * `"auto"`: Automatically derive the dtype from the model’s weights.
* **trust_remote_code** (`bool`, _optional_ , defaults to `False`) — Whether to allow for custom models defined on the Hub in their own modeling files. This option should only be set to `True` for repositories you trust and in which you have read the code, as it will execute code present on the Hub on your local machine.
* **attn_implementation** (`str` or `None`, _optional_ , defaults to `None`) — Which attention implementation to use. You can run `--attn_implementation=flash_attention_2`, in which case you must install this manually by running `pip install flash-attn --no-build-isolation`.
* **use_peft** (`bool`, _optional_ , defaults to `False`) — Whether to use PEFT for training.
* **lora_r** (`int`, _optional_ , defaults to `16`) — LoRA R value.
* **lora_alpha** (`int`, _optional_ , defaults to `32`) — LoRA alpha.
* **lora_dropout** (`float`, _optional_ , defaults to `0.05`) — LoRA dropout.
* **lora_target_modules** (`Union[str, list[str]]` or `None`, _optional_ , defaults to `None`) — LoRA target modules.
* **lora_modules_to_save** (`list[str]` or `None`, _optional_ , defaults to `None`) — Model layers to unfreeze & train.
* **lora_task_type** (`str`, _optional_ , defaults to `"CAUSAL_LM"`) — Task type to pass for LoRA (use `"SEQ_CLS"` for reward modeling).
* **use_rslora** (`bool`, _optional_ , defaults to `False`) — Whether to use Rank-Stabilized LoRA, which sets the adapter scaling factor to `lora_alpha/√r`, instead of the original default value of `lora_alpha/r`.
* **use_dora** (`bool`, _optional_ , defaults to `False`) — Enable [Weight-Decomposed Low-Rank Adaptation (DoRA)](https://huggingface.co/papers/2402.09353). This technique decomposes the updates of the weights into two parts, magnitude and direction. Direction is handled by normal LoRA, whereas the magnitude is handled by a separate learnable parameter. This can improve the performance of LoRA, especially at low ranks. Right now, DoRA only supports linear and Conv2D layers. DoRA introduces a bigger overhead than pure LoRA, so it is recommended to merge weights for inference.
* **load_in_8bit** (`bool`, _optional_ , defaults to `False`) — Whether to use 8 bit precision for the base model. Works only with LoRA.
* **load_in_4bit** (`bool`, _optional_ , defaults to `False`) — Whether to use 4 bit precision for the base model. Works only with LoRA.
* **bnb_4bit_quant_type** (`str`, _optional_ , defaults to `"nf4"`) — Quantization type (`"fp4"` or `"nf4"`).
* **use_bnb_nested_quant** (`bool`, _optional_ , defaults to `False`) — Whether to use nested quantization.

Configuration class for the models.

Using [HfArgumentParser](https://huggingface.co/docs/transformers/v4.53.1/en/internal/trainer_utils#transformers.HfArgumentParser) we can turn this class into [argparse](https://docs.python.org/3/library/argparse#module-argparse) arguments that can be specified on the command line.

```python
    from trl import ModelConfig, SFTTrainer, get_kbit_device_map, get_peft_config, get_quantization_config
    model_args = ModelConfig(
        model_name_or_path="facebook/opt-350m"
        attn_implementation=None, # or "flash_attention_2"
    )
    torch_dtype = (
        model_args.torch_dtype
        if model_args.torch_dtype in ["auto", None]
        else getattr(torch, model_args.torch_dtype)
    )
    quantization_config = get_quantization_config(model_args)
    model_kwargs = dict(
        revision=model_args.model_revision,
        trust_remote_code=model_args.trust_remote_code,
        attn_implementation=model_args.attn_implementation,
        torch_dtype=torch_dtype,
        use_cache=False if training_args.gradient_checkpointing else True,
        device_map=get_kbit_device_map() if quantization_config is not None else None,
        quantization_config=quantization_config,
    )
    model = AutoModelForCausalLM.from_pretrained(model_args.model_name_or_path, **model_kwargs)
    trainer = SFTTrainer(
        ...,
        model=model_args.model_name_or_path,
        peft_config=get_peft_config(model_args),
    )
```

## Best practices

Pay attention to the following best practices when training a model with that trainer:

* [SFTTrainer](/docs/trl/v0.19.1/en/sft_trainer#trl.SFTTrainer) always truncates by default the sequences to the `max_length` argument of the [SFTConfig](/docs/trl/v0.19.1/en/sft_trainer#trl.SFTConfig). If none is passed, the trainer will retrieve that value from the tokenizer. Some tokenizers do not provide a default value, so there is a check to retrieve the minimum between 1024 and that value. Make sure to check it before training.
* For training adapters in 8bit, you might need to tweak the arguments of the `prepare_model_for_kbit_training` method from PEFT, hence we advise users to use `prepare_in_int8_kwargs` field, or create the `PeftModel` outside the [SFTTrainer](/docs/trl/v0.19.1/en/sft_trainer#trl.SFTTrainer) and pass it.
* For a more memory-efficient training using adapters, you can load the base model in 8bit, for that simply add `load_in_8bit` argument when creating the [SFTTrainer](/docs/trl/v0.19.1/en/sft_trainer#trl.SFTTrainer), or create a base model in 8bit outside the trainer and pass it.
* If you create a model outside the trainer, make sure not to pass to the trainer any additional keyword arguments that are relative to `from_pretrained()` method.

## GPTQ Conversion

You may experience some issues with GPTQ Quantization after completing training. Lowering `gradient_accumulation_steps` to `4` will resolve most issues during the quantization process to GPTQ format.

## SFTTrainer

Parameters

* **model** (`Union[str, PreTrainedModel]`) — Model to be trained. Can be either:
  * A string, being the _model id_ of a pretrained model hosted inside a model repo on huggingface.co, or a path to a _directory_ containing model weights saved using [save_pretrained](https://huggingface.co/docs/transformers/v4.53.1/en/main_classes/model#transformers.PreTrainedModel.save_pretrained), e.g., `'./my_model_directory/'`. The model is loaded using [from_pretrained](https://huggingface.co/docs/transformers/v4.53.1/en/model_doc/auto#transformers.AutoModelForCausalLM.from_pretrained) with the keyword arguments in `args.model_init_kwargs`.
  * A [PreTrainedModel](https://huggingface.co/docs/transformers/v4.53.1/en/main_classes/model#transformers.PreTrainedModel) object. Only causal language models are supported.
* **args** ([SFTConfig](/docs/trl/v0.19.1/en/sft_trainer#trl.SFTConfig), _optional_ , defaults to `None`) — Configuration for this trainer. If `None`, a default configuration is used.
* **data_collator** (`DataCollator`, _optional_) — Function to use to form a batch from a list of elements of the processed `train_dataset` or `eval_dataset`. Will default to a custom `DataCollatorForLanguageModeling`.
* **train_dataset** ([Dataset](https://huggingface.co/docs/datasets/v3.6.0/en/package_reference/main_classes#datasets.Dataset) or [IterableDataset](https://huggingface.co/docs/datasets/v3.6.0/en/package_reference/main_classes#datasets.IterableDataset)) — Dataset to use for training. SFT supports both language modeling type and prompt-completion type. The format of the samples can be either:
  * [Standard](dataset_formats#standard): Each sample contains plain text.
  * [Conversational](dataset_formats#conversational): Each sample contains structured messages (e.g., role and content).

The trainer also supports processed datasets (tokenized) as long as they contain an `input_ids` field.

* **eval_dataset** ([Dataset](https://huggingface.co/docs/datasets/v3.6.0/en/package_reference/main_classes#datasets.Dataset), [IterableDataset](https://huggingface.co/docs/datasets/v3.6.0/en/package_reference/main_classes#datasets.IterableDataset) or `dict[str, Union[Dataset, IterableDataset]]`) — Dataset to use for evaluation. It must meet the same requirements as `train_dataset`.
* **processing_class** ([PreTrainedTokenizerBase](https://huggingface.co/docs/transformers/v4.53.1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase), _optional_ , defaults to `None`) — Processing class used to process the data. If `None`, the processing class is loaded from the model’s name with [from_pretrained](https://huggingface.co/docs/transformers/v4.53.1/en/model_doc/auto#transformers.AutoTokenizer.from_pretrained).
* **callbacks** (list of [TrainerCallback](https://huggingface.co/docs/transformers/v4.53.1/en/main_classes/callback#transformers.TrainerCallback), _optional_ , defaults to `None`) — List of callbacks to customize the training loop. Will add those to the list of default callbacks detailed in [here](https://huggingface.co/docs/transformers/main_classes/callback).

If you want to remove one of the default callbacks used, use the [remove_callback](https://huggingface.co/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer.remove_callback) method.

* **optimizers** (`tuple[torch.optim.Optimizer, torch.optim.lr_scheduler.LambdaLR]`, _optional_ , defaults to `(None, None)`) — A tuple containing the optimizer and the scheduler to use. Will default to an instance of `AdamW` on your model and a scheduler given by `get_linear_schedule_with_warmup` controlled by `args`.
* **optimizer_cls_and_kwargs** (`Tuple[Type[torch.optim.Optimizer], Dict[str, Any]]`, _optional_ , defaults to `None`) — A tuple containing the optimizer class and keyword arguments to use. Overrides `optim` and `optim_args` in `args`. Incompatible with the `optimizers` argument.

Unlike `optimizers`, this argument avoids the need to place model parameters on the correct devices before initializing the Trainer.

* **preprocess_logits_for_metrics** (`Callable[[torch.Tensor, torch.Tensor], torch.Tensor]`, _optional_ , defaults to `None`) — A function that preprocess the logits right before caching them at each evaluation step. Must take two tensors, the logits and the labels, and return the logits once processed as desired. The modifications made by this function will be reflected in the predictions received by `compute_metrics`.

Note that the labels (second parameter) will be `None` if the dataset does not have them.

* **peft_config** (`~peft.PeftConfig`, _optional_ , defaults to `None`) — PEFT configuration used to wrap the model. If `None`, the model is not wrapped.
* **formatting_func** (`Optional[Callable]`) — Formatting function applied to the dataset before tokenization. Applying the formatting function explicitly converts the dataset into a language modeling type.

Trainer for Supervised Fine-Tuning (SFT) method.

This class is a wrapper around the [transformers.Trainer](https://huggingface.co/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer) class and inherits all of its attributes and methods.

Example:

```python
    from datasets import load_dataset
    from trl import SFTTrainer
    
    dataset = load_dataset("roneneldan/TinyStories", split="train[:1%]")
    
    trainer = SFTTrainer(model="Qwen/Qwen2-0.5B-Instruct", train_dataset=dataset)
    trainer.train()
```

Compute training loss and additionally compute token accuracies

Parameters

* **model_name** (`str` or `None`, _optional_ , defaults to `None`) — Name of the model.
* **dataset_name** (`str` or `None`, _optional_ , defaults to `None`) — Name of the dataset used for training.
* **tags** (`str`, `list[str]` or `None`, _optional_ , defaults to `None`) — Tags to be associated with the model card.

Creates a draft of a model card using the information available to the `Trainer`.

## SFTConfig

Parameters that control the model

* **model_init_kwargs** (`dict[str, Any]` or `None`, _optional_ , defaults to `None`) — Keyword arguments for [from_pretrained](https://huggingface.co/docs/transformers/v4.53.1/en/model_doc/auto#transformers.AutoModelForCausalLM.from_pretrained), used when the `model` argument of the [SFTTrainer](/docs/trl/v0.19.1/en/sft_trainer#trl.SFTTrainer) is provided as a string.
* **chat_template_path** (`str` or `None`, _optional_ , defaults to `None`) — If specified, sets the model’s chat template. This can either be the path to a tokenizer (local directory or Hugging Face Hub model) or a direct path to a Jinja template file. When using a Jinja file, you must ensure that any special tokens referenced in the template are added to the tokenizer and that the model’s embedding layer is resized accordingly.

Parameters that control the data preprocessing

* **dataset_text_field** (`str`, _optional_ , defaults to `"text"`) — Name of the column that contains text data in the dataset.
* **dataset_kwargs** (`dict[str, Any]` or `None`, _optional_ , defaults to `None`) — Dictionary of optional keyword arguments for the dataset preparation. The only supported key is `skip_prepare_dataset`.
* **dataset_num_proc** (`int` or `None`, _optional_ , defaults to `None`) — Number of processes to use for processing the dataset.
* **eos_token** (`str` or `None`, _optional_ , defaults to `None`) — Token used to indicate the end of a turn or sequence. If `None`, it defaults to `processing_class.eos_token`.
* **pad_token** (`int` or `None`, _optional_ , defaults to `None`) — Token used for padding. If `None`, it defaults to `processing_class.pad_token`, or if that is also `None`, it falls back to `processing_class.eos_token`.
* **max_length** (`int` or `None`, _optional_ , defaults to `1024`) — Maximum length of the tokenized sequence. Sequences longer than `max_length` are truncated from the right. If `None`, no truncation is applied. When packing is enabled, this value sets the sequence length.
* **packing** (`bool`, _optional_ , defaults to `False`) — Whether to group multiple sequences into fixed-length blocks to improve computational efficiency and reduce padding. Uses `max_length` to define sequence length.
* **packing_strategy** (`str`, _optional_ , defaults to `"ffd"`) — Strategy for packing sequences. Can be either `"ffd"` (first-fit decreasing, default), or `"wrapped"`.
* **padding_free** (`bool`, _optional_ , defaults to `False`) — Whether to perform forward passes without padding by flattening all sequences in the batch into a single continuous sequence. This reduces memory usage by eliminating padding overhead. Currently, this is only supported with the `flash_attention_2` attention implementation, which can efficiently handle the flattened batch structure. When packing is enabled with strategy `"ffd"`, padding-free is enabled, regardless of the value of this parameter.
* **pad_to_multiple_of** (`int` or `None`, _optional_ , defaults to `None`) — If set, the sequences will be padded to a multiple of this value.
* **eval_packing** (`bool` or `None`, _optional_ , defaults to `None`) — Whether to pack the eval dataset. If `None`, uses the same value as `packing`.

Parameters that control the training

* **completion_only_loss** (`bool` or `None`, _optional_ , defaults to `None`) — Whether to compute loss only on the completion part of the sequence. If set to `True`, loss is computed only on the completion, which is supported only for prompt-completion datasets. If `False`, loss is computed on the entire sequence. If `None` (default), the behavior depends on the dataset: loss is computed on the completion for prompt-completion datasets, and on the full sequence for language modeling datasets.
* **assistant_only_loss** (`bool`, _optional_ , defaults to `False`) — Whether to compute loss only on the assistant part of the sequence. If set to `True`, loss is computed only on the assistant responses, which is supported only for conversational datasets. If `False`, loss is computed on the entire sequence.
* **activation_offloading** (`bool`, _optional_ , defaults to `False`) — Whether to offload the activations to the CPU.

Configuration class for the [SFTTrainer](/docs/trl/v0.19.1/en/sft_trainer#trl.SFTTrainer).

This class includes only the parameters that are specific to SFT training. For a full list of training arguments, please refer to the [TrainingArguments](https://huggingface.co/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.TrainingArguments) documentation. Note that default values in this class may differ from those in [TrainingArguments](https://huggingface.co/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.TrainingArguments).

Using [HfArgumentParser](https://huggingface.co/docs/transformers/v4.53.1/en/internal/trainer_utils#transformers.HfArgumentParser) we can turn this class into [argparse](https://docs.python.org/3/library/argparse#module-argparse) arguments that can be specified on the command line.

## Datasets

In the SFTTrainer, we smartly support `datasets.IterableDataset` in addition to other style datasets. This is useful if you are using large corpora that you do not want to save all to disk. The data will be tokenized and processed on the fly, even when packing is enabled.

Additionally, in the SFTTrainer, we support pre-tokenized datasets if they are `datasets.Dataset` or `datasets.IterableDataset`. In other words, if such a dataset has a column of `input_ids`, no further processing (tokenization or packing) will be done, and the dataset will be used as-is. This can be useful if you have pretokenized your dataset outside of this script and want to reuse it directly.

[< > Update on GitHub](https://github.com/huggingface/trl/blob/main/docs/source/sft_trainer.md)
