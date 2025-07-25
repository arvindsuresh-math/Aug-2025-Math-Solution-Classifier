### Cell 1: Initial setup


```python
# --- Python Standard Library Imports ---
import json
import re
import ast
import inspect
import importlib.util
from pathlib import Path
from types import ModuleType
from typing import Callable, Any, Dict, List
from fractions import Fraction
import datetime
import functools
import random
import copy

# --- Third-Party Imports ---
import pandas as pd
from tqdm.notebook import tqdm
from datasets import load_dataset, Dataset

# --- MODIFIED: Path and Directory Definitions ---
def find_project_root(marker: str = ".git") -> Path:
    current_path = Path.cwd().resolve()
    while current_path != current_path.parent:
        if (current_path / marker).exists():
            return current_path
        current_path = current_path.parent
    raise FileNotFoundError(f"Could not find project root. Marker '{marker}' not found.")

PROJECT_ROOT = find_project_root()
DATA_DIR = PROJECT_ROOT / 'data'

PROCESSED_MANIFEST_DIR = DATA_DIR / "tier-manifests-gen-processed"
GENERATED_ERRORS_DIR = DATA_DIR / "computational-errors-generated"

# --- NEW: Define the list of models we will process ---
MODELS = ['openai_gpt-4.1', 'google_gemini-2.5-flash']

print(f"Project root: {PROJECT_ROOT}")
print(f"Input (Split Manifests): {PROCESSED_MANIFEST_DIR}")
print(f"Output (Generated Errors): {GENERATED_ERRORS_DIR}")

# --- Ensure Output Directory Exists ---
PROCESSED_MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
GENERATED_ERRORS_DIR.mkdir(parents=True, exist_ok=True)
```

    Project root: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math
    Input (Split Manifests): /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/tier-manifests-gen-processed
    Output (Generated Errors): /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/computational-errors-generated


### Cell 2: Load dataset and define tiers


```python
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
    # (Function content is unchanged)
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
print("Tier definitions loaded and samples categorized.")
for tier, indices in TIER_LISTS.items():
    print(f"{tier:<10}: {len(indices)} samples")
```

    Tier definitions loaded and samples categorized.
    tier1     : 2767 samples
    tier2     : 837 samples
    tier3     : 3113 samples
    tier4     : 544 samples
    tier5     : 212 samples


### Cell 3: Manifest loading and processing utilities


```python
def load_function_module(
    tier: str,
    index: int,
    model_name: str, 
    base_dir: Path = PROCESSED_MANIFEST_DIR # 
) -> ModuleType | None:
    """
    Dynamically loads the '{model_name}.py' file for a given tier, index, and model.
    """
    py_file_path = base_dir / tier / str(index) / f"{model_name}.py"
    if not py_file_path.exists():
        return None

    # Make module name unique to avoid import caching issues
    module_name = f"manifests.t{tier}.i{index}.m_{model_name.replace('.', '_')}.solve"
    spec = importlib.util.spec_from_file_location(module_name, py_file_path)
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    return None

def load_logical_steps(
    tier: str,
    index: int,
    model_name: str, 
    base_dir: Path = PROCESSED_MANIFEST_DIR
) -> list[dict] | None:
    """
    Loads the '{model_name}.json' file for a given tier, index, and model.
    """
    json_file_path = base_dir / tier / str(index) / f"{model_name}.json"
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def build_solution_mapping(index: int, dataset: Dataset = GSM8K_TRAIN):
    """
    (Function is unchanged)
    Extracts the original NL solution for comparison. Not strictly needed for the
    pipeline but useful for debugging.
    """
    solution_mapping = {}
    solution_text = dataset[index]["answer"]
    lines = [ln.strip() for ln in solution_text.splitlines() if ln.strip()]
    if lines and re.match(r"^####\s*[\d\.,]+$", lines[-1]):
        lines.pop(-1)
    for i, line in enumerate(lines, 1):
        solution_mapping[f"L{i}"] = line
    return solution_mapping


print("Manifest loading functions updated to read from the split-file directory.")
```

    Manifest loading functions updated to read from the split-file directory.


### Cell 4: General and core utilities


```python
# In Cell 4 of BOTH notebooks, add this class at the top.

from fractions import Fraction as BuiltinFraction

class NonSimplifyingFraction(BuiltinFraction):
    """
    A subclass of fractions.Fraction that does NOT simplify when converted
    to a string. This preserves the original representation from the manifest.
    
    For example, str(NonSimplifyingFraction(80, 100)) will be "80/100", 
    not "4/5".
    """
    def __new__(cls, numerator=0, denominator=None):
        # We must use __new__ because Fraction is immutable
        self = super(NonSimplifyingFraction, cls).__new__(cls, numerator, denominator)
        # Store the original denominator for the __str__ method.
        # The built-in .denominator will be simplified.
        if denominator is not None:
            self._original_denominator = denominator
            self._original_numerator = numerator if isinstance(numerator, int) else numerator.numerator
        else: # Handle cases like Fraction(0.5)
            self._original_numerator, self._original_denominator = self.as_integer_ratio()
        
        return self

    def __str__(self):
        return f"{self._original_numerator}/{self._original_denominator}"


# --- General Numeric and String Helpers ---
def normalize_value(value):
    if isinstance(value, float) and value.is_integer(): return int(value)
    return value


def get_sign(n) -> int:
    if n > 0: return 1
    if n < 0: return -1
    return 0


def has_distinct_adjacent_digits(n: int) -> bool:
    s = str(abs(n))
    return len(s) >= 2 and any(s[i] != s[i+1] for i in range(len(s) - 1))



def execution_trace(func: Callable[[], Any]) -> dict[str, Any] | None:
    """
    --- MODIFIED ---
    Now uses the NonSimplifyingFraction class in its execution environment
    to prevent auto-simplification of fractions in the variable trace.
    """
    try:
        src = inspect.getsource(func)
        tree = ast.parse(src)
        func_def = tree.body[0]
        # This is the key change: 'Fraction' now points to our custom class.
        global_namespace = {'Fraction': NonSimplifyingFraction}
        local_env = {}
        for stmt in func_def.body:
            if isinstance(stmt, ast.Assign):
                module_node = ast.Module([stmt], type_ignores=[])
                code_obj = compile(module_node, '<string>', 'exec')
                exec(code_obj, global_namespace, local_env)
        return local_env
    except Exception:
        return None


def generate_flawed_trace(func: Callable, error_details: dict[str, Any]) -> dict[str, Any] | None:
    """
    --- MODIFIED ---
    Also uses the NonSimplifyingFraction class to ensure consistency.
    """
    # ... (the first part of the function that modifies the AST is unchanged) ...
    try:
        src = inspect.getsource(func)
        tree = ast.parse(src)
        func_def = tree.body[0]
        variable_to_change = error_details["variable"]
        flawed_value = error_details["flawed_value"]
        modified_body = copy.deepcopy(func_def.body)
        node_found_and_modified = False
        for node in modified_body:
            if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == variable_to_change for t in node.targets):
                if isinstance(flawed_value, BuiltinFraction): # Check against the base class
                    # When creating a new node, we use the custom class name
                    new_value_node = ast.Call(
                        func=ast.Name(id='Fraction', ctx=ast.Load()),
                        args=[ast.Constant(value=flawed_value.numerator), ast.Constant(value=flawed_value.denominator)],
                        keywords=[]
                    )
                else: new_value_node = ast.Constant(value=flawed_value)
                ast.copy_location(new_value_node, node.value)
                ast.fix_missing_locations(new_value_node)
                node.value = new_value_node
                node_found_and_modified = True
                break
        if not node_found_and_modified: return None

        # This is the key change, same as in execution_trace.
        global_namespace = {'Fraction': NonSimplifyingFraction}
        env = {}
        for stmt in modified_body:
            if isinstance(stmt, ast.Assign):
                code_obj = compile(ast.Module([stmt], type_ignores=[]), '<string>', 'exec')
                exec(code_obj, global_namespace, env)
        return env
    except Exception: return None


def reconstruct_solution_lines_enhanced(logical_steps: list[dict], eval_trace: dict[str, Any]) -> dict[str, str]:
    # (Function content is unchanged from old Cell 4)
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
            if isinstance(value, Fraction):
                if value.denominator == 1: return str(value.numerator)
                return f"{value.numerator}/{value.denominator}"
            return str(normalize_value(value))
        reconstructed_mapping[line_number] = placeholder_pattern.sub(replacer, template)
    return reconstructed_mapping


def is_trace_valid(
    flawed_trace: dict[str, Any],
    correct_trace: dict[str, Any]
    ):
    """
    Validates a flawed trace to ensure it adheres to project constraints.

    Checks for two conditions:
    1. Type Integrity: An integer-like value must remain integer-like.
       (e.g., 15 students cannot become 15.5 students).
    2. Sign Integrity: A value cannot change its sign
       (e.g., a cost of $20 cannot become -$20).
    """
    for var_name, correct_val in correct_trace.items():
        if var_name not in flawed_trace:
            continue

        flawed_val = flawed_trace.get(var_name)
        
        # Rule 1: Type Integrity Check
        is_correct_int_like = isinstance(normalize_value(correct_val), int)
        is_flawed_int_like = isinstance(normalize_value(flawed_val), int)

        if is_correct_int_like and not is_flawed_int_like:
            return False

        # Rule 2: Sign Integrity Check
        processed_correct = normalize_value(correct_val)
        processed_flawed = normalize_value(flawed_val)
        
        if isinstance(processed_correct, (int, float)) and processed_correct != 0:
            if get_sign(processed_correct) != get_sign(processed_flawed):
                return False
                
    return True


```

### Cell 5: Individual error generators


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


def generate_reciprocal_error(correct_value: NonSimplifyingFraction) -> dict[str, Any] | None:
    """Swaps the numerator and denominator of a fraction."""
    if correct_value.denominator == 0: return None
    
    # --- MODIFIED: Return our custom class to preserve the representation ---
    flawed_value = NonSimplifyingFraction(correct_value.denominator, correct_value.numerator)
    return {
        "flawed_value": flawed_value,
        "explanation_type": "It appears the numerator and denominator were swapped."
    }

def generate_off_by_one_in_fraction_part_error(correct_value: NonSimplifyingFraction) -> dict[str, Any]:
    """Adds or subtracts 1 from either the numerator or the denominator."""
    part_to_change = random.choice(["numerator", "denominator"])
    offset = random.choice([-1, 1])

    if part_to_change == "numerator":
        new_num = correct_value.numerator + offset
        new_den = correct_value.denominator
    else:
        new_num = correct_value.numerator
        new_den = correct_value.denominator + offset
        if new_den == 0:
            new_den = correct_value.denominator + (offset * 2)

    # --- MODIFIED: Return our custom class ---
    return {
        "flawed_value": NonSimplifyingFraction(new_num, new_den),
        "explanation_type": "It appears there was an off-by-one error in the fraction."
    }

def generate_multiplication_by_reciprocal_error(
    numeric_val: Any, 
    fraction_val: NonSimplifyingFraction
) -> dict[str, Any] | None:
    """Simulates an error where a value is multiplied by the reciprocal."""
    if fraction_val.numerator == 0:
        return None

    # This creates a standard, simplifying fraction for the calculation.
    reciprocal_fraction = BuiltinFraction(fraction_val.denominator, fraction_val.numerator)
    flawed_value_result = numeric_val * reciprocal_fraction
    
    # --- MODIFIED: The final return value must be a NonSimplifyingFraction ---
    # We must construct it from the un-simplified components to preserve the logic.
    new_numerator = numeric_val * fraction_val.denominator
    new_denominator = fraction_val.numerator
    
    return {
        # The value is correct, but the representation now preserves the logic.
        "flawed_value": NonSimplifyingFraction(new_numerator, new_denominator),
        "explanation_type": "It appears the value was multiplied by the reciprocal of the intended fraction."
    }

```

### Cell 6: AST and Logical Step Helpers


```python
import functools
import random
from typing import Callable, Any

def get_target_variables(logical_steps: list[dict]) -> list[str]:
    """Extracts all 'output_variable' names from the logical steps."""
    return [step['output_variable'] for step in logical_steps if 'output_variable' in step]


def get_operator_for_variable(func: Callable, variable_name: str) -> str | None:
    """Inspects the AST to find the operator used to compute a variable."""
    try:
        src = inspect.getsource(func)
        tree = ast.parse(src)
    except (TypeError, FileNotFoundError, SyntaxError):
        return None
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == variable_name for t in node.targets):
            if isinstance(node.value, ast.BinOp):
                op = node.value.op
                if isinstance(op, ast.Add): return "add"
                if isinstance(op, ast.Sub): return "sub"
                if isinstance(op, ast.Mult): return "mult"
                if isinstance(op, ast.Div): return "div"
            return "other"
    return None


def get_operand_names_for_variable(func: Callable, variable_name: str) -> list[str]:
    """Finds the names of variables used as operands for a target variable."""
    operand_names = []
    try:
        src = inspect.getsource(func)
        tree = ast.parse(src)
    except (TypeError, FileNotFoundError, SyntaxError):
        return []

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == variable_name for t in node.targets):
            for sub_node in ast.walk(node.value):
                if isinstance(sub_node, ast.Name):
                    operand_names.append(sub_node.id)
            return list(set(operand_names))
    return []

```

### Cell 7: Error applicability logic


```python

def _get_applicable_integer_errors(
    correct_value: int,
    operator: str,
    operand_values: list
    ):
    """
    Returns a list of applicable error generator functions for an integer.
    Refined to separate logic for addition/subtraction vs. other operations.
    """
    applicable_generators = []
    
    # Rule 1: Off-by-n and stem errors are only for addition/subtraction.
    if operator in ["add", "sub"]:
        all_end_in_zero = all(isinstance(v, int) and v % 10 == 0 for v in operand_values) if operand_values else False
        if all_end_in_zero and correct_value % 10 == 0 and correct_value != 0:
            applicable_generators.append(generate_stem_off_by_n_error)
        else:
            applicable_generators.append(generate_off_by_n_error)

    # Rule 2: Factor-of-10 error applies to any operation resulting in a multiple of 100.
    if correct_value % 100 == 0 and correct_value != 0:
        applicable_generators.append(generate_off_by_factor_of_10_error)
    
    # Rule 3: Digit transposition applies to any operation resulting in a suitable integer.
    if has_distinct_adjacent_digits(correct_value):
        applicable_generators.append(generate_digit_transposition_error)
        
    return applicable_generators


def get_applicable_generators(
    func: Callable,
    correct_trace: dict[str, Any],
    variable_name: str
    ):
    """
    Identifies and partially instantiates all applicable error generators for a variable.
    This version correctly handles integer multiplication.
    """
    applicable_generators = []
    correct_value = correct_trace.get(variable_name)
    if not isinstance(correct_value, (int, float, Fraction)):
        return []

    def add_generator(gen_func, value_to_pass):
        """Creates a callable partial function with the correct value and name."""
        partial_gen = functools.partial(gen_func, value_to_pass)
        partial_gen.__name__ = gen_func.__name__
        applicable_generators.append(partial_gen)

    # --- Part 1: Type-Based Error Selection ---
    if isinstance(correct_value, int) or (isinstance(correct_value, float) and correct_value.is_integer()) or (isinstance(correct_value, Fraction) and correct_value.denominator == 1):
        int_val = int(correct_value)
        operator = get_operator_for_variable(func, variable_name)
        op_names = get_operand_names_for_variable(func, variable_name)
        op_vals = [correct_trace.get(name) for name in op_names if name in correct_trace]
        
        # This now correctly applies integer errors (including transposition) to multiplication results.
        integer_gens = _get_applicable_integer_errors(int_val, operator, op_vals)
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

    # --- Part 2: Context-Based Error Selection (Multiplication by Reciprocal) ---
    operator = get_operator_for_variable(func, variable_name)
    if operator == "mult":
        operand_names = get_operand_names_for_variable(func, variable_name)
        operand_values = [correct_trace.get(name) for name in operand_names if name in correct_trace]
        
        if len(operand_values) == 2:
            num_op = next((op for op in operand_values if isinstance(op, (int, float))), None)
            frac_op = next((op for op in operand_values if isinstance(op, Fraction)), None)

            if num_op is not None and frac_op is not None and frac_op.denominator != 1:
                # This error is specific and does not use the standard `add_generator`
                reciprocal_mult_gen = functools.partial(
                    generate_multiplication_by_reciprocal_error,
                    numeric_val=num_op,
                    fraction_val=frac_op
                )
                reciprocal_mult_gen.__name__ = 'generate_multiplication_by_reciprocal_error'
                applicable_generators.append(reciprocal_mult_gen)

    # Return unique generators, as some rules might overlap
    return list(dict.fromkeys(applicable_generators))


```

### Cell 8: Orchestrator and artifact generation


```python
def find_error_line_number(variable_name: str, logical_steps: list[dict]) -> str | None:
    """Finds the line number corresponding to a given output variable."""
    for step in logical_steps:
        if step.get("output_variable") == variable_name:
            return step.get("line_number")
    return None


def generate_training_artifacts(
    logical_steps: list[dict],
    error_details: dict[str, Any],
    flawed_trace: dict[str, Any]
) -> tuple[str, dict] | None:
    """Generates the final training data: a flawed NL solution and a JSON label."""
    flawed_solution_map = reconstruct_solution_lines_enhanced(logical_steps, flawed_trace)
    if not flawed_solution_map:
        return None
    
    sorted_lines = sorted(flawed_solution_map.items(), key=lambda item: int(item[0][1:]))
    flawed_nl_solution = "\n".join([line for _, line in sorted_lines])

    erroneous_line = find_error_line_number(error_details["variable"], logical_steps)
    if not erroneous_line:
        return None

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


# def generate_all_valid_errors(
#     func: Callable,
#     logical_steps: list[dict],
#     correct_trace: dict[str, Any]
# ) -> list[dict]:
#     """
#     Deterministically generates and validates all possible computational errors for a problem.

#     This function iterates through every target variable and every applicable error type,
#     producing a comprehensive list of valid flawed examples without retries.

#     Returns:
#         A list of dictionaries, where each dictionary represents a single valid
#         flawed example and has the structure:
#         {
#             "variable": str,
#             "error_type": str,
#             "flawed_nl_solution": str,
#             "target_json": dict
#         }
#     """
#     all_generated_examples = []
#     target_variables = get_target_variables(logical_steps)

#     for variable_name in target_variables:
#         correct_value = correct_trace.get(variable_name)
        
#         # Use a consistent seed for each variable to ensure deterministic error generation
#         seed = hash(f"{variable_name}")
        
#         applicable_generators = get_applicable_generators(func, correct_trace, variable_name)

#         for generator_func in applicable_generators:
#             # Seed based on variable and generator for reproducibility
#             random.seed(seed + hash(generator_func.__name__))

#             error_result = generator_func()
#             if not error_result:
#                 continue

#             error_details = {"variable": variable_name, "correct_value": correct_value, **error_result}
            
#             # Ensure integer-like floats remain floats after error injection
#             if isinstance(correct_value, float) and correct_value.is_integer():
#                 error_details['flawed_value'] = float(error_details['flawed_value'])

#             flawed_trace = generate_flawed_trace(func, error_details)
#             if not flawed_trace or not is_trace_valid(flawed_trace, correct_trace):
#                 continue
            
#             artifacts = generate_training_artifacts(logical_steps, error_details, flawed_trace)
#             if artifacts:
#                 flawed_nl_solution, target_json = artifacts
#                 all_generated_examples.append({
#                     "variable": variable_name,
#                     "error_type": generator_func.__name__,
#                     "flawed_nl_solution": flawed_nl_solution,
#                     "target_json": target_json
#                 })

#     return all_generated_examples

# In Cell 8

def generate_all_valid_errors(
    func: Callable,
    logical_steps: list[dict],
    correct_trace: dict[str, Any]
) -> list[dict]:
    """
    Deterministically generates and validates all possible computational errors.
    --- MODIFIED ---
    Now includes correct/flawed values and the specific seed in its output
    for enhanced metadata logging.
    """
    all_generated_examples = []
    target_variables = get_target_variables(logical_steps)

    for variable_name in target_variables:
        correct_value = correct_trace.get(variable_name)
        base_seed = hash(f"{variable_name}")
        
        applicable_generators = get_applicable_generators(func, correct_trace, variable_name)

        for generator_func in applicable_generators:
            # --- MODIFIED: Create a reproducible seed specific to this generator ---
            repro_seed = base_seed + hash(generator_func.__name__)
            random.seed(repro_seed)

            error_result = generator_func()
            if not error_result:
                continue

            error_details = {"variable": variable_name, "correct_value": correct_value, **error_result}
            
            if isinstance(correct_value, float) and correct_value.is_integer():
                error_details['flawed_value'] = float(error_details['flawed_value'])

            flawed_trace = generate_flawed_trace(func, error_details)
            if not flawed_trace or not is_trace_valid(flawed_trace, correct_trace):
                continue
            
            artifacts = generate_training_artifacts(logical_steps, error_details, flawed_trace)
            if artifacts:
                flawed_nl_solution, target_json = artifacts
                
                # --- MODIFIED: Append a richer dictionary ---
                all_generated_examples.append({
                    "variable": variable_name,
                    "error_type": generator_func.__name__,
                    "flawed_nl_solution": flawed_nl_solution,
                    "target_json": target_json,
                    "correct_value": error_details['correct_value'],
                    "flawed_value": error_details['flawed_value'],
                    "repro_seed": repro_seed  # <-- Add the seed
                })

    return all_generated_examples
```

### Cell 9: Serialization Logic


```python
# def save_error_artifacts(
#     tier: str,
#     index: int,
#     model_name: str,
#     valid_errors: list[dict],
#     base_output_dir: Path = GENERATED_ERRORS_DIR
# ) -> list[dict]:
#     """
#     Saves all valid error artifacts to disk in a structured format and
#     returns a list of metadata records for the catalog, now including a timestamp.
#     """
#     output_dir = base_output_dir / tier / str(index)
#     output_dir.mkdir(parents=True, exist_ok=True)
    
#     metadata_records = []

#     for error_example in valid_errors:
#         variable = error_example['variable']
#         error_type = error_example['error_type']
        
#         filename = f"{model_name}_{variable}_{error_type}.json"
#         filepath = output_dir / filename
        
#         artifact_content = {
#             "flawed_nl_solution": error_example["flawed_nl_solution"],
#             "target_json": error_example["target_json"]
#         }
        
#         with open(filepath, 'w', encoding='utf-8') as f:
#             json.dump(artifact_content, f, indent=2)

#         # Create a record for the metadata catalog
#         record = {
#             "index": index,
#             "tier": tier,
#             "model": model_name,
#             "target_variable": variable,
#             "error_type": error_type,
#             "filepath": str(filepath.relative_to(PROJECT_ROOT)),
#             # --- ADDED: Generate a timezone-aware ISO format timestamp ---
#             "utc_timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
#         }
#         metadata_records.append(record)
        
#     return metadata_records


# In Cell 9

def save_error_artifacts(
    tier: str,
    index: int,
    model_name: str,
    valid_errors: list[dict],
    base_output_dir: Path = GENERATED_ERRORS_DIR
) -> list[dict]:
    """
    Saves all valid error artifacts to disk and returns metadata records.
    --- MODIFIED ---
    - Extracts correct/flawed values and the seed.
    - Formats the timestamp into separate date and time columns.
    """
    output_dir = base_output_dir / tier / str(index)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    metadata_records = []
    now_utc = datetime.datetime.now(datetime.timezone.utc)

    for error_example in valid_errors:
        variable = error_example['variable']
        error_type = error_example['error_type']
        
        filename = f"{model_name}_{variable}_{error_type}.json"
        filepath = output_dir / filename
        
        artifact_content = {
            "flawed_nl_solution": error_example["flawed_nl_solution"],
            "target_json": error_example["target_json"]
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(artifact_content, f, indent=2)

        # --- MODIFIED: Create the enhanced metadata record ---
        record = {
            "index": index,
            "tier": tier,
            "model": model_name,
            "target_variable": variable,
            "error_type": error_type,
            "correct_value": normalize_value(error_example['correct_value']),
            "flawed_value": normalize_value(error_example['flawed_value']),
            "repro_seed": error_example['repro_seed'],
            "date_utc": now_utc.strftime('%Y-%m-%d'),
            "time_utc": now_utc.strftime('%H:%M:%S'),
            "filepath": str(filepath.relative_to(PROJECT_ROOT))
        }
        metadata_records.append(record)
        
    return metadata_records
```

### Cell 10: Main function for error injection pipeline execution


```python

# def generate_errors_for_all_manifests(
#     manifest_dir: Path,
#     output_dir: Path,
#     models: list[str]
# ):
#     """
#     Main driver function to orchestrate error generation for all processed manifests.
#     """
#     print("\n--- Starting Error Generation for All Processed Manifests ---")
#     all_metadata = []
    
#     tier_dirs = sorted([d for d in manifest_dir.iterdir() if d.is_dir() and d.name.startswith('tier')])

#     for tier_dir in tqdm(tier_dirs, desc="Tiers"):
#         index_dirs = sorted([d for d in tier_dir.iterdir() if d.is_dir()], key=lambda p: int(p.name))
        
#         for index_dir in tqdm(index_dirs, desc=f"Processing {tier_dir.name}", leave=False):
#             index = int(index_dir.name)
            
#             for model_name in models:
#                 # Load components using the modified loading functions
#                 solve_module = load_function_module(tier_dir.name, index, model_name)
#                 logical_steps = load_logical_steps(tier_dir.name, index, model_name)

#                 if not (solve_module and logical_steps):
#                     continue
                
#                 # Generate correct trace (from Cell 4)
#                 solve_function = solve_module.solve
#                 correct_trace = execution_trace(solve_function)
#                 if not correct_trace:
#                     continue
                
#                 # Generate all valid errors using the orchestrator (from Cell 8)
#                 valid_errors = generate_all_valid_errors(solve_function, logical_steps, correct_trace)
                
#                 # Save artifacts and collect metadata (from Cell 9)
#                 if valid_errors:
#                     records = save_error_artifacts(
#                         tier=tier_dir.name,
#                         index=index,
#                         model_name=model_name,
#                         valid_errors=valid_errors
#                     )
#                     all_metadata.extend(records)

#     # Create and Save the Final Metadata Catalog
#     if all_metadata:
#         catalog_df = pd.DataFrame(all_metadata)
#         catalog_path = output_dir / "computational_error_catalog.csv"
#         catalog_df.to_csv(catalog_path, index=False)
#         print(f"\nSuccessfully generated {len(catalog_df)} error examples.")
#         print(f"Metadata catalog saved to: {catalog_path}")
#     else:
#         print("\nNo error examples were generated.")
        
#     print("\n--- Error Generation Pipeline Complete ---")


# In Cell 10, replace the main driver function.

def generate_errors_for_all_manifests(
    manifest_dir: Path,
    output_dir: Path,
    models: list[str]
):
    """
    Main driver function.
    --- MODIFIED ---
    Now logs a record for every manifest, including those where execution_trace fails,
    and adds a 'correct_trace_generated' column to the final catalog.
    """
    print("\n--- Starting Error Generation for All Processed Manifests ---")
    all_metadata = []
    
    tier_dirs = sorted([d for d in manifest_dir.iterdir() if d.is_dir() and d.name.startswith('tier')])

    for tier_dir in tqdm(tier_dirs, desc="Tiers"):
        index_dirs = sorted([d for d in tier_dir.iterdir() if d.is_dir() and d.name.isdigit()], key=lambda p: int(p.name))
        
        for index_dir in tqdm(index_dirs, desc=f"Processing {tier_dir.name}", leave=False):
            index = int(index_dir.name)
            
            for model_name in models:
                solve_module = load_function_module(tier_dir.name, index, model_name)
                logical_steps = load_logical_steps(tier_dir.name, index, model_name)

                if not (solve_module and logical_steps):
                    continue
                
                # --- MODIFIED LOGIC BLOCK ---
                solve_function = solve_module.solve
                correct_trace = execution_trace(solve_function)
                
                # If the trace fails, log a failure record and move on.
                if not correct_trace:
                    failure_record = {
                        "index": index, "tier": tier_dir.name, "model": model_name,
                        "correct_trace_generated": False,
                        # Add null values for other columns for a consistent schema
                        "target_variable": None, "error_type": None,
                        "correct_value": None, "flawed_value": None,
                        "repro_seed": None, "date_utc": None, "time_utc": None,
                        "filepath": None
                    }
                    all_metadata.append(failure_record)
                    continue # Move to the next manifest

                # If the trace succeeds, proceed with error generation.
                valid_errors = generate_all_valid_errors(solve_function, logical_steps, correct_trace)
                
                if valid_errors:
                    # `save_error_artifacts` returns records for successfully generated errors.
                    records = save_error_artifacts(
                        tier=tier_dir.name,
                        index=index,
                        model_name=model_name,
                        valid_errors=valid_errors
                    )
                    # Add the success flag to each of these records.
                    for record in records:
                        record['correct_trace_generated'] = True
                    all_metadata.extend(records)
                else:
                    # If trace succeeded but no valid errors could be made (e.g., all failed validation)
                    # we still log a record to show it was processed.
                    no_valid_error_record = {
                        "index": index, "tier": tier_dir.name, "model": model_name,
                        "correct_trace_generated": True,
                        "target_variable": "N/A", "error_type": "NoValidErrorsFound",
                        "correct_value": None, "flawed_value": None,
                        "repro_seed": None, "date_utc": None, "time_utc": None,
                        "filepath": None
                    }
                    all_metadata.append(no_valid_error_record)

    # --- The rest of the function is unchanged ---
    if all_metadata:
        catalog_df = pd.DataFrame(all_metadata)
        catalog_path = output_dir / "computational_error_catalog.csv"
        catalog_df.to_csv(catalog_path, index=False)
        print(f"\nCatalog with {len(catalog_df)} records saved to: {catalog_path}")
    else:
        print("\nNo manifests were found to process.")
        
    print("\n--- Error Generation Pipeline Complete ---")
```

### Executing the whole pipeline


```python
# --- Execute the Pipeline ---
generate_errors_for_all_manifests(
    manifest_dir=PROCESSED_MANIFEST_DIR,
    output_dir=GENERATED_ERRORS_DIR,
    models=MODELS
)
```

    
    --- Starting Error Generation for All Processed Manifests ---



    Tiers:   0%|          | 0/4 [00:00<?, ?it/s]



    Processing tier1:   0%|          | 0/1138 [00:00<?, ?it/s]



    Processing tier2:   0%|          | 0/332 [00:00<?, ?it/s]



    Processing tier3:   0%|          | 0/1262 [00:00<?, ?it/s]



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[35], line 2
          1 # --- Execute the Pipeline ---
    ----> 2 generate_errors_for_all_manifests(
          3     manifest_dir=PROCESSED_MANIFEST_DIR,
          4     output_dir=GENERATED_ERRORS_DIR,
          5     models=MODELS
          6 )


    Cell In[34], line 110, in generate_errors_for_all_manifests(manifest_dir, output_dir, models)
        107     continue # Move to the next manifest
        109 # If the trace succeeds, proceed with error generation.
    --> 110 valid_errors = generate_all_valid_errors(solve_function, logical_steps, correct_trace)
        112 if valid_errors:
        113     # `save_error_artifacts` returns records for successfully generated errors.
        114     records = save_error_artifacts(
        115         tier=tier_dir.name,
        116         index=index,
        117         model_name=model_name,
        118         valid_errors=valid_errors
        119     )


    Cell In[32], line 133, in generate_all_valid_errors(func, logical_steps, correct_trace)
        130 repro_seed = base_seed + hash(generator_func.__name__)
        131 random.seed(repro_seed)
    --> 133 error_result = generator_func()
        134 if not error_result:
        135     continue


    Cell In[29], line 196, in generate_multiplication_by_reciprocal_error(numeric_val, fraction_val)
        191 new_numerator = numeric_val * fraction_val.denominator
        192 new_denominator = fraction_val.numerator
        194 return {
        195     # The value is correct, but the representation now preserves the logic.
    --> 196     "flawed_value": NonSimplifyingFraction(new_numerator, new_denominator),
        197     "explanation_type": "It appears the value was multiplied by the reciprocal of the intended fraction."
        198 }


    Cell In[28], line 15, in NonSimplifyingFraction.__new__(cls, numerator, denominator)
         13 def __new__(cls, numerator=0, denominator=None):
         14     # We must use __new__ because Fraction is immutable
    ---> 15     self = super(NonSimplifyingFraction, cls).__new__(cls, numerator, denominator)
         16     # Store the original denominator for the __str__ method.
         17     # The built-in .denominator will be simplified.
         18     if denominator is not None:


    File /opt/miniconda3/envs/erdos-dl/lib/python3.12/fractions.py:277, in Fraction.__new__(cls, numerator, denominator)
        272     numerator, denominator = (
        273         numerator.numerator * denominator.denominator,
        274         denominator.numerator * numerator.denominator
        275         )
        276 else:
    --> 277     raise TypeError("both arguments should be "
        278                     "Rational instances")
        280 if denominator == 0:
        281     raise ZeroDivisionError('Fraction(%s, 0)' % numerator)


    TypeError: both arguments should be Rational instances



```python
# In a new cell, after the pipeline finishes:
df = pd.read_csv(GENERATED_ERRORS_DIR / "computational_error_catalog.csv")

# Find all manifests where execution_trace failed
trace_failures = df[df['correct_trace_generated'] == False]

print(f"Found {len(trace_failures)} manifests that failed the execution_trace step.")
display(trace_failures.head())
```

    Found 4 manifests that failed the execution_trace step.



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>tier</th>
      <th>model</th>
      <th>target_variable</th>
      <th>error_type</th>
      <th>correct_value</th>
      <th>flawed_value</th>
      <th>repro_seed</th>
      <th>date_utc</th>
      <th>time_utc</th>
      <th>filepath</th>
      <th>correct_trace_generated</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>307</th>
      <td>116</td>
      <td>tier1</td>
      <td>google_gemini-2.5-flash</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td></td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>False</td>
    </tr>
    <tr>
      <th>11822</th>
      <td>497</td>
      <td>tier3</td>
      <td>openai_gpt-4.1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td></td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>False</td>
    </tr>
    <tr>
      <th>15868</th>
      <td>2250</td>
      <td>tier4</td>
      <td>openai_gpt-4.1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td></td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>False</td>
    </tr>
    <tr>
      <th>15869</th>
      <td>2250</td>
      <td>tier4</td>
      <td>google_gemini-2.5-flash</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td></td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>

