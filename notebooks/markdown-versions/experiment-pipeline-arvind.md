```python
!pip install -Uq transformers==4.53.2
!pip install -Uq peft
!pip install -Uq trl
!pip install -Uq accelerate
!pip install -Uq datasets
!pip install -Uq bitsandbytes

# Install Flash Attention 2
!pip install flash-attn==2.7.4.post1 \
  --extra-index-url https://download.pytorch.org/whl/cu124 \
  --no-build-isolation
```

Cell 1: Configuration and setup


```python
# ===== EXPERIMENT CONFIGURATION =====
CONFIG = {
    # Core experiment parameters
    "experiment_type": "generative",  # "discriminative" or "generative"
    "classification_type": "ternary",   # "binary" or "ternary"
    "dataset_strategy": "4N",          # "4N" or "3N" (generative only)
    "include_explanation": True,      # True or False (generative only)
    "include_eln": True,              # True or False (generative only)
    "solution_format": "nl",        # "dict" or "nl" (generative only)
    "model_name": "microsoft/phi-4-mini-instruct",  # or "Qwen/Qwen3-4B"
    
    # Prompting configuration
    "system_prompt": None,  # Will auto-generate if None, or use custom string
    "include_examples": False,
    "num_examples": 3,
    "example_strategy": "balanced",  # "balanced", "error_focused", "custom"
    
    # Training parameters
    "learning_rate": 2e-4,
    "num_epochs": 3,
    "batch_size": 8,
    "max_length": 1600,
    "gradient_accumulation_steps": 4,
    
    # Infrastructure
    "use_lora": True,
    "lora_rank": 16,
    "lora_alpha": 32,
    "lora_dropout": 0.1,
    
    # Paths and tokens
    # "base_dataset_dir": "/content/drive/MyDrive/sft_datasets",
    "base_dataset_dir": "../data/base-datasets-sanitized",
    "output_base_dir": "/content/drive/MyDrive/sft_experiments",
    # "hf_token": "your_huggingface_token_here",
    # "wandb_project": "math_error_classification",
    
    # Experiment tracking
    "save_to_hf": True,
    "save_locally": True,
    "use_wandb": False
}

# Generate experiment ID
import datetime
experiment_components = [
    CONFIG["experiment_type"][:4],  # "gene" or "disc"
    CONFIG["classification_type"][:3],  # "bin" or "ter"
    CONFIG["dataset_strategy"] if CONFIG["experiment_type"] == "generative" else "",
    "exp" if CONFIG["include_explanation"] else "no_exp",
    "eln" if CONFIG["include_eln"] else "no_eln",
    CONFIG["solution_format"] if CONFIG["experiment_type"] == "generative" else "",
    "qwen" if "Qwen" in CONFIG["model_name"] else "phi4"
]
experiment_id = "_".join([c for c in experiment_components if c]) + "_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
CONFIG["experiment_id"] = experiment_id

print(f"Experiment ID: {experiment_id}")
print(f"Configuration loaded successfully!")
```

    Experiment ID: gene_ter_4N_exp_eln_nl_phi4_20250731_152617
    Configuration loaded successfully!


Cell 2: Import dependencies


```python
import torch
import random
import numpy as np

# Set random seeds for reproducibility
def set_seeds(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)

set_seeds(42)
print("Dependencies imported and seeds set!")
```

    Dependencies imported and seeds set!


Cell 3: System Prompt Generation


```python
def generate_system_prompt(config):
    """Auto-generates appropriate system prompt based on config"""
    
    if config["experiment_type"] == "discriminative":
        return "You are a mathematics tutor. Classify the given solution."
    
    # Generative prompts
    base_prompt = "You are a mathematics tutor. Analyze the given solution and provide your assessment in JSON format."
    
    # Add classification instructions
    if config["classification_type"] == "binary":
        base_prompt += " Determine if the solution is 'correct' or 'flawed'."
    else:
        base_prompt += " Classify as 'correct', 'conceptual_error', or 'computational_error'."
    
    # Add field instructions
    fields = []
    if config["include_eln"]:
        if config["solution_format"] == "dict":
            fields.append("identify the erroneous line number (e.g., 'L1', 'FA')")
        else:
            fields.append("quote the full erroneous line text")
    
    if config["include_explanation"]:
        fields.append("provide a brief explanation of any error")
    
    if fields:
        base_prompt += f" Also {', and '.join(fields)}."
    
    base_prompt += " Respond only with valid JSON."
    
    return base_prompt

# Auto-generate system prompt if not provided
if CONFIG["system_prompt"] is None:
    CONFIG["system_prompt"] = generate_system_prompt(CONFIG)

print("System Prompt:")
print(CONFIG["system_prompt"])
print()

# Allow manual override
print("To customize the system prompt, run:")
print('CONFIG["system_prompt"] = "Your custom prompt here"')
```

    System Prompt:
    You are a mathematics tutor. Analyze the given solution and provide your assessment in JSON format. Classify as 'correct', 'conceptual_error', or 'computational_error'. Also quote the full erroneous line text, and provide a brief explanation of any error. Respond only with valid JSON.
    
    To customize the system prompt, run:
    CONFIG["system_prompt"] = "Your custom prompt here"


Cell 4: Example Manager


```python
class ExampleManager:
    def __init__(self, base_dataset, config):
        # Convert DataFrame to list of dicts if needed
        if hasattr(base_dataset, 'to_dict'):  # It's a DataFrame
            self.samples = base_dataset.to_dict('records')
        else:
            self.samples = base_dataset  # Already a list of dicts
            
        self.config = config
        self._prepare_examples_by_problem()
    
    def _prepare_examples_by_problem(self):
        """Organizes samples by problem index and error type"""
        self.problems_by_type = {
            "correct": {},
            "conceptual_error": {},
            "computational_error": {}
        }
        
        # Group samples by problem index and error type
        for sample in self.samples:
            problem_index = sample["index"]
            error_type = sample["error_type"]
            
            if problem_index not in self.problems_by_type[error_type]:
                self.problems_by_type[error_type][problem_index] = []
            self.problems_by_type[error_type][problem_index].append(sample)
        
        print(f"Problems by type: correct={len(self.problems_by_type['correct'])}, "
              f"conceptual={len(self.problems_by_type['conceptual_error'])}, "
              f"computational={len(self.problems_by_type['computational_error'])}")
    
    def get_examples(self):
        """Returns examples based on dataset strategy"""
        if not self.config["include_examples"]:
            return []
        
        num_examples = self.config["num_examples"]
        dataset_strategy = self.config["dataset_strategy"]
        
        import random
        
        if dataset_strategy == "3N":
            # Choose num_examples distinct problem indices that have all 3 versions
            available_problems = set(self.problems_by_type["correct"].keys()) & \
                               set(self.problems_by_type["conceptual_error"].keys()) & \
                               set(self.problems_by_type["computational_error"].keys())
            
            if not available_problems:
                print("Warning: No problems found with all 3 versions (correct/conceptual/computational)")
                return []
            
            # Sample problem indices
            selected_problems = random.sample(
                list(available_problems), 
                min(num_examples, len(available_problems))
            )
            
            examples = []
            for problem_index in selected_problems:
                # Add all 3 versions: correct, conceptual_error, computational_error
                examples.append(self.problems_by_type["correct"][problem_index][0])
                examples.append(self.problems_by_type["conceptual_error"][problem_index][0])
                examples.append(self.problems_by_type["computational_error"][problem_index][0])
            
            return examples
            
        elif dataset_strategy == "4N":
            import math
            
            # Get problems that have conceptual errors (with correct versions)
            conceptual_problems = list(
                set(self.problems_by_type["correct"].keys()) & 
                set(self.problems_by_type["conceptual_error"].keys())
            )
            
            # Get problems that have computational errors (with correct versions)
            computational_problems = list(
                set(self.problems_by_type["correct"].keys()) & 
                set(self.problems_by_type["computational_error"].keys())
            )
            
            # Calculate splits: floor(n/2) conceptual, ceil(n/2) computational
            n_conceptual = num_examples // 2  # This is floor(n/2)
            n_computational = math.ceil(num_examples / 2)
            
            examples = []
            
            # Sample conceptual problems
            if conceptual_problems and n_conceptual > 0:
                selected_conceptual = random.sample(
                    conceptual_problems,
                    min(n_conceptual, len(conceptual_problems))
                )
                
                for problem_index in selected_conceptual:
                    # Add correct + conceptual_error pair
                    examples.append(self.problems_by_type["correct"][problem_index][0])
                    examples.append(self.problems_by_type["conceptual_error"][problem_index][0])
            
            # Sample computational problems
            if computational_problems and n_computational > 0:
                selected_computational = random.sample(
                    computational_problems,
                    min(n_computational, len(computational_problems))
                )
                
                for problem_index in selected_computational:
                    # Add correct + computational_error pair
                    examples.append(self.problems_by_type["correct"][problem_index][0])
                    examples.append(self.problems_by_type["computational_error"][problem_index][0])
            
            return examples
        
        else:
            print(f"Warning: Unknown dataset strategy '{dataset_strategy}'")
            return []

print("Updated ExampleManager class loaded!")
```

    Updated ExampleManager class loaded!


Cell 5: Dataset Loading and Formatting Functions


```python
import json
import pandas as pd
from pathlib import Path

def load_base_dataset(config):
    """Loads the appropriate base dataset"""
    dataset_strategy = config["dataset_strategy"]
    base_dir = Path(config["base_dataset_dir"])
    
    dataset_file = base_dir / f"base_{dataset_strategy}_dataset_sanitized.csv"
    
    if not dataset_file.exists():
        raise FileNotFoundError(f"Base dataset not found: {dataset_file}")

    data = pd.read_csv(dataset_file)

    print(f"Loaded base {dataset_strategy} dataset with {len(data)} samples")
    return data

def format_solution(sample, config):
    """Formats solution according to config - updated for CSV structure"""
    # Use wrong_answer for the solution (this contains the solution steps)
    solution_text = sample.get('wrong_answer', sample.get('correct_answer', ''))
    
    if config["solution_format"] == "dict":
        # Split solution into lines and format as dict
        lines = solution_text.strip().split('\n')
        solution = {}
        for i, line in enumerate(lines[:-1]):
            if line.strip():  # Skip empty lines
                solution[f"L{i+1}"] = line.strip()
        if lines and lines[-1].strip():
            solution["FA"] = lines[-1].strip()
        return json.dumps(solution, indent=2)
    else:
        return solution_text.strip()

def format_expected_output(sample, config):
    """Creates the expected JSON output for a sample - updated for CSV structure"""
    output = {}
    
    # Verdict
    if config["classification_type"] == "binary":
        output["verdict"] = "correct" if sample["error_type"] == "correct" else "flawed"
    else:
        output["verdict"] = sample["error_type"]
    
    # ELN (Erroneous Line Number)
    if config["include_eln"]:
        if sample["error_type"] != "correct":
            if config["solution_format"] == "dict":
                output["erroneous_line_number"] = sample.get("erroneous_line_number", None)
            else:
                # For natural language format, try to extract the actual erroneous line text
                eln = sample.get("erroneous_line_number")
                if eln and pd.notna(eln):
                    # Extract line number (e.g., "L3" -> 3)
                    try:
                        if eln.startswith('L'):
                            line_num = int(eln[1:]) - 1
                            solution_lines = sample.get('wrong_answer', '').strip().split('\n')
                            if 0 <= line_num < len(solution_lines):
                                output["erroneous_line"] = solution_lines[line_num].strip()
                            else:
                                output["erroneous_line"] = eln  # Fallback to the ELN itself
                        elif eln == 'FA':
                            solution_lines = sample.get('wrong_answer', '').strip().split('\n')
                            output["erroneous_line"] = solution_lines[-1].strip() if solution_lines else None
                        else:
                            output["erroneous_line"] = eln
                    except:
                        output["erroneous_line"] = eln
                else:
                    output["erroneous_line"] = None
        else:
            key = "erroneous_line_number" if config["solution_format"] == "dict" else "erroneous_line"
            output[key] = None
    
    # Explanation
    if config["include_explanation"]:
        explanation = sample.get("explanation")
        output["explanation"] = explanation if pd.notna(explanation) and sample["error_type"] != "correct" else None
    
    return json.dumps(output)

def format_user_message(sample, config):
    """Format a sample into a user message."""
    return f"### Question:\n{sample['question']}\n\n### Answer:\n{format_solution(sample, config)}"

def create_sample_messages(sample, examples, config):
    """Create complete message list for a sample."""
    messages = []
    
    # System message
    messages.append({
        "role": "system",
        "content": config["system_prompt"]
    })
    
    # Few-shot examples
    if config["include_examples"]:
        for example in examples:
            user_content = format_user_message(example, config)
            assistant_content = format_expected_output(example, config)
            
            messages.append({"role": "user", "content": user_content})
            messages.append({"role": "assistant", "content": assistant_content})
    
    # Actual sample
    user_content = format_user_message(sample, config)
    messages.append({"role": "user", "content": user_content})
    
    return messages

print("Updated formatting functions loaded!")
```

    Updated formatting functions loaded!


Cell 6: Dataset Preparation


```python
def prepare_dataset(config):
    """Loads and formats complete dataset for training/evaluation"""
    
    # Load base dataset
    base_samples = load_base_dataset(config)
    
    # Initialize example manager - convert DataFrame to list of dicts
    example_manager = ExampleManager(base_samples, config)
    examples = example_manager.get_examples()
    
    print(f"Using {len(examples)} few-shot examples")
    
    # Format all samples
    formatted_data = []
    
    # Iterate over DataFrame rows
    for idx, sample in base_samples.iterrows():
        # Convert pandas Series to dict for easier access
        sample_dict = sample.to_dict()
        
        # Use modular function to create messages
        messages = create_sample_messages(sample_dict, examples, config)
        
        # Expected output
        expected_output = format_expected_output(sample_dict, config)
        
        formatted_data.append({
            "id": sample_dict.get("id", f"sample_{len(formatted_data)}"),
            "messages": messages,
            "expected_output": expected_output,
            "metadata": {
                "error_type": sample_dict["error_type"],
                "tier": sample_dict.get("tier", "unknown"),
                "source": sample_dict.get("source", "unknown")
            }
        })
    
    # Split into train/eval
    split_point = int(0.8 * len(formatted_data))
    train_data = formatted_data[:split_point]
    eval_data = formatted_data[split_point:]
    
    print(f"Dataset prepared: {len(train_data)} training, {len(eval_data)} evaluation samples")
    
    return train_data, eval_data, examples
```

Cell 7: Model and Tokenizer Loading


```python
from transformers import (
    AutoTokenizer, 
    AutoModelForCausalLM,
    AutoModelForSequenceClassification
)

from transformers.utils.quantization_config import BitsAndBytesConfig

from peft import (
    LoraConfig, 
    get_peft_model, 
    TaskType, 
    prepare_model_for_kbit_training
)

def load_tokenizer(model_name):
    """Loads tokenizer with proper configuration"""
    print(f"Loading tokenizer: {model_name}")
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    tokenizer.padding_side = "left"  # Ensure left padding for causal models
    
    print(f"✓ Tokenizer loaded successfully!")
    return tokenizer

def load_model(model_name, config):
    """Loads model with appropriate configuration"""
    print(f"Loading model: {model_name}")
    
    # Configure quantization if using LoRA
    bnb_config = None
    if config["use_lora"]:
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_use_double_quant=True
        )
    
    # Load model based on experiment type
    if config["experiment_type"] == "discriminative":
        # For discriminative, we need a classification model
        num_labels = 2 if config["classification_type"] == "binary" else 3
        model = AutoModelForSequenceClassification.from_pretrained(
            model_name,
            num_labels=num_labels,
            quantization_config=bnb_config,
            device_map="auto",
            trust_remote_code=True
        )
    else:
        # For generative, use causal LM
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            quantization_config=bnb_config,
            device_map="auto",
            trust_remote_code=True,
            attn_implementation="flash_attention_2"
        )
    
    # Apply LoRA if configured
    if config["use_lora"]:
        model = prepare_model_for_kbit_training(model)
        
        # Configure LoRA based on experiment type
        if config["experiment_type"] == "discriminative":
            task_type = TaskType.SEQ_CLS
            target_modules = ["q_proj", "v_proj", "k_proj", "o_proj"]
        else:
            task_type = TaskType.CAUSAL_LM
            target_modules = ["q_proj", "v_proj", "k_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]
        
        lora_config = LoraConfig(
            task_type=task_type,
            r=config["lora_rank"],
            lora_alpha=config["lora_alpha"],
            lora_dropout=config["lora_dropout"],
            target_modules=target_modules,
            bias="none"
        )
        
        model = get_peft_model(model, lora_config)
        model.print_trainable_parameters()
    
    print(f"✓ Model loaded successfully!")
    print(f"✓ Model device: {next(model.parameters()).device}")
    
    return model

def apply_chat_template(
        messages, 
        tokenizer, 
        add_generation_prompt=False, 
        tokenize=True, 
        **kwargs
    ):
    """
    Applies chat template to messages with consistent interface
    
    Args:
        messages: List of message dictionaries with 'role' and 'content' keys
        tokenizer: The tokenizer to use for formatting
        add_generation_prompt: Whether to add generation prompt (for inference)
        tokenize: Whether to return tokens (True) or text (False)
        **kwargs: Additional arguments for tokenizer (like return_tensors, max_length, etc.)
    
    Returns:
        If tokenize=True: tokenizer output dict with input_ids, attention_mask, etc.
        If tokenize=False: formatted text string
    """
    
    # Check if this is a Qwen3 model and disable thinking if so
    template_kwargs = {}
    if CONFIG["model_name"].startswith("Qwen"):
        template_kwargs['enable_thinking'] = False
    
    # Apply chat template to get formatted text
    formatted_text = tokenizer.apply_chat_template(
        messages, 
        tokenize=False, 
        add_generation_prompt=add_generation_prompt,
        **template_kwargs
    )
    
    # Return text if not tokenizing
    if not tokenize:
        return formatted_text
    
    # Tokenize and return tensor format
    return tokenizer(formatted_text, **kwargs)

def load_model_and_tokenizer(config):
    """
    Convenience function that loads both model and tokenizer
    Uses the modular functions above
    """
    model_name = config["model_name"]
    
    # Load components separately
    tokenizer = load_tokenizer(model_name)
    model = load_model(model_name, config)
    
    return model, tokenizer
```

Cell 8: Output Directory Setup


```python
# def setup_output_directory(config):
#     """Creates organized output directory structure"""
    
#     output_dir = Path(config["output_base_dir"]) / config["experiment_id"]
    
#     # Create subdirectories
#     subdirs = ["baseline", "training", "final", "checkpoints"]
#     for subdir in subdirs:
#         (output_dir / subdir).mkdir(parents=True, exist_ok=True)
    
#     # Save configuration
#     config_path = output_dir / "config.json"
#     with open(config_path, 'w') as f:
#         json.dump(config, f, indent=2, default=str)
    
#     print(f"Output directory created: {output_dir}")
#     return output_dir

# # Setup output directory
# output_dir = setup_output_directory(CONFIG)
# CONFIG["output_dir"] = str(output_dir)
```

Cell 9: Inference Functions


```python
import time

def prepare_inference_batch(messages_batch, tokenizer, max_length=1024):
    """
    Prepares a batch of messages for inference by applying chat templates and tokenizing.
    
    Args:
        messages_batch: List of message conversations (each is a list of message dicts)
        tokenizer: The tokenizer to use
        max_length: Maximum sequence length
        
    Returns:
        dict: Batch with input_ids, attention_mask, and metadata
    """
    batch_data = {
        "input_ids": [],
        "attention_mask": [],
        "metadata": {
            "formatted_prompts": [],
            "input_token_counts": [],
            "conversation_lengths": []
        }
    }
    
    for messages in messages_batch:
        # Use our custom apply_chat_template function
        formatted_prompt = apply_chat_template(
            messages,
            tokenizer,
            add_generation_prompt=True,
            tokenize=False
        )
        
        # Tokenize the formatted prompt
        tokenized = tokenizer(
            formatted_prompt,
            return_tensors="pt",
            truncation=True,
            max_length=max_length,
            padding=False  # We'll pad at batch level
        )
        
        # Store batch data
        batch_data["input_ids"].append(tokenized["input_ids"].squeeze(0))
        batch_data["attention_mask"].append(tokenized["attention_mask"].squeeze(0))
        
        # Store metadata
        batch_data["metadata"]["formatted_prompts"].append(formatted_prompt)
        batch_data["metadata"]["input_token_counts"].append(len(tokenized["input_ids"][0]))
        batch_data["metadata"]["conversation_lengths"].append(len(messages))
    
    return batch_data

def apply_batch_padding(batch_data, tokenizer):
    """
    Applies padding to a batch of tokenized sequences.
    
    Args:
        batch_data: Output from prepare_inference_batch
        tokenizer: The tokenizer (for pad_token_id)
        
    Returns:
        dict: Padded tensors ready for model input
    """
    from torch.nn.utils.rnn import pad_sequence
    
    # Pad sequences to same length
    input_ids_padded = pad_sequence(
        batch_data["input_ids"],
        batch_first=True,
        padding_value=tokenizer.pad_token_id
    )
    
    attention_mask_padded = pad_sequence(
        batch_data["attention_mask"],
        batch_first=True,
        padding_value=0
    )
    
    return {
        "input_ids": input_ids_padded,
        "attention_mask": attention_mask_padded,
        "metadata": batch_data["metadata"]
    }

def decode_batch_outputs(outputs, input_lengths, tokenizer):
    """
    Decodes model outputs for a batch, extracting only the generated portions.
    
    Args:
        outputs: Model generation outputs (batch_size, sequence_length)
        input_lengths: List of input sequence lengths for each item in batch
        tokenizer: The tokenizer for decoding
        
    Returns:
        list: Decoded responses (only the generated parts)
    """
    responses = []
    
    for i, output_sequence in enumerate(outputs):
        # Extract only the generated tokens (after input)
        input_length = input_lengths[i]
        generated_tokens = output_sequence[input_length:]
        
        # Decode to text
        response = tokenizer.decode(generated_tokens, skip_special_tokens=True)
        responses.append(response.strip())
    
    return responses

def create_attention_masks(input_ids, tokenizer):
    """
    Creates attention masks for tokenized inputs.
    
    Args:
        input_ids: Tokenized input sequences
        tokenizer: The tokenizer (for pad_token_id)
        
    Returns:
        torch.Tensor: Attention masks
    """
    
    if isinstance(input_ids, list):
        input_ids = torch.stack(input_ids)
    
    # Create attention mask (1 for real tokens, 0 for padding)
    attention_mask = (input_ids != tokenizer.pad_token_id).long()
    return attention_mask

def run_inference(model, tokenizer, prepared_inputs, batch_size=1):
    """
    Pure inference function that accepts pre-processed inputs and returns results.
    
    Args:
        model: The model to use for inference
        tokenizer: The tokenizer (only used for pad_token_id in generation)
        prepared_inputs: Pre-processed batch of inputs with input_ids, attention_mask, metadata
        batch_size: Batch size for processing (legacy parameter for compatibility)
        
    Returns:
        tuple: (responses, generation_metadata)
    """
    
    model.eval()
    
    with torch.no_grad():
        start_time = time.time()
        
        # Move inputs to model device
        input_ids = prepared_inputs["input_ids"].to(model.device)
        attention_mask = prepared_inputs["attention_mask"].to(model.device)
        
        # Generate responses
        outputs = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_new_tokens=200,
            do_sample=False,
            temperature=0.1,
            pad_token_id=tokenizer.pad_token_id,
            return_dict_in_generate=True,
            output_scores=False
        )
        
        end_time = time.time()
        
        # Decode outputs
        input_lengths = prepared_inputs["metadata"]["input_token_counts"]
        responses = decode_batch_outputs(outputs.sequences, input_lengths, tokenizer)
        
        # Calculate generation metadata
        generation_metadata = {
            "total_inference_time": end_time - start_time,
            "batch_size": len(responses),
            "avg_inference_time_per_sample": (end_time - start_time) / len(responses),
            "input_token_counts": input_lengths,
            "output_token_counts": [len(outputs.sequences[i]) - input_lengths[i] for i in range(len(responses))],
            "total_tokens_generated": sum(len(outputs.sequences[i]) - input_lengths[i] for i in range(len(responses)))
        }
        
        if torch.cuda.is_available():
            generation_metadata["gpu_memory_used"] = torch.cuda.memory_allocated() / 1024**3  # GB
    
    return responses, generation_metadata

def save_results(results, metadata, stage, config):
    """Saves results and metadata to appropriate locations"""
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path(config["output_dir"]) / stage
    
    # Save results
    results_path = output_dir / f"results_{timestamp}.json"
    with open(results_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    # Save metadata
    metadata_path = output_dir / f"metadata_{timestamp}.json"
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f, indent=2, default=str)
    
    print(f"Results saved to: {results_path}")
    print(f"Metadata saved to: {metadata_path}")
    
    return results_path, metadata_path

print("Inference functions loaded!")
```

    Inference functions loaded!


Cell 10: Compute metrics function



```python
import json
import re
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

def normalize_text(text):
    """Normalize text for flexible comparison (removes spaces, converts to lowercase)."""
    if text is None:
        return ""
    return re.sub(r'\s+', '', str(text).lower().strip())

def extract_json_from_response(response):
    """Extract JSON from model response, handling various formatting issues."""
    if not response:
        return {}
    
    response = response.strip()
    
    # Look for JSON patterns
    json_patterns = [
        r'\{.*\}',  # Basic JSON pattern
        r'```json\s*(\{.*\})\s*```',  # Markdown code block
        r'```\s*(\{.*\})\s*```',  # Generic code block
    ]
    
    for pattern in json_patterns:
        matches = re.findall(pattern, response, re.DOTALL)
        for match in matches:
            try:
                return json.loads(match)
            except json.JSONDecodeError:
                continue
    
    # Try parsing the whole response
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        return {}

def compute_metrics(results, config):
    """
    Compute simple metrics: verdict accuracy/precision/recall/F1 and ELN accuracy.
    
    Args:
        results: List of result dictionaries with expected_output and model_response
        config: Configuration dictionary
        
    Returns:
        dict: Simple metrics dictionary
    """
    
    # Parse responses
    verdict_expected = []
    verdict_predicted = []
    eln_expected = []
    eln_predicted = []
    
    parse_failures = 0
    
    for result in results:
        expected = json.loads(result["expected_output"])
        predicted = extract_json_from_response(result["model_response"])
        
        if not predicted:
            parse_failures += 1
        
        # Verdict
        verdict_expected.append(expected.get("verdict", "unknown"))
        verdict_predicted.append(predicted.get("verdict", "unknown"))
        
        # Erroneous line (if applicable)
        if config["include_eln"]:
            if config["solution_format"] == "dict":
                eln_expected.append(expected.get("erroneous_line_number"))
                eln_predicted.append(predicted.get("erroneous_line_number"))
            else:
                eln_expected.append(expected.get("erroneous_line"))
                eln_predicted.append(predicted.get("erroneous_line"))
    
    # Compute verdict metrics
    verdict_accuracy = accuracy_score(verdict_expected, verdict_predicted)
    precision, recall, f1, _ = precision_recall_fscore_support(
        verdict_expected, verdict_predicted, average='macro', zero_division=0
    )
    
    metrics = {
        "verdict_accuracy": verdict_accuracy,
        "verdict_precision": precision,
        "verdict_recall": recall,
        "verdict_f1": f1,
        "parse_failures": parse_failures,
        "total_samples": len(results)
    }
    
    # Compute ELN accuracy if applicable
    if config["include_eln"] and eln_expected:
        if config["solution_format"] == "dict":
            # For dict format, exact match
            eln_accuracy = accuracy_score(eln_expected, eln_predicted)
        else:
            # For nl format, use normalized comparison for flexibility
            normalized_expected = [normalize_text(eln) for eln in eln_expected]
            normalized_predicted = [normalize_text(eln) for eln in eln_predicted]
            eln_accuracy = accuracy_score(normalized_expected, normalized_predicted)
        
        metrics["eln_accuracy"] = eln_accuracy
    
    return metrics

def print_metrics(metrics, stage_name="Evaluation"):
    """Print simple metrics summary."""
    print(f"\n{stage_name} Results:")
    print(f"Total samples: {metrics['total_samples']} (Parse failures: {metrics['parse_failures']})")
    print(f"Verdict - Accuracy: {metrics['verdict_accuracy']:.3f}, Precision: {metrics['verdict_precision']:.3f}, Recall: {metrics['verdict_recall']:.3f}, F1: {metrics['verdict_f1']:.3f}")
    
    if "eln_accuracy" in metrics:
        print(f"ELN Accuracy: {metrics['eln_accuracy']:.3f}")

# Simple evaluation function
def evaluate_results(results, config, stage_name="Evaluation"):
    """Evaluate results with simple metrics."""
    metrics = compute_metrics(results, config)
    print_metrics(metrics, stage_name)
    return metrics

print("✅ Simplified metrics functions loaded (with text normalization)!")
print("\nTo evaluate your baseline results, run:")
print("baseline_metrics = evaluate_results(baseline_results, CONFIG, 'Baseline')")
```

    ✅ Simplified metrics functions loaded (with text normalization)!
    
    To evaluate your baseline results, run:
    baseline_metrics = evaluate_results(baseline_results, CONFIG, 'Baseline')



```python
from transformers import (
    TrainingArguments, 
    Trainer, 
    DataCollatorForLanguageModeling,
    EarlyStoppingCallback
)
import torch
from datasets import Dataset

def prepare_training_data(train_data, tokenizer, config):
    """
    Prepares training data for generative fine-tuning with chat templates.
    
    Args:
        train_data: List of training samples with messages and expected outputs
        tokenizer: The tokenizer to use
        config: Configuration dictionary
        
    Returns:
        Dataset: Formatted dataset ready for training
    """
    formatted_samples = []
    
    for sample in train_data:
        # Get the messages (includes system, examples, and user message)
        messages = sample["messages"]
        expected_output = sample["expected_output"]
        
        # Add the assistant response to complete the conversation
        complete_messages = messages + [{"role": "assistant", "content": expected_output}]
        
        # Use our custom apply_chat_template function
        formatted_text = apply_chat_template(
            complete_messages,
            tokenizer,
            add_generation_prompt=False,  # We have the complete conversation
            tokenize=False
        )
        
        formatted_samples.append({
            "text": formatted_text,
            "sample_id": sample["id"],
            "metadata": sample["metadata"]
        })
    
    return Dataset.from_list(formatted_samples)

def setup_training_components(model, tokenizer, train_data, eval_data, config):
    """
    Sets up training arguments, data collator, and trainer for generative fine-tuning.
    
    Args:
        model: The loaded model
        tokenizer: The loaded tokenizer  
        train_data: Training samples
        eval_data: Evaluation samples
        config: Configuration dictionary
        
    Returns:
        tuple: (trainer, train_dataset, eval_dataset)
    """
    
    # Prepare datasets
    print("Preparing training datasets...")
    train_dataset = prepare_training_data(train_data, tokenizer, config)
    eval_dataset = prepare_training_data(eval_data, tokenizer, config)
    
    print(f"✓ Training dataset: {len(train_dataset)} samples")
    print(f"✓ Evaluation dataset: {len(eval_dataset)} samples")
    
    # Tokenize datasets
    def tokenize_function(examples):
        # Tokenize the formatted text
        tokenized = tokenizer(
            examples["text"],
            truncation=True,
            max_length=config["max_length"],
            padding=False,  # Dynamic padding handled by data collator
            return_tensors=None  # Return lists, not tensors
        )
        
        # For causal LM, labels are the same as input_ids
        tokenized["labels"] = tokenized["input_ids"].copy()
        
        return tokenized
    
    print("Tokenizing datasets...")
    train_dataset = train_dataset.map(
        tokenize_function,
        batched=True,
        remove_columns=train_dataset.column_names
    )
    
    eval_dataset = eval_dataset.map(
        tokenize_function,
        batched=True,
        remove_columns=eval_dataset.column_names
    )
    
    print("✓ Datasets tokenized")
    
    # Data collator for language modeling
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False  # We're doing causal LM, not masked LM
    )
    
    # Training arguments
    output_dir = Path(config["output_dir"]) / "training"
    
    training_args = TrainingArguments(
        output_dir=str(output_dir),
        
        # Training schedule
        num_train_epochs=config["num_epochs"],
        per_device_train_batch_size=config["batch_size"],
        per_device_eval_batch_size=config["batch_size"],
        gradient_accumulation_steps=config["gradient_accumulation_steps"],
        
        # Optimization
        learning_rate=config["learning_rate"],
        weight_decay=0.01,
        warmup_ratio=0.1,
        lr_scheduler_type="cosine",
        
        # FREQUENT EVALUATION & SAVING
        eval_strategy="steps",        # Evaluate every 25 steps
        eval_steps=25,
        save_strategy="steps",       # Save every 25 steps
        save_steps=25,
        save_total_limit=1,          # Keep only the most recent checkpoint
        load_best_model_at_end=True,
        metric_for_best_model="eln_accuracy",
        greater_is_better=True,
        
        # Logging
        logging_strategy="steps",
        logging_steps=25,
        report_to=None,  # Disable wandb/tensorboard for now
        save_safetensors=False,
        
        # Mixed precision
        fp16=True if torch.cuda.is_available() else False,
        
        # Reproducibility
        seed=42,
        data_seed=42,
    )
    # Initialize early stopping callback
    early_stopping_callback = EarlyStoppingCallback(
        early_stopping_patience=10,    # Stop after 10 evaluations without improvement
        early_stopping_threshold=0.0  # Any improvement counts
    )

    # Initialize trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        processing_class=tokenizer,
        compute_metrics=compute_metrics,
        callbacks=[early_stopping_callback]
    )
    
    print("✓ Trainer initialized successfully!")
    print(f"✓ Training arguments configured")
    print(f"✓ Data collator ready")
    
    # Print training summary
    print(f"\nTraining Summary:")
    print(f"  Model: {config['model_name']}")
    print(f"  Training samples: {len(train_dataset)}")
    print(f"  Evaluation samples: {len(eval_dataset)}")
    print(f"  Epochs: {config['num_epochs']}")
    print(f"  Batch size: {config['batch_size']}")
    print(f"  Gradient accumulation: {config['gradient_accumulation_steps']}")
    print(f"  Effective batch size: {config['batch_size'] * config['gradient_accumulation_steps']}")
    print(f"  Learning rate: {config['learning_rate']}")
    print(f"  Max length: {config['max_length']}")
    print(f"  Output directory: {output_dir}")
    
    return trainer, train_dataset, eval_dataset
```


```python
tokenizer = load_tokenizer(CONFIG["model_name"])
```

    Loading tokenizer: microsoft/phi-4-mini-instruct
    ✓ Tokenizer loaded successfully!



```python
tokenizer.padding_side
```




    'left'




```python
# # Load dataset and model for baseline inference
# print("=== LOADING DATASET AND MODEL ===")

# # Load and prepare dataset
# train_data, eval_data, examples = prepare_dataset(CONFIG)

# # Load model and tokenizer
# model, tokenizer = load_model_and_tokenizer(CONFIG)

# print(f"✅ Dataset loaded: {len(train_data)} train, {len(eval_data)} eval")
# print(f"✅ Model and tokenizer loaded")
```


```python
# # Perform baseline inference on evaluation set
# print("=== BASELINE INFERENCE ===")

# # Prepare inference data (use first 50 samples for faster testing)
# eval_subset = eval_data[:50]  # Adjust size as needed
# messages_batch = [sample["messages"] for sample in eval_subset]

# # Prepare inference batch
# prepared_inputs = prepare_inference_batch(
#     messages_batch, 
#     tokenizer, 
#     max_length=CONFIG["max_length"]
# )

# # Apply padding
# padded_inputs = apply_batch_padding(prepared_inputs, tokenizer)

# # Run inference
# baseline_responses, baseline_metadata = run_inference(
#     model, tokenizer, padded_inputs
# )

# # Format results
# baseline_results = []
# for i, sample in enumerate(eval_subset):
#     baseline_results.append({
#         "id": sample["id"],
#         "expected_output": sample["expected_output"],
#         "model_response": baseline_responses[i],
#         "metadata": sample["metadata"]
#     })

# print(f"✅ Baseline inference completed on {len(baseline_results)} samples")
# print(f"Avg inference time: {baseline_metadata['avg_inference_time_per_sample']:.2f}s")

# # Evaluate baseline
# baseline_metrics = evaluate_results(baseline_results, CONFIG, "Baseline")
```


```python
# # Save baseline results
# print("=== SAVING BASELINE RESULTS ===")

# import json
# from pathlib import Path

# # Create output directory
# output_dir = Path(f"./baseline_results_{CONFIG['experiment_id']}")
# output_dir.mkdir(exist_ok=True)

# # Save results
# baseline_results_path = output_dir / "baseline_results.json"
# with open(baseline_results_path, 'w') as f:
#     json.dump(baseline_results, f, indent=2)

# # Save metadata  
# baseline_metadata_path = output_dir / "baseline_metadata.json"
# baseline_metadata.update(baseline_metrics)  # Include metrics in metadata
# with open(baseline_metadata_path, 'w') as f:
#     json.dump(baseline_metadata, f, indent=2, default=str)

# # Save config
# config_path = output_dir / "config.json"
# with open(config_path, 'w') as f:
#     json.dump(CONFIG, f, indent=2, default=str)

# print(f"✅ Baseline results saved to: {output_dir}")
# print(f"   - Results: {baseline_results_path}")
# print(f"   - Metadata: {baseline_metadata_path}")
# print(f"   - Config: {config_path}")
```


```python
# # Setup and perform training
# print("=== SETTING UP TRAINING ===")

# # Setup training components
# trainer, train_dataset, eval_dataset = setup_training_components(
#     model, tokenizer, train_data, eval_data, CONFIG
# )

# print("=== STARTING TRAINING ===")

# # Start training
# training_results = trainer.train()

# print("✅ Training completed!")
# print(f"Final training loss: {training_results.training_loss:.4f}")
# print(f"Training steps: {training_results.global_step}")
```


```python
# # Save training results and model
# print("=== SAVING TRAINING RESULTS ===")

# # Create training output directory
# training_output_dir = Path(f"./training_results_{CONFIG['experiment_id']}")
# training_output_dir.mkdir(exist_ok=True)

# # Save training history
# training_history_path = training_output_dir / "training_history.json"
# training_history = {
#     "training_loss": training_results.training_loss,
#     "global_step": training_results.global_step,
#     "training_time": str(training_results.metrics.get('train_runtime', 'unknown')),
#     "log_history": trainer.state.log_history
# }

# with open(training_history_path, 'w') as f:
#     json.dump(training_history, f, indent=2, default=str)

# # Save model locally
# local_model_path = training_output_dir / "trained_model"
# trainer.save_model(str(local_model_path))
# tokenizer.save_pretrained(str(local_model_path))

# print(f"✅ Training results saved to: {training_output_dir}")
# print(f"   - Training history: {training_history_path}")
# print(f"   - Model: {local_model_path}")
```


```python
# # Perform final inference with trained model
# print("=== FINAL INFERENCE ===")

# # The trainer already has the best model loaded
# # Prepare the same evaluation subset
# prepared_inputs_final = prepare_inference_batch(
#     messages_batch, 
#     tokenizer, 
#     max_length=CONFIG["max_length"]
# )

# # Apply padding
# padded_inputs_final = apply_batch_padding(prepared_inputs_final, tokenizer)

# # Run final inference
# final_responses, final_metadata = run_inference(
#     trainer.model, tokenizer, padded_inputs_final
# )

# # Format final results
# final_results = []
# for i, sample in enumerate(eval_subset):
#     final_results.append({
#         "id": sample["id"],
#         "expected_output": sample["expected_output"],
#         "model_response": final_responses[i],
#         "metadata": sample["metadata"]
#     })

# print(f"✅ Final inference completed on {len(final_results)} samples")
# print(f"Avg inference time: {final_metadata['avg_inference_time_per_sample']:.2f}s")

# # Evaluate final results
# final_metrics = evaluate_results(final_results, CONFIG, "Final")

# # Compare with baseline
# print(f"\n=== PERFORMANCE COMPARISON ===")
# print(f"Baseline Accuracy: {baseline_metrics['verdict_accuracy']:.3f}")
# print(f"Final Accuracy: {final_metrics['verdict_accuracy']:.3f}")
# print(f"Improvement: {final_metrics['verdict_accuracy'] - baseline_metrics['verdict_accuracy']:.3f}")

# if CONFIG["include_eln"]:
#     print(f"Baseline ELN Accuracy: {baseline_metrics.get('eln_accuracy', 'N/A')}")
#     print(f"Final ELN Accuracy: {final_metrics.get('eln_accuracy', 'N/A')}")
```


```python
# # Save final results
# print("=== SAVING FINAL RESULTS ===")

# # Save final inference results
# final_results_path = training_output_dir / "final_results.json"
# with open(final_results_path, 'w') as f:
#     json.dump(final_results, f, indent=2)

# # Save final metadata
# final_metadata_path = training_output_dir / "final_metadata.json"
# final_metadata.update(final_metrics)  # Include metrics
# with open(final_metadata_path, 'w') as f:
#     json.dump(final_metadata, f, indent=2, default=str)

# # Save comparison results
# comparison_results = {
#     "baseline_metrics": baseline_metrics,
#     "final_metrics": final_metrics,
#     "improvement": {
#         "verdict_accuracy": final_metrics['verdict_accuracy'] - baseline_metrics['verdict_accuracy'],
#         "verdict_f1": final_metrics['verdict_f1'] - baseline_metrics['verdict_f1']
#     }
# }

# if CONFIG["include_eln"]:
#     comparison_results["improvement"]["eln_accuracy"] = final_metrics.get('eln_accuracy', 0) - baseline_metrics.get('eln_accuracy', 0)

# comparison_path = training_output_dir / "performance_comparison.json"
# with open(comparison_path, 'w') as f:
#     json.dump(comparison_results, f, indent=2, default=str)

# print(f"✅ Final results saved:")
# print(f"   - Results: {final_results_path}")
# print(f"   - Metadata: {final_metadata_path}")
# print(f"   - Comparison: {comparison_path}")
```
