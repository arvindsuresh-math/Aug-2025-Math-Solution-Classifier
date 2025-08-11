import json
import re
from pathlib import Path
from typing import Dict, Any, List
import pandas as pd
from IPython.display import display, Markdown
from datasets import load_dataset

import os
import openai
import google.generativeai as genai
import anthropic
import asyncio
import nest_asyncio
from openai import AsyncOpenAI
from anthropic import AsyncClient
from dotenv import load_dotenv

import time
import math
import random
import datetime
from tqdm.notebook import tqdm

# --- API Client and Concurrency Configuration --- #

# This must be done once per kernel to allow asyncio to run in a Jupyter notebook..
nest_asyncio.apply()

# Load API Keys from .env file
load_dotenv()
print("Loaded environment variables from .env file.")

# Initialize Asynchronous API Clients
try:
    openai_client_async = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    anthropic_client_async = AsyncClient(api_key=os.getenv("ANTHROPIC_API_KEY"))
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    print("API clients initialized successfully.")
except TypeError:
    print("API key not found for one or more services. Please check your .env file.")
    # Assign None to prevent errors in subsequent cells
    openai_client_async = None
    anthropic_client_async = None

# Define API Concurrency Limits to prevent 429 "Too Many Requests" errors.
API_CONCURRENCY_LIMITS = {
    "google": 2,    # Gemini API has low RPM limits, so keep this low.
    "anthropic": 2, # Anthropic's token-based limits are complex, 2 is a safe start.
    "openai": 2,    # OpenAI APIs are generally more permissive.
}
print(f"API concurrency limits set to: {API_CONCURRENCY_LIMITS}")

MODEL_DICT = {
    "anthropic": "claude-sonnet-4-20250514",
    # "google": "gemini-2.5-pro"
    }

MODELS = [f"{provider}_{model}" for provider, model in MODEL_DICT.items()]
print(f"Available models: {MODELS}")


# --- Set directories and paths --- #

def find_project_root():
    """Traverse upwards to find the project root, marked by the .git folder."""
    current_path = Path.cwd()
    while current_path != current_path.parent:
        if (current_path / ".git").is_dir():
            return current_path
        current_path = current_path.parent
    raise FileNotFoundError("Could not find project root. Is this a git repository?")

PROJECT_ROOT = find_project_root()
DATA_DIR = PROJECT_ROOT / 'data'
SAMPLE_MANIFESTS_DIR = DATA_DIR / 'sample_manifests'
MANIFEST_OUTPUT_DIR = DATA_DIR / 'generated_manifests_raw'
MANIFEST_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
SOURCE_DIR = DATA_DIR / 'generated_manifests_raw'
DEST_DIR = DATA_DIR / 'generated_manifests_json'

# Create the destination directory if it doesn't exist
DEST_DIR.mkdir(parents=True, exist_ok=True)
print(f"Source directory: {SOURCE_DIR}")
print(f"Destination directory for cleaned JSON: {DEST_DIR}")

print(f"Project root found at: {PROJECT_ROOT}")
print(f"Data directory found at: {DATA_DIR}")
print(f"Sample manifests directory found at: {SAMPLE_MANIFESTS_DIR}")
print(f"Raw manifest output directory set to: {MANIFEST_OUTPUT_DIR}")
print(f"Source directory for raw manifests: {SOURCE_DIR}")
print(f"Destination directory for manifest json files: {DEST_DIR}")

# Load the GSM8K dataset
GSM8K_TRAIN = load_dataset("gsm8k", "main", split="train")

# Few shot example indices (chosen for maximum diversity)
EXAMPLE_INDICES = [54, 72, 310]

# Indices to generate manifests for
INDICES_TO_GENERATE = list(range(10)) 


# --- Helper Functions for Manifest loading and displaying --- #

def build_solution_mapping(
        index: int, 
        dataset: 'datasets.Dataset' = GSM8K_TRAIN,
        exclude_FA: bool = True
    ) -> Dict[str, str]:
    """
    Extracts the natural language solution for a given problem index,
    cleans it, and structures it into a line-numbered dictionary.
    """
    solution_mapping = {}
    solution_text = dataset[index]["answer"]
    lines = [ln.strip() for ln in solution_text.splitlines() if ln.strip()]

    # Improved regex to handle commas in the final answer
    if lines and re.match(r"^####\s*[\d\.,]+$", lines[-1]):
        solution_mapping["FA"] = lines.pop(-1).strip()

    for i, line in enumerate(lines, 1):
        solution_mapping[f"L{i}"] = line

    if exclude_FA and "FA" in solution_mapping:
        del solution_mapping["FA"]

    return solution_mapping

def load_manifest(index: int, manifest_dir: Path):
    """Loads the manifest for a given index."""
    manifest_path = manifest_dir / f'_{index}.json'
    if not manifest_path.exists():
        raise FileNotFoundError(f"Manifest for index {index} not found at {manifest_path}")
    with open(manifest_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def display_manifest(
        index: int, 
        manifest_dir: Path, 
        dataset: 'datasets.Dataset' = GSM8K_TRAIN):
    """Loads and displays the final, streamlined Formalization Manifest."""
    try:
        manifest = load_manifest(index, manifest_dir)

        # --- Extract info and display Top-Level ---
        code = manifest.get('function_code', '# Code not found')
        display(Markdown(f"### Manifest for Index: **{index}**"))
        display(Markdown("#### Question"))
        display(Markdown(f"> {dataset[index]['question']}"))

        # --- Display Function Code ---
        display(Markdown("#### Function Code"))
        display(Markdown(f"```python\n{code}\n```"))

        # --- Display Logical Steps in a DataFrame ---
        display(Markdown("#### Logical Steps"))
        steps = manifest.get('logical_steps', [])
        if not steps:
            print("No logical steps found in the manifest.")
            return
        
        df_steps = pd.DataFrame(steps)
        original_solution = build_solution_mapping(
            index=index, 
            dataset=dataset, 
            exclude_FA=True
        )
        
        df_steps['original_solution_line'] = df_steps['line_number'].apply(
            lambda ln: original_solution.get(ln, "N/A")
        )
        
        column_order = [
            'line_number', 
            'original_solution_line',
            'solution_line_template',
            'new_inputs',
            'output_variable'
        ]
        
        existing_columns_ordered = [col for col in column_order if col in df_steps.columns]
        df_steps = df_steps[existing_columns_ordered]
        
        pd.set_option('display.max_colwidth', None)
        display(df_steps)
    except Exception as e:
        print(f"An error occurred: {e}")

def display_generated_manifest(
        index: int, 
        model_name: str,
        manifest_dir: Path = DEST_DIR):
    """
    Loads and displays a generated manifest from a specific model and index.

    Args:
        index: The problem index.
        model_name: The name of the model (e.g., 'openai_gpt-4.1-mini').
    """
    try:
        # Construct the path to the specific JSON file
        manifest_path = manifest_dir / str(index) / f"{model_name}.json"
        
        if not manifest_path.exists():
            print(f"❌ Error: Manifest file not found at {manifest_path}")
            return

        with open(manifest_path, 'r', encoding='utf-8') as f:
            manifest = json.load(f)

        # --- Display Top-Level Information ---
        display(Markdown(f"# Generated Manifest for Index: `{index}` | Model: `{model_name}`"))
        display(Markdown("## Question"))
        display(Markdown(f"> {GSM8K_TRAIN[index]['question']}"))

        # --- Display Function Code ---
        code = manifest.get('function_code', '# Code not found')
        display(Markdown("## Function Code"))
        display(Markdown(f"```python\n{code}\n```"))

        # --- Display Logical Steps in a DataFrame ---
        display(Markdown("## Logical Steps"))
        steps = manifest.get('logical_steps', [])
        if not steps:
            print("No logical steps found in the manifest.")
            return
        
        df_steps = pd.DataFrame(steps)
        
        # Get the original solution text for comparison
        original_solution = build_solution_mapping(index=index, exclude_FA=True)
        
        df_steps['original_solution_line'] = df_steps['line_number'].apply(
            lambda ln: original_solution.get(ln, "N/A")
        )
        
        column_order = [
            'line_number', 
            'original_solution_line',
            'solution_line_template',
            'new_inputs',
            'output_variable'
        ]
        
        # Ensure columns exist before reordering
        existing_columns = [col for col in column_order if col in df_steps.columns]
        df_steps = df_steps[existing_columns]
        
        pd.set_option('display.max_colwidth', None)
        display(df_steps)

    except Exception as e:
        print(f"An error occurred while displaying the manifest for index {index}, model {model_name}: {e}")

def process_and_clean_manifests(
    source_dir: Path = SOURCE_DIR,
    dest_dir: Path = DEST_DIR
):
    """
    Traverses the source directory, cleans raw .txt model outputs,
    validates them as JSON, and writes them as .json files to the destination.

    - If a ```json ... ``` fence is found, its content is extracted.
    - Otherwise, the entire file content is used.
    - The extracted string is validated as JSON before being written.
    """
    if not source_dir.is_dir():
        print(f"❌ Error: Source directory '{source_dir}' not found.")
        return

    files_processed = 0
    files_written = 0
    files_failed = 0

    # Regex to find a JSON block fenced by ```json ... ``` or ``` ... ```
    # It is non-greedy and handles potential whitespace.
    _JSON_FENCE_RE = re.compile(r"```(?:json)?\s*\r?\n(.*?)\r?\n```", re.DOTALL)
    
    # Recursively find all .txt files in the source directory and its subfolders
    for txt_path in sorted(source_dir.rglob("*.txt")):
        files_processed += 1
        cleaned_json_str = ""
        
        try:
            # Determine the corresponding output path, preserving subdirectories
            relative_path = txt_path.relative_to(source_dir)
            dest_path = dest_dir / relative_path.with_suffix('.json')
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Read the raw content from the source file
            raw_content = txt_path.read_text(encoding="utf-8")

            # Try to find and extract a fenced JSON block
            match = _JSON_FENCE_RE.search(raw_content)
            if match:
                cleaned_json_str = match.group(1).strip()
                print(f"✓ Extracted fenced JSON from: {relative_path}")
            else:
                # If no fence is found, assume the whole file is the JSON string
                cleaned_json_str = raw_content.strip()
                print(f"⚠ No fence found, using full file: {relative_path}")

            # Validate that the extracted string is valid JSON before writing
            json.loads(cleaned_json_str) # This will raise an error if invalid
            
            # Write the clean, valid JSON to the destination file
            dest_path.write_text(cleaned_json_str, encoding="utf-8")
            files_written += 1

        except json.JSONDecodeError:
            print(f"❌ Invalid JSON content in: {relative_path}. File not written.")
            files_failed += 1
        except Exception as e:
            print(f"❌ An unexpected error occurred while processing {relative_path}: {e}")
            files_failed += 1
    
    print("\n--- Processing Complete ---")
    print(f"Total files found: {files_processed}")
    print(f"Successfully written: {files_written}")
    print(f"Failed to process: {files_failed}")

def concat_json_texts(
        indices: List[int], 
        model_name: str, 
        parent_dir: Path):
    """
    Reads JSON files for the given indices and model_name from parent_dir,
    concatenates their text content, and returns as a single string.
    """
    parent_dir = Path(parent_dir)
    all_text = []
    for idx in indices:
        file_path = parent_dir / str(idx) / f"{model_name}.json"
        if file_path.exists():
            text = file_path.read_text(encoding="utf-8")
            all_text.append(text)
        else:
            print(f"Warning: File not found: {file_path}")
    return "\n".join(all_text)

def save_concatenated_outputs(
        indices: List[int] = INDICES_TO_GENERATE, 
        models: List[str] = MODELS, 
        parent_dir: Path = DEST_DIR):
    """
    Concatenates the JSON outputs for each model and saves them as text files.
    
    Args:
        models: List of model names to process.
        parent_dir: Directory where the JSON files are stored.
    """
    outputs = {}
    for model in models:
        try:
            outputs[model] = concat_json_texts(
                indices=indices, 
                model_name=model, 
                parent_dir=parent_dir
            )
            print(f"Concatenated output for model {model} with {len(outputs[model])} characters.")
        except Exception as e:
            print(f"Error processing model {model}: {e}")

    # Save as text files
    for model, text in outputs.items():
        output_path = SAMPLE_MANIFESTS_DIR / f"{model}_output.txt"
        output_path.write_text(text, encoding='utf-8')
        print(f"Saved concatenated output for {model} to {output_path}")


# --- Models --- #

model_dict = {
    "anthropic": ["claude-sonnet-4-20250514", "claude-3-5-sonnet-20241022"],
    "openai": ["gpt-4.1-mini", "gpt-4.1"],
    "google": ["gemini-2.5-pro", "gemini-2.5-flash"]
}

models = [f"{provider}_{model}" for provider, model_list in model_dict.items() for model in model_list]

# --- Prompts --- #

SYSTEM_PROMPT = """You are a data formalization expert who excels in mathematical reasoning and writing python code. You will be presented with math word problems accompanied by step-by-step natural language solutions. You goal is to carefully and meticulously analyze the given question and solution, and formalize it by converting it into a structured json object that deconstructs the logic of the solution.

You MUST follow all rules and formatting instructions provided in the user prompt without deviation. Your entire output MUST be a single JSON object wrapped in ```json ... ```. Do not include any text or explanation before or after the JSON object."""

FORMAT_GUIDELINES = """In the TASK below, you will be given a math problem and its corresponding step-by-step solution. Each step in the solution is numbered (e.g. "L1", "L2" and so on), and many of the steps include calculator annotations (e.g. "<<20*0.1=2>>"). Your goal is to convert this information into a structured JSON object according to the following schema and detailed instructions.

# JSON Schema Definition

Your output must adhere to the following JSON structure:

```json
{
  "function_code": "A single string containing a complete, self-contained Python function that constitutes an end-to-end formalization of the solution.",
  "logical_steps": [
    {
      "line_number": "The line number from the original solution (e.g., 'L1', 'L2').",
      "question_inputs": "A (possibly empty) list of variable names extracted from the question text, used for the first time in this step.",
      "WK_inputs": "A (possibly empty) list of variable names from 'world knowledge' (e.g., minutes_per_hour), used for the first time in this step.",
      "output_variable": "The name of the variable being assigned as the result of the main computation in this step.",
      "solution_line_template": "The complete original line from the solution, including the calculator annotation, with all computational numbers replaced by `{variable_name}` placeholders."
    }
  ]
}
```

# Detailed Field Instructions

## "function_code"

This string must contain a Python function with the following characteristics:

1.  **Conditional Imports:** The function_code string should contain no imports, with one exception: if the function body uses the Fraction class (e.g., rate = Fraction(1, 10)), then the very first line of the function_code string MUST be from fractions import Fraction. If not, then the very first line MUST be the function definition (i.e. `def solve():`).

2.  **Function Naming & Docstring:** The function must be named `solve`, and it should not have any args. It must begin with a docstring that has exactly two lines:
    *   The first line must be: "Index: [Index]." using the index from the task header.
    *   The second line must be a succinct, one-sentence description of what the function returns (e.g., "Returns: the total cost of wages and taxes.").

3.  **Line comments:** For each solution line that is used to compute the final answer, include a comment of the form `# L1`, `# L2` and so on, which references the line number.
    *   Such a comment must immediately be followed by a code block that precisely formalizes the corresponding solution line.
    *   If a solution line does not contain any computation relevant to the final answer, then omit it completely from the function code and do NOT add a corresponding line comment.

4.  **Code blocks:** Each code block must consist of the following:
    *   First, define any new input variables needed for the computation. These fall into two categories:
        *   **Question Inputs:** These are variables whose values are stated in or can be extracted from the `question` text. Each `question_input` variable definition MUST be followed on the same line by a comment (`#`) that quotes or refers to the phrase in the `question` from which it is extracted.
        *   **World Knowledge Inputs:** These are variables drawn from common-sense "world knowledge" (e.g. `minutes_per_hour = 60`). The comment for these variables MUST simply say `# WK`.
    *   Second, there should be EXACTLY ONE line of code which formalizes the computation in the solution line and assigns the resulting value to a new variable (this is the `output_variable`).

5.  **The Direct Substitution Rule:** This is the most important rule, which ensures that the `nl_template` is purely identical to the original solution line except that numerical values in computations have been replaced with variable placeholders: You MUST define variables in such a way that they can be DIRECTLY SUBSTITUTED into the solution text without changing any operators. For example:
    *   If the solution line has a computation like `... / 5`, you MUST define a variable like `var = 5`.
    *   If the solution line has a computation like `... * 1/5`, you MUST define a variable like `var = Fraction(1, 5)`.
    *   If the solution line has a computation like `... * 0.2`, you MUST define a variable like `var = 0.2`.

6.  **Final Answer:** The line that assigns the final result to the `answer` variable must be immediately preceded by a line containing only the comment `# FA`. The last line of the function must always return the `answer` variable.

## "solution_line_template"

These artifacts will serve as precise links between the solution line and the code line.
*   The template should be EXACTLY identical to the original solution line, with the ONLY CHANGES being that every numerical value used in a computation is replaced by its corresponding `{variable_name}` placeholder. This applies to the entire content of the solution line, including the inside and outside of the calculator annotations.
*   In particular, EVERY SINGLE numerical value appearing inside the calculator annotation MUST be replaced with a `{variable_name}` placeholder.
*   Note: The Direct Substitution Rule will ensure that for correctly defined variables, it will be possible to replace the numerical values with variable name placeholders while leaving all surrounding text, symbols, and operators unchanged.
*   Thus, in a correct `nl_template`, the calculator annotation will not contain any numerical values, and moreover, replacing each `{variable_name}` by its value should exactly recover the original solution line, including the original calculator annotation.
*   Note: If a number appears in different forms (e.g., as "10%" in the narrative and as ".1" in the calculation), only the form that appears in the calculation should be replaced with a placeholder.
"""

def assemble_example(
    index: int, 
    manifest_dir: Path, 
    dataset: 'datasets.Dataset'
) -> str:
    """
    Assembles a single, complete few-shot example string (Input + Output). 
    Returns a formatted string for one few-shot example.
    """
    try:
        # 1. Construct the Input block
        question = dataset[index]['question']
        solution_map = build_solution_mapping(index, dataset, exclude_FA=True)
        
        input_data = {
            "index": index,
            "question": question,
            "solution_mapping": solution_map
        }
        
        input_json_str = json.dumps(input_data, indent=2)
        input_block = f"**Input:**\n\n{input_json_str}\n"

        # 2. Construct the Output block
        manifest_path = manifest_dir / f'_{index}_alt.json'
        with open(manifest_path, 'r', encoding='utf-8') as f:
            manifest_content = json.load(f)
        
        output_json_str = json.dumps(manifest_content, indent=2)
        output_block = f"**Output:**\n```json\n{output_json_str}\n```"

        return f"{input_block}\n\n{output_block}"

    except Exception as e:
        print(f"Warning: Failed to assemble example for index {index}. Error: {e}")
        return "" # Return empty string on failure

def assemble_static_prefix(
    format_guidelines: str = FORMAT_GUIDELINES,
    example_indices: List[int] = EXAMPLE_INDICES,
    manifest_dir: Path = SAMPLE_MANIFESTS_DIR,
    dataset: 'datasets.Dataset' = GSM8K_TRAIN
) -> str:
    """
    Constructs the static user prompt prefix, including guidelines and few-shot examples.

    Args:
        format_guidelines: The string containing the rules and schema.
        example_indices: A list of integer indices for the few-shot examples.
        manifest_dir: The path to the manifest directory.
        dataset: The loaded Hugging Face dataset.

    Returns:
        A single string containing the complete user prompt.
    """
    # 1. Start with the guidelines
    prompt_parts = [format_guidelines, "\n---\n", "\n### Examples"]

    # 2. Assemble and append each few-shot example
    for index in example_indices:
        example_str = assemble_example(index, manifest_dir, dataset)
        if example_str:
            prompt_parts.append(f"\n\n---\n\n{example_str}")
            
    return "".join(prompt_parts) # Use join for efficiency

def assemble_user_prompt(
    index_to_generate: int,
    static_prefix: str,
    dataset: 'datasets.Dataset' = GSM8K_TRAIN
) -> str:
    """
    Appends the final task block to the static prefix to create a complete user prompt.

    Args:
        index_to_generate: The new problem index to generate a manifest for.
        static_prefix: The pre-computed string containing guidelines and few-shot examples.
        dataset: The loaded Hugging Face dataset.

    Returns:
        A single string containing the complete user prompt, ready for an API call.
    """
    # 1. Assemble the final input block for the new task
    try:
        question = dataset[index_to_generate]['question']
        solution_map = build_solution_mapping(
            index=index_to_generate, 
            dataset=dataset, 
            exclude_FA=True
        )
        
        task_input_data = {
            "index": index_to_generate,
            "question": question,
            "solution_mapping": solution_map
        }
        task_input_json_str = json.dumps(task_input_data, indent=2)
        
        # This is the final part of the prompt that asks the model for the new output
        task_block = f"\n\n--- TASK ---\n\n**Input:**\n\n{task_input_json_str}\n\n**Output:**"

    except Exception as e:
        print(f"Error: Could not assemble task block for index {index_to_generate}. Error: {e}")
        return "" # Return empty string on failure

    # 2. Combine the static prefix with the new task block
    return static_prefix + task_block

# Generate the static prefix ONCE.
STATIC_USER_PROMPT_PREFIX = assemble_static_prefix()
print(f"Static user prompt prefix generated successfully. Length: {len(STATIC_USER_PROMPT_PREFIX)} characters.")


# --- Code for API calls to generate manifests --- #



# --- 1. Helper Functions (Unchanged) ---
# These two helpers are generic and can be used by any provider's function.

_anthropic_bucket = {"tokens": 50_000, "reset_at": time.monotonic() + 60}

async def _anthropic_throttle(tokens_needed: int):
    # (Code for this function is unchanged)
    global _anthropic_bucket
    while True:
        now = time.monotonic()
        if now >= _anthropic_bucket["reset_at"]:
            _anthropic_bucket = {"tokens": 50_000, "reset_at": now + 60}
        if tokens_needed <= _anthropic_bucket["tokens"]:
            _anthropic_bucket["tokens"] -= tokens_needed
            return
        else:
            to_sleep = _anthropic_bucket["reset_at"] - now
            await asyncio.sleep(max(to_sleep, 0.01))

async def with_api_retries(send_coroutine_factory, *, max_attempts: int = 10, base_wait_seconds: int = 5):
    # (Code for this function is unchanged)
    for attempt in range(max_attempts):
        try:
            return await send_coroutine_factory()
        except (openai.RateLimitError, anthropic.RateLimitError, Exception) as e:
            if isinstance(e, (openai.RateLimitError, anthropic.RateLimitError)) or "429" in str(e):
                if attempt == max_attempts - 1:
                    raise
                wait_time = base_wait_seconds * (2 ** attempt) + random.uniform(0, 1)
                print(f"🕒 Rate limit error encountered. Retrying in {wait_time:.2f} seconds... (Attempt {attempt + 1}/{max_attempts})")
                await asyncio.sleep(wait_time)
            else:
                raise
    return None

# --- 2. NEW: Provider-Specific API Calling Functions ---

async def call_openai_async(model: str, system_prompt: str, user_prompt: str) -> (str, Dict[str, int]):
    """Handles an API call to OpenAI."""
    messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}]
    response = await with_api_retries(lambda: openai_client_async.chat.completions.create(
        model=model, messages=messages, temperature=0.1, max_tokens=4000, response_format={"type": "json_object"}
    ))
    
    text_response = response.choices[0].message.content
    usage = {"input_tokens": 0, "output_tokens": 0, "cached_tokens": 0}
    if response.usage:
        usage["input_tokens"] = response.usage.prompt_tokens
        usage["output_tokens"] = response.usage.completion_tokens
        if hasattr(response.usage, 'prompt_tokens_details') and response.usage.prompt_tokens_details:
             usage["cached_tokens"] = response.usage.prompt_tokens_details.get("cached_tokens", 0)
    return text_response, usage

async def call_google_async(model: str, system_prompt: str, user_prompt: str) -> (str, Dict[str, int]):
    """Handles an API call to Google."""
    gemini = genai.GenerativeModel(model_name=model, system_instruction=system_prompt)
    cfg = genai.types.GenerationConfig(temperature=0.1, max_output_tokens=4000)
    response = await with_api_retries(lambda: gemini.generate_content_async(user_prompt, generation_config=cfg))

    text_response = response.text
    usage = {"input_tokens": 0, "output_tokens": 0, "cached_tokens": 0}
    if response.usage_metadata:
        usage["input_tokens"] = response.usage_metadata.prompt_token_count
        usage["output_tokens"] = response.usage_metadata.candidates_token_count
    return text_response, usage

async def call_anthropic_async(model: str, system_prompt: str, user_prompt: str) -> (str, Dict[str, int]):
    """Handles an API call to Anthropic, including prompt caching."""
    system_block = {"type": "text", "text": system_prompt, "cache_control": {"type": "ephemeral"}}
    
    est_tokens = math.ceil(1.2 * len(system_prompt.split()))
    await _anthropic_throttle(est_tokens)

    response = await with_api_retries(lambda: anthropic_client_async.messages.create(
        model=model, max_tokens=4000, temperature=0.1,
        system=[system_block], messages=[{"role": "user", "content": user_prompt}],
    ))

    text_response = response.content[0].text
    usage = {"input_tokens": 0, "output_tokens": 0, "cached_tokens": 0}
    if response.usage:
        usage["input_tokens"] = response.usage.input_tokens
        usage["output_tokens"] = response.usage.output_tokens
        usage["cached_tokens"] = response.usage.cache_read_input_tokens if response.usage.cache_read_input_tokens else 0
    return text_response, usage


# --- 3. UPDATED: Per-Problem Orchestration (Dispatcher Logic) ---

async def run_one_problem_async(
    index: int, 
    static_prefix: str,
    system_prompt: str,
    model_dict: Dict[str, str],
    provider_sems: Dict[str, asyncio.Semaphore], 
    output_dir: Path,
    pbar: tqdm
) -> List[Dict]:
    """
    Generates manifests for a single problem and returns a list of result dictionaries.
    """
    user_prompt = assemble_user_prompt(index, static_prefix=static_prefix)
    
    # This list is now local to this function
    problem_results = []
    
    tasks = []
    for provider, model in model_dict.items():
        async with provider_sems[provider]: # Acquire semaphore before creating the task
            if provider == "openai":
                coro = call_openai_async(model, system_prompt, user_prompt)
            elif provider == "google":
                coro = call_google_async(model, system_prompt, user_prompt)
            elif provider == "anthropic":
                coro = call_anthropic_async(model, system_prompt, user_prompt)
            else:
                # Create a coroutine that will immediately raise an error
                async def unknown_provider(): raise ValueError(f"Unknown provider: {provider}")
                coro = unknown_provider()
        
            task = asyncio.create_task(coro)
            task.meta = {"provider": provider, "model": model, "index": index, "start_time": time.time()}
            tasks.append(task)
        
    task_results = await asyncio.gather(*tasks, return_exceptions=True)
    
    for task, result in zip(tasks, task_results):
        meta = task.meta
        elapsed = time.time() - meta["start_time"]
        status = "Failed"
        usage = {"input_tokens": 0, "output_tokens": 0, "cached_tokens": 0}
        
        output_path = output_dir / str(meta['index']) / f"{meta['provider']}_{meta['model']}.txt"
        output_path.parent.mkdir(parents=True, exist_ok=True)

        if isinstance(result, Exception):
            error_message = f"--- ERROR ---\nIndex: {meta['index']}, Model: {meta['model']}\n{type(result).__name__}: {result}"
            output_path.write_text(error_message, encoding='utf-8')
            print(f"❌ Error for Index {meta['index']}, Model {meta['model']}: {type(result).__name__}")
        else:
            text_response, usage = result
            output_path.write_text(text_response, encoding='utf-8')
            status = "Success"
        
        # Append to the local list instead of a shared one
        problem_results.append({
            "provider": meta["provider"], "model": meta["model"], "index": meta["index"],
            "status": status, "time_s": round(elapsed, 2),
            "input_tokens": usage["input_tokens"], "output_tokens": usage["output_tokens"],
            "cached_tokens": usage["cached_tokens"],
            "utc_completed": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
        })
    
    pbar.update(1)
    # Explicitly return the results for this specific problem
    return problem_results


# --- 4. UPDATED: Main Batch Generation Function ---

async def generate_manifests_parallel(
    indices_to_generate: List[int],
    model_dict: Dict[str, str] = MODEL_DICT,
    system_prompt: str = SYSTEM_PROMPT,
    output_dir: Path = MANIFEST_OUTPUT_DIR,
    concurrency_limits: Dict[str, int] = API_CONCURRENCY_LIMITS
) -> pd.DataFrame:
    """
    Runs the manifest generation process and returns a DataFrame with performance stats.
    """
    print("--- Starting Manifest Generation ---")
    start_time = time.time()
    
    static_prefix = assemble_static_prefix()
    provider_semaphores = {prov: asyncio.Semaphore(limit) for prov, limit in concurrency_limits.items()}
    
    with tqdm(total=len(indices_to_generate), desc="Generating Manifests") as pbar:
        problem_tasks = [
            run_one_problem_async(
                index=idx, static_prefix=static_prefix, system_prompt=system_prompt,
                model_dict=model_dict, provider_sems=provider_semaphores,
                output_dir=output_dir, pbar=pbar
            )
            for idx in indices_to_generate
        ]
        # This will now be a list of lists, e.g., [[results_for_p0], [results_for_p1], ...]
        all_results = await asyncio.gather(*problem_tasks)

    # Flatten the list of lists into a single list of result dictionaries
    flat_results = [item for sublist in all_results for item in sublist]

    # Create and save the performance DataFrame
    df = pd.DataFrame(flat_results)
    run_ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d_%H%M%S")
    csv_path = output_dir / f"generation_performance_{run_ts}.csv"
    df.to_csv(csv_path, index=False)
    
    end_time = time.time()
    print(f"\n--- Manifest Generation Complete ---")
    print(f"Processed {len(indices_to_generate)} indices in {end_time - start_time:.2f} seconds.")
    print(f"Performance log saved to: {csv_path}")
    
    return df

# Convert to json and save to the destination directory
process_and_clean_manifests()

# Concatenate outputs for each model and save as text files
save_concatenated_outputs()