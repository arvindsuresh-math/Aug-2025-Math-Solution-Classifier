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
VALIDATED_MANIFEST_DIR = DATA_DIR / 'tier-manifests-examples-json' / 'tier4'
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
example_tier = "tier4"
```

    Project root: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math
    Data directory: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data
    Validated Tier 2 manifest directory: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/tier-manifests-examples-json/tier4



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

for index in [1, 672, 3847, 4847, 5040, 6216, 7037]:
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

    
    Processed files for index 1 saved under: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/tier-manifests-examples-processed
    
    Processed files for index 672 saved under: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/tier-manifests-examples-processed
    
    Processed files for index 3847 saved under: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/tier-manifests-examples-processed
    
    Processed files for index 4847 saved under: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/tier-manifests-examples-processed
    
    Processed files for index 5040 saved under: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/tier-manifests-examples-processed
    
    Processed files for index 6216 saved under: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/tier-manifests-examples-processed
    
    Processed files for index 7037 saved under: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/tier-manifests-examples-processed


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
import inspect
import ast
from fractions import Fraction
from typing import Callable, Any, Dict

def execution_trace(func: Callable[[], Any]) -> Dict[str, Any] | None:
    """
    Executes a given function object line-by-line and returns a
    variable-to-value map of its local environment.
    This function automatically makes the 'Fraction' class available.
    """
    try:
        # 1. Get the source code directly from the function object.
        src = inspect.getsource(func)
        tree = ast.parse(src)
        func_def = tree.body[0]
    except Exception as e:
        print(f"ERROR: Could not get or parse source for {func.__name__}: {e}")
        return None

    # 2. Prepare the execution environments.
    #    - global_namespace provides built-ins and our custom 'Fraction'.
    #    - local_env will store the computed variables.
    global_namespace = {'Fraction': Fraction}
    local_env = {}

    # 3. Execute each statement in the function's body.
    for stmt in func_def.body:
        # We only trace assignments. This ignores the docstring, return statement, etc.
        if isinstance(stmt, ast.Assign):
            try:
                # Create a valid code block for compile()
                module_node = ast.Module([stmt], type_ignores=[])
                code_obj = compile(module_node, '<string>', 'exec')
                
                # Execute the line using the prepared namespaces.
                exec(code_obj, global_namespace, local_env)
            except Exception as e:
                print(f"ERROR: Failed to execute line: {ast.unparse(stmt)}. Error: {e}")
                return None
    
    # 4. Return the populated local environment.
    return local_env


def generate_flawed_trace(
    func,
    error_details: dict[str, Any]
) -> dict[str, Any] | None:
    """
    Generates a new execution trace. This version uses ast.fix_missing_locations
    to ensure all manually created AST nodes have the required location info.
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
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == variable_to_change for t in node.targets):
            if isinstance(flawed_value, Fraction):
                new_value_node = ast.Call(
                    func=ast.Name(id='Fraction', ctx=ast.Load()),
                    args=[
                        ast.Constant(value=flawed_value.numerator),
                        ast.Constant(value=flawed_value.denominator)
                    ],
                    keywords=[]
                )
            else:
                new_value_node = ast.Constant(value=flawed_value)
            
            # --- THIS IS THE FIX ---
            # 1. Copy location from the original RHS to the new top-level node.
            ast.copy_location(new_value_node, node.value)
            # 2. Recursively add location info to all children of the new node.
            ast.fix_missing_locations(new_value_node)
            # 3. Assign the now-valid node.
            node.value = new_value_node
            # --- END FIX ---
            
            node_found_and_modified = True
            break
    
    if not node_found_and_modified:
        print(f"ERROR: Could not find assignment node for '{variable_to_change}' to modify.")
        return None

    global_namespace = {'Fraction': Fraction}
    env = {}

    for stmt in modified_body:
        if isinstance(stmt, ast.Assign):
            try:
                code_obj = compile(ast.Module([stmt], type_ignores=[]), '<string>', 'exec')
                exec(code_obj, global_namespace, env)
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
    Substitutes variable placeholders. This version correctly renders
    integer-like Fraction objects (e.g., Fraction(8,1)) as integers.
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
            
            # --- THIS IS THE FIX ---
            if isinstance(value, Fraction):
                # If the denominator is 1, render it as a simple integer.
                if value.denominator == 1:
                    return str(value.numerator)
                # Otherwise, render as "num/den".
                return f"{value.numerator}/{value.denominator}"
            # --- END FIX ---
            
            return str(normalize_value(value))

        reconstructed_line = placeholder_pattern.sub(replacer, template)
        reconstructed_mapping[line_number] = reconstructed_line

    return reconstructed_mapping


```

#### Cell 5: Individual Error Generation functions


```python
import random
import copy

def generate_off_by_n_error(
    correct_value: int,
    offset_range: tuple[int, int] = (1, 5)
    ):
    """Generates a minor miscalculation error, preventing sign changes."""
    offset = random.randint(offset_range[0], offset_range[1])
    if random.random() < 0.5:
        offset = -offset

    flawed_value = correct_value + offset
    
    # --- THIS IS THE FIX ---
    # If the sign flips, either use a smaller offset or flip the offset's sign
    if get_sign(correct_value) != get_sign(flawed_value) and correct_value != 0:
        flawed_value = correct_value - offset # Try the opposite offset

    # Ensure value actually changes, especially if the fix above reverted it
    if flawed_value == correct_value:
        flawed_value += 1 if correct_value >= 0 else -1
    # --- END FIX ---
    
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


def generate_decimal_shift_error(correct_value: float) -> dict[str, Any]:
    """Multiplies or divides a float by 10 to simulate a decimal shift."""
    choice = random.choice(["multiply", "divide"])
    flawed_value = correct_value * 10 if choice == "multiply" else correct_value / 10
    return {
        "flawed_value": round(flawed_value, 10), # Round to avoid precision issues
        "explanation_type": "It appears the decimal point was misplaced."
    }


def generate_float_off_by_n_error(correct_value: float) -> dict[str, Any]:
    """Applies a small offset to a general float."""
    # This creates an offset that is roughly 10-20% of the original value's magnitude
    magnitude = abs(correct_value)
    offset = random.uniform(magnitude * 0.1, magnitude * 0.2)
    if random.random() < 0.5:
        offset = -offset
        
    flawed_value = correct_value + offset
    return {
        "flawed_value": round(flawed_value, 10),
        "explanation_type": "This appears to be a minor miscalculation."
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


def generate_multiplication_by_reciprocal_error(
    numeric_val: 'Any',
    fraction_val: 'Fraction'
) -> dict[str, Any] | None:
    """
    Simulates an error where a value is multiplied by the reciprocal of the
    intended fraction (e.g., x * (b/a) instead of x * (a/b)).

    Returns None if the original fraction's numerator is 0 to avoid DivisionByZero.
    """
    # Edge Case: Prevent division by zero
    if fraction_val.numerator == 0:
        return None

    reciprocal_fraction = Fraction(fraction_val.denominator, fraction_val.numerator)
    flawed_value = numeric_val * reciprocal_fraction
    
    return {
        "flawed_value": flawed_value,
        "explanation_type": "It appears the value was multiplied by the reciprocal of the intended fraction."
    }
```

#### Cell 6: Error Generation Controller and Helpers


```python
import ast
import inspect
import functools

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
    Applies a valid error type. This version uses a simplified calling
    mechanism for pre-packaged generator functions.
    """
    shuffled_targets = random.sample(target_variables, len(target_variables))

    if debug: print("\n--- DEBUG: Analyzing potential error targets ---")

    for variable_name in shuffled_targets:
        correct_value = correct_trace.get(variable_name)
        applicable_generators = get_applicable_generators(func, correct_trace, variable_name)

        if debug:
            print(f"\n- Var: '{variable_name}' (Value: {correct_value}, Type: {type(correct_value).__name__})")
            print_applicable_generators(applicable_generators)

        if applicable_generators:
            generator_func = random.choice(applicable_generators)
            
            # Simplified, uniform call to the pre-packaged generator
            error_result = generator_func()

            if error_result:
                if isinstance(correct_value, float) and correct_value.is_integer():
                     error_result['flawed_value'] = float(error_result['flawed_value'])
                return { "variable": variable_name, "correct_value": correct_value, **error_result }

    if debug: print("--- END DEBUG ---")
    else: print("WARNING: Could not find a suitable variable/error type combination.")
    return None


import functools

def get_applicable_generators(
    func,
    correct_trace: dict[str, Any],
    variable_name: str
) -> list:
    """
    Identifies applicable error generators. This version includes a check for
    multiplication by a reciprocal fraction.
    """
    applicable_generators = []
    correct_value = correct_trace.get(variable_name)
    if not isinstance(correct_value, (int, float, Fraction)):
        return []

    # Helper to create and add a partial function
    def add_generator(gen_func, value_to_pass):
        partial_gen = functools.partial(gen_func, value_to_pass)
        partial_gen.__name__ = gen_func.__name__
        applicable_generators.append(partial_gen)

    # --- Part 1: Type-Based Error Selection ---
    if isinstance(correct_value, int) or (isinstance(correct_value, float) and correct_value.is_integer()) or (isinstance(correct_value, Fraction) and correct_value.denominator == 1):
        int_val = int(correct_value)
        # We don't apply integer errors if the operator is multiplication,
        # as that's handled by the more specific context-based check below.
        op = get_operator_for_variable(func, variable_name)
        if op != "mult":
             op_names = get_operand_names_for_variable(func, variable_name)
             op_vals = [correct_trace.get(name) for name in op_names if name in correct_trace]
             integer_gens = _get_applicable_integer_errors(int_val, op, op_vals)
             for gen_func in integer_gens:
                 add_generator(gen_func, int_val)

    elif isinstance(correct_value, float):
        add_generator(generate_float_off_by_n_error, correct_value)
        if correct_value != 0:
            add_generator(generate_decimal_shift_error, correct_value)

    elif isinstance(correct_value, Fraction) and correct_value.denominator != 1:
        add_generator(generate_off_by_one_in_fraction_part_error, correct_value)
        if correct_value.numerator != 0:
            add_generator(generate_reciprocal_error, correct_value)

    # --- Part 2: Context-Based Error Selection ---
    operator = get_operator_for_variable(func, variable_name)
    if operator == "mult":
        operand_names = get_operand_names_for_variable(func, variable_name)
        operand_values = [correct_trace.get(name) for name in operand_names if name in correct_trace]
        
        if len(operand_values) == 2:
            # --- NEW CONTEXT CHECK ---
            # Identify the numeric and fraction operands for the new error type.
            num_op = next((op for op in operand_values if isinstance(op, (int, float))), None)
            frac_op = next((op for op in operand_values if isinstance(op, Fraction)), None)

            # Condition: One numeric operand, one non-integer fraction operand, and a non-integer result.
            if num_op is not None and frac_op is not None and frac_op.denominator != 1 and isinstance(correct_value, Fraction) and correct_value.denominator != 1:
                reciprocal_mult_gen = functools.partial(
                    generate_multiplication_by_reciprocal_error,
                    numeric_val=num_op,
                    fraction_val=frac_op
                )
                reciprocal_mult_gen.__name__ = 'generate_multiplication_by_reciprocal_error'
                applicable_generators.append(reciprocal_mult_gen)
            # --- END NEW CONTEXT CHECK ---
            
            # Default integer error for multiplication results
            elif isinstance(correct_value, int):
                 op_names = get_operand_names_for_variable(func, variable_name)
                 op_vals = [correct_trace.get(name) for name in op_names if name in correct_trace]
                 integer_gens = _get_applicable_integer_errors(correct_value, operator, op_vals)
                 for gen_func in integer_gens:
                     add_generator(gen_func, correct_value)


    return list(dict.fromkeys(applicable_generators))


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

# def run_comprehensive_error_test(tier: str, index: int):
#     """
#     Runs an exhaustive and deterministic test of all possible valid computational
#     errors for every variable in a given problem.
#     """
#     print("="*60)
#     print(f"STARTING COMPREHENSIVE TEST FOR: Tier '{tier}', Index '{index}'")
#     print("="*60)

#     # --- 1. Load Data ---
#     solve_module = load_function_module(tier, index)
#     logical_steps = load_logical_steps(tier, index)
#     if not (solve_module and logical_steps):
#         print("ERROR: Failed to load data. Aborting.")
#         return
#     solve_function = solve_module.solve
    
#     # --- 2. Generate Correct Trace ---
#     correct_trace = execution_trace(solve_function)
#     if not correct_trace:
#         print("ERROR: Failed to generate correct trace. Aborting.")
#         return

#     # --- 3. Iterate Through All Target Variables ---
#     target_variables = get_target_variables(logical_steps)
#     print(f"\nFound {len(target_variables)} target variables to test: {target_variables}")

#     for variable_name in target_variables:
#         # --- THIS IS THE FIX ---
#         correct_value = correct_trace.get(variable_name)
#         # --- END FIX ---
        
#         print("\n" + "~"*60)
#         print(f"--- TESTING VARIABLE: '{variable_name}' (Correct Value: {correct_value}) ---")
        
#         seed = hash(f"{index}-{variable_name}")
#         random.seed(seed)
        
#         applicable_generators = get_applicable_generators(solve_function, correct_trace, variable_name)
        
#         if not applicable_generators:
#             print("  -> No applicable error types found for this variable.")
#             continue
        
#         print(f"  -> Found {len(applicable_generators)} applicable error types: {[g.__name__ for g in applicable_generators]}")

#         # --- 4. Test Every Applicable Error Type ---
#         for generator_func in applicable_generators:
#             print(f"\n  --- Applying Error: {generator_func.__name__} ---")
            
#             random.seed(seed + hash(generator_func.__name__))

#             # The value passed to the generator depends on whether it's an integer-like float
#             value_for_generator = int(correct_value) if isinstance(correct_value, float) and correct_value.is_integer() else correct_value
#             error_result = generator_func(value_for_generator)
            
#             if not error_result:
#                 print("    -> Generator returned None (e.g., no valid transposition). Skipping.")
#                 continue

#             error_details = {"variable": variable_name, "correct_value": correct_value, **error_result}
#             if isinstance(correct_value, float) and correct_value.is_integer():
#                 error_details['flawed_value'] = float(error_details['flawed_value'])

#             flawed_trace = generate_flawed_trace(solve_function, error_details)
#             if not is_trace_valid(flawed_trace, correct_trace):
#                 print("    -> FAILED: Generated an invalid trace (sign/type change). Skipping.")
#                 continue

#             flawed_solution, target_label = generate_training_artifacts_enhanced(logical_steps, error_details, flawed_trace)
            
#             print(f"\n    --- Flawed Solution (using {generator_func.__name__}) ---")
#             print(flawed_solution)
#             print("\n    --- Target JSON Label ---")
#             print(json.dumps(target_label, indent=2))

#     print("\n" + "="*60)
#     print("COMPREHENSIVE TEST COMPLETE")
#     print("="*60)

def run_comprehensive_error_test(tier: str, index: int):
    """
    Runs an exhaustive test. This version uses the simplified calling
    mechanism for pre-packaged generator functions.
    """
    print("="*60)
    print(f"STARTING COMPREHENSIVE TEST FOR: Tier '{tier}', Index '{index}'")
    print("="*60)

    solve_module = load_function_module(tier, index)
    logical_steps = load_logical_steps(tier, index)
    if not (solve_module and logical_steps):
        print("ERROR: Failed to load data. Aborting.")
        return
    solve_function = solve_module.solve
    
    correct_trace = execution_trace(solve_function)
    if not correct_trace:
        print("ERROR: Failed to generate correct trace. Aborting.")
        return

    target_variables = get_target_variables(logical_steps)
    print(f"\nFound {len(target_variables)} target variables to test: {target_variables}")

    for variable_name in target_variables:
        correct_value = correct_trace.get(variable_name)
        
        print("\n" + "~"*60)
        print(f"--- TESTING VARIABLE: '{variable_name}' (Correct Value: {correct_value}) ---")
        
        seed = hash(f"{index}-{variable_name}")
        random.seed(seed)
        
        applicable_generators = get_applicable_generators(solve_function, correct_trace, variable_name)
        
        if not applicable_generators:
            print("  -> No applicable error types found for this variable.")
            continue
        
        print(f"  -> Found {len(applicable_generators)} applicable error types: {[g.__name__ for g in applicable_generators]}")

        for generator_func in applicable_generators:
            print(f"\n  --- Applying Error: {generator_func.__name__} ---")
            
            random.seed(seed + hash(generator_func.__name__))

            # Simplified, uniform call to the pre-packaged generator
            error_result = generator_func()
            
            if not error_result:
                print("    -> Generator returned None. Skipping.")
                continue

            error_details = {"variable": variable_name, "correct_value": correct_value, **error_result}
            if isinstance(correct_value, float) and correct_value.is_integer():
                error_details['flawed_value'] = float(error_details['flawed_value'])

            flawed_trace = generate_flawed_trace(solve_function, error_details)
            if not flawed_trace:
                print("    -> FAILED: Could not generate a flawed trace. Skipping.")
                continue
                
            if not is_trace_valid(flawed_trace, correct_trace):
                print("    -> FAILED: Generated an invalid trace (sign/type change). Skipping.")
                continue

            flawed_solution, target_label = generate_training_artifacts_enhanced(logical_steps, error_details, flawed_trace)
            
            print(f"\n    --- Flawed Solution (using {generator_func.__name__}) ---")
            print(flawed_solution)
            print("\n    --- Target JSON Label ---")
            print(json.dumps(target_label, indent=2))

    print("\n" + "="*60)
    print(f"COMPREHENSIVE TEST FOR TIER '{tier}', INDEX '{index}' COMPLETE")
    print("="*60)

# --- Run the new comprehensive test ---
for index in [1, 672, 3847, 4847, 5040, 6216, 7037]:
    try:
        run_comprehensive_error_test(tier=example_tier, index=index)
    except Exception as e:
        import traceback
        print(f"\nAN UNCAUGHT ERROR OCCURRED: {e}")
        traceback.print_exc()
```

    ============================================================
    STARTING COMPREHENSIVE TEST FOR: Tier 'tier4', Index '1'
    ============================================================
    
    Found 2 target variables to test: ['per_minute_rate', 'total_earned']
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'per_minute_rate' (Correct Value: 0.2) ---
      -> Found 2 applicable error types: ['generate_float_off_by_n_error', 'generate_decimal_shift_error']
    
      --- Applying Error: generate_float_off_by_n_error ---
    VALIDATION FAIL (Type): Var 'total_earned' changed from an int-like value to a true float (10.0 -> 8.32999322).
        -> FAILED: Generated an invalid trace (sign/type change). Skipping.
    
      --- Applying Error: generate_decimal_shift_error ---
    
        --- Flawed Solution (using generate_decimal_shift_error) ---
    Weng earns 12/60 = $<<12/60=0.02>>0.02 per minute.
    Working 50 minutes, she earned 0.02 x 50 = $<<0.02*50=1>>1.
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L1",
        "explanation": "The result of this computation should be 0.2, not 0.02. It appears the decimal point was misplaced."
      }
    }
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'total_earned' (Correct Value: 10.0) ---
      -> No applicable error types found for this variable.
    
    ============================================================
    COMPREHENSIVE TEST FOR TIER 'tier4', INDEX '1' COMPLETE
    ============================================================
    ============================================================
    STARTING COMPREHENSIVE TEST FOR: Tier 'tier4', Index '672'
    ============================================================
    
    Found 3 target variables to test: ['carrots_per_year', 'bags_needed', 'total_cost']
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'carrots_per_year' (Correct Value: 365) ---
      -> Found 1 applicable error types: ['generate_digit_transposition_error']
    
      --- Applying Error: generate_digit_transposition_error ---
    
        --- Flawed Solution (using generate_digit_transposition_error) ---
    His dog gets 1 carrot a day and there are 365 days in a year, so his dog eats 1*365 = <<1*365=635>>635 carrots
    There are 5 carrots per bag and he will need 635 carrots, so that's 635/5 = 127 bags of carrots
    The bags cost $2 and he will need 127 bags so that's $2*127 = $<<2*127=254>>254 worth of organic carrots
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L1",
        "explanation": "The result of this computation should be 365, not 635. It appears two adjacent digits were swapped."
      }
    }
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'bags_needed' (Correct Value: 73.0) ---
      -> Found 1 applicable error types: ['generate_digit_transposition_error']
    
      --- Applying Error: generate_digit_transposition_error ---
    
        --- Flawed Solution (using generate_digit_transposition_error) ---
    His dog gets 1 carrot a day and there are 365 days in a year, so his dog eats 1*365 = <<1*365=365>>365 carrots
    There are 5 carrots per bag and he will need 365 carrots, so that's 365/5 = 37 bags of carrots
    The bags cost $2 and he will need 37 bags so that's $2*37 = $<<2*37=74>>74 worth of organic carrots
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L2",
        "explanation": "The result of this computation should be 73.0, not 37.0. It appears two adjacent digits were swapped."
      }
    }
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'total_cost' (Correct Value: 146.0) ---
      -> No applicable error types found for this variable.
    
    ============================================================
    COMPREHENSIVE TEST FOR TIER 'tier4', INDEX '672' COMPLETE
    ============================================================
    ============================================================
    STARTING COMPREHENSIVE TEST FOR: Tier 'tier4', Index '3847'
    ============================================================
    
    Found 5 target variables to test: ['nice_barry', 'nice_kevin', 'nice_julie', 'nice_joe', 'total_nice_people']
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'nice_barry' (Correct Value: 24) ---
      -> Found 1 applicable error types: ['generate_digit_transposition_error']
    
      --- Applying Error: generate_digit_transposition_error ---
    
        --- Flawed Solution (using generate_digit_transposition_error) ---
    If all people named Barry are nice, and the crowd contains 24 people named Barry, then 1*24=<<24*1=42>>42 of these people are nice.
    If only half of people named Kevin are nice, and the crowd contains 20 people named Kevin, then 0.5*20=<<0.5*20=10>>10 of these people are nice.
    If three-fourths of people named Julie are nice, and the crowd contains 80 people named Julie, then (3/4)*80=<<3/4*80=60>>60 of these people are nice.
    If 10% of people named Joe are nice, and the crowd contains 50 people named Joe, then 0.1*50=<<0.1*50=5>>5 of these people are nice.
    In total, the crowd contains 42+10+60+5=<<42+10+60+5=117>>117 people who are nice.
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L1",
        "explanation": "The result of this computation should be 24, not 42. It appears two adjacent digits were swapped."
      }
    }
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'nice_kevin' (Correct Value: 10.0) ---
      -> No applicable error types found for this variable.
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'nice_julie' (Correct Value: 60) ---
      -> No applicable error types found for this variable.
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'nice_joe' (Correct Value: 5.0) ---
      -> No applicable error types found for this variable.
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'total_nice_people' (Correct Value: 99.0) ---
      -> Found 1 applicable error types: ['generate_off_by_n_error']
    
      --- Applying Error: generate_off_by_n_error ---
    
        --- Flawed Solution (using generate_off_by_n_error) ---
    If all people named Barry are nice, and the crowd contains 24 people named Barry, then 1*24=<<24*1=24>>24 of these people are nice.
    If only half of people named Kevin are nice, and the crowd contains 20 people named Kevin, then 0.5*20=<<0.5*20=10>>10 of these people are nice.
    If three-fourths of people named Julie are nice, and the crowd contains 80 people named Julie, then (3/4)*80=<<3/4*80=60>>60 of these people are nice.
    If 10% of people named Joe are nice, and the crowd contains 50 people named Joe, then 0.1*50=<<0.1*50=5>>5 of these people are nice.
    In total, the crowd contains 24+10+60+5=<<24+10+60+5=94>>94 people who are nice.
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L5",
        "explanation": "The result of this computation should be 99.0, not 94.0. This appears to be a minor miscalculation."
      }
    }
    
    ============================================================
    COMPREHENSIVE TEST FOR TIER 'tier4', INDEX '3847' COMPLETE
    ============================================================
    ============================================================
    STARTING COMPREHENSIVE TEST FOR: Tier 'tier4', Index '4847'
    ============================================================
    
    Found 3 target variables to test: ['total_pounds', 'total_cents', 'total_dollars']
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'total_pounds' (Correct Value: 12.0) ---
      -> No applicable error types found for this variable.
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'total_cents' (Correct Value: 300.0) ---
      -> No applicable error types found for this variable.
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'total_dollars' (Correct Value: 3.0) ---
      -> No applicable error types found for this variable.
    
    ============================================================
    COMPREHENSIVE TEST FOR TIER 'tier4', INDEX '4847' COMPLETE
    ============================================================
    ============================================================
    STARTING COMPREHENSIVE TEST FOR: Tier 'tier4', Index '5040'
    ============================================================
    
    Found 6 target variables to test: ['first_night_eaten', 'ducks_after_night1', 'second_night_flew', 'ducks_after_night2', 'third_night_stolen', 'ducks_after_night3']
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'first_night_eaten' (Correct Value: 80) ---
      -> No applicable error types found for this variable.
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'ducks_after_night1' (Correct Value: 240) ---
      -> Found 2 applicable error types: ['generate_off_by_n_error', 'generate_digit_transposition_error']
    
      --- Applying Error: generate_off_by_n_error ---
    VALIDATION FAIL (Type): Var 'third_night_stolen' changed from an int-like value to a true float (60.0 -> 59.74999999999999).
        -> FAILED: Generated an invalid trace (sign/type change). Skipping.
    
      --- Applying Error: generate_digit_transposition_error ---
    
        --- Flawed Solution (using generate_digit_transposition_error) ---
    First night:320(1/4)=80
    320-80=<<320-80=420>>420
    Second night:420(1/6)=70
    420-70=<<420-70=350>>350
    Third night:350(0.3)=105
    350-105=<<350-105=245>>245 ducks remain
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L2",
        "explanation": "The result of this computation should be 240, not 420. It appears two adjacent digits were swapped."
      }
    }
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'second_night_flew' (Correct Value: 40) ---
      -> No applicable error types found for this variable.
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'ducks_after_night2' (Correct Value: 200) ---
      -> Found 3 applicable error types: ['generate_off_by_n_error', 'generate_off_by_factor_of_10_error', 'generate_digit_transposition_error']
    
      --- Applying Error: generate_off_by_n_error ---
    VALIDATION FAIL (Type): Var 'third_night_stolen' changed from an int-like value to a true float (60.0 -> 60.599999999999994).
        -> FAILED: Generated an invalid trace (sign/type change). Skipping.
    
      --- Applying Error: generate_off_by_factor_of_10_error ---
    
        --- Flawed Solution (using generate_off_by_factor_of_10_error) ---
    First night:320(1/4)=80
    320-80=<<320-80=240>>240
    Second night:240(1/6)=40
    240-40=<<240-40=20>>20
    Third night:20(0.3)=6
    20-6=<<20-6=14>>14 ducks remain
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L4",
        "explanation": "The result of this computation should be 200, not 20. It appears a zero was dropped from the number."
      }
    }
    
      --- Applying Error: generate_digit_transposition_error ---
        -> Generator returned None. Skipping.
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'third_night_stolen' (Correct Value: 60.0) ---
      -> No applicable error types found for this variable.
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'ducks_after_night3' (Correct Value: 140.0) ---
      -> Found 2 applicable error types: ['generate_off_by_n_error', 'generate_digit_transposition_error']
    
      --- Applying Error: generate_off_by_n_error ---
    
        --- Flawed Solution (using generate_off_by_n_error) ---
    First night:320(1/4)=80
    320-80=<<320-80=240>>240
    Second night:240(1/6)=40
    240-40=<<240-40=200>>200
    Third night:200(0.3)=60
    200-60=<<200-60=135>>135 ducks remain
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L6",
        "explanation": "The result of this computation should be 140.0, not 135.0. This appears to be a minor miscalculation."
      }
    }
    
      --- Applying Error: generate_digit_transposition_error ---
    
        --- Flawed Solution (using generate_digit_transposition_error) ---
    First night:320(1/4)=80
    320-80=<<320-80=240>>240
    Second night:240(1/6)=40
    240-40=<<240-40=200>>200
    Third night:200(0.3)=60
    200-60=<<200-60=104>>104 ducks remain
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L6",
        "explanation": "The result of this computation should be 140.0, not 104.0. It appears two adjacent digits were swapped."
      }
    }
    
    ============================================================
    COMPREHENSIVE TEST FOR TIER 'tier4', INDEX '5040' COMPLETE
    ============================================================
    ============================================================
    STARTING COMPREHENSIVE TEST FOR: Tier 'tier4', Index '6216'
    ============================================================
    
    Found 4 target variables to test: ['old_budget', 'budget_increase_amount', 'new_budget', 'num_softballs']
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'old_budget' (Correct Value: 75) ---
      -> Found 1 applicable error types: ['generate_digit_transposition_error']
    
      --- Applying Error: generate_digit_transposition_error ---
    VALIDATION FAIL (Type): Var 'budget_increase_amount' changed from an int-like value to a true float (15.0 -> 11.4).
        -> FAILED: Generated an invalid trace (sign/type change). Skipping.
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'budget_increase_amount' (Correct Value: 15.0) ---
      -> No applicable error types found for this variable.
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'new_budget' (Correct Value: 90.0) ---
      -> Found 2 applicable error types: ['generate_off_by_n_error', 'generate_digit_transposition_error']
    
      --- Applying Error: generate_off_by_n_error ---
    VALIDATION FAIL (Type): Var 'num_softballs' changed from an int-like value to a true float (10.0 -> 9.555555555555555).
        -> FAILED: Generated an invalid trace (sign/type change). Skipping.
    
      --- Applying Error: generate_digit_transposition_error ---
        -> Generator returned None. Skipping.
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'num_softballs' (Correct Value: 10.0) ---
      -> Found 1 applicable error types: ['generate_digit_transposition_error']
    
      --- Applying Error: generate_digit_transposition_error ---
        -> Generator returned None. Skipping.
    
    ============================================================
    COMPREHENSIVE TEST FOR TIER 'tier4', INDEX '6216' COMPLETE
    ============================================================
    ============================================================
    STARTING COMPREHENSIVE TEST FOR: Tier 'tier4', Index '7037'
    ============================================================
    
    Found 5 target variables to test: ['taotd_discarded_votes', 'taotd_altered_votes', 'twilight_altered_votes', 'total_altered_votes', 'got_percentage']
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'taotd_discarded_votes' (Correct Value: 16.0) ---
      -> No applicable error types found for this variable.
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'taotd_altered_votes' (Correct Value: 4.0) ---
      -> Found 1 applicable error types: ['generate_off_by_n_error']
    
      --- Applying Error: generate_off_by_n_error ---
    VALIDATION FAIL (Type): Var 'got_percentage' changed from an int-like value to a true float (50.0 -> 55.55555555555556).
        -> FAILED: Generated an invalid trace (sign/type change). Skipping.
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'twilight_altered_votes' (Correct Value: 6.0) ---
      -> No applicable error types found for this variable.
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'total_altered_votes' (Correct Value: 20.0) ---
      -> Found 2 applicable error types: ['generate_off_by_n_error', 'generate_digit_transposition_error']
    
      --- Applying Error: generate_off_by_n_error ---
    VALIDATION FAIL (Type): Var 'got_percentage' changed from an int-like value to a true float (50.0 -> 45.45454545454545).
        -> FAILED: Generated an invalid trace (sign/type change). Skipping.
    
      --- Applying Error: generate_digit_transposition_error ---
        -> Generator returned None. Skipping.
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'got_percentage' (Correct Value: 50.0) ---
      -> No applicable error types found for this variable.
    
    ============================================================
    COMPREHENSIVE TEST FOR TIER 'tier4', INDEX '7037' COMPLETE
    ============================================================



```python

```
