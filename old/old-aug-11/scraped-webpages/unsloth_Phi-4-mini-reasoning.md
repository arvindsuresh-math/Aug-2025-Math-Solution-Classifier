# Hugging Face Model Page: https://huggingface.co/unsloth/Phi-4-mini-reasoning

**Scraped on:** 2025-07-22 10:39:17

---

##  Model Summary 

Phi-4-mini-reasoning is a lightweight open model built upon synthetic data with a focus on high-quality, reasoning dense data further finetuned for more advanced math reasoning capabilities. The model belongs to the Phi-4 model family and supports 128K token context length. 

##  Intended Uses 

###  Primary Use Cases 

Phi-4-mini-reasoning is designed for multi-step, logic-intensive mathematical problem-solving tasks under memory/compute constrained environments and latency bound scenarios. Some of the use cases include formal proof generation, symbolic computation, advanced word problems, and a wide range of mathematical reasoning scenarios. These models excel at maintaining context across steps, applying structured logic, and delivering accurate, reliable solutions in domains that require deep analytical thinking.

##  Release Notes 

This release of Phi-4-mini-reasoning addresses user feedback and market demand for a compact reasoning model. It is a compact transformer-based language model optimized for mathematical reasoning, built to deliver high-quality, step-by-step problem solving in environments where computing or latency is constrained. The model is fine-tuned with synthetic math data from a more capable model (much larger, smarter, more accurate, and better at following instructions), which has resulted in enhanced reasoning performance. Phi-4-mini-reasoning balances reasoning ability with efficiency, making it potentially suitable for educational applications, embedded tutoring, and lightweight deployment on edge or mobile systems. If a critical issue is identified with Phi-4-mini-reasoning, it should be promptly reported through the MSRC Researcher Portal or [secure@microsoft.com](mailto:secure@microsoft.com)

###  Model Quality 

To understand the capabilities, the 3.8B parameters Phi-4-mini-reasoning model was compared with a set of models over a variety of reasoning benchmarks. A high-level overview of the model quality is as follows:

Model | AIME | MATH-500 | GPQA Diamond  
---|---|---|---  
o1-mini* | 63.6 | 90.0 | 60.0  
DeepSeek-R1-Distill-Qwen-7B | 53.3 | 91.4 | 49.5  
DeepSeek-R1-Distill-Llama-8B | 43.3 | 86.9 | 47.3  
Bespoke-Stratos-7B* | 20.0 | 82.0 | 37.8  
OpenThinker-7B* | 31.3 | 83.0 | 42.4  
Llama-3.2-3B-Instruct | 6.7 | 44.4 | 25.3  
Phi-4-Mini (base model, 3.8B) | 10.0 | 71.8 | 36.9  
**Phi-4-mini-reasoning (3.8B)** | **57.5** | **94.6** | **52.0**  
  
Overall, the model with only 3.8B-param achieves a similar level of multilingual language understanding and reasoning ability as much larger models. However, it is still fundamentally limited by its size for certain tasks. The model simply does not have the capacity to store too much factual knowledge, therefore, users may experience factual incorrectness. However, it may be possible to resolve such weakness by augmenting Phi-4 with a search engine, particularly when using the model under RAG settings.

##  Usage 

###  Tokenizer 

Phi-4-mini-reasoning supports a vocabulary size of up to `200064` tokens. The [tokenizer files](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/added_tokens.json) already provide placeholder tokens that can be used for downstream fine-tuning, but they can also be extended up to the model's vocabulary size.

###  Input Formats 

Given the nature of the training data, the Phi-4-mini-instruct model is best suited for prompts using specific formats. Below are the two primary formats:

####  Chat format 

This format is used for general conversation and instructions:
    
    
    <|system|>Your name is Phi, an AI math expert developed by Microsoft.<|end|><|user|>How to solve 3*x^2+4*x+5=1?<|end|><|assistant|>
    

###  Inference with transformers 

Phi-4-mini-reasoning has been integrated in the `4.51.3` version of `transformers`. The current `transformers` version can be verified with: `pip list | grep transformers`. Python 3.8 and 3.10 will work best. List of required packages:
    
```python
    flash_attn==2.7.4.post1
    torch==2.5.1
    transformers==4.51.3
    accelerate==1.3.0
```

Phi-4-mini-reasoning is also available in [Azure AI Studio](https://aka.ms/phi-4-mini-reasoning/azure)

####  Example 

After obtaining the Phi-4-mini-instruct model checkpoints, users can use this sample code for inference.
    
```python
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
    torch.random.manual_seed(0)
    
    model_id = "microsoft/Phi-4-mini-reasoning"
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        device_map="cuda",
        torch_dtype="auto",
        trust_remote_code=True,
    )
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    
    messages = [{
        "role": "user",
        "content": "How to solve 3*x^2+4*x+5=1?"
    }]   
    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        return_dict=True,
        return_tensors="pt",
    )
    
    outputs = model.generate(
        **inputs.to(model.device),
        max_new_tokens=32768,
        temperature=0.8,
        top_p=0.95,
        do_sample=True,
    )
    outputs = tokenizer.batch_decode(outputs[:, inputs["input_ids"].shape[-1]:])
    
    print(outputs[0])
```   

##  Training 

###  Model 

  * **Architecture:** Phi-4-mini-reasoning shares the same architecture as Phi-4-Mini, which has 3.8B parameters and is a dense decoder-only Transformer model. When compared with Phi-3.5-Mini, the major changes with Phi-4-Mini are 200K vocabulary, grouped-query attention, and shared input and output embedding.  

  * **Inputs:** Text. It is best suited for prompts using the chat format.  

  * **Context length:** 128K tokens  

  * **GPUs:** 128 H100-80G  

  * **Training time:** 2 days  

  * **Training data:** 150B tokens  

  * **Outputs:** Generated text  

  * **Dates:** Trained in February 2024  

  * **Status:** This is a static model trained on offline datasets with the cutoff date of February 2025 for publicly available data.  

  * **Supported languages:** English  

  * **Release date:** April 2025  

###  Training Datasets 

The training data for Phi-4-mini-reasoning consists exclusively of synthetic mathematical content generated by a stronger and more advanced reasoning model, Deepseek-R1. The objective is to distill knowledge from this model. This synthetic dataset comprises over one million diverse math problems spanning multiple levels of difficulty (from middle school to Ph.D. level). For each problem in the synthetic dataset, eight distinct solutions (rollouts) were sampled, and only those verified as correct were retained, resulting in approximately 30 billion tokens of math content. The dataset integrates three primary components: 

  1. a curated selection of high-quality, publicly available math questions and a part of the SFT(Supervised Fine-Tuning) data that was used to train the base Phi-4-Mini model;
  2. an extensive collection of synthetic math data generated by the Deepseek-R1 model, designed specifically for high-quality supervised fine-tuning and model distillation; and
  3. a balanced set of correct and incorrect answers used to construct preference data aimed at enhancing Phi-4-mini-reasoning's reasoning capabilities by learning more effective reasoning trajectories

##  Software 

  * [PyTorch](https://github.com/pytorch/pytorch)
  * [Transformers](https://github.com/huggingface/transformers)
  * [Flash-Attention](https://github.com/HazyResearch/flash-attention)

##  Hardware 

Note that by default, the Phi-4-mini-reasoning model uses flash attention, which requires certain types of GPU hardware to run. We have tested on the following GPU types:

  * NVIDIA A100
  * NVIDIA H100

If you want to run the model on:

  * NVIDIA V100 or earlier generation GPUs: call AutoModelForCausalLM.from_pretrained() with attn_implementation="eager"


##  License 

The model is licensed under the [MIT license](/unsloth/Phi-4-mini-reasoning/blob/main/./LICENSE).

##  Trademarks 

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow [Microsoft’s Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks). Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos are subject to those third-party’s policies.

Safetensors[](https://huggingface.co/docs/safetensors)

Model size

3.84B params

Tensor type

BF16 

