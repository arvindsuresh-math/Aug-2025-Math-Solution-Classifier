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

# To contain generated template txt files
TEMPLATE_OUTPUT_DIR = DATA_DIR / "template-generated-raw" 

# Contains sample template json files, questions answers, and user prompt prefixes
TEMPLATE_EXAMPLE_DIR = DATA_DIR / "template-examples-raw"

TIER_OUTPUT_DIRS = {f"tier{i}": TEMPLATE_OUTPUT_DIR / f"tier{i}" for i in range(1, 6)}
TIER_EXAMPLES_DIRS = {f"tier{i}": TEMPLATE_EXAMPLE_DIR / f"tier{i}" for i in range(1, 6)}

# Make the directory for the tier if it doesn't exist
for tier_dir in TIER_OUTPUT_DIRS.values():
    tier_dir.mkdir(parents=True, exist_ok=True)

for tier_dir in TIER_EXAMPLES_DIRS.values():
    tier_dir.mkdir(parents=True, exist_ok=True)

print(f"Project root found at: {PROJECT_ROOT}")
print(f"Data directory found at: {DATA_DIR}")
print(f"Raw template output directory set to: {TEMPLATE_OUTPUT_DIR}")
```

    Project root found at: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math
    Data directory found at: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data
    Raw template output directory set to: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/template-generated-raw


#### Cell 2: Dataset and tier definitions


```python
from datasets import Dataset
from datasets import load_dataset 
import re

# --- Load GSM8K Dataset ---
GSM8K_TRAIN: Dataset = load_dataset("gsm8k", "main")["train"]

# --- Tier Definition Functions ---
def has_computational_division(solution_text: str) -> bool:
    pattern = re.compile(r'/\s*\d')
    return bool(pattern.search(solution_text))

def has_float(solution_text: str) -> bool:
    pattern = re.compile(r'(?<!\d)\.\d+|\d+\.\d+')
    return bool(pattern.search(solution_text))

def is_symbolic(solution_text: str) -> bool:
    pattern = re.compile(r'^Let [a-zA-Z] ', re.MULTILINE)
    return bool(pattern.search(solution_text))

def mutually_disjoint_tiers(dataset: Dataset) -> dict[str, list[int]]:
    tiers = {}

    symbolic_set = set(idx for idx, sample in enumerate(dataset) if is_symbolic(sample.get("answer", "")))

    non_symbolic_indices = [idx for idx in range(len(dataset)) if idx not in symbolic_set]

    tiers["tier1"] = sorted([idx for idx in non_symbolic_indices if not has_float(dataset[idx].get("answer", "")) and not has_computational_division(dataset[idx].get("answer", ""))])

    tiers["tier2"] = sorted([idx for idx in non_symbolic_indices if has_float(dataset[idx].get("answer", "")) and not has_computational_division(dataset[idx].get("answer", ""))])

    tiers["tier3"] = sorted([idx for idx in non_symbolic_indices if not has_float(dataset[idx].get("answer", "")) and has_computational_division(dataset[idx].get("answer", ""))])

    tiers["tier4"] = sorted([idx for idx in non_symbolic_indices if has_float(dataset[idx].get("answer", "")) and has_computational_division(dataset[idx].get("answer", ""))])
    
    tiers["tier5"] = sorted(list(symbolic_set))
    return tiers

TIER_LISTS = mutually_disjoint_tiers(GSM8K_TRAIN)
print("Tier definitions loaded.")

# Display the number of samples in each tier
for tier, indices in TIER_LISTS.items():
    print(f"{tier:<10}: {len(indices)} samples")
print(f"{'Total':<10}: {len(GSM8K_TRAIN)} samples")
```

    Tier definitions loaded.
    tier1     : 2767 samples
    tier2     : 837 samples
    tier3     : 3113 samples
    tier4     : 544 samples
    tier5     : 212 samples
    Total     : 7473 samples


#### **Selecting the current tier for this notebook**


```python
### --- Select the tier ONCE for this notebook --- ###
CURRENT_TIER = "tier4"

CURRENT_INDICES = TIER_LISTS[CURRENT_TIER]
CURRENT_TIER_OUTPUT_DIR = TIER_OUTPUT_DIRS[CURRENT_TIER]
CURRENT_TIER_EXAMPLES_DIR = TIER_EXAMPLES_DIRS[CURRENT_TIER]

print(f"Tier for this notebook: {CURRENT_TIER}")
print(f"Number of samples in {CURRENT_TIER}: {len(CURRENT_INDICES)}")
print(f"Output directory for {CURRENT_TIER}: {CURRENT_TIER_OUTPUT_DIR}")
print(f"Examples directory for {CURRENT_TIER}: {CURRENT_TIER_EXAMPLES_DIR}")
```

    Tier for this notebook: tier4
    Number of samples in tier4: 544
    Output directory for tier4: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/template-generated-raw/tier4
    Examples directory for tier4: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/template-examples-raw/tier4


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


BASE_TEMPLATE_SCHEMA = {
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
        dataset: 'datasets.Dataset' = GSM8K_TRAIN
    ):
    """
    Appends a chosen sample from the GSM8K dataset to the user prompt for a specific tier. Returns the complete user prompt, ready to be sent to the LLM for template generation.
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

    User prompt for index 1 in tier4 has 22581 characters:
    --------------------------------------------------------------------------------
    In the TASK below, you will be given a math problem and its corresponding step-by-step solution. Each step in the solution is numbered (e.g. "L1", "L2" and so on), and many of the steps include calculator annotations (e.g. "<<20*0.1=2>>"). Your goal is to convert this information into a structured JSON object according to the following detialed instructions.
    
    # Detailed Field Instructions
    
    ## 1. "function_code"
    
    This string must contain a Python function with the following characteristics:
    
    *   **1.A. Handling Imports:** The `function_code` should have no imports **unless** your formalization requires the `Fraction` object.
        *   If your code uses the `Fraction()` constructor, the very first line of the string MUST be `from fractions import Fraction`.
        *   If your code does **not** use the `Fraction()` constructor (e.g., it only uses integers, floats, or standard division `/`), the function definition `def solve():` MUST be the very first line.
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
    
    *   **A rigid adherence to the Direct Substitution Rule (1.E)**. This is the most important principle. The `solution_line_template` must be an exact copy of the original solution line, with only computational numbers replaced by `{variable}` placeholders. Every other point follows from this rule.
    
    *   **How to formalize a rational number depends entirely on how it appears in the solution text.** It is crucial to distinguish between `floats`, `Fractions`, and the division operation (`/`).
        *   **Use `float` for decimals:** In **Example 1**, "half" is used in the calculation as `0.5`, so it is formalized as `kevin_nice_fraction = 0.5`. In **Example 3**, "30 percent" is used as `.30`, formalized as `third_night_stolen_percent = 0.30`.
        *   **Use `fractions.Fraction` for fractional quantities:** If "/" acts as a separator within a single fractional quantity, use `Fraction`. In **Example 1**, "three-fourths" appears as `(3/4)`, so it is formalized as `Fraction(3, 4)`. This requires the `from fractions import Fraction` import.
        *   **Use the `/` operator for division operations:** If "/" represents the operation of dividing two values, use the standard operator. In **Example 2**, the solution `300/100` is a division operation, formalized using `/`: `total_dollars = total_cents / cents_per_dollar`. This does **not** require an import.
    
    *   **A single template can require multiple formalizations.** **Example 1** shows a problem using both `float` (`0.5`) and `Fraction` (`3/4`). **Example 4** shows a mix of percentages (decomposed into floats) and division (`/`). The model must adapt to each line.
    
    *   **Decomposition is sometimes needed to follow the rules.** This is a critical and advanced point. In **Example 4**, the solution for L1 is `80% * 20 votes = <<80*0.01*20=16>>16 votes`. To satisfy the Direct Substitution Rule for the calculator annotation, this must be decomposed into two variables: `taotd_discard_percent_num = 80` and `percent_factor = 0.01`.
    
    *   **Strict adherence to defining only NEW variables** in each step's `question_inputs` and `WK_inputs` lists. For instance, in **Example 3**, `initial_ducks` is defined in L1 and then simply re-used in the computation for L2 without being listed as an input again.
    
    *   Comments for `question_inputs` must cite the question text only, **NEVER** the solution text. Note how `cents_per_dollar = 100` in **Example 2** is correctly labeled `# WK` because that fact constitutes common-sense World Knowledge and is not present in the question text.
    
    ## Example 1
    
    ### Input
    
    **Index:**
    3847
    
    **Question:**
    All people named Barry are nice, while only half of the people named Kevin are nice.  Three-fourths of people named Julie are nice, while 10% of people named Joe are nice.  If a crowd contains 24 people named Barry, 20 people named Kevin, 80 people named Julie, and 50 people named Joe, how many nice people are in the crowd?
    
    **Solution mapping:**
    {
      "L1": "If all people named Barry are nice, and the crowd contains 24 people named Barry, then 1*24=<<24*1=24>>24 of these people are nice.",
      "L2": "If only half of people named Kevin are nice, and the crowd contains 20 people named Kevin, then 0.5*20=<<0.5*20=10>>10 of these people are nice.",
      "L3": "If three-fourths of people named Julie are nice, and the crowd contains 80 people named Julie, then (3/4)*80=<<3/4*80=60>>60 of these people are nice.",
      "L4": "If 10% of people named Joe are nice, and the crowd contains 50 people named Joe, then 0.1*50=<<0.1*50=5>>5 of these people are nice.",
      "L5": "In total, the crowd contains 24+10+60+5=<<24+10+60+5=99>>99 people who are nice."
    }
    
    ### Output
    
    ```json
    {
      "function_code": "from fractions import Fraction\n\ndef solve():\n    \"\"\"Index: 3847.\n    Returns: the number of nice people in the crowd.\n    \"\"\"\n    # L1\n    num_barry = 24 # 24 people named Barry\n    barry_nice_fraction = 1 # All people named Barry are nice\n    nice_barry = barry_nice_fraction * num_barry\n\n    # L2\n    num_kevin = 20 # 20 people named Kevin\n    kevin_nice_fraction = 0.5 # half of the people named Kevin are nice\n    nice_kevin = kevin_nice_fraction * num_kevin\n\n    # L3\n    num_julie = 80 # 80 people named Julie\n    julie_nice_fraction = Fraction(3, 4) # Three-fourths of people named Julie are nice\n    nice_julie = julie_nice_fraction * num_julie\n\n    # L4\n    num_joe = 50 # 50 people named Joe\n    joe_nice_fraction = 0.1 # 10% of people named Joe are nice\n    nice_joe = joe_nice_fraction * num_joe\n\n    # L5\n    total_nice_people = nice_barry + nice_kevin + nice_julie + nice_joe\n\n    # FA\n    answer = total_nice_people\n    return answer",
      "logical_steps": [
        {
          "line_number": "L1",
          "question_inputs": ["num_barry", "barry_nice_fraction"],
          "WK_inputs": [],
          "output_variable": "nice_barry",
          "solution_line_template": "If all people named Barry are nice, and the crowd contains {num_barry} people named Barry, then {barry_nice_fraction}*{num_barry}=<<{num_barry}*{barry_nice_fraction}={nice_barry}>>{nice_barry} of these people are nice."
        },
        {
          "line_number": "L2",
          "question_inputs": ["num_kevin", "kevin_nice_fraction"],
          "WK_inputs": [],
          "output_variable": "nice_kevin",
          "solution_line_template": "If only half of people named Kevin are nice, and the crowd contains {num_kevin} people named Kevin, then {kevin_nice_fraction}*{num_kevin}=<<{kevin_nice_fraction}*{num_kevin}={nice_kevin}>>{nice_kevin} of these people are nice."
        },
        {
          "line_number": "L3",
          "question_inputs": ["num_julie", "julie_nice_fraction"],
          "WK_inputs": [],
          "output_variable": "nice_julie",
          "solution_line_template": "If three-fourths of people named Julie are nice, and the crowd contains {num_julie} people named Julie, then ({julie_nice_fraction})*{num_julie}=<<{julie_nice_fraction}*{num_julie}={nice_julie}>>{nice_julie} of these people are nice."
        },
        {
          "line_number": "L4",
          "question_inputs": ["num_joe", "joe_nice_fraction"],
          "WK_inputs": [],
          "output_variable": "nice_joe",
          "solution_line_template": "If 10% of people named Joe are nice, and the crowd contains {num_joe} people named Joe, then {joe_nice_fraction}*{num_joe}=<<{joe_nice_fraction}*{num_joe}={nice_joe}>>{nice_joe} of these people are nice."
        },
        {
          "line_number": "L5",
          "question_inputs": [],
          "WK_inputs": [],
          "output_variable": "total_nice_people",
          "solution_line_template": "In total, the crowd contains {nice_barry}+{nice_kevin}+{nice_julie}+{nice_joe}=<<{nice_barry}+{nice_kevin}+{nice_julie}+{nice_joe}={total_nice_people}>>{total_nice_people} people who are nice."
        }
      ]
    }
    ```
    
    ## Example 2
    
    ### Input
    
    **Index:**
    4847
    
    **Question:**
    Lucy plans to purchase potato chips for a party. Ten people will be at the party, including Lucy. The potato chips cost 25 cents per pound. How much will Lucy pay (in dollars) for the potato chips if she wants each person to get 1.2 pounds?
    
    **Solution mapping:**
    {
      "L1": "Lucy needs to purchase 10 x 1.2 = <<10*1.2=12>>12 pounds of potato chips.",
      "L2": "So, Lucy will pay 12 x 25 = <<12*25=300>>300 cents for it.",
      "L3": "Since there are 100 cents in $1, thus, Lucy will pay 300/100 = <<300/100=3>>3 dollars."
    }
    
    ### Output
    
    ```json
    {
      "function_code": "def solve():\n    \"\"\"Index: 4847.\n    Returns: the amount Lucy will pay in dollars.\n    \"\"\"\n    # L1\n    num_people = 10 # Ten people will be at the party\n    chips_per_person = 1.2 # each person to get 1.2 pounds\n    total_pounds = num_people * chips_per_person\n\n    # L2\n    cents_per_pound = 25 # 25 cents per pound\n    total_cents = total_pounds * cents_per_pound\n\n    # L3\n    cents_per_dollar = 100 # WK\n    total_dollars = total_cents / cents_per_dollar\n\n    # FA\n    answer = total_dollars\n    return answer",
      "logical_steps": [
        {
          "line_number": "L1",
          "question_inputs": ["num_people", "chips_per_person"],
          "WK_inputs": [],
          "output_variable": "total_pounds",
          "solution_line_template": "Lucy needs to purchase {num_people} x {chips_per_person} = <<{num_people}*{chips_per_person}={total_pounds}>>{total_pounds} pounds of potato chips."
        },
        {
          "line_number": "L2",
          "question_inputs": ["cents_per_pound"],
          "WK_inputs": [],
          "output_variable": "total_cents",
          "solution_line_template": "So, Lucy will pay {total_pounds} x {cents_per_pound} = <<{total_pounds}*{cents_per_pound}={total_cents}>>{total_cents} cents for it."
        },
        {
          "line_number": "L3",
          "question_inputs": [],
          "WK_inputs": ["cents_per_dollar"],
          "output_variable": "total_dollars",
          "solution_line_template": "Since there are 100 cents in $1, thus, Lucy will pay {total_cents}/{cents_per_dollar} = <<{total_cents}/{cents_per_dollar}={total_dollars}>>{total_dollars} dollars."
        }
      ]
    }
    ```
    
    ## Example 3
    
    ### Input
    
    **Index:**
    5040
    
    **Question:**
    There are 320 ducks in a pond.  On the first night 1/4 of them get eaten by a fox.  On the second night 1/6 of the remaining ducks fly away, and on the third night 30 percent are stolen.  How many ducks remain after the three nights?
    
    **Solution mapping:**
    {
      "L1": "First night:320(1/4)=80",
      "L2": "320-80=<<320-80=240>>240",
      "L3": "Second night:240(1/6)=40",
      "L4": "240-40=<<240-40=200>>200",
      "L5": "Third night:200(.30)=60",
      "L6": "200-60=<<200-60=140>>140 ducks remain"
    }
    
    ### Output
    
    ```json
    {
      "function_code": "from fractions import Fraction\n\ndef solve():\n    \"\"\"Index: 5040.\n    Returns: the number of ducks remaining after three nights.\n    \"\"\"\n    # L1\n    initial_ducks = 320 # 320 ducks in a pond\n    first_night_eaten_fraction = Fraction(1, 4) # 1/4 of them get eaten\n    first_night_eaten = initial_ducks * first_night_eaten_fraction\n\n    # L2\n    ducks_after_night1 = initial_ducks - first_night_eaten\n\n    # L3\n    second_night_flew_fraction = Fraction(1, 6) # 1/6 of the remaining ducks fly away\n    second_night_flew = ducks_after_night1 * second_night_flew_fraction\n\n    # L4\n    ducks_after_night2 = ducks_after_night1 - second_night_flew\n\n    # L5\n    third_night_stolen_percent = 0.30 # 30 percent are stolen\n    third_night_stolen = ducks_after_night2 * third_night_stolen_percent\n\n    # L6\n    ducks_after_night3 = ducks_after_night2 - third_night_stolen\n\n    # FA\n    answer = ducks_after_night3\n    return answer",
      "logical_steps": [
        {
          "line_number": "L1",
          "question_inputs": ["initial_ducks", "first_night_eaten_fraction"],
          "WK_inputs": [],
          "output_variable": "first_night_eaten",
          "solution_line_template": "First night:{initial_ducks}({first_night_eaten_fraction})={first_night_eaten}"
        },
        {
          "line_number": "L2",
          "question_inputs": [],
          "WK_inputs": [],
          "output_variable": "ducks_after_night1",
          "solution_line_template": "{initial_ducks}-{first_night_eaten}=<<{initial_ducks}-{first_night_eaten}={ducks_after_night1}>>{ducks_after_night1}"
        },
        {
          "line_number": "L3",
          "question_inputs": ["second_night_flew_fraction"],
          "WK_inputs": [],
          "output_variable": "second_night_flew",
          "solution_line_template": "Second night:{ducks_after_night1}({second_night_flew_fraction})={second_night_flew}"
        },
        {
          "line_number": "L4",
          "question_inputs": [],
          "WK_inputs": [],
          "output_variable": "ducks_after_night2",
          "solution_line_template": "{ducks_after_night1}-{second_night_flew}=<<{ducks_after_night1}-{second_night_flew}={ducks_after_night2}>>{ducks_after_night2}"
        },
        {
          "line_number": "L5",
          "question_inputs": ["third_night_stolen_percent"],
          "WK_inputs": [],
          "output_variable": "third_night_stolen",
          "solution_line_template": "Third night:{ducks_after_night2}({third_night_stolen_percent})={third_night_stolen}"
        },
        {
          "line_number": "L6",
          "question_inputs": [],
          "WK_inputs": [],
          "output_variable": "ducks_after_night3",
          "solution_line_template": "{ducks_after_night2}-{third_night_stolen}=<<{ducks_after_night2}-{third_night_stolen}={ducks_after_night3}>>{ducks_after_night3} ducks remain"
        }
      ]
    }
    ```
    
    ## Example 4
    
    ### Input
    
    **Index:**
    7037
    
    **Question:**
    At a book burning, Fran counts 20 votes for The Art of the Deal, 12 votes for Twilight, and 10 votes for Game of Thrones.  She decides to alter the results by throwing away 80% of the votes for The Art of the Deal and half the votes for Twilight. What percentage of the altered votes are for Game of Thrones?
    
    **Solution mapping:**
    {
      "L1": "First find the total number of The Art of the Deal votes Fran throws away: 80% * 20 votes = <<80*0.01*20=16>>16 votes",
      "L2": "Then subtract these votes from the total number of The Art of the Deal votes to find the altered number: 20 votes - 16 votes = <<20-16=4>>4 votes",
      "L3": "Then divide the total number Twilight votes by 2 to find the altered number of votes: 12 votes / 2 = <<12/2=6>>6 votes",
      "L4": "Then add the altered number of votes for each book to find the total altered number of votes: 6 votes + 4 votes + 10 votes = <<6+4+10=20>>20 votes",
      "L5": "Then divide the number of votes for Game of Thrones by the total altered number of votes and multiply by 100% to express the answer as a percentage: 10 votes / 20 votes * 100% = 50%"
    }
    
    ### Output
    
    ```json
    {
      "function_code": "def solve():\n    \"\"\"Index: 7037.\n    Returns: the percentage of altered votes for Game of Thrones.\n    \"\"\"\n    # L1\n    taotd_initial_votes = 20 # 20 votes for The Art of the Deal\n    taotd_discard_percent_num = 80 # throws away 80% of the votes\n    percent_factor = 0.01 # WK\n    taotd_discarded_votes = taotd_discard_percent_num * percent_factor * taotd_initial_votes\n\n    # L2\n    taotd_altered_votes = taotd_initial_votes - taotd_discarded_votes\n\n    # L3\n    twilight_initial_votes = 12 # 12 votes for Twilight\n    twilight_discard_divisor = 2 # half the votes for Twilight\n    twilight_altered_votes = twilight_initial_votes / twilight_discard_divisor\n\n    # L4\n    got_initial_votes = 10 # 10 votes for Game of Thrones\n    total_altered_votes = twilight_altered_votes + taotd_altered_votes + got_initial_votes\n\n    # L5\n    percent_multiplier = 100 # WK\n    got_percentage = got_initial_votes / total_altered_votes * percent_multiplier\n\n    # FA\n    answer = got_percentage\n    return answer",
      "logical_steps": [
        {
          "line_number": "L1",
          "question_inputs": ["taotd_discard_percent_num", "taotd_initial_votes"],
          "WK_inputs": ["percent_factor"],
          "output_variable": "taotd_discarded_votes",
          "solution_line_template": "First find the total number of The Art of the Deal votes Fran throws away: 80% * {taotd_initial_votes} votes = <<{taotd_discard_percent_num}*{percent_factor}*{taotd_initial_votes}={taotd_discarded_votes}>>{taotd_discarded_votes} votes"
        },
        {
          "line_number": "L2",
          "question_inputs": [],
          "WK_inputs": [],
          "output_variable": "taotd_altered_votes",
          "solution_line_template": "Then subtract these votes from the total number of The Art of the Deal votes to find the altered number: {taotd_initial_votes} - {taotd_discarded_votes} votes = <<{taotd_initial_votes}-{taotd_discarded_votes}={taotd_altered_votes}>>{taotd_altered_votes} votes"
        },
        {
          "line_number": "L3",
          "question_inputs": ["twilight_initial_votes", "twilight_discard_divisor"],
          "WK_inputs": [],
          "output_variable": "twilight_altered_votes",
          "solution_line_template": "Then divide the total number Twilight votes by {twilight_discard_divisor} to find the altered number of votes: {twilight_initial_votes} votes / {twilight_discard_divisor} = <<{twilight_initial_votes}/{twilight_discard_divisor}={twilight_altered_votes}>>{twilight_altered_votes} votes"
        },
        {
          "line_number": "L4",
          "question_inputs": ["got_initial_votes"],
          "WK_inputs": [],
          "output_variable": "total_altered_votes",
          "solution_line_template": "Then add the altered number of votes for each book to find the total altered number of votes: {twilight_altered_votes} votes + {taotd_altered_votes} votes + {got_initial_votes} votes = <<{twilight_altered_votes}+{taotd_altered_votes}+{got_initial_votes}={total_altered_votes}>>{total_altered_votes} votes"
        },
        {
          "line_number": "L5",
          "question_inputs": [],
          "WK_inputs": ["percent_multiplier"],
          "output_variable": "got_percentage",
          "solution_line_template": "Then divide the number of votes for Game of Thrones by the total altered number of votes and multiply by {percent_multiplier}% to express the answer as a percentage: {got_initial_votes} votes / {total_altered_votes} votes * {percent_multiplier}% = {got_percentage}%"
        }
      ]
    }
    ```
    
    ## Input
    
    **Index:**:
    1
    
    **Question:**:
    Weng earns $12 an hour for babysitting. Yesterday, she just did 50 minutes of babysitting. How much did she earn?
    
    **Solution mapping:**:
    {
      "L1": "Weng earns 12/60 = $<<12/60=0.2>>0.2 per minute.",
      "L2": "Working 50 minutes, she earned 0.2 x 50 = $<<0.2*50=10>>10."
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
        "name": "template_formalization", 
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

#### Cell 8: Main template generation functions


```python
from tqdm.notebook import tqdm
import pandas as pd

async def generate_templates_parallel_fixed(
    indices_to_generate: list[int],
    tier: str = CURRENT_TIER,
    dataset: 'datasets.Dataset' = GSM8K_TRAIN,
    model_dict: dict[str, str] = MODEL_DICT,
    system_prompt: str = SYSTEM_PROMPT,
    concurrency_limits: dict[str, int] = API_CONCURRENCY_LIMITS,
    json_schema: dict = BASE_TEMPLATE_SCHEMA,
    openai_max_tokens: int = 4000
    ):
    """
    Fully parallel version with a robust token bucket coordinator for OpenAI.
    """
    print("--- Starting Template Generation (Token Bucket) ---")
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
    print(f"\n--- Template Generation Complete ---")
    print(f"Processed {len(indices_to_generate)} indices in {end_time - start_time:.2f} seconds.")
    print(f"Performance log saved to: {csv_path}")
    
    success_count = len(df[df['status'] == 'Success'])
    total_calls = len(df)
    if total_calls > 0:
      print(f"Success rate: {success_count}/{total_calls} ({100*success_count/total_calls:.1f}%)")
    
    return df
```

#### Cell 9: Running the main Template generation function


```python
LOWER_LIMIT = 0
UPPER_LIMIT = 3000
INDICES_TO_GENERATE = [idx for idx in CURRENT_INDICES if idx <= UPPER_LIMIT and idx >= LOWER_LIMIT]

# print(f"Starting generation for {len(INDICES_TO_GENERATE)} indices in {CURRENT_TIER} between {LOWER_LIMIT} and {UPPER_LIMIT}.")

# perf_df = await generate_templates_parallel_fixed(indices_to_generate=INDICES_TO_GENERATE)

# print("\n--- Generation Performance Summary ---")
# perf_df.head()
```
