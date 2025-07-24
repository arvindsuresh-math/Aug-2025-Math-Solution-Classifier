# Hugging Face Model Page: <https://huggingface.co/microsoft/Phi-4-mini-instruct>

**Scraped on:** 2025-07-22 17:40:52

---

## Model Summary

Phi-4-mini-instruct is a lightweight open model built upon synthetic data and filtered publicly available websites - with a focus on high-quality, reasoning dense data. The model belongs to the Phi-4 model family and supports 128K token context length. The model underwent an enhancement process, incorporating both supervised fine-tuning and direct preference optimization to support precise instruction adherence and robust safety measures.

## Intended Uses

### Primary Use Cases

The model is intended for broad multilingual commercial and research use. The model provides uses for general purpose AI systems and applications which require:

  1. Memory/compute constrained environments
  2. Latency bound scenarios
  3. Strong reasoning (especially math and logic).

The model is designed to accelerate research on language and multimodal models, for use as a building block for generative AI powered features.

## Usage

### Tokenizer

Phi-4-mini-instruct supports a vocabulary size of up to `200064` tokens. The [tokenizer files](https://huggingface.co/microsoft/Phi-4-mini-instruct/blob/main/added_tokens.json) already provide placeholder tokens that can be used for downstream fine-tuning, but they can also be extended up to the model's vocabulary size.

### Input Formats

Given the nature of the training data, the Phi-4-mini-instruct model is best suited for prompts using specific formats. Below are the two primary formats:

#### Chat format

This format is used for general conversation and instructions:

    <|system|>Insert System Message<|end|><|user|>Insert User Message<|end|><|assistant|>
    

### Inference with Transformers

#### Example

After obtaining the Phi-4-mini-instruct model checkpoints, users can use this sample code for inference.

```python
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
     
    torch.random.manual_seed(0)
    
    model_path = "microsoft/Phi-4-mini-instruct"
    
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        device_map="auto",
        torch_dtype="auto",
        trust_remote_code=True,
    )
    tokenizer = AutoTokenizer.from_pretrained(model_path)
     
    messages = [
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": "Can you provide ways to eat combinations of bananas and dragonfruits?"},
        {"role": "assistant", "content": "Sure! Here are some ways to eat bananas and dragonfruits together: 1. Banana and dragonfruit smoothie: Blend bananas and dragonfruits together with some milk and honey. 2. Banana and dragonfruit salad: Mix sliced bananas and dragonfruits together with some lemon juice and honey."},
        {"role": "user", "content": "What about solving an 2x + 3 = 7 equation?"},
    ]
     
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
    )
     
    generation_args = {
        "max_new_tokens": 500,
        "return_full_text": False,
        "temperature": 0.0,
        "do_sample": False,
    }
     
    output = pipe(messages, **generation_args)
    print(output[0]['generated_text'])
```
