#### Cell 1: Paths, definitions, dataset


```python
import json
from pathlib import Path
import ast
import inspect
from datasets import load_dataset

GSM8K_TRAIN = load_dataset("gsm8k", "main")["train"]

# 1. Define Project Root and Data Directories
def find_project_root(marker: str = ".git") -> Path:
    """Traverse upwards to find the project root, marked by `marker`."""
    current_path = Path.cwd().resolve()
    while current_path != current_path.parent:
        if (current_path / marker).exists():
            return current_path
        current_path = current_path.parent
    raise FileNotFoundError(f"Could not find project root. Marker '{marker}' not found.")

PROJECT_ROOT = find_project_root()
DATA_DIR = PROJECT_ROOT / 'data'

# 2. Define path to validated manifests 
VALIDATED_MANIFEST_DIR = DATA_DIR / 'tier-manifests-examples-json' / 'tier3'
# Base directory for all processed outputs
PROCESSED_DATA_DIR = DATA_DIR / 'tier-manifests-examples-processed'

print(f"Project root: {PROJECT_ROOT}")
print(f"Data directory: {DATA_DIR}")
print(f"Validated Tier 2 manifest directory: {VALIDATED_MANIFEST_DIR}")

# 3. Check if the directory exists to prevent downstream errors
if not VALIDATED_MANIFEST_DIR.is_dir():
    print(f"\nWARNING: Directory not found: {VALIDATED_MANIFEST_DIR}")

# Specify the index to process
example_index = 4822
example_tier = "tier3"
```

    Project root: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math
    Data directory: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data
    Validated Tier 2 manifest directory: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/tier-manifests-examples-json/tier3



```python
### Generating tier lists
import re

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


#### Cell 2: Data loading and processing


```python
import importlib.util
from types import ModuleType

def load_manifest_as_string(manifest_dir: Path, index: int) -> str | None:
    """
    Loads a specific manifest file as a string.
    Note: Assumes filename is '{index}.json'. Adjust if format differs.
    """
    file_path = manifest_dir / f"_{index}.json"
    try:
        return file_path.read_text()
    except FileNotFoundError:
        print(f"ERROR: Manifest file not found at {file_path}")
        return None


def save_manifest_components(
    manifest_string: str,
    tier: str,
    index: int,
    base_output_dir: Path
) -> None:
    """
    Parses a manifest string and saves its components to structured directories.
    """
    try:
        manifest_data = json.loads(manifest_string)
    except json.JSONDecodeError:
        print(f"ERROR: Invalid JSON in manifest string for index {index}.")
        return

    function_code = manifest_data.get("function_code")
    logical_steps = manifest_data.get("logical_steps")

    if not function_code or not logical_steps:
        print(f"WARNING: Manifest for index {index} is missing required keys.")
        return

    # 1. Define output directory for the specific index
    output_dir = base_output_dir / tier / str(index)
    output_dir.mkdir(parents=True, exist_ok=True)

    # 2. Save function_code to a .py file
    py_file_path = output_dir / "solve.py"
    py_file_path.write_text(function_code)

    # 3. Save logical_steps to a .json file
    json_file_path = output_dir / "logical_steps.json"
    with open(json_file_path, 'w') as f:
        json.dump(logical_steps, f, indent=2)


def load_function_module(
    tier: str,
    index: int,
    base_dir: Path = PROCESSED_DATA_DIR
) -> ModuleType | None:
    """
    Dynamically loads the 'solve.py' function for a given tier and index.

    Args:
        tier: The tier of the problem (e.g., 'tier1').
        index: The index of the problem.
        base_dir: The base directory for processed files.

    Returns:
        The loaded module object, or None if the file is not found.
    """
    py_file_path = base_dir / tier / str(index) / "solve.py"
    if not py_file_path.exists():
        print(f"ERROR: Python file not found at {py_file_path}")
        return None

    # Create a unique name for the module to avoid conflicts
    module_name = f"manifests.t{tier}.i{index}.solve"

    spec = importlib.util.spec_from_file_location(module_name, py_file_path)
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    else:
        print(f"ERROR: Could not create module spec for {py_file_path}")
        return None


def load_logical_steps(
    tier: str,
    index: int,
    base_dir: Path = PROCESSED_DATA_DIR
) -> list[dict] | None:
    """
    Loads the 'logical_steps.json' for a given tier and index.

    Args:
        tier: The tier of the problem (e.g., 'tier1').
        index: The index of the problem.
        base_dir: The base directory for processed files.

    Returns:
        A list of dictionaries representing the logical steps, or None on error.
    """
    json_file_path = base_dir / tier / str(index) / "logical_steps.json"
    try:
        with open(json_file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"ERROR: JSON file not found at {json_file_path}")
        return None
    except json.JSONDecodeError:
        print(f"ERROR: Failed to decode JSON from {json_file_path}")
        return None

for index in [5, 54, 72, 964, 2332, 2422, 3592, 3822, 4764, 5531]:
    # Load
    manifest_str = load_manifest_as_string(VALIDATED_MANIFEST_DIR, index)

    # Process and Save
    if manifest_str:
        save_manifest_components(
            manifest_string=manifest_str,
            tier=example_tier,
            index=index,
            base_output_dir=PROCESSED_DATA_DIR
        )
        print(f"\nProcessed files for index {index} saved under: {PROCESSED_DATA_DIR}")
```

    
    Processed files for index 5 saved under: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/tier-manifests-examples-processed
    
    Processed files for index 54 saved under: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/tier-manifests-examples-processed
    
    Processed files for index 72 saved under: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/tier-manifests-examples-processed
    
    Processed files for index 964 saved under: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/tier-manifests-examples-processed
    
    Processed files for index 2332 saved under: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/tier-manifests-examples-processed
    
    Processed files for index 2422 saved under: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/tier-manifests-examples-processed
    
    Processed files for index 3592 saved under: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/tier-manifests-examples-processed
    
    Processed files for index 3822 saved under: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/tier-manifests-examples-processed
    
    Processed files for index 4764 saved under: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/tier-manifests-examples-processed
    
    Processed files for index 5531 saved under: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/tier-manifests-examples-processed


#### Cell 3: General utility functions


```python
def normalize_value(value):
    """
    Normalizes a numeric value for consistent comparison and rendering.
    If a float can be represented as an integer (e.g., 20.0), it is cast to int.
    """
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value

def get_sign(n) -> int:
    """Returns the sign of a number (1 for positive, -1 for negative, 0 for zero)."""
    if n > 0: return 1
    if n < 0: return -1
    return 0

def has_distinct_adjacent_digits(n: int) -> bool:
    """Helper to check if a number is suitable for digit transposition."""
    s = str(abs(n))
    return len(s) >= 2 and any(s[i] != s[i+1] for i in range(len(s) - 1))
```

#### Cell 4: Core trace and solution generation


```python
from typing import Any, Dict
import re
import copy
import random
from fractions import Fraction


def execution_trace(func_code_string: str) -> dict[str, Any] | None:
    """
    Executes a function string that may contain imports and returns a
    variable-to-value map of the 'solve' function's environment.
    """
    try:
        # 1. Execute the entire code string. This handles the import and
        #    defines the 'solve' function in a local namespace (`namespace`).
        namespace = {}
        exec(func_code_string, namespace)
        solve_func = namespace['solve']
    except Exception as e:
        print(f"ERROR: Failed to execute function code string: {e}")
        return None

    # 2. Get the source of the now-defined function and parse its body.
    try:
        src = inspect.getsource(solve_func)
        tree = ast.parse(src)
        func_def = tree.body[0]
    except Exception as e:
        print(f"ERROR: Could not get or parse source for solve(): {e}")
        return None

    # 3. Trace execution as before.
    env = {}
    for stmt in func_def.body:
        if isinstance(stmt, ast.Assign):
            try:
                # ast.Module is required to create a valid code block
                code_obj = compile(ast.Module([stmt], type_ignores=[]), '<string>', 'exec')
                exec(code_obj, namespace, env) # Use the same namespace to access Fraction
            except Exception as e:
                print(f"ERROR: Failed to execute line: {ast.unparse(stmt)}. Error: {e}")
                return None
    return env


def generate_flawed_trace(
    func,
    error_details: dict[str, Any]
) -> dict[str, Any] | None:
    """
    Generates a new execution trace by injecting a computational error.

    It modifies the function's AST in memory to replace a calculation
    with a hardcoded flawed value, then re-executes the logic to
    propagate the error.

    Args:
        func: The original function object to modify.
        error_details: Dict containing 'variable', 'correct_value', 'flawed_value'.

    Returns:
        A new dictionary representing the flawed execution trace, or None on error.
    """
    try:
        src = inspect.getsource(func)
        tree = ast.parse(src)
    except (TypeError, FileNotFoundError, SyntaxError) as e:
        print(f"ERROR: Could not get or parse source for {func.__name__}: {e}")
        return None

    func_def = tree.body[0]
    if not isinstance(func_def, ast.FunctionDef):
        print("ERROR: Parsed source does not start with a function definition.")
        return None

    variable_to_change = error_details["variable"]
    flawed_value = error_details["flawed_value"]
    
    modified_body = copy.deepcopy(func_def.body)

    node_found_and_modified = False
    for i, node in enumerate(modified_body):
        if isinstance(node, ast.Assign):
            if node.targets[0].id == variable_to_change:
                # --- FIX IS HERE ---
                # Create a new constant node for the flawed value and copy the
                # location info (lineno, col_offset) from the original node.
                new_value_node = ast.copy_location(
                    ast.Constant(value=flawed_value),
                    node.value  # The original RHS node we are replacing
                )
                node.value = new_value_node
                node_found_and_modified = True
                break
    
    if not node_found_and_modified:
        print(f"ERROR: Could not find assignment node for '{variable_to_change}' to modify.")
        return None

    env = {}
    for stmt in modified_body:
        if isinstance(stmt, ast.Assign):
            try:
                code_obj = compile(ast.Module([stmt], type_ignores=[]), '<string>', 'exec')
                exec(code_obj, {}, env)
            except Exception as e:
                print(f"ERROR: Failed to execute modified line: {ast.unparse(stmt)}. Error: {e}")
                return None
    
    return env


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


def reconstruct_solution_lines_enhanced(
    logical_steps: list[dict],
    eval_trace: dict[str, Any]
) -> dict[str, str]:
    """
    Substitutes variable placeholders. Includes logic to render Fraction objects
    as 'num/den' strings.
    """
    reconstructed_mapping = {}
    placeholder_pattern = re.compile(r'\{([a-zA-Z0-9_]+)\}')

    for step in logical_steps:
        line_number = step.get("line_number")
        template = step.get("solution_line_template")
        if not line_number or not template: continue

        def replacer(match):
            variable_name = match.group(1)
            value = eval_trace.get(variable_name)
            if value is None: return f"{{ERROR}}"
            
            # --- NEW FRACTION LOGIC ---
            if isinstance(value, Fraction):
                # Custom rendering for fractions as "num/den"
                return f"{value.numerator}/{value.denominator}"
            # --- END NEW LOGIC ---
            
            # Existing normalization for ints/floats
            return str(normalize_value(value))

        reconstructed_line = placeholder_pattern.sub(replacer, template)
        reconstructed_mapping[line_number] = reconstructed_line

    return reconstructed_mapping


```

#### Cell 5: Individual Error Generation functions


```python


def generate_off_by_n_error(
    correct_value: int,
    offset_range: tuple[int, int] = (1, 5)
    ):
    """Generates a minor miscalculation error. Assumes input is an integer."""
    offset = random.randint(offset_range[0], offset_range[1])
    if random.random() < 0.5:
        offset = -offset

    flawed_value = correct_value + offset
    if flawed_value == correct_value: # Avoid generating a non-error
        flawed_value += 1

    return {
        "flawed_value": flawed_value,
        "explanation_type": "This appears to be a minor miscalculation."
    }


def generate_off_by_factor_of_10_error(correct_value: int):
    """Generates a dropped/added zero error. Assumes input is a multiple of 100."""
    options = ["divide", "multiply"]
    choice = random.choice(options)
    
    if choice == "divide":
        flawed_value = correct_value // 10
        explanation = "It appears a zero was dropped from the number."
    else: # multiply
        flawed_value = correct_value * 10
        explanation = "It appears an extra zero was added to the number."

    return {
        "flawed_value": flawed_value,
        "explanation_type": explanation
    }


def generate_digit_transposition_error(correct_value: int) -> dict[str, Any] | None:
    """
    Swaps two adjacent digits. Now includes a check to prevent creating
    a leading zero, which would alter the number's magnitude.
    """
    # This check is important as this function should only ever receive integers
    if not isinstance(correct_value, int):
        return None

    s_val = str(abs(correct_value))
    
    # Pre-condition: must have at least 2 digits to swap.
    if len(s_val) < 2:
        return None

    # Find all indices where adjacent digits are different
    possible_indices = [i for i in range(len(s_val) - 1) if s_val[i] != s_val[i+1]]
    
    # --- NEW VALIDATION LOGIC ---
    # Filter out swaps that would create a leading zero.
    # A swap at index i is invalid if i=0 and the digit at i+1 is '0'.
    valid_indices = [
        i for i in possible_indices
        if not (i == 0 and s_val[i+1] == '0')
    ]
    
    # If no valid swaps are possible, we cannot generate this error.
    if not valid_indices:
        return None
    # --- END NEW LOGIC ---

    idx_to_swap = random.choice(valid_indices)
    
    s_list = list(s_val)
    s_list[idx_to_swap], s_list[idx_to_swap+1] = s_list[idx_to_swap+1], s_list[idx_to_swap]
    
    flawed_value = int("".join(s_list))
    if correct_value < 0:
        flawed_value = -flawed_value

    return {
        "flawed_value": flawed_value,
        "explanation_type": "It appears two adjacent digits were swapped."
    }


def generate_stem_off_by_n_error(
    correct_value: int,
    offset_range: tuple[int, int] = (1, 3)
) -> dict[str, Any]:
    """
    Applies a small offset to the 'stem' of a number (the part before the final zero).
    Assumes the input is a non-zero multiple of 10.
    """
    stem = correct_value // 10
    
    offset = random.randint(offset_range[0], offset_range[1])
    if random.random() < 0.5:
        offset = -offset

    flawed_stem = stem + offset
    if flawed_stem == stem:
        flawed_stem += 1 # Ensure the value changes

    flawed_value = flawed_stem * 10

    return {
        "flawed_value": flawed_value,
        "explanation_type": "It appears there was a miscalculation with the digits before the final zero."
    }


def generate_reciprocal_error(correct_value: Fraction) -> dict[str, Any] | None:
    """Swaps the numerator and denominator of a fraction."""
    if correct_value.denominator == 0: return None # Should not happen
    
    flawed_value = Fraction(correct_value.denominator, correct_value.numerator)
    return {
        "flawed_value": flawed_value,
        "explanation_type": "It appears the numerator and denominator were swapped."
    }


def generate_off_by_one_in_fraction_part_error(correct_value: Fraction) -> dict[str, Any]:
    """Adds or subtracts 1 from either the numerator or the denominator."""
    part_to_change = random.choice(["numerator", "denominator"])
    offset = random.choice([-1, 1])

    if part_to_change == "numerator":
        new_num = correct_value.numerator + offset
        new_den = correct_value.denominator
    else: # denominator
        new_num = correct_value.numerator
        new_den = correct_value.denominator + offset
        # Avoid creating a zero denominator
        if new_den == 0:
            new_den = correct_value.denominator + (offset * 2)

    return {
        "flawed_value": Fraction(new_num, new_den),
        "explanation_type": "It appears there was an off-by-one error in the fraction."
    }


def generate_fraction_pemdas_error(fraction_val: Fraction, integer_val: int) -> dict[str, Any]:
    """
    Simulates the PEMDAS error: a/b * c -> a / (b * c).
    """
    new_den = fraction_val.denominator * integer_val
    # The numerator remains the same
    new_num = fraction_val.numerator
    
    flawed_value = Fraction(new_num, new_den)
    return {
        "flawed_value": flawed_value,
        "explanation_type": "It appears the integer was incorrectly multiplied with the denominator."
    }
```

#### Cell 6: Error Generation Controller and Helpers


```python
import ast
import inspect

def get_target_variables(logical_steps: list[dict]) -> list[str]:
    """
    Extracts all 'output_variable' names from the logical steps.
    These are the potential locations for injecting a computational error.
    """
    return [step['output_variable'] for step in logical_steps if 'output_variable' in step]


def has_distinct_adjacent_digits(n: int) -> bool:
    """Helper to check if a number is suitable for digit transposition."""
    s = str(abs(n))
    return len(s) >= 2 and any(s[i] != s[i+1] for i in range(len(s) - 1))


def get_operator_for_variable(func, variable_name: str) -> str | None:
    """Inspects the AST to find the operator used to compute a variable."""
    # (implementation from previous response is unchanged)
    try:
        src = inspect.getsource(func)
        tree = ast.parse(src)
    except (TypeError, FileNotFoundError, SyntaxError): return None
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and node.targets[0].id == variable_name:
            if isinstance(node.value, ast.BinOp):
                op = node.value.op
                if isinstance(op, ast.Add): return "add"
                if isinstance(op, ast.Sub): return "sub"
                if isinstance(op, ast.Mult): return "mult"
                if isinstance(op, ast.Div): return "div"
            return "other"
    return None


def get_operand_names_for_variable(func, variable_name: str) -> list[str]:
    """
    Inspects the AST to find the names of variables used as operands
    in the calculation for the given target variable.
    """
    operand_names = []
    try:
        src = inspect.getsource(func)
        tree = ast.parse(src)
    except (TypeError, FileNotFoundError, SyntaxError):
        return []

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and node.targets[0].id == variable_name:
            # We walk the right-hand side of the assignment
            for sub_node in ast.walk(node.value):
                # And collect the names of all variables used
                if isinstance(sub_node, ast.Name):
                    operand_names.append(sub_node.id)
            return list(set(operand_names)) # Use set to get unique names
    return []


def find_fraction_times_integer_vars(func) -> dict[str, tuple[str, str]]:
    """
    Finds variables resulting from `Fraction * Integer`.
    Returns a dictionary mapping the output variable to the names of the
    fraction and integer operand variables.
    e.g., {'output_var': ('fraction_var', 'integer_var')}
    """
    candidates = {}
    try:
        src = inspect.getsource(func)
        tree = ast.parse(src)
    except Exception:
        return {}

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            var_name = node.targets[0].id
            # Must be a multiplication
            if not (isinstance(node.value, ast.BinOp) and isinstance(node.value.op, ast.Mult)):
                continue

            left_operand = node.value.left
            right_operand = node.value.right
            
            # Check if the structure is `Call(Fraction(...)) * Name`
            if isinstance(left_operand, ast.Call) and isinstance(right_operand, ast.Name):
                if isinstance(left_operand.func, ast.Name) and left_operand.func.id == 'Fraction':
                    candidates[var_name] = (left_operand.func.id, right_operand.id) # Storing 'Fraction' is a placeholder
            # Check if structure is `Name * Name`
            elif isinstance(left_operand, ast.Name) and isinstance(right_operand, ast.Name):
                 # This is more complex as we don't know which is the fraction.
                 # For now, we stick to the simpler, explicit `Fraction(...) * int` case.
                 pass

    return candidates

# This is a helper function to avoid repeating the integer logic.
# The leading underscore indicates it's for internal use by the main controller.
def _get_applicable_integer_errors(correct_value: int, operator: str, operand_values: list) -> list:
    """Returns a list of applicable error generator functions for an integer."""
    applicable_generators = []
    
    # Rule: Handle addition and subtraction with special cases
    if operator in ["add", "sub"]:
        all_end_in_zero = all(isinstance(v, int) and v % 10 == 0 for v in operand_values) if operand_values else False
        if all_end_in_zero and correct_value % 10 == 0 and correct_value != 0:
            applicable_generators.append(generate_stem_off_by_n_error)
        else:
            applicable_generators.append(generate_off_by_n_error)

    # Rule: Factor-of-10 error for multiples of 100.
    if correct_value % 100 == 0 and correct_value != 0:
        applicable_generators.append(generate_off_by_factor_of_10_error)
    
    # Rule: Digit transposition.
    if has_distinct_adjacent_digits(correct_value):
        applicable_generators.append(generate_digit_transposition_error)
        
    return applicable_generators


def generate_computational_error(
    func,
    correct_trace: dict[str, Any],
    target_variables: list[str],
    debug: bool = False
) -> dict[str, Any] | None:
    """
    Applies a valid error type based on a rule-based system for ints and floats.
    Includes the fix for integer-like float handling.
    """
    shuffled_targets = random.sample(target_variables, len(target_variables))

    if debug: print("\n--- DEBUG: Analyzing potential error targets ---")

    for variable_name in shuffled_targets:
        correct_value = correct_trace.get(variable_name)
        operator = get_operator_for_variable(func, variable_name)

        if debug: print(f"\n- Var: '{variable_name}' (Value: {correct_value}, Type: {type(correct_value).__name__}, Op: '{operator}')")

        # --- Integer Branch ---
        if isinstance(correct_value, int):
            operand_names = get_operand_names_for_variable(func, variable_name)
            operand_values = [correct_trace.get(name) for name in operand_names]
            applicable_generators = _get_applicable_integer_errors(correct_value, operator, operand_values)
            
            if debug: print_applicable_generators(applicable_generators)
                
            if applicable_generators:
                generator_func = random.choice(applicable_generators)
                error_result = generator_func(correct_value)
                return { "variable": variable_name, "correct_value": correct_value, **error_result }

        # --- Float Branch ---
        elif isinstance(correct_value, float):
            applicable_generators = []
            
            # Rule #3: Integer-like floats (e.g., 2000.0)
            if correct_value.is_integer():
                int_val = int(correct_value)
                operand_names = get_operand_names_for_variable(func, variable_name)
                operand_values = [correct_trace.get(name) for name in operand_names]
                
                # Get the list of applicable INTEGER generators
                integer_error_gens = _get_applicable_integer_errors(int_val, operator, operand_values)

                if debug: print_applicable_generators(integer_error_gens)

                if integer_error_gens:
                    # --- THIS IS THE FIX ---
                    # 1. Choose an integer-based generator.
                    generator_func = random.choice(integer_error_gens)
                    # 2. Call it with the INTEGER value.
                    error_result = generator_func(int_val)
                    # 3. Convert the resulting flawed integer BACK to a float.
                    error_result['flawed_value'] = float(error_result['flawed_value'])
                    # 4. Return the complete error details.
                    return { "variable": variable_name, "correct_value": correct_value, **error_result }

            # Rules for "true" floats
            else:
                # Rule #2: Monetary floats ending in .00
                if str(correct_value).endswith('.00'):
                    applicable_generators.append(generate_monetary_off_by_cents_error)
                # Rule #4: General floats
                else:
                    applicable_generators.append(generate_float_off_by_n_error)
                
                # Decimal shift is applicable to most true floats
                applicable_generators.append(generate_decimal_shift_error)
                
                if debug: print_applicable_generators(applicable_generators)

                if applicable_generators:
                    generator_func = random.choice(applicable_generators)
                    error_result = generator_func(correct_value)
                    return { "variable": variable_name, "correct_value": correct_value, **error_result }

    if debug: print("--- END DEBUG ---")
    else: print("WARNING: Could not find a suitable variable/error type combination.")
    return None


def get_applicable_generators(
    func,
    correct_trace: dict[str, Any],
    variable_name: str
) -> list:
    """
    Final refined logic to provide diverse but non-redundant error types.
    """
    correct_value = correct_trace.get(variable_name)
    if not isinstance(correct_value, (int, float)): return []

    operator = get_operator_for_variable(func, variable_name)
    operand_names = get_operand_names_for_variable(func, variable_name)
    operand_values = [correct_trace.get(name) for name in operand_names]
    
    # --- Integer and Integer-like Float Logic ---
    if isinstance(correct_value, int) or (isinstance(correct_value, float) and correct_value.is_integer()):
        int_val = int(correct_value)
        return _get_applicable_integer_errors(int_val, operator, operand_values)
    
    # --- "True" Float Logic ---
    elif isinstance(correct_value, float):
        applicable_generators = []
        applicable_generators.append(generate_float_off_by_n_error)
        
        # Decimal shift is only for true floats.
        if correct_value != 0:
            applicable_generators.append(generate_decimal_shift_error)
            
        return list(set(applicable_generators))
        
    return []


# Helper for cleaner debug output
def print_applicable_generators(generators: list):
    gen_names = [g.__name__ for g in generators]
    print(f"  Applicable Generators: {gen_names if gen_names else 'NONE'}")

```

#### Cell 7: Validation Logic


```python
def is_trace_valid(
    flawed_trace: dict[str, Any],
    correct_trace: dict[str, Any]
) -> bool:
    """
    Validates a flawed trace with a strict but correct type-checking rule:
    An integer-like value must remain integer-like.
    """
    for var_name, correct_val in correct_trace.items():
        if var_name not in flawed_trace:
            continue

        flawed_val = flawed_trace.get(var_name)
        
        # --- NEW, CORRECTED TYPE CHECK ---
        # Normalize both values to see if they represent integers.
        is_correct_int_like = isinstance(normalize_value(correct_val), int)
        is_flawed_int_like = isinstance(normalize_value(flawed_val), int)

        # Rule: If the correct value was integer-like, the flawed one must also be.
        # This prevents errors like "15 students" becoming "15.5 students".
        if is_correct_int_like and not is_flawed_int_like:
            print(f"VALIDATION FAIL (Type): Var '{var_name}' changed from an int-like value to a true float ({correct_val} -> {flawed_val}).")
            return False
        # --- END NEW TYPE CHECK ---

        # Sign Check remains the same
        processed_correct = normalize_value(correct_val)
        processed_flawed = normalize_value(flawed_val)
        if isinstance(processed_correct, (int, float)):
            if get_sign(processed_correct) != get_sign(processed_flawed):
                print(f"VALIDATION FAIL (Sign): Var '{var_name}' changed sign from {correct_val} to {flawed_val}.")
                return False
                
    return True


# # --- Example of how to use and verify the new function ---

# # 1. Load your module, logical steps, and generate the correct trace first
# solve_module = load_function_module(example_tier, example_index)
# logical_steps = load_logical_steps(example_tier, example_index)
# correct_trace = None
# if solve_module:
#     solve_function = solve_module.solve
#     correct_trace = execution_trace(solve_function)

# # 2. Run the enhanced reconstruction
# if logical_steps and correct_trace:
#     print("Reconstructing solution lines with enhanced formatting...")
#     reconstructed_solution = reconstruct_solution_lines_enhanced(logical_steps, correct_trace)

#     print("\n--- RECONSTRUCTED SOLUTION (ENHANCED) ---")
#     print(json.dumps(reconstructed_solution, indent=2))

#     # 3. Build and print the original solution for direct comparison
#     print("\n--- ORIGINAL SOLUTION (FOR COMPARISON) ---")
#     original_solution = build_solution_mapping(index=example_index)
#     print(json.dumps(original_solution, indent=2))
```

#### Cell 8: Final Artifact assembly


```python

def find_error_line_number(
    variable_name: str,
    logical_steps: list[dict]
) -> str | None:
    """Finds the line number corresponding to a given output variable."""
    for step in logical_steps:
        if step.get("output_variable") == variable_name:
            return step.get("line_number")
    return None


def generate_training_artifacts_enhanced(
    logical_steps: list[dict],
    error_details: dict[str, Any],
    flawed_trace: dict[str, Any]
    ):
    """
    Generates the final training data with an enhanced explanation.
    """
    flawed_solution_map = reconstruct_solution_lines_enhanced(logical_steps, flawed_trace)
    if not flawed_solution_map:
        return None
    
    sorted_lines = sorted(flawed_solution_map.items(), key=lambda item: int(item[0][1:]))
    flawed_nl_solution = "\n".join([line for _, line in sorted_lines])

    erroneous_line = find_error_line_number(error_details["variable"], logical_steps)
    if not erroneous_line:
        return None

    # --- Create the enhanced explanation ---
    base_explanation = (
        f"The result of this computation should be {error_details['correct_value']}, "
        f"not {error_details['flawed_value']}."
    )
    type_explanation = error_details["explanation_type"]
    final_explanation = f"{base_explanation} {type_explanation}"

    target_json = {
        "verdict": "Flawed",
        "error_details": {
            "error_type": "computational_error",
            "erroneous_line_number": erroneous_line,
            "explanation": final_explanation,
        }
    }

    return flawed_nl_solution, target_json


```

#### Cell 9: Main Orchestrator


```python

def create_single_error_example(
    func,
    logical_steps,
    correct_trace,
    max_attempts=10
):
    """
    Orchestrates the entire error generation process with validation and retries.
    """
    target_variables = get_target_variables(logical_steps)

    for i in range(max_attempts):
        print(f"Attempt {i+1}/{max_attempts}...")
        
        error_details = generate_computational_error(func, correct_trace, target_variables)
        if not error_details:
            print(" -> Failed to generate an error candidate. Retrying.")
            continue

        flawed_trace = generate_flawed_trace(func, error_details)
        if not flawed_trace:
            print(" -> Failed to generate a flawed trace. Retrying.")
            continue

        # The orchestrator calls the new, more robust validator
        if is_trace_valid(flawed_trace, correct_trace):
            flawed_nl_solution, target_json = generate_training_artifacts_enhanced(
                logical_steps, error_details, flawed_trace
            )
            print(f" -> Success! Generated a valid flawed example.")
            return flawed_nl_solution, target_json
        else:
            print(" -> Generated trace was invalid. Retrying.")

    print(f"\nFailed to generate a valid error example after {max_attempts} attempts.")
    return None, None


```

#### Cell 9: Testing


```python
import json
import random
import inspect

def run_comprehensive_error_test(tier: str, index: int):
    """
    Runs an exhaustive and deterministic test of all possible valid computational
    errors for every variable in a given problem.
    """
    print("="*60)
    print(f"STARTING COMPREHENSIVE TEST FOR: Tier '{tier}', Index '{index}'")
    print("="*60)

    # --- 1. Load Data ---
    solve_module = load_function_module(tier, index)
    logical_steps = load_logical_steps(tier, index)
    if not (solve_module and logical_steps):
        print("ERROR: Failed to load data. Aborting.")
        return
    solve_function = solve_module.solve
    
    # --- 2. Generate Correct Trace ---
    correct_trace = execution_trace(solve_function)
    if not correct_trace:
        print("ERROR: Failed to generate correct trace. Aborting.")
        return

    # --- 3. Iterate Through All Target Variables ---
    target_variables = get_target_variables(logical_steps)
    print(f"\nFound {len(target_variables)} target variables to test: {target_variables}")

    for variable_name in target_variables:
        # --- THIS IS THE FIX ---
        correct_value = correct_trace.get(variable_name)
        # --- END FIX ---
        
        print("\n" + "~"*60)
        print(f"--- TESTING VARIABLE: '{variable_name}' (Correct Value: {correct_value}) ---")
        
        seed = hash(f"{index}-{variable_name}")
        random.seed(seed)
        
        applicable_generators = get_applicable_generators(solve_function, correct_trace, variable_name)
        
        if not applicable_generators:
            print("  -> No applicable error types found for this variable.")
            continue
        
        print(f"  -> Found {len(applicable_generators)} applicable error types: {[g.__name__ for g in applicable_generators]}")

        # --- 4. Test Every Applicable Error Type ---
        for generator_func in applicable_generators:
            print(f"\n  --- Applying Error: {generator_func.__name__} ---")
            
            random.seed(seed + hash(generator_func.__name__))

            # The value passed to the generator depends on whether it's an integer-like float
            value_for_generator = int(correct_value) if isinstance(correct_value, float) and correct_value.is_integer() else correct_value
            error_result = generator_func(value_for_generator)
            
            if not error_result:
                print("    -> Generator returned None (e.g., no valid transposition). Skipping.")
                continue

            error_details = {"variable": variable_name, "correct_value": correct_value, **error_result}
            if isinstance(correct_value, float) and correct_value.is_integer():
                error_details['flawed_value'] = float(error_details['flawed_value'])

            flawed_trace = generate_flawed_trace(solve_function, error_details)
            if not is_trace_valid(flawed_trace, correct_trace):
                print("    -> FAILED: Generated an invalid trace (sign/type change). Skipping.")
                continue

            flawed_solution, target_label = generate_training_artifacts_enhanced(logical_steps, error_details, flawed_trace)
            
            print(f"\n    --- Flawed Solution (using {generator_func.__name__}) ---")
            print(flawed_solution)
            print("\n    --- Target JSON Label ---")
            print(json.dumps(target_label, indent=2))

    print("\n" + "="*60)
    print("COMPREHENSIVE TEST COMPLETE")
    print("="*60)


# --- Run the new comprehensive test ---
for index in [5, 54, 72, 964, 2332, 2422, 3592, 3822, 4764, 5531]:
    try:
        run_comprehensive_error_test(tier=example_tier, index=index)
    except Exception as e:
        import traceback
        print(f"\nAN UNCAUGHT ERROR OCCURRED: {e}")
        traceback.print_exc()
```

    ============================================================
    STARTING COMPREHENSIVE TEST FOR: Tier 'tier3', Index '5'
    ============================================================
    ERROR: Failed to execute function code string: exec() arg 1 must be a string, bytes or code object
    ERROR: Failed to generate correct trace. Aborting.
    ============================================================
    STARTING COMPREHENSIVE TEST FOR: Tier 'tier3', Index '54'
    ============================================================
    ERROR: Failed to execute function code string: exec() arg 1 must be a string, bytes or code object
    ERROR: Failed to generate correct trace. Aborting.
    ============================================================
    STARTING COMPREHENSIVE TEST FOR: Tier 'tier3', Index '72'
    ============================================================
    ERROR: Failed to execute function code string: exec() arg 1 must be a string, bytes or code object
    ERROR: Failed to generate correct trace. Aborting.
    ============================================================
    STARTING COMPREHENSIVE TEST FOR: Tier 'tier3', Index '964'
    ============================================================
    ERROR: Failed to execute function code string: exec() arg 1 must be a string, bytes or code object
    ERROR: Failed to generate correct trace. Aborting.
    ============================================================
    STARTING COMPREHENSIVE TEST FOR: Tier 'tier3', Index '2332'
    ============================================================
    ERROR: Failed to execute function code string: exec() arg 1 must be a string, bytes or code object
    ERROR: Failed to generate correct trace. Aborting.
    ============================================================
    STARTING COMPREHENSIVE TEST FOR: Tier 'tier3', Index '2422'
    ============================================================
    ERROR: Failed to execute function code string: exec() arg 1 must be a string, bytes or code object
    ERROR: Failed to generate correct trace. Aborting.
    ============================================================
    STARTING COMPREHENSIVE TEST FOR: Tier 'tier3', Index '3592'
    ============================================================
    ERROR: Failed to execute function code string: exec() arg 1 must be a string, bytes or code object
    ERROR: Failed to generate correct trace. Aborting.
    ============================================================
    STARTING COMPREHENSIVE TEST FOR: Tier 'tier3', Index '3822'
    ============================================================
    ERROR: Failed to execute function code string: exec() arg 1 must be a string, bytes or code object
    ERROR: Failed to generate correct trace. Aborting.
    ============================================================
    STARTING COMPREHENSIVE TEST FOR: Tier 'tier3', Index '4764'
    ============================================================
    ERROR: Failed to execute function code string: exec() arg 1 must be a string, bytes or code object
    ERROR: Failed to generate correct trace. Aborting.
    ============================================================
    STARTING COMPREHENSIVE TEST FOR: Tier 'tier3', Index '5531'
    ============================================================
    ERROR: Failed to execute function code string: exec() arg 1 must be a string, bytes or code object
    ERROR: Failed to generate correct trace. Aborting.

