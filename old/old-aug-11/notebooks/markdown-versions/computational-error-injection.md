### Cell 1: Imports and Setup


```python
import json
import re
import ast
import inspect
import importlib.util
from pathlib import Path
from types import ModuleType
from typing import Callable, Any, Dict, List
from fractions import Fraction as BuiltinFraction
import datetime
import functools
import random
import copy

import pandas as pd
from tqdm.notebook import tqdm
from datasets import load_dataset, Dataset

# --- Path and Directory Definitions ---
def find_project_root(marker: str = ".git") -> Path:
    current_path = Path.cwd().resolve()
    while current_path != current_path.parent:
        if (current_path / marker).exists():
            return current_path
        current_path = current_path.parent
    raise FileNotFoundError(f"Could not find project root. Marker '{marker}' not found.")

PROJECT_ROOT = find_project_root()
DATA_DIR = PROJECT_ROOT / 'data'

PROCESSED_TEMPLATE_DIR = DATA_DIR / "template-generated-processed"
GENERATED_ERRORS_DIR = DATA_DIR / "computational-errors-generated"

MODELS = ['openai_gpt-4.1', 'google_gemini-2.5-flash']

print(f"Project root: {PROJECT_ROOT}")
print(f"Input (Processed Templates): {PROCESSED_TEMPLATE_DIR}")
print(f"Output (Generated Errors): {GENERATED_ERRORS_DIR}")

# --- Ensure Directories Exist ---
PROCESSED_TEMPLATE_DIR.mkdir(parents=True, exist_ok=True)
GENERATED_ERRORS_DIR.mkdir(parents=True, exist_ok=True)
```

    Project root: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math
    Input (Processed Templates): /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/template-generated-processed
    Output (Generated Errors): /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/computational-errors-generated


### Cell 2: Load dataset and define the tiers


```python
# --- Load GSM8K Dataset ---
GSM8K_TRAIN: Dataset = load_dataset("gsm8k", "main")["train"] #type: ignore

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
```

    Tier definitions loaded.


### Cell 3: Template Loading Utilities


```python
def load_function_module(tier: str, index: int, model_name: str) -> ModuleType | None:
    """Dynamically loads the '{model_name}.py' file for a given template."""
    py_file_path = PROCESSED_TEMPLATE_DIR / tier / str(index) / f"{model_name}.py"
    if not py_file_path.exists():
        return None
    module_name = f"templates.t{tier}.i{index}.m_{model_name.replace('.', '_')}.solve"
    spec = importlib.util.spec_from_file_location(module_name, py_file_path)
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    return None

def load_logical_steps(tier: str, index: int, model_name: str) -> list[dict] | None:
    """Loads the '{model_name}.json' file for a given template."""
    json_file_path = PROCESSED_TEMPLATE_DIR / tier / str(index) / f"{model_name}.json"
    try:
        return json.loads(json_file_path.read_text(encoding='utf-8'))
    except (FileNotFoundError, json.JSONDecodeError):
        return None

print("Template loading functions defined.")
```

    Template loading functions defined.


### Cell 4: Core Pipeline Utilities


```python
# --- ADD THIS CLASS ---
class FormattingTrace(dict):
    """A dictionary subclass that formats numbers for clean reconstruction."""
    def __getitem__(self, key):
        val = super().__getitem__(key)
        if isinstance(val, float) and val.is_integer():
            return str(int(val))
        if isinstance(val, float):
            # Round to 2 decimal places, but remove trailing .0 if it exists
            rounded_val = round(val, 2)
            if rounded_val == int(rounded_val):
                 return str(int(rounded_val))
            return str(rounded_val)
        return str(val)

class NonSimplifyingFraction(BuiltinFraction):
    """
    A subclass of fractions.Fraction that does NOT simplify when converted
    to a string, preserving the original representation from the template.
    """
    def __new__(cls, numerator=0, denominator=None):
        self = super().__new__(cls, numerator, denominator)
        if denominator is not None:
            self._original_denominator = denominator
            self._original_numerator = numerator
        else:
            self._original_numerator, self._original_denominator = self.as_integer_ratio()
        return self

    def __str__(self):
        return f"{self._original_numerator}/{self._original_denominator}"

def normalize_value(value: Any) -> Any:
    """Normalizes a numeric value by casting integer-like floats to int."""
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value

def get_sign(n) -> int:
    """Returns the sign of a number (1 for positive, -1 for negative, 0 for zero)."""
    if n > 0: return 1
    if n < 0: return -1
    return 0

def has_distinct_adjacent_digits(n: int) -> bool:
    """Checks if an integer is suitable for digit transposition."""
    s = str(abs(n))
    return len(s) >= 2 and any(s[i] != s[i+1] for i in range(len(s) - 1))

def execution_trace(func: Callable[[], Any]) -> dict[str, Any] | None:
    """
    Executes a function's source code line by line to build a variable trace,
    using NonSimplifyingFraction to preserve fraction representations.
    """
    try:
        src = inspect.getsource(func)
        tree = ast.parse(src)
        func_def = tree.body[0]
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
    Creates a flawed execution trace by modifying an assignment in the function's
    AST and re-executing it, using NonSimplifyingFraction.
    """
    try:
        src = inspect.getsource(func)
        tree = ast.parse(src)
        func_def = tree.body[0]
        variable_to_change = error_details["variable"]
        flawed_value = error_details["flawed_value"]
        modified_body = copy.deepcopy(func_def.body)
        node_found_and_modified = False
        for node in modified_body:
            if isinstance(node, ast.Assign) and any(t.id == variable_to_change for t in node.targets if isinstance(t, ast.Name)):
                if isinstance(flawed_value, BuiltinFraction):
                    new_value_node = ast.Call(
                        func=ast.Name(id='Fraction', ctx=ast.Load()),
                        args=[ast.Constant(value=flawed_value._original_numerator), ast.Constant(value=flawed_value._original_denominator)],
                        keywords=[]
                    )
                else:
                    new_value_node = ast.Constant(value=flawed_value)
                ast.copy_location(new_value_node, node.value)
                ast.fix_missing_locations(new_value_node)
                node.value = new_value_node
                node_found_and_modified = True
                break
        if not node_found_and_modified: return None

        global_namespace = {'Fraction': NonSimplifyingFraction}
        env = {}
        for stmt in modified_body:
            if isinstance(stmt, ast.Assign):
                code_obj = compile(ast.Module([stmt], type_ignores=[]), '<string>', 'exec')
                exec(code_obj, global_namespace, env)
        return env
    except Exception:
        return None

def reconstruct_solution_lines(logical_steps: list[dict], eval_trace: dict[str, Any]) -> dict[str, str] | None:
    """Reconstructs natural language solution lines from templates and a variable trace."""
    reconstructed_mapping = {}
    # --- MODIFICATION: Wrap eval_trace with FormattingTrace ---
    formatted_trace = FormattingTrace(eval_trace)
    for step in logical_steps:
        ln, template = step.get("line_number"), step.get("solution_line_template")
        if not (ln and template): continue
        try:
            reconstructed_mapping[ln] = template.format_map(formatted_trace)
        except (KeyError, ValueError):
            return None
    return reconstructed_mapping

def is_trace_valid(flawed_trace: dict[str, Any], correct_trace: dict[str, Any]) -> bool:
    """Validates a flawed trace for type integrity and sign integrity."""
    for var_name, correct_val in correct_trace.items():
        flawed_val = flawed_trace.get(var_name)
        if flawed_val is None: continue
        is_correct_int_like = isinstance(normalize_value(correct_val), int)
        is_flawed_int_like = isinstance(normalize_value(flawed_val), int)
        if is_correct_int_like and not is_flawed_int_like: return False
        
        processed_correct = normalize_value(correct_val)
        processed_flawed = normalize_value(flawed_val)
        if isinstance(processed_correct, (int, float)) and processed_correct != 0:
            if get_sign(processed_correct) != get_sign(processed_flawed): return False
    return True

print("Core pipeline utilities defined.")
```

    Core pipeline utilities defined.


### Cell 5: Error Generator Functions


```python
def generate_off_by_n_error(correct_value: int, offset_range: tuple[int, int] = (1, 5)):
    offset = random.randint(offset_range[0], offset_range[1]) * random.choice([-1, 1])
    flawed_value = correct_value + offset
    if get_sign(correct_value) != get_sign(flawed_value) and correct_value != 0: flawed_value = correct_value - offset
    if flawed_value == correct_value: flawed_value += 1 if correct_value >= 0 else -1
    return {"flawed_value": flawed_value, "explanation_type": "This appears to be a minor miscalculation."}

def generate_off_by_factor_of_10_error(correct_value: int):
    if random.random() < 0.5:
        return {"flawed_value": correct_value // 10, "explanation_type": "It appears a zero was dropped from the number."}
    else:
        return {"flawed_value": correct_value * 10, "explanation_type": "It appears an extra zero was added to the number."}

def generate_digit_transposition_error(correct_value: int) -> dict[str, Any] | None:
    s_val = str(abs(correct_value))
    if len(s_val) < 2: return None
    valid_indices = [i for i in range(len(s_val) - 1) if s_val[i] != s_val[i+1] and not (i == 0 and s_val[i+1] == '0')]
    if not valid_indices: return None
    idx_to_swap = random.choice(valid_indices)
    s_list = list(s_val)
    s_list[idx_to_swap], s_list[idx_to_swap+1] = s_list[idx_to_swap+1], s_list[idx_to_swap]
    flawed_value = int("".join(s_list))
    if correct_value < 0: flawed_value = -flawed_value
    return {"flawed_value": flawed_value, "explanation_type": "It appears two adjacent digits were swapped."}

def generate_stem_off_by_n_error(correct_value: int, offset_range: tuple[int, int] = (1, 3)):
    stem = correct_value // 10
    offset = random.randint(offset_range[0], offset_range[1]) * random.choice([-1, 1])
    flawed_stem = stem + offset
    if flawed_stem == stem: flawed_stem += 1
    return {"flawed_value": flawed_stem * 10, "explanation_type": "It appears there was a miscalculation with the digits before the final zero."}

def generate_decimal_shift_error(correct_value: float):
    flawed_value = correct_value * 10 if random.random() < 0.5 else correct_value / 10
    return {"flawed_value": round(flawed_value, 10), "explanation_type": "It appears the decimal point was misplaced."}

def generate_float_off_by_n_error(correct_value: float):
    magnitude = abs(correct_value)
    offset = random.uniform(magnitude * 0.1, magnitude * 0.2) * random.choice([-1, 1])
    return {"flawed_value": round(correct_value + offset, 10), "explanation_type": "This appears to be a minor miscalculation."}

def generate_reciprocal_error(correct_value: NonSimplifyingFraction):
    if correct_value.denominator == 0: return None
    return {"flawed_value": NonSimplifyingFraction(correct_value.denominator, correct_value.numerator), "explanation_type": "It appears the numerator and denominator were swapped."}

def generate_off_by_one_in_fraction_part_error(correct_value: NonSimplifyingFraction):
    offset = random.choice([-1, 1])
    if random.random() < 0.5:
        new_num, new_den = correct_value.numerator + offset, correct_value.denominator
    else:
        new_num, new_den = correct_value.numerator, correct_value.denominator + offset
        if new_den == 0: new_den = correct_value.denominator + (offset * 2)
    return {"flawed_value": NonSimplifyingFraction(new_num, new_den), "explanation_type": "It appears there was an off-by-one error in the fraction."}

def generate_multiplication_by_reciprocal_error(numeric_val: Any, fraction_val: NonSimplifyingFraction):
    if fraction_val.numerator == 0: return None
    numeric_as_frac = BuiltinFraction(numeric_val)
    new_num = numeric_as_frac.numerator * fraction_val.denominator
    new_den = numeric_as_frac.denominator * fraction_val.numerator
    return {"flawed_value": NonSimplifyingFraction(new_num, new_den), "explanation_type": "It appears the value was multiplied by the reciprocal of the intended fraction."}

print("Error generator functions defined.")
```

    Error generator functions defined.


### Cell 6: Error Applicability Logic


```python
def get_target_variables(logical_steps: list[dict]) -> list[str]:
    """Extracts all 'output_variable' names from the logical steps."""
    return [step['output_variable'] for step in logical_steps if 'output_variable' in step]

def get_operator_for_variable(func: Callable, variable_name: str) -> str | None:
    """Inspects the AST to find the operator used to compute a variable."""
    try:
        src = inspect.getsource(func)
        tree = ast.parse(src)
    except (TypeError, FileNotFoundError, SyntaxError): return None
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(t.id == variable_name for t in node.targets if isinstance(t, ast.Name)):
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
    except (TypeError, FileNotFoundError, SyntaxError): return []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(t.id == variable_name for t in node.targets if isinstance(t, ast.Name)):
            for sub_node in ast.walk(node.value):
                if isinstance(sub_node, ast.Name): operand_names.append(sub_node.id)
            return list(set(operand_names))
    return []

def _get_applicable_integer_errors(correct_value: int, operator: str, operand_values: list):
    """Returns a list of applicable error generator functions for an integer."""
    applicable_generators = []
    if operator in ["add", "sub"]:
        if all(isinstance(v, int) and v % 10 == 0 for v in operand_values) and correct_value % 10 == 0 and correct_value != 0:
            applicable_generators.append(generate_stem_off_by_n_error)
        else:
            applicable_generators.append(generate_off_by_n_error)
    if correct_value % 100 == 0 and correct_value != 0:
        applicable_generators.append(generate_off_by_factor_of_10_error)
    if has_distinct_adjacent_digits(correct_value):
        applicable_generators.append(generate_digit_transposition_error)
    return applicable_generators

def get_applicable_generators(func: Callable, correct_trace: dict[str, Any], variable_name: str):
    """Identifies and partially instantiates all applicable error generators for a variable."""
    applicable_generators = []
    correct_value = correct_trace.get(variable_name)
    if not isinstance(correct_value, (int, float, BuiltinFraction)): return []

    def add_generator(gen_func, value_to_pass):
        partial_gen = functools.partial(gen_func, value_to_pass)
        partial_gen.__name__ = gen_func.__name__
        applicable_generators.append(partial_gen)

    if isinstance(correct_value, int) or (isinstance(correct_value, float) and correct_value.is_integer()):
        int_val, op = int(correct_value), get_operator_for_variable(func, variable_name)
        op_names = get_operand_names_for_variable(func, variable_name)
        op_vals = [correct_trace.get(name) for name in op_names if name in correct_trace]
        for gen_func in _get_applicable_integer_errors(int_val, op, op_vals):
            add_generator(gen_func, int_val)
    elif isinstance(correct_value, float):
        add_generator(generate_float_off_by_n_error, correct_value)
        if correct_value != 0: add_generator(generate_decimal_shift_error, correct_value)
    elif isinstance(correct_value, NonSimplifyingFraction) and correct_value.denominator != 1:
        add_generator(generate_off_by_one_in_fraction_part_error, correct_value)
        if correct_value.numerator != 0: add_generator(generate_reciprocal_error, correct_value)

    if get_operator_for_variable(func, variable_name) == "mult":
        op_names = get_operand_names_for_variable(func, variable_name)
        op_vals = [correct_trace.get(name) for name in op_names if name in correct_trace]
        if len(op_vals) == 2:
            num_op = next((op for op in op_vals if isinstance(op, (int, float))), None)
            frac_op = next((op for op in op_vals if isinstance(op, NonSimplifyingFraction)), None)
            if num_op is not None and frac_op is not None and frac_op.denominator != 1:
                gen = functools.partial(generate_multiplication_by_reciprocal_error, numeric_val=num_op, fraction_val=frac_op)
                gen.__name__ = 'generate_multiplication_by_reciprocal_error'
                applicable_generators.append(gen)
    return list(dict.fromkeys(applicable_generators))

print("Error applicability logic defined.")
```

    Error applicability logic defined.


### Cell 7: Orchestrator and Artifact Generation


```python
def find_error_line_number(variable_name: str, logical_steps: list[dict]) -> str | None:
    """Finds the line number corresponding to a given output variable."""
    for step in logical_steps:
        if step.get("output_variable") == variable_name:
            return step.get("line_number")
    return None

def generate_training_artifacts(
    logical_steps: list[dict], # <- 'func' argument removed
    error_details: dict[str, Any],
    flawed_trace: dict[str, Any]
):
    """Generates the final training data: a flawed NL solution and a JSON label."""
    flawed_solution_map = reconstruct_solution_lines(logical_steps, flawed_trace)
    if not flawed_solution_map: return None
    
    sorted_lines = sorted(flawed_solution_map.items(), key=lambda item: int(item[0][1:]))
    flawed_nl_solution = "\n".join([line for _, line in sorted_lines])
    
    # --- START OF SIMPLIFIED LOGIC ---
    # The return variable is always 'answer'.
    return_variable = "answer"
    
    if return_variable in flawed_trace:
        final_answer = normalize_value(flawed_trace[return_variable])
        flawed_nl_solution += f"\n#### {final_answer}"
    # --- END OF SIMPLIFIED LOGIC ---

    erroneous_line = find_error_line_number(error_details["variable"], logical_steps)
    if not erroneous_line: return None

    correct_val_str = str(normalize_value(error_details['correct_value']))
    flawed_val_str = str(normalize_value(error_details['flawed_value']))
    
    base_explanation = f"The result of this computation should be {correct_val_str}, not {flawed_val_str}."
    type_explanation = error_details["explanation_type"]
    
    target_json = {
        "verdict": "Flawed",
        "error_details": {
            "error_type": "computational_error",
            "erroneous_line_number": erroneous_line,
            "explanation": f"{base_explanation} {type_explanation}",
        }
    }
    return flawed_nl_solution, target_json

def generate_all_valid_errors(
    func: Callable,
    logical_steps: list[dict],
    correct_trace: dict[str, Any],
    max_attempts: int = 10
) -> list[dict]:
    """
    Deterministically generates and validates all possible computational errors.
    """
    all_generated_examples = []
    target_variables = get_target_variables(logical_steps)
    
    for variable_name in target_variables:
        correct_value = correct_trace.get(variable_name)
        base_seed = hash(f"{variable_name}")
        applicable_generators = get_applicable_generators(func, correct_trace, variable_name)

        for generator_func in applicable_generators:
            for attempt in range(max_attempts):
                repro_seed = base_seed + hash(generator_func.__name__) + attempt
                random.seed(repro_seed)
                
                error_result = generator_func()
                if not error_result: continue

                error_details = {"variable": variable_name, "correct_value": correct_value, **error_result}
                if isinstance(correct_value, float) and correct_value.is_integer():
                    error_details['flawed_value'] = float(error_details['flawed_value'])

                flawed_trace = generate_flawed_trace(func, error_details)
                
                if flawed_trace and is_trace_valid(flawed_trace, correct_trace):
                    # --- MODIFICATION: The call no longer needs 'func' ---
                    artifacts = generate_training_artifacts(logical_steps, error_details, flawed_trace)
                    if artifacts:
                        all_generated_examples.append({
                            "variable": variable_name, "error_type": generator_func.__name__,
                            "flawed_nl_solution": artifacts[0], "target_json": artifacts[1],
                            "correct_value": error_details['correct_value'],
                            "flawed_value": error_details['flawed_value'], "repro_seed": repro_seed,
                        })
                        break
    return all_generated_examples

def save_error_artifacts(tier: str, index: int, model_name: str, valid_errors: list[dict]):
    """Saves all valid error artifacts to disk and returns a list of metadata records."""
    output_dir = GENERATED_ERRORS_DIR / tier / str(index)
    output_dir.mkdir(parents=True, exist_ok=True)
    metadata_records = []
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    for error_example in valid_errors:
        variable, error_type = error_example['variable'], error_example['error_type']
        filename = f"{model_name}_{variable}_{error_type}.json"
        filepath = output_dir / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump({"flawed_nl_solution": error_example["flawed_nl_solution"], "target_json": error_example["target_json"]}, f, indent=2)
        record = {
            "index": index, "tier": tier, "model": model_name, "target_variable": variable,
            "error_type": error_type, "correct_value": normalize_value(error_example['correct_value']),
            "flawed_value": normalize_value(error_example['flawed_value']), "repro_seed": error_example['repro_seed'],
            "date_utc": now_utc.strftime('%Y-%m-%d'), "time_utc": now_utc.strftime('%H:%M:%S'),
            "filepath": str(filepath.relative_to(PROJECT_ROOT))
        }
        metadata_records.append(record)
    return metadata_records

print("Orchestration and artifact generation functions defined.")
```

    Orchestration and artifact generation functions defined.


### Cell 8: Parallel worker function


```python
from joblib import Parallel, delayed

def process_single_template(tier: str, index: int, model_name: str, project_root: Path, processed_dir: Path, output_dir: Path) -> list[dict]:
    """
    Worker function to process a single template. This function is designed to be
    called in parallel by joblib. It includes comprehensive error handling.
    """
    # --- START OF MODIFICATION: Add try...except block ---
    try:
        solve_module = load_function_module(tier, index, model_name)
        logical_steps = load_logical_steps(tier, index, model_name)
        
        if not (solve_module and logical_steps):
            return [{"index": index, "tier": tier, "model": model_name, "correct_trace_generated": False, "error_type": "TemplateFilesMissing"}]

        solve_function = solve_module.solve
        correct_trace = execution_trace(solve_function)

        if not correct_trace:
            return [{"index": index, "tier": tier, "model": model_name, "correct_trace_generated": False}]

        valid_errors = generate_all_valid_errors(solve_function, logical_steps, correct_trace)
        
        if valid_errors:
            records = save_error_artifacts(tier, index, model_name, valid_errors)
            for record in records:
                record['correct_trace_generated'] = True
            return records
        
        return [{"index": index, "tier": tier, "model": model_name, "correct_trace_generated": True, "error_type": "NoValidErrorsFound"}]
    
    except Exception as e:
        # If any unexpected error occurs, print a diagnostic message and return
        # an empty list so the main process does not crash.
        print(f"\n---")
        print(f"WARNING: A critical error occurred while processing template (tier={tier}, index={index}, model={model_name}).")
        print(f"Error Type: {type(e).__name__}")
        print(f"Error Details: {e}")
        print(f"This template will be skipped. The pipeline will continue.")
        print(f"---")
        return []
    # --- END OF MODIFICATION ---

print("Parallel worker function defined.")
```

    Parallel worker function defined.


### Cell 9: Main Driver


```python
def generate_errors_for_all_templates_parallel():
    """
    Drives the error generation pipeline in parallel using joblib.
    """
    print("--- Starting Parallel Error Generation for All Processed Templates ---")

    # 1. Prepare the list of all tasks to be executed.
    tasks = []
    tier_dirs = sorted([d for d in PROCESSED_TEMPLATE_DIR.iterdir() if d.is_dir() and d.name.startswith('tier')])
    for tier_dir in tier_dirs:
        index_dirs = sorted([d for d in tier_dir.iterdir() if d.is_dir() and d.name.isdigit()], key=lambda p: int(p.name))
        for index_dir in index_dirs:
            index = int(index_dir.name)
            for model_name in MODELS:
                tasks.append((tier_dir.name, index, model_name, PROJECT_ROOT, PROCESSED_TEMPLATE_DIR, GENERATED_ERRORS_DIR))
    
    print(f"Found {len(tasks)} total templates to process across all models.")

    # 2. Execute all tasks in parallel.
    # n_jobs=-1 uses all available CPU cores.
    # The 'loky' backend is more robust for complex Python objects.
    results = Parallel(n_jobs=-1, backend="loky")(
        delayed(process_single_template)(*task_args) for task_args in tqdm(tasks, desc="Generating Errors")
    )

    # 3. Flatten the list of lists into a single list of metadata records.
    all_metadata = [record for sublist in results for record in sublist]

    # 4. Save the final catalog CSV file.
    if all_metadata:
        catalog_df = pd.DataFrame(all_metadata)
        cols = ['index', 'tier', 'model', 'correct_trace_generated', 'target_variable', 'error_type', 'correct_value', 'flawed_value', 'repro_seed', 'date_utc', 'time_utc', 'filepath']
        catalog_df = catalog_df.reindex(columns=cols).sort_values(by=['tier', 'index', 'model']).reset_index(drop=True)
        catalog_path = GENERATED_ERRORS_DIR / "computational_error_catalog.csv"
        catalog_df.to_csv(catalog_path, index=False)
        print(f"\nCatalog with {len(catalog_df)} records saved to: {catalog_path}")
    else:
        print("\nNo templates were found to process or no metadata was returned.")
    print("--- Parallel Error Generation Pipeline Complete ---")

# Note: Your old "Cell 9: Execute the Pipeline" is now Cell 10.
# It simply calls this new function.
```

### Cell 10: Execute the Pipeline


```python
generate_errors_for_all_templates_parallel()
```

    --- Starting Parallel Error Generation for All Processed Templates ---
    Found 5832 total templates to process across all models.



    Generating Errors:   0%|          | 0/5832 [00:00<?, ?it/s]


    
    ---
    WARNING: A critical error occurred while processing template (tier=tier3, index=400, model=openai_gpt-4.1).
    Error Type: AttributeError
    Error Details: 'str' object has no attribute 'denominator'
    This template will be skipped. The pipeline will continue.
    ---
    
    Catalog with 16506 records saved to: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/computational-errors-generated/computational_error_catalog.csv
    --- Parallel Error Generation Pipeline Complete ---



```python
catalog_df = pd.read_csv(GENERATED_ERRORS_DIR / "computational_error_catalog.csv")
error_type_counts = catalog_df['error_type'].value_counts()
print("\n--- Error Type Counts ---")
print(error_type_counts)
```

    
    --- Error Type Counts ---
    error_type
    generate_digit_transposition_error             6632
    generate_off_by_n_error                        4972
    generate_off_by_factor_of_10_error             1781
    generate_stem_off_by_n_error                   1105
    TemplateFilesMissing                           1037
    NoValidErrorsFound                              358
    generate_multiplication_by_reciprocal_error     333
    generate_decimal_shift_error                    195
    generate_float_off_by_n_error                    70
    generate_off_by_one_in_fraction_part_error       11
    generate_reciprocal_error                         8
    Name: count, dtype: int64

