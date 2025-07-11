#### Cell 1: Paths


```python
from pathlib import Path

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

# To contain generated manifest txt files
MANIFEST_OUTPUT_DIR = DATA_DIR / "tier-manifests-gen-txt" 

# Contains sample manifest json files, questions answers, and user prompt prefixes
MANIFEST_EXAMPLES_DIR = DATA_DIR / "tier-manifests-examples-json" 

TIER_OUTPUT_DIRS = {f"tier{i}": MANIFEST_OUTPUT_DIR / f"tier{i}" for i in range(1, 6)}
TIER_EXAMPLES_DIRS = {f"tier{i}": MANIFEST_EXAMPLES_DIR / f"tier{i}" for i in range(1, 6)}

# Make the directory for the tier if it doesn't exist
for tier_dir in TIER_OUTPUT_DIRS.values():
    tier_dir.mkdir(parents=True, exist_ok=True)

for tier_dir in TIER_EXAMPLES_DIRS.values():
    tier_dir.mkdir(parents=True, exist_ok=True)

print(f"Project root found at: {PROJECT_ROOT}")
print(f"Data directory found at: {DATA_DIR}")
print(f"Raw manifest output directory set to: {MANIFEST_OUTPUT_DIR}")
```

    Project root found at: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math
    Data directory found at: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data
    Raw manifest output directory set to: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/tier-manifests-gen-txt


#### Cell 2: Dataset and tier definitions


```python
import datasets
from datasets import load_dataset 
import re

GSM8K_TRAIN = load_dataset("gsm8k", "main", split="train")

def has_computational_division(solution_text: str):
    """Returns True if a '/' is followed by optional whitespace and then a digit."""
    pattern = re.compile(r'/\s*\d')
    return bool(pattern.search(solution_text))


def has_float(solution_text: str):
    """Returns True if the solution text contains a floating-point number."""
    pattern = re.compile(r'(?<!\d)\.\d+|\d+\.\d+')
    return bool(pattern.search(solution_text))


def is_symbolic(solution_text: str):
    """Returns True if the solution contains a symbolic reasoning line (Let @ ...)."""
    pattern = re.compile(r'^Let [a-zA-Z] ', re.MULTILINE)
    return bool(pattern.search(solution_text))


def mutually_disjoint_tiers(dataset: datasets.Dataset):
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


#### **Selecting the current tier for this notebook**


```python
### --- Select the tier ONCE for this notebook --- ###
CURRENT_TIER = "tier2"

CURRENT_INDICES = TIER_LISTS[CURRENT_TIER]
CURRENT_TIER_OUTPUT_DIR = TIER_OUTPUT_DIRS[CURRENT_TIER]
CURRENT_TIER_EXAMPLES_DIR = TIER_EXAMPLES_DIRS[CURRENT_TIER]

print(f"Tier for this notebook: {CURRENT_TIER}")
print(f"Number of samples in {CURRENT_TIER}: {len(CURRENT_INDICES)}")
print(f"Output directory for {CURRENT_TIER}: {CURRENT_TIER_OUTPUT_DIR}")
print(f"Examples directory for {CURRENT_TIER}: {CURRENT_TIER_EXAMPLES_DIR}")
```

    Tier for this notebook: tier2
    Number of samples in tier2: 837
    Output directory for tier2: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/tier-manifests-gen-txt/tier2
    Examples directory for tier2: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/tier-manifests-examples-json/tier2


#### Cell 3: Prompt creation


```python
import json


def sanitize_text(text: str):
    """
    Replaces a comprehensive set of problematic Unicode characters with their
    ASCII equivalents to prevent model generation and string parsing errors.
    """
    replacements = {
        # Mathematical Operators
        "\u2212": "-",  # Minus Sign
        "\u00d7": "*",  # Multiplication Sign
        "\u00f7": "/",  # Division Sign
        "\u22c5": "*",  # Dot Operator
        
        # Typographic Quotes
        "\u201c": '"',  # Left Double Quotation Mark
        "\u201d": '"',  # Right Double Quotation Mark
        "\u2018": "'",  # Left Single Quotation Mark
        "\u2019": "'",  # Right Single Quotation Mark
        
        # Typographic Dashes
        "\u2014": "-",  # Em Dash
        "\u2013": "-",  # En Dash
        
        # Other
        "\u2026": "...", # Horizontal Ellipsis
        "\u00a0": " ",  # Non-breaking Space
    }
    for uni, ascii_char in replacements.items():
        text = text.replace(uni, ascii_char)
    return text


def build_solution_mapping(
        index: int, 
        dataset: 'datasets.Dataset' = GSM8K_TRAIN,
        exclude_FA: bool = True
    ):
    """
    Extracts the natural language solution, sanitizes it, and structures
    it into a line-numbered dictionary.
    """
    solution_mapping = {}
    solution_text = dataset[index]["answer"]
    sanitized_solution_text = sanitize_text(solution_text)
    
    # --- CORRECTION: Use the sanitized variable ---
    lines = [ln.strip() for ln in sanitized_solution_text.splitlines() if ln.strip()]

    if lines and re.match(r"^####\s*[\d\.,]+$", lines[-1]):
        solution_mapping["FA"] = lines.pop(-1).strip()

    for i, line in enumerate(lines, 1):
        solution_mapping[f"L{i}"] = line

    if exclude_FA and "FA" in solution_mapping:
        del solution_mapping["FA"]

    return solution_mapping


BASE_MANIFEST_SCHEMA = {
    "type": "object",
    "properties": {
        "function_code": {
            "type": "string",
            "description": "A single string containing a complete, self-contained Python function that constitutes an end-to-end formalization of the solution."
        },
        "logical_steps": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "line_number": {"type": "string"},
                    "question_inputs": {"type": "array", "items": {"type": "string"}},
                    "WK_inputs": {"type": "array", "items": {"type": "string"}},
                    "output_variable": {"type": "string"},
                    "solution_line_template": {"type": "string"}
                },
                "required": ["line_number", "question_inputs", "WK_inputs", "output_variable", "solution_line_template"]
            }
        }
    },
    "required": ["function_code", "logical_steps"]
}


SYSTEM_PROMPT = """You are a data formalization expert who excels in mathematical reasoning and writing python code. You will be presented with a math word problem accompanied by a step-by-step natural language solution. You goal is to carefully and meticulously analyze the given question and solution, and formalize it by converting it into a structured json object that deconstructs the logic of the solution.

You MUST follow all rules and formatting instructions provided in the user prompt without deviation. Your entire output MUST be a single JSON object wrapped in ```json ... ```. Do not include any text or explanation before or after the JSON object."""

STATIC_PREFIXES = {}
for tier in TIER_LISTS.keys():
    prefix_file = TIER_EXAMPLES_DIRS[tier] / f"{tier}_user_prompt_prefix.txt"
    with open(prefix_file, 'r', encoding='utf-8') as f:
        STATIC_PREFIXES[tier] = f.read()


def append_sample_to_user_prompt(
        tier: str, 
        index: int, 
        dataset: datasets.Dataset = GSM8K_TRAIN
    ):
    """
    Appends a chosen sample from the GSM8K dataset to the user prompt for a specific tier. Returns the complete user prompt, ready to be sent to the LLM for manifest generation.
    """
    if tier not in TIER_LISTS:
        raise ValueError(f"Invalid tier: {tier}. Must be one of {list(TIER_LISTS.keys())}.")

    sample = dataset[index]
    question = sample['question']
    answer = build_solution_mapping(index, dataset)

    task_block = f"""## Input

**Index:**:
{index}

**Question:**:
{question}

**Solution mapping:**:
{json.dumps(answer, indent=2)}

## Output

"""
    return STATIC_PREFIXES[tier] + task_block


# Example usage
idx = CURRENT_INDICES[0]
user_prompt = append_sample_to_user_prompt(CURRENT_TIER, idx, GSM8K_TRAIN)
print(f"User prompt for index {idx} in {CURRENT_TIER} has {len(user_prompt)} characters:")
print("-"*80)
print(user_prompt)
```

    User prompt for index 9 in tier2 has 18046 characters:
    --------------------------------------------------------------------------------
    In the TASK below, you will be given a math problem and its corresponding step-by-step solution. Each step in the solution is numbered (e.g. "L1", "L2" and so on), and many of the steps include calculator annotations (e.g. "<<20*0.1=2>>"). Your goal is to convert this information into a structured JSON object according to the following schema and detailed instructions.
    
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
    *   Output: complete output, following the correct JSON schema.
    
    In all examples, you will observe the following:
    
    *   **A rigid adherence to the Direct Substitution Rule (1.E)**. This is the most important principle. The `solution_line_template` must be an exact copy of the original solution line, with only computational numbers replaced by `{variable}` placeholders. Every other point follows from this rule.
    
    *   **How to formalize numbers depends entirely on how they appear in the solution text.** The goal is to create variables so that the numerical values can be directly substituted.
        *   **Simple Case:** In **Example 3**, the calculation uses `.8`. This is formalized with a single variable: `insurance_coverage_percent = 0.8`. In **Example 1**, "half an hour" is used in a calculation as `.5`, so it is formalized as `chase_duration = 0.5`.
        *   **Complex Case (Inconsistent Text):** A solution can be inconsistent, using multiple representations for the same concept. The Direct Substitution Rule must still be followed, even if it requires creating multiple variables. For instnace, in line L2 of **Example 2**:
            *   The text "10%" requires `discount_percent_num = 10`.
            *   The text ".10" requires `discount_percent_decimal = 0.10`.
            *   The calculation `10 * .01` inside the annotation requires `percent_factor = 0.01` to represent the `.01` that does not appear elsewhere.
            *   This results in three distinct variables to satisfy the substitution rule for one conceptual idea.
    
    *   **Strict adherence to defining only NEW variables** in each step's `question_inputs` and `WK_inputs` lists. For instance, in **Example 1**, `fast_speed` is defined in L2 and then simply re-used in the computation for L4 without being listed as an input again.
    
    *   Comments for `question_inputs` must cite the question text only, **NEVER** the solution text. Note how `percent_factor = 0.01` in **Example 2** is correctly labeled `# WK` because that fact constitutes common-sense World Knowledge and is not present in the question text.
    
    ## Example 1
    
    ### Input
    
    **Index:**
    2401
    
    **Question:**
    A wild tiger escapes the zoo.  He escapes at 1 AM and zookeepers do not notice he is missing until 4 AM.  He runs at a speed of 25 mph.  It takes 2 more hours to find him but after 4 hours of running, the tiger slows his speed to 10 mph.  He then gets chased for half an hour going 50 mph.  How far away from the zoo was he caught?
    
    **Solution mapping:**
    {
      "L1": "He was running for 4-1=<<4-1=3>>3 hours",
      "L2": "So in that time he runs 3*25=<<3*25=75>>75 miles",
      "L3": "Since he slowed down after 4 hours, the time he spent running at 25mph was an additional 4-3=<<4-3=1>>1 hours",
      "L4": "So in the first hour they were finding him, he ran 1*25=<<1*25=25>>25 miles",
      "L5": "In the second hour they were finding him, he ran 1*10=<<1*10=10>>10 miles",
      "L6": "Finally, during the chase, he ran 50*.5=<<50*.5=25>>25 miles",
      "L7": "So he is 75+25+10+25=<<75+25+10+25=135>>135 miles away"
    }
    
    ### Output
    
    ```json
    {
      "function_code": "def solve():\n    \"\"\"Index: 2401.\n    Returns: how far away from the zoo the tiger was caught.\n    \"\"\"\n    # L1\n    notice_time = 4 # notice he is missing until 4 AM\n    escape_time = 1 # escapes at 1 AM\n    initial_run_duration = notice_time - escape_time\n\n    # L2\n    fast_speed = 25 # runs at a speed of 25 mph\n    distance_before_notice = initial_run_duration * fast_speed\n\n    # L3\n    time_before_slow = 4 # after 4 hours of running\n    additional_fast_run_duration = time_before_slow - initial_run_duration\n\n    # L4\n    additional_fast_distance = additional_fast_run_duration * fast_speed\n\n    # L5\n    slow_run_duration = 1 # In the second hour\n    slow_speed = 10 # slows his speed to 10 mph\n    slow_distance = slow_run_duration * slow_speed\n\n    # L6\n    chase_speed = 50 # going 50 mph\n    chase_duration = 0.5 # for half an hour\n    chase_distance = chase_speed * chase_duration\n\n    # L7\n    total_distance = distance_before_notice + additional_fast_distance + slow_distance + chase_distance\n\n    # FA\n    answer = total_distance\n    return answer",
      "logical_steps": [
        {
          "line_number": "L1",
          "question_inputs": ["notice_time", "escape_time"],
          "WK_inputs": [],
          "output_variable": "initial_run_duration",
          "solution_line_template": "He was running for {notice_time}-{escape_time}=<<{notice_time}-{escape_time}={initial_run_duration}>>{initial_run_duration} hours"
        },
        {
          "line_number": "L2",
          "question_inputs": ["fast_speed"],
          "WK_inputs": [],
          "output_variable": "distance_before_notice",
          "solution_line_template": "So in that time he runs {initial_run_duration}*{fast_speed}=<<{initial_run_duration}*{fast_speed}={distance_before_notice}>>{distance_before_notice} miles"
        },
        {
          "line_number": "L3",
          "question_inputs": ["time_before_slow"],
          "WK_inputs": [],
          "output_variable": "additional_fast_run_duration",
          "solution_line_template": "Since he slowed down after 4 hours, the time he spent running at 25mph was an additional {time_before_slow}-{initial_run_duration}=<<{time_before_slow}-{initial_run_duration}={additional_fast_run_duration}>>{additional_fast_run_duration} hours"
        },
        {
          "line_number": "L4",
          "question_inputs": [],
          "WK_inputs": [],
          "output_variable": "additional_fast_distance",
          "solution_line_template": "So in the first hour they were finding him, he ran {additional_fast_run_duration}*{fast_speed}=<<{additional_fast_run_duration}*{fast_speed}={additional_fast_distance}>>{additional_fast_distance} miles"
        },
        {
          "line_number": "L5",
          "question_inputs": ["slow_speed", "slow_run_duration"],
          "WK_inputs": [],
          "output_variable": "slow_distance",
          "solution_line_template": "In the second hour they were finding him, he ran {slow_run_duration}*{slow_speed}=<<{slow_run_duration}*{slow_speed}={slow_distance}>>{slow_distance} miles"
        },
        {
          "line_number": "L6",
          "question_inputs": ["chase_speed", "chase_duration"],
          "WK_inputs": [],
          "output_variable": "chase_distance",
          "solution_line_template": "Finally, during the chase, he ran {chase_speed}*{chase_duration}=<<{chase_speed}*{chase_duration}={chase_distance}>>{chase_distance} miles"
        },
        {
          "line_number": "L7",
          "question_inputs": [],
          "WK_inputs": [],
          "output_variable": "total_distance",
          "solution_line_template": "So he is {distance_before_notice}+{additional_fast_distance}+{slow_distance}+{chase_distance}=<<{distance_before_notice}+{additional_fast_distance}+{slow_distance}+{chase_distance}={total_distance}>>{total_distance} miles away"
        }
      ]
    }
    ```
    
    ## Example 2
    
    ### Input
    
    **Index:**
    2918
    
    **Question:**
    Monica charges $25.00 per person when catering a dinner party.  For repeat customers, she offers a 10% discount.  Phoebe is a repeat customer who is having a dinner party for 20 guests.  How much will Monica make from the party?
    
    **Solution mapping:**
    {
      "L1": "Phoebe is having 20 guests and Monica charges $25.00 per person so that’s 20*25 = $<<20*25=500.00>>500.00",
      "L2": "Phoebe is a repeat customer so she gets 10% off of $500.00 so that’s .10*500 = $<<10*.01*500=50.00>>50.00 discount",
      "L3": "Monica is charging $500.00 minus the repeat customer discount of $50.00 so she will make 500-50 = $<<500-50=450.00>>450.00"
    }
    
    ### Output
    
    ```json
    {
      "function_code": "def solve():\n    \"\"\"Index: 2918.\n    Returns: the amount Monica will make from the party.\n    \"\"\"\n    # L1\n    num_guests = 20 # 20 guests\n    cost_per_person = 25.00 # $25.00 per person\n    base_cost = num_guests * cost_per_person\n\n    # L2\n    discount_percent_decimal = 0.10 # from solution text: .10*500\n    discount_percent_num = 10 # 10% discount\n    percent_factor = 0.01 # WK\n    discount_amount = discount_percent_num * percent_factor * base_cost\n\n    # L3\n    final_cost = base_cost - discount_amount\n\n    # FA\n    answer = final_cost\n    return answer",
      "logical_steps": [
        {
          "line_number": "L1",
          "question_inputs": ["num_guests", "cost_per_person"],
          "WK_inputs": [],
          "output_variable": "base_cost",
          "solution_line_template": "Phoebe is having {num_guests} guests and Monica charges ${cost_per_person} per person so that’s {num_guests}*{cost_per_person} = $<<{num_guests}*{cost_per_person}={base_cost}>>{base_cost}"
        },
        {
          "line_number": "L2",
          "question_inputs": ["discount_percent_num", "discount_percent_decimal"],
          "WK_inputs": ["percent_factor"],
          "output_variable": "discount_amount",
          "solution_line_template": "Phoebe is a repeat customer so she gets {discount_percent_num}% off of ${base_cost} so that’s {discount_percent_decimal}*{base_cost} = $<<{discount_percent_num}*{percent_factor}*{base_cost}={discount_amount}>>{discount_amount} discount"
        },
        {
          "line_number": "L3",
          "question_inputs": [],
          "WK_inputs": [],
          "output_variable": "final_cost",
          "solution_line_template": "Monica is charging ${base_cost} minus the repeat customer discount of ${discount_amount} so she will make {base_cost}-{discount_amount} = $<<{base_cost}-{discount_amount}={final_cost}>>{final_cost}"
        }
      ]
    }
    ```
    
    ## Example 3
    
    ### Input
    
    **Index:**
    4822
    
    **Question:**
    James needs to get a new pair of glasses.  His frames cost $200 and the lenses cost $500.  Insurance will cover 80% of the cost of lenses and he has a $50 off coupon for frames.  How much does everything cost?
    
    **Solution mapping:**
    {
      "L1": "He gets 500*.8=$<<500*.8=400>>400 off the cost of lenses",
      "L2": "That means the lenses cost 500-400=$<<500-400=100>>100",
      "L3": "The frames cost 200-50=$<<200-50=150>>150",
      "L4": "So he pays 100+150=$<<100+150=250>>250"
    }
    ```
    
    ### Output
    
    ```json
    {
      "function_code": "def solve():\n    \"\"\"Index: 4822.\n    Returns: the total cost for the glasses.\n    \"\"\"\n    # L1\n    lenses_cost = 500 # lenses cost $500\n    insurance_coverage_percent = 0.8 # cover 80% of the cost\n    lenses_coverage_amount = lenses_cost * insurance_coverage_percent\n\n    # L2\n    final_lenses_cost = lenses_cost - lenses_coverage_amount\n\n    # L3\n    frames_cost = 200 # frames cost $200\n    coupon_discount = 50 # $50 off coupon\n    final_frames_cost = frames_cost - coupon_discount\n\n    # L4\n    total_cost = final_lenses_cost + final_frames_cost\n\n    # FA\n    answer = total_cost\n    return answer",
      "logical_steps": [
        {
          "line_number": "L1",
          "question_inputs": ["lenses_cost", "insurance_coverage_percent"],
          "WK_inputs": [],
          "output_variable": "lenses_coverage_amount",
          "solution_line_template": "He gets {lenses_cost}*{insurance_coverage_percent}=$<<{lenses_cost}*{insurance_coverage_percent}={lenses_coverage_amount}>>{lenses_coverage_amount} off the cost of lenses"
        },
        {
          "line_number": "L2",
          "question_inputs": [],
          "WK_inputs": [],
          "output_variable": "final_lenses_cost",
          "solution_line_template": "That means the lenses cost {lenses_cost}-{lenses_coverage_amount}=$<<{lenses_cost}-{lenses_coverage_amount}={final_lenses_cost}>>{final_lenses_cost}"
        },
        {
          "line_number": "L3",
          "question_inputs": ["frames_cost", "coupon_discount"],
          "WK_inputs": [],
          "output_variable": "final_frames_cost",
          "solution_line_template": "The frames cost {frames_cost}-{coupon_discount}=$<<{frames_cost}-{coupon_discount}={final_frames_cost}>>{final_frames_cost}"
        },
        {
          "line_number": "L4",
          "question_inputs": [],
          "WK_inputs": [],
          "output_variable": "total_cost",
          "solution_line_template": "So he pays {final_lenses_cost}+{final_frames_cost}=$<<{final_lenses_cost}+{final_frames_cost}={total_cost}>>{total_cost}"
        }
      ]
    }
    ```
    
    ## Input
    
    **Index:**:
    9
    
    **Question:**:
    Tina makes $18.00 an hour.  If she works more than 8 hours per shift, she is eligible for overtime, which is paid by your hourly wage + 1/2 your hourly wage.  If she works 10 hours every day for 5 days, how much money does she make?
    
    **Solution mapping:**:
    {
      "L1": "She works 8 hours a day for $18 per hour so she makes 8*18 = $<<8*18=144.00>>144.00 per 8-hour shift",
      "L2": "She works 10 hours a day and anything over 8 hours is eligible for overtime, so she gets 10-8 = <<10-8=2>>2 hours of overtime",
      "L3": "Overtime is calculated as time and a half so and she makes $18/hour so her overtime pay is 18*.5 = $<<18*.5=9.00>>9.00",
      "L4": "Her overtime pay is 18+9 = $<<18+9=27.00>>27.00",
      "L5": "Her base pay is $144.00 per 8-hour shift and she works 5 days and makes 5 * $144 = $<<144*5=720.00>>720.00",
      "L6": "Her overtime pay is $27.00 per hour and she works 2 hours of overtime per day and makes 27*2 = $<<27*2=54.00>>54.00 in overtime pay",
      "L7": "2 hours of overtime pay for 5 days means she makes 54*5 = $270.00",
      "L8": "In 5 days her base pay is $720.00 and she makes $270.00 in overtime pay so she makes $720 + $270 = $<<720+270=990.00>>990.00"
    }
    
    ## Output
    
    


#### Cell 4: API clients, concurrency limits, models


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
    "google": 30,    
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
    API concurrency limits set to: {'google': 30, 'anthropic': 2, 'openai': 2}
    Available models: ['openai_gpt-4.1', 'google_gemini-2.5-flash']


#### Cell 5: Helper functions to avoid rate limits in API calls


```python
import time
import random

import threading
import datetime


_log_lock = threading.Lock()
def log_event(
        level: str, 
        index: int, 
        model: str, 
        message: str
    ):
    """A thread-safe logger for concurrent operations."""
    with _log_lock:
        ts = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="milliseconds")
        task_id = asyncio.current_task().get_name()
        print(f"{ts} [{level:^7s}] [Idx {index:<4}] [Mdl: {model:<15}] [Task {task_id:<8}] {message}")
 

async def with_api_retries(
        send_coroutine_factory,
        *,
        model_info: str,  # For informative logging
        max_attempts: int = 10,
        base_wait_seconds: int = 10
    ):
    """A wrapper to handle API retries with exponential backoff."""
    for attempt in range(max_attempts):
        try:
            return await send_coroutine_factory()
        except (openai.RateLimitError, anthropic.RateLimitError, Exception) as e:
            # Check for specific rate limit error types or a 429 status code in the error string
            if isinstance(e, (openai.RateLimitError, anthropic.RateLimitError)) or "429" in str(e):
                if attempt == max_attempts - 1:
                    print(f"❌ Final attempt failed for {model_info}. Giving up.")
                    raise
                
                # Exponential backoff with jitter
                wait_time = base_wait_seconds * (2 ** attempt) + random.uniform(0, 1)
                
                # More informative error message
                print(f"🕒 Rate limit on {model_info}. Retrying in {wait_time:.2f}s... (Attempt {attempt + 1}/{max_attempts})")
                await asyncio.sleep(wait_time)
            else:
                # If it's not a rate limit error, re-raise immediately
                raise
    return None


class RateLimitCoordinator:
    def __init__(self, refill_rate_per_sec: float, max_tokens: int):
        self.refill_rate_per_sec = refill_rate_per_sec
        self.max_tokens = float(max_tokens)
        self.tokens = self.max_tokens
        self._lock = asyncio.Lock()
        self._refill_task = None
        
    async def _refill(self):
        """The background task that refills the token bucket at 1-second intervals."""
        while True:
            await asyncio.sleep(1)
            async with self._lock:
                self.tokens = min(self.max_tokens, self.tokens + self.refill_rate_per_sec)
                if int(time.time()) % 10 == 0:
                    log_event("REFILL", -1, "Coordinator", f"Bucket budget at {int(self.tokens)} / {int(self.max_tokens)}")

    async def start(self):
        if self._refill_task is None:
            self._refill_task = asyncio.create_task(self._refill())

    async def stop(self):
        if self._refill_task:
            self._refill_task.cancel()
            self._refill_task = None

    async def get_tokens(self, index: int, model: str, tokens_needed: int):
        while True:
            async with self._lock:
                if self.tokens >= tokens_needed:
                    self.tokens -= tokens_needed
                    log_event("GRANT", index, model, f"Permission granted. Budget: {int(self.tokens + tokens_needed)} -> {int(self.tokens)}")
                    return
            
            deficit = tokens_needed - self.tokens
            wait_time = max(0.1, deficit / self.refill_rate_per_sec) # Ensure at least a small wait
            
            log_event("WAIT", index, model, f"Budget low. Needed: {tokens_needed}, Have: {int(self.tokens)}. Waiting ~{wait_time:.2f}s...")
            await asyncio.sleep(wait_time)

    async def return_tokens(self, index: int, model: str, tokens_returned: int):
        async with self._lock:
            self.tokens += tokens_returned
            log_event("RETURN", index, model, f"Tokens returned on failure. Budget restored to {int(self.tokens)}.")

    async def refund_tokens(self, index: int, model: str, tokens_refunded: int):
        """Refunds tokens to the budget after a successful call, correcting our estimate."""
        async with self._lock:
            self.tokens += tokens_refunded
            log_event("REFUND", index, model, f"Correcting estimate. Budget restored by {tokens_refunded} -> {int(self.tokens)}.")
```

#### Cell 6: Provider-specific API calling functions


```python
import math
import copy

async def call_openai_async(
        model: str,
        system_prompt: str,
        user_prompt: str,
        index: int,
        json_schema: dict,
        openai_max_tokens: int 
    ) -> tuple[str, dict, dict]:
    """
    Prepares a provider-specific schema and handles an API call to OpenAI.
    """
    
    openai_schema = copy.deepcopy(json_schema)

    def add_additional_properties(schema_part):
        if isinstance(schema_part, dict):
            if schema_part.get("type") == "object":
                schema_part["additionalProperties"] = False
            for value in schema_part.values():
                add_additional_properties(value)
        elif isinstance(schema_part, list):
            for item in schema_part:
                add_additional_properties(item)

    add_additional_properties(openai_schema)
    openai_schema_wrapper = {
        "name": "manifest_formalization", 
        "strict": True, 
        "schema": openai_schema
    }
    
    messages = [{"role": "system", "content": system_prompt}, 
                {"role": "user", "content": user_prompt}]
    
    model_info = f"{model} (Index {index})"
    
    response_with_headers = await with_api_retries(
        lambda: openai_client_async.chat.completions.with_raw_response.create(
            model=model, 
            messages=messages, 
            temperature=0, 
            max_tokens=openai_max_tokens, 
            response_format={"type": "json_schema", "json_schema": openai_schema_wrapper} # type: ignore
        ),
        model_info=model_info
    )
    
    response = response_with_headers.parse()
    text_response = response.choices[0].message.content
    
    usage = {"input_tokens": 0, "output_tokens": 0, "cached_tokens": 0}
    if response.usage:
        usage["input_tokens"] = response.usage.prompt_tokens
        usage["output_tokens"] = response.usage.completion_tokens
        if hasattr(response.usage, 'prompt_tokens_details') and response.usage.prompt_tokens_details:
             usage["cached_tokens"] = response.usage.prompt_tokens_details.get("cached_tokens", 0)

    headers = response_with_headers.headers
    rate_limit_info = {
        "limit_requests": headers.get("x-ratelimit-limit-requests"),
        "limit_tokens": headers.get("x-ratelimit-limit-tokens"),
        "remaining_requests": headers.get("x-ratelimit-remaining-requests"),
        "remaining_tokens": headers.get("x-ratelimit-remaining-tokens"),
        "reset_requests": headers.get("x-ratelimit-reset-requests"),
        "reset_tokens": headers.get("x-ratelimit-reset-tokens"),
    }
             
    return text_response, usage, rate_limit_info


async def call_google_async(
        model: str,
        system_prompt: str,
        user_prompt: str,
        index: int,
        json_schema: dict
    ):
    """
    Handles a Google API call with schema enforcement and a safe
    upper bound on output tokens to prevent runaway generation.
    """
    
    safety_settings = {
        "HARM_CATEGORY_HARASSMENT": "BLOCK_NONE",
        "HARM_CATEGORY_HATE_SPEECH": "BLOCK_NONE",
        "HARM_CATEGORY_SEXUALLY_EXPLICIT": "BLOCK_NONE",
        "HARM_CATEGORY_DANGEROUS_CONTENT": "BLOCK_NONE",
    }
    
    gemini = genai.GenerativeModel(
        model_name=model,
        system_instruction=system_prompt,
        safety_settings=safety_settings
    )
    
    cfg = genai.types.GenerationConfig(
        temperature=0, 
        max_output_tokens=8192, # Safe upper bound
        response_mime_type="application/json",
        response_schema=json_schema
    )
    
    model_info = f"{model} (Index {index})"

    response = await with_api_retries(
        lambda: gemini.generate_content_async(user_prompt, generation_config=cfg),
        model_info=model_info
    )

    if not response.parts:
        raise ValueError(f"Google API returned an empty response for Index {index}.")

    text_response = response.text
    usage = {"input_tokens": 0, "output_tokens": 0, "cached_tokens": 0}
    if response.usage_metadata:
        usage["input_tokens"] = response.usage_metadata.prompt_token_count
        usage["output_tokens"] = response.usage_metadata.candidates_token_count
        
    return text_response, usage

```

#### Cell 7: Single API call function


```python

import datetime
import json

async def run_single_api_call(
    provider: str,
    model: str,
    index: int,
    tier: str,
    dataset: 'datasets.Dataset',
    system_prompt: str,
    output_dir: Path,
    provider_sem: asyncio.Semaphore,
    json_schema: dict,
    coordinator: RateLimitCoordinator,
    openai_max_tokens: int,
    ):
    """
    Runs a single API call, but first checks if the output file already
    exists to avoid re-generating completed work.
    """

    output_path = output_dir / str(index) / f"{provider}_{model}.txt"
    if output_path.exists() and output_path.stat().st_size > 0:
        log_event("SKIPPED", index, model, "Output file already exists.")
        return {
            "provider": provider, "model": model, "index": index,
            "status": "Skipped", "time_s": 0,
            "input_tokens": 0, "output_tokens": 0, "cached_tokens": 0,
            "utc_completed": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
        }
        
    async with provider_sem:
        user_prompt = append_sample_to_user_prompt(tier=tier, index=index, dataset=dataset)

        tokens_needed = 0
        if provider == "openai":
            estimated_prompt_tokens = len(user_prompt.split()) * 1.25
            tokens_needed = int(estimated_prompt_tokens + openai_max_tokens)
            await coordinator.get_tokens(index, model, tokens_needed)

        start_time = time.time()
        status = "Failed"
        usage = {"input_tokens": 0, "output_tokens": 0, "cached_tokens": 0}

        try:
            if provider == "openai":
                text_response, usage, _ = await call_openai_async(
                    model, system_prompt, user_prompt, index, json_schema, openai_max_tokens
                )
                log_event("SUCCESS", index, model, f"Call OK. Usage: {json.dumps(usage)}")
                
                true_cost = usage['input_tokens'] + usage['output_tokens']
                refund_amount = tokens_needed - true_cost
                if refund_amount > 0:
                    await coordinator.refund_tokens(index, model, refund_amount)
                    
            elif provider == "google":
                text_response, usage = await call_google_async(
                    model, system_prompt, user_prompt, index, json_schema
                )
                log_event("SUCCESS", index, model, f"Call OK. Usage: {json.dumps(usage)}")
            
            status = "Success"

        except Exception as e:
            log_event("ERROR", index, model, f"{type(e).__name__}: {str(e).splitlines()[0]}")
            text_response = f"--- ERROR ---\nIndex: {index}, Model: {model}\n{type(e).__name__}: {e}"
            
        finally:
            if status == "Failed" and provider == "openai" and tokens_needed > 0:
                await coordinator.return_tokens(index, model, tokens_needed)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(text_response, encoding='utf-8')
        
        elapsed = time.time() - start_time
        
        return {
            "provider": provider, "model": model, "index": index,
            "status": status, "time_s": round(elapsed, 2),
            "input_tokens": usage["input_tokens"], "output_tokens": usage["output_tokens"],
            "cached_tokens": usage["cached_tokens"],
            "utc_completed": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
        }
```

#### Cell 8: Main manifest generation functions


```python
from tqdm.notebook import tqdm
import pandas as pd

async def generate_manifests_parallel_fixed(
    indices_to_generate: list[int],
    tier: str = CURRENT_TIER,
    dataset: 'datasets.Dataset' = GSM8K_TRAIN,
    model_dict: dict[str, str] = MODEL_DICT,
    system_prompt: str = SYSTEM_PROMPT,
    concurrency_limits: dict[str, int] = API_CONCURRENCY_LIMITS,
    json_schema: dict = BASE_MANIFEST_SCHEMA,
    openai_max_tokens: int = 4000
    ):
    """
    Fully parallel version with a robust token bucket coordinator for OpenAI.
    """
    print("--- Starting Manifest Generation (Token Bucket) ---")
    start_time = time.time()

    openai_coordinator = RateLimitCoordinator(refill_rate_per_sec=800, max_tokens=30000)
    await openai_coordinator.start()
    
    provider_semaphores = {prov: asyncio.Semaphore(limit) for prov, limit in concurrency_limits.items()}
    output_dir = TIER_OUTPUT_DIRS[tier]
    
    all_tasks = []
    for index in indices_to_generate:
        for provider, model in model_dict.items():
            task = asyncio.create_task(
                run_single_api_call(
                    provider=provider, model=model, index=index,
                    tier=tier, dataset=dataset, system_prompt=system_prompt,
                    output_dir=output_dir, provider_sem=provider_semaphores[provider],
                    json_schema=json_schema,
                    coordinator=openai_coordinator,
                    openai_max_tokens=openai_max_tokens
                )
            )
            all_tasks.append(task)
    
    print(f"Created {len(all_tasks)} total API call tasks")
    
    results = []
    try:
        with tqdm(total=len(all_tasks), desc="API Calls") as pbar:
            for task in asyncio.as_completed(all_tasks):
                result = await task
                results.append(result)
                pbar.update(1)
    finally:
        await openai_coordinator.stop()
    
    df = pd.DataFrame(results)
    run_ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d_%H%M%S")
    csv_path = output_dir / f"generation_performance_{run_ts}.csv"
    df.to_csv(csv_path, index=False)
    
    end_time = time.time()
    print(f"\n--- Manifest Generation Complete ---")
    print(f"Processed {len(indices_to_generate)} indices in {end_time - start_time:.2f} seconds.")
    print(f"Performance log saved to: {csv_path}")
    
    success_count = len(df[df['status'] == 'Success'])
    total_calls = len(df)
    if total_calls > 0:
      print(f"Success rate: {success_count}/{total_calls} ({100*success_count/total_calls:.1f}%)")
    
    return df
```

#### Cell 9: Running the main manifest generation function


```python
# --- Test Run Configuration ---
# Generate manifests for all indices up to 200 for the current tier.
LOWER_LIMIT = 200
UPPER_LIMIT = 3000
INDICES_TO_GENERATE = [idx for idx in CURRENT_INDICES if idx <= UPPER_LIMIT and idx >= LOWER_LIMIT]

print(f"Starting test run for {len(INDICES_TO_GENERATE)} indices in {CURRENT_TIER} between {LOWER_LIMIT} and {UPPER_LIMIT}.")

# Run the parallel generation function with the test indices.
# This will test the full pipeline, including the new RateLimitCoordinator.
perf_df = await generate_manifests_parallel_fixed(indices_to_generate=INDICES_TO_GENERATE)

# Display the head of the resulting performance dataframe to verify execution.
print("\n--- Test Run Performance Summary ---")
perf_df.head()