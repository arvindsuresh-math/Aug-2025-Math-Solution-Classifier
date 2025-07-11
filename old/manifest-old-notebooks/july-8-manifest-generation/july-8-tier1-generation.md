### Basic imports


```python
import json
import re
from pathlib import Path
from typing import Dict, Any, List
import pandas as pd
from IPython.display import display, Markdown
from datasets import load_dataset
```

### Directories and Paths


```python
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
MANIFEST_OUTPUT_DIR = DATA_DIR / "july-8-manifests-raw"
SAMPLE_MANIFEST_DIR = DATA_DIR / "july-7-sample-manifests"
TIER_OUTPUT_DIRS = {f"tier{i}": MANIFEST_OUTPUT_DIR / f"tier{i}" for i in range(1, 6)}
TIER_SAMPLE_DIRS = {f"tier{i}": SAMPLE_MANIFEST_DIR / f"tier{i}" for i in range(1, 6)}

# Make the directory for the tier if it doesn't exist
for tier_dir in TIER_OUTPUT_DIRS.values():
    tier_dir.mkdir(parents=True, exist_ok=True)

for tier_dir in TIER_SAMPLE_DIRS.values():
    tier_dir.mkdir(parents=True, exist_ok=True)

print(f"Project root found at: {PROJECT_ROOT}")
print(f"Data directory found at: {DATA_DIR}")
print(f"Raw manifest output directory set to: {MANIFEST_OUTPUT_DIR}")
```

    Project root found at: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math
    Data directory found at: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data
    Raw manifest output directory set to: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/july-8-manifests-raw


### Loading the dataset


```python
# Load the GSM8K dataset
GSM8K_TRAIN = load_dataset("gsm8k", "main", split="train")
```

### Generating tier lists


```python
def has_computational_division(solution_text: str) -> bool:
    """Returns True if a '/' is followed by optional whitespace and then a digit."""
    pattern = re.compile(r'/\s*\d')
    return bool(pattern.search(solution_text))

def has_float(solution_text: str) -> bool:
    """Returns True if the solution text contains a floating-point number."""
    pattern = re.compile(r'(?<!\d)\.\d+|\d+\.\d+')
    return bool(pattern.search(solution_text))

def is_symbolic(solution_text: str) -> bool:
    """Returns True if the solution contains a symbolic reasoning line (Let @ ...)."""
    pattern = re.compile(r'^Let [a-zA-Z] ', re.MULTILINE)
    return bool(pattern.search(solution_text))

def mutually_disjoint_tiers(dataset):
    tiers = {}
    symbolic_set = set(
        idx for idx, sample in enumerate(dataset)
        if is_symbolic(sample.get("answer", ""))
    )
    non_symbolic_indices = [
        idx for idx in range(len(dataset)) if idx not in symbolic_set
    ]

    # Tier 1: Only integer arithmetic (no floats, no computational division)
    tiers["tier1"] = sorted([
        idx for idx in non_symbolic_indices
        if not has_float(dataset[idx].get("answer", "")) and not has_computational_division(dataset[idx].get("answer", ""))
    ])

    # Tier 2: Float arithmetic, no computational division
    tiers["tier2"] = sorted([
        idx for idx in non_symbolic_indices
        if has_float(dataset[idx].get("answer", "")) and not has_computational_division(dataset[idx].get("answer", ""))
    ])

    # Tier 3: Computational division, no floats
    tiers["tier3"] = sorted([
        idx for idx in non_symbolic_indices
        if not has_float(dataset[idx].get("answer", "")) and has_computational_division(dataset[idx].get("answer", ""))
    ])

    # Tier 4: Both floats and computational division
    tiers["tier4"] = sorted([
        idx for idx in non_symbolic_indices
        if has_float(dataset[idx].get("answer", "")) and has_computational_division(dataset[idx].get("answer", ""))
    ])

    # Tier 5: Symbolic reasoning (Let @ ...)
    tiers["tier5"] = sorted(symbolic_set)

    return tiers

TIER_LISTS = mutually_disjoint_tiers(GSM8K_TRAIN)

# Display the number of samples in each tier
for tier, indices in TIER_LISTS.items():
    print(f"{tier:<10}: {len(indices)} samples")
print(f"{'Total':<10}: {len(GSM8K_TRAIN)} samples")
```

    tier1     : 2767 samples
    tier2     : 837 samples
    tier3     : 3113 samples
    tier4     : 544 samples
    tier5     : 212 samples
    Total     : 7473 samples


### Load the system prompt and static prefixes for each tier's user prompt


```python
SYSTEM_PROMPT = """You are a data formalization expert who excels in mathematical reasoning and writing python code. You will be presented with a math word problem accompanied by a step-by-step natural language solution. You goal is to carefully and meticulously analyze the given question and solution, and formalize it by converting it into a structured json object that deconstructs the logic of the solution.

You MUST follow all rules and formatting instructions provided in the user prompt without deviation. Your entire output MUST be a single JSON object wrapped in ```json ... ```. Do not include any text or explanation before or after the JSON object."""

STATIC_PREFIXES = {}
for tier in TIER_LISTS.keys():
    prefix_file = TIER_SAMPLE_DIRS[tier] / f"{tier}_user_prompt_prefix.txt"
    with open(prefix_file, 'r', encoding='utf-8') as f:
        STATIC_PREFIXES[tier] = f.read()

# Display the prefix for tier 1
# print("Static prefix for tier 1:")
# print("="*50,"\n")
# print(STATIC_PREFIXES["tier1"])
```

### A simple function to append a chosen sample to a user prompt


```python
def build_solution_mapping(
        index: int, 
        dataset: 'datasets.Dataset' = GSM8K_TRAIN,
        exclude_FA: bool = True
    ):
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

def append_sample_to_user_prompt(
        tier: str, 
        index: int, 
        dataset: 'datasets.Dataset' = GSM8K_TRAIN
    ):
    """
    Appends a chosen sample from the GSM8K dataset to the user prompt for a specific tier. Returns the complete user prompt, ready to be sent to the LLM for manifest generation.
    """
    if tier not in TIER_LISTS:
        raise ValueError(f"Invalid tier: {tier}. Must be one of {list(TIER_LISTS.keys())}.")

    sample = dataset[index]
    question = sample['question']
    answer = build_solution_mapping(index, dataset)

    user_prompt = \
        STATIC_PREFIXES[tier] + \
        f"## Input\n\n" + \
        f"**Index**:\n{index}\n\n" + \
        f"**Question**:\n{question}\n\n" + \
        f"**Solution Mapping**:\n{answer}\n\n" + \
        f"## Output\n\n"

    return user_prompt

# Example usage
idx = TIER_LISTS["tier1"][0]  # Get the first index from tier 1
user_prompt = append_sample_to_user_prompt("tier1", idx, GSM8K_TRAIN)
print("User prompt for tier 1, index", idx, ":\n")
print(user_prompt)
```

    User prompt for tier 1, index 4 :
    
    In the TASK below, you will be given a math problem and its corresponding step-by-step solution. Each step in the solution is numbered (e.g. "L1", "L2" and so on), and many of the steps include calculator annotations (e.g. "<<20*0.1=2>>"). Your goal is to convert this information into a structured JSON object according to the following schema and detailed instructions.
    
    # JSON Schema Definition
    
    Your output must adhere to the following JSON structure:
    
    ```json
    {
      "function_code": "A single string containing a complete, self-contained Python function that constitutes an end-to-end formalization of the solution.",
      "logical_steps": [
        {
          "line_number": "The line number from the original solution (e.g., 'L1', 'L2').",
          "question_inputs": "A (possibly empty) list of variable names with values extracted from the question text, used for the first time in this step.",
          "WK_inputs": "A (possibly empty) list of variable names with values coming from 'world knowledge' (e.g., minutes_per_hour), used for the first time in this step.",
          "output_variable": "The name of the variable being assigned as the result of the main computation in this step.",
          "solution_line_template": "The complete original line from the solution, including the calculator annotation, with all computational numbers replaced by `{variable_name}` placeholders."
        }
      ]
    }
    ```
    
    # Detailed Field Instructions
    
    ## 1. "function_code"
    
    This string must contain a Python function with the following characteristics:
    
    *   **1.A. No Imports:** You should not have ANY imports. The very first line MUST be the function definition (i.e. `def solve():`).
    *   **1.B. Function Naming & Docstring:** The function must be named `solve`, and it should not have any args. It must begin with a docstring that has exactly two lines:
        *   **1.B.i.** The first line must be: "Index: [Index]." using the index from the task header.
        *   **1.B.ii.** The second line must be a succinct, one-sentence description of what the function returns (e.g., "Returns: the total cost of wages and taxes.").
    *   **1.C. Line comments:** For each solution line that is used to compute the final answer, include a comment of the form `# L1`, `# L2` and so on, which references the line number.
        *   **1.C.i.** Such a comment must immediately be followed by a code block that precisely formalizes the corresponding solution line. More details about code blocks are provided in 1.D below.
        *   **1.C.ii.** If a solution line does not contain any computation relevant to the final answer, then omit it completely from the function code and do NOT add a corresponding line comment.
    *   **1.D. Code blocks:** Each code block constitutes a complete formalization of its corresponding solution line. It must consist of the following:
        *   **1.D.i. Input Variables** First, define any NEW variables needed for the computation, i.e. that will be used for the first time in the solution. Each input variable MUST be followed by a comment (`#`) in the same line. These variables fall into two categories:
            *   "question_inputs": These are variables whose values are stated in or can be extracted from the question text (only the question text, NOT the answer text). The comment for these variables should quote or refer to the phrase in the question text from which it is extracted.
            *   "WK_inputs": These are variables drawn from common-sense "World Knowledge" (e.g. `minutes_per_hour = 60`, `dozen = 12`). The comment for these variables MUST simply say `# WK`.
        *   **1.D.ii. Output Variables** Second, there should be EXACTLY ONE line of code which formalizes the computation in the solution line and assigns the resulting value to a new variable (this is the "output_variable" field).
    *   **1.E. The Direct Substitution Rule:** This is the MOST IMPORTANT RULE, which ensures that the "solution_line_template" is purely identical to the original solution line except that numerical values in computations have been replaced with variable placeholders: You MUST define variables in such a way that they can be DIRECTLY SUBSTITUTED into the solution line without changing any operators or surrounding text in the line. 
    *   **1.F. Final Answer:** The line that assigns the final result to the `answer` variable must be immediately preceded by a line containing only the comment `# FA`. The last line of the function must always return the `answer` variable.
    
    ## 2. "solution_line_template"
    
    *   **2.A.** The template should be EXACTLY identical to the original solution line, with the ONLY CHANGES being that every NUMERICAL value used in a computation is replaced by its corresponding `{variable_name}` placeholder. This applies to the entire content of the solution line, including the inside and outside of the calculator annotations.
    *   **2.B.** In particular, EVERY SINGLE numerical value appearing inside the calculator annotation (`<<..>>`) MUST be replaced with a `{variable_name}` placeholder.
    *   **2.C.** Note: some quantities may appear as words in the solution line (e.g. "twice as many"). Do NOT attempt to replace these with variable name placeholders.
    *   **2.D.** The Direct Substitution Rule will ensure that for correctly defined variables, it will be possible to replace the numerical values with variable name placeholders while leaving all surrounding text, symbols, and operators unchanged. Thus, in a correct "solution_line_template", the calculator annotation will not contain any numerical values, and moreover, replacing each `{variable_name}` by its value should exactly recover the original solution line, including the original calculator annotation.
    
    # Examples
    
    Given below are three examples that illustrate what a perfect formalization will look like. For each example, you are given the following:
    
    *   Input: consisting of an index, question, and solution mapping. 
    *   Output: complete output, wrapped inside ```json .. ```
    
    In all examples, you will observe the following:
    *   A rigid adherence to the Direct Substitution Rule (1.E), resulting in a solution_line_template that perfectly satisfies properties 2.A - 2.D. For instance, in Example 1 below, "two dozen" is not formalized as a stand-alone variable because the computation in "L1" and "L4" treat "two" and "dozen" as separate variables.
    *   The function_code only uses solution lines with a relevant computation (rule 1.C.ii), and omits lines that are irrelevant (e.g. "L1" is ommitted in Example 3 below).
    *   Code blocks that are precisely formatted as in 1.D, consisting of line comments, then input variable declarations, then a single output variable assignment (i.e. the single computation for that solution line).
    *   A careful distinction between numerical values and word-based quantities in the solution_line_template. Per rule 2.C, only numerical values like 2 are replaced with placeholders, and word-based quantities are not, even though they are formalized as variables in the function_code (For example, in "L2" of Example 2, the word "Twice" remains in the solution_line_template).
    *   Precise categorization of input variables as described in rule 1.D.i. Note how `dozen = 12` is a WK_input (common knowledge), while `father_ate = 8` is a question_input (explicitly stated in the problem text).
    *   Strict adherence to defining only NEW variables in each step's question_inputs and WK_inputs lists. Observe that once a variable like `days_in_week` is defined in one step, it is simply re-used in later calculations without being re-defined or listed as an input again.
    *   Comments for question_inputs must cite the question text only, NEVER the solution text. For instance, in Example 3, even though "60 minutes in an hour" is stated in L1 of the solution, the variable `minutes_per_hour` is correctly labeled # WK because that fact is not present in the question text, and the number of minutes in an hour constitutes common-sense World Knowledge.
    
    ## Example 1
    
    ### Input
    
    **Index:**
    3946
    
    **Question:**
    Mother made 2 dozen brownies and placed them on the kitchen counter to cool.  Father smelled the brownies, came into the kitchen and ate 8 of them. Then, their daughter, Mooney, wandered into the kitchen and ate 4 of the brownies. The next morning, Mother made another two dozen brownies and added them to those remaining from the day before.  After that, how many brownies were on the counter?
    
    **Solution mapping:**
    {'L1': 'Two dozen brownies is 2 * 12 = <<2*12=24>>24 brownies.', 'L2': 'After Father ate his 8, there were 24 - 8 = <<24-8=16>>16 brownies remaining on the counter.', 'L3': 'After Mooney ate her 4, there were 16 - 4 = <<16-4=12>>12 brownies remaining on the counter.', 'L4': 'Mother made a second batch of two-dozen brownies, or 2 * 12 = <<2*12=24>>24 brownies.', 'L5': 'After Mother added the second two-dozen, there were 12 + 24 = <<12+24=36>>36 brownies on the kitchen counter.'}
    
    ### Output
    
    ```json
    {
      "function_code": "def solve():\n    \"\"\"Index: 3946.\n    Returns: the number of brownies on the counter at the end.\n    \"\"\"\n    # L1\n    num_dozen_initial = 2 # 2 dozen brownies\n    dozen = 12 # WK\n    initial_brownies = num_dozen_initial * dozen\n\n    # L2\n    father_ate = 8 # ate 8 of them\n    after_father = initial_brownies - father_ate\n\n    # L3\n    mooney_ate = 4 # ate 4 of the brownies\n    after_mooney = after_father - mooney_ate\n\n    # L4\n    num_dozen_second_batch = 2 # another two dozen brownies\n    second_batch = num_dozen_second_batch * dozen\n\n    # L5\n    total_brownies = after_mooney + second_batch\n\n    # FA\n    answer = total_brownies\n    return answer",
      "logical_steps": [
        {
          "line_number": "L1",
          "question_inputs": ["num_dozen_initial"],
          "WK_inputs": ["dozen"],
          "output_variable": "initial_brownies",
          "solution_line_template": "Two dozen brownies is {num_dozen_initial} * {dozen} = <<{num_dozen_initial}*{dozen}={initial_brownies}>>{initial_brownies} brownies."
        },
        {
          "line_number": "L2",
          "question_inputs": ["father_ate"],
          "WK_inputs": [],
          "output_variable": "after_father",
          "solution_line_template": "After Father ate his {father_ate}, there were {initial_brownies} - {father_ate} = <<{initial_brownies}-{father_ate}={after_father}>>{after_father} brownies remaining on the counter."
        },
        {
          "line_number": "L3",
          "question_inputs": ["mooney_ate"],
          "WK_inputs": [],
          "output_variable": "after_mooney",
          "solution_line_template": "After Mooney ate her {mooney_ate}, there were {after_father} - {mooney_ate} = <<{after_father}-{mooney_ate}={after_mooney}>>{after_mooney} brownies remaining on the counter."
        },
        {
          "line_number": "L4",
          "question_inputs": ["num_dozen_second_batch"],
          "WK_inputs": [],
          "output_variable": "second_batch",
          "solution_line_template": "Mother made a second batch of two-dozen brownies, or {num_dozen_second_batch} * {dozen} = <<{num_dozen_second_batch}*{dozen}={second_batch}>>{second_batch} brownies."
        },
        {
          "line_number": "L5",
          "question_inputs": [],
          "WK_inputs": [],
          "output_variable": "total_brownies",
          "solution_line_template": "After Mother added the second two-dozen, there were {after_mooney} + {second_batch} = <<{after_mooney}+{second_batch}={total_brownies}>>{total_brownies} brownies on the kitchen counter."
        }
      ]
    }
    ```
    
    ## Example 2
    
    ### Input
    
    **Index**:
    4258
    
    **Question**:
    Cowboy Mickey and cowgirl Minnie train horses for a living.  On average, Mickey mounts six less than twice as many horses per day as does Minnie,  while Minnie mounts three more horses per day than there are days in a week.  How many horses does Mickey Mount per week?
    
    **Solution mapping**:
    {'L1': 'If Minnie mounts three more horses per day than there are days in a week, then Minnie mounts 7+3=<<3+7=10>>10 horses per day.', 'L2': 'Twice as many horses per day as Minnie mounts is 10*2=<<10*2=20>>20 horses per day.', 'L3': 'If Mickey mounts six less than twice as many horses per day as does Minnie, then Mickey mounts 20-6=<<20-6=14>>14 horses per day.', 'L4': 'Since there are 7 days in a week, then Mickey mounts 7*14=<<7*14=98>>98 horses per week.'}
    
    ### Output
    
    ```json
    {
      "function_code": "def solve():\n    \"\"\"Index: 4258.\n    Returns: the number of horses Mickey mounts per week.\n    \"\"\"\n    # L1\n    days_in_week = 7 # WK\n    minnie_more_than_week = 3 # three more horses per day than there are days in a week\n    minnie_per_day = days_in_week + minnie_more_than_week\n\n    # L2\n    multiplier_for_twice = 2 # twice as many horses\n    twice_minnie = minnie_per_day * multiplier_for_twice\n\n    # L3\n    mickey_less_than_twice_minnie = 6 # six less than twice as many horses\n    mickey_per_day = twice_minnie - mickey_less_than_twice_minnie\n\n    # L4\n    mickey_per_week = mickey_per_day * days_in_week\n\n    # FA\n    answer = mickey_per_week\n    return answer",
      "logical_steps": [
        {
          "line_number": "L1",
          "question_inputs": ["minnie_more_than_week"],
          "WK_inputs": ["days_in_week"],
          "output_variable": "minnie_per_day",
          "solution_line_template": "If Minnie mounts three more horses per day than there are days in a week, then Minnie mounts {days_in_week}+{minnie_more_than_week}=<<{days_in_week}+{minnie_more_than_week}={minnie_per_day}>>{minnie_per_day} horses per day."
        },
        {
          "line_number": "L2",
          "question_inputs": ["multiplier_for_twice"],
          "WK_inputs": [],
          "output_variable": "twice_minnie",
          "solution_line_template": "Twice as many horses per day as Minnie mounts is {minnie_per_day}*{multiplier_for_twice}=<<{minnie_per_day}*{multiplier_for_twice}={twice_minnie}>>{twice_minnie} horses per day."
        },
        {
          "line_number": "L3",
          "question_inputs": ["mickey_less_than_twice_minnie"],
          "WK_inputs": [],
          "output_variable": "mickey_per_day",
          "solution_line_template": "If Mickey mounts six less than twice as many horses per day as does Minnie, then Mickey mounts {twice_minnie}-{mickey_less_than_twice_minnie}=<<{twice_minnie}-{mickey_less_than_twice_minnie}={mickey_per_day}>>{mickey_per_day} horses per day."
        },
        {
          "line_number": "L4",
          "question_inputs": [],
          "WK_inputs": [],
          "output_variable": "mickey_per_week",
          "solution_line_template": "Since there are 7 days in a week, then Mickey mounts {days_in_week}*{mickey_per_day}=<<{days_in_week}*{mickey_per_day}={mickey_per_week}>>{mickey_per_week} horses per week."
        }
      ]
    }
    ```
    
    ## Example 3
    
    ### Input
    
    **Index**:
    1372
    
    **Question**:
    Micah can type 20 words per minute and Isaiah can type 40 words per minute. How many more words can Isaiah type than Micah in an hour?
    
    **Solution mapping**:
    {'L1': 'There are 60 minutes in an hour.', 'L2': 'Micah can type 20 x 60 = <<20*60=1200>>1200 words in an hour.', 'L3': 'Isaiah can type 40 x 60 = <<40*60=2400>>2400 words in an hour.', 'L4': 'Isaiah can type 2400 - 1200 = <<2400-1200=1200>>1200 words more than Micah in an hour.'}
    
    ### Output
    
    ```json
    {
      "function_code": "def solve():\n    \"\"\"Index: 1372.\n    Returns: how many more words Isaiah can type than Micah in an hour.\n    \"\"\"\n    # L2\n    micah_wpm = 20 # 20 words per minute\n    minutes_per_hour = 60 # WK\n    micah_wph = micah_wpm * minutes_per_hour\n\n    # L3\n    isaiah_wpm = 40 # 40 words per minute\n    isaiah_wph = isaiah_wpm * minutes_per_hour\n\n    # L4\n    difference_in_words = isaiah_wph - micah_wph\n\n    # FA\n    answer = difference_in_words\n    return answer",
      "logical_steps": [
        {
          "line_number": "L2",
          "question_inputs": ["micah_wpm"],
          "WK_inputs": ["minutes_per_hour"],
          "output_variable": "micah_wph",
          "solution_line_template": "Micah can type {micah_wpm} x {minutes_per_hour} = <<{micah_wpm}*{minutes_per_hour}={micah_wph}>>{micah_wph} words in an hour."
        },
        {
          "line_number": "L3",
          "question_inputs": ["isaiah_wpm"],
          "WK_inputs": [],
          "output_variable": "isaiah_wph",
          "solution_line_template": "Isaiah can type {isaiah_wpm} x {minutes_per_hour} = <<{isaiah_wpm}*{minutes_per_hour}={isaiah_wph}>>{isaiah_wph} words in an hour."
        },
        {
          "line_number": "L4",
          "question_inputs": [],
          "WK_inputs": [],
          "output_variable": "difference_in_words",
          "solution_line_template": "Isaiah can type {isaiah_wph} - {micah_wph} = <<{isaiah_wph}-{micah_wph}={difference_in_words}>>{difference_in_words} words more than Micah in an hour."
        }
      ]
    }
    ```
    
    # TASK
    
    ## Input
    
    **Index**:
    4
    
    **Question**:
    James writes a 3-page letter to 2 different friends twice a week.  How many pages does he write a year?
    
    **Solution Mapping**:
    {'L1': 'He writes each friend 3*2=<<3*2=6>>6 pages a week', 'L2': 'So he writes 6*2=<<6*2=12>>12 pages every week', 'L3': 'That means he writes 12*52=<<12*52=624>>624 pages a year'}
    
    ## Output
    
    


### API Clients, Concurrency Limits, Models


```python
# Imports for API clients and related functionality
import os
import openai
import google.generativeai as genai
import anthropic
import asyncio
import nest_asyncio
from openai import AsyncOpenAI
from anthropic import AsyncClient
from dotenv import load_dotenv

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
    "google": 2,    
    "anthropic": 2, 
    "openai": 2,    
}
print(f"API concurrency limits set to: {API_CONCURRENCY_LIMITS}")

MODEL_DICT = {
  "openai": "gpt-4.1",
  "google": "gemini-2.5-flash"
}

MODELS = [f"{provider}_{model}" for provider, model in MODEL_DICT.items()]
print(f"Available models: {MODELS}")
```

    Loaded environment variables from .env file.
    API clients initialized successfully.
    API concurrency limits set to: {'google': 2, 'anthropic': 2, 'openai': 2}
    Available models: ['openai_gpt-4.1', 'google_gemini-2.5-flash']


### Main code for making API calls


```python
import time
import math
import random
import datetime
from tqdm.notebook import tqdm

# --- 1. Helper Functions ---
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

async def with_api_retries(
        send_coroutine_factory, 
        *, 
        max_attempts: int = 10, 
        base_wait_seconds: int = 5):
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

# --- 2. Provider-Specific API Calling Functions ---

async def call_openai_async(
        model: str, 
        system_prompt: str, 
        user_prompt: str):
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

async def call_google_async(
        model: str, 
        system_prompt: str, 
        user_prompt: str):
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

async def call_anthropic_async(
        model: str, 
        system_prompt: str, 
        user_prompt: str):
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


# --- 3. Per-Problem Orchestration (Dispatcher Logic) ---

async def run_one_problem_async(
    index: int, 
    tier: str,
    dataset: 'datasets.Dataset',
    system_prompt: str,
    model_dict: Dict[str, str],
    provider_sems: Dict[str, asyncio.Semaphore], 
    output_dir: Path,
    pbar: tqdm
) -> List[Dict]:
    """
    Generates manifests for a single problem and returns a list of result dictionaries.
    """
    user_prompt = append_sample_to_user_prompt(
        tier=tier,
        index=index,
        dataset=dataset
    )
    
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
            task.meta = {
                "provider": provider, 
                "model": model, 
                "index": index, 
                "start_time": time.time()}
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
        
        # Append to the list of results for this problem
        problem_results.append({
            "provider": meta["provider"], 
            "model": meta["model"], 
            "index": meta["index"],
            "status": status, 
            "time_s": round(elapsed, 2),
            "input_tokens": usage["input_tokens"], "output_tokens": usage["output_tokens"],
            "cached_tokens": usage["cached_tokens"],
            "utc_completed": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
        })
    
    pbar.update(1)
    # Return result for this problem
    return problem_results


# --- 4. Main Batch Generation Function ---

async def generate_manifests_parallel(
    indices_to_generate: List[int],
    tier: str = "tier1",
    dataset: 'datasets.Dataset' = GSM8K_TRAIN,
    model_dict: Dict[str, str] = MODEL_DICT,
    system_prompt: str = SYSTEM_PROMPT,
    output_dir: Path = MANIFEST_OUTPUT_DIR,
    concurrency_limits: Dict[str, int] = API_CONCURRENCY_LIMITS
):
    """
    Runs the manifest generation process and returns a DataFrame with performance stats.
    """
    print("--- Starting Manifest Generation ---")
    start_time = time.time()
    
    provider_semaphores = {prov: asyncio.Semaphore(limit) for prov, limit in concurrency_limits.items()}
    
    with tqdm(total=len(indices_to_generate), desc="Generating Manifests") as pbar:
        problem_tasks = [
            run_one_problem_async(
                index=idx, 
                tier=tier,
                dataset=dataset,
                system_prompt=system_prompt,
                model_dict=model_dict,
                provider_sems=provider_semaphores, 
                output_dir=output_dir,
                pbar=pbar
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

```

### Running the manifest generation process


```python
# Choose the list of indices to generate manifests for
INDICES_TO_GENERATE = TIER_LISTS["tier1"][:10]  # Adjust this as needed

# Run the manifest generation process
perf_df = await generate_manifests_parallel(indices_to_generate=INDICES_TO_GENERATE)
```

### Display the performance DataFrame


```python
display(perf_df)
```
