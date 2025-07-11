#### Cell 3: Core trace and solution generation


```python
from typing import Any, Dict
import re
import copy

def execution_trace(func) -> Dict[str, Any] | None:
    """
    Parses a function's source code and executes it line by line
    to capture the final value of each assigned variable.

    This function is designed for simple, self-contained functions
    like the 'solve()' methods in the manifests.

    Args:
        func: The function object to trace.

    Returns:
        A dictionary mapping variable names to their computed values, or None on error.
    """
    try:
        # 1. Get the source code and parse it into an Abstract Syntax Tree (AST)
        src = inspect.getsource(func)
        tree = ast.parse(src)
    except (TypeError, FileNotFoundError, SyntaxError) as e:
        print(f"ERROR: Could not get or parse source for {func.__name__}: {e}")
        return None

    # 2. Assume the first node in the file is the function definition
    func_def = tree.body[0]
    if not isinstance(func_def, ast.FunctionDef):
        print("ERROR: The parsed source code does not start with a function definition.")
        return None

    # 3. `env` will store the execution environment (variable states)
    env = {}

    # 4. Execute each statement in the function body sequentially
    for stmt in func_def.body:
        # We only process simple assignments (e.g., x = y + z)
        if isinstance(stmt, ast.Assign):
            # Compile and execute the single assignment statement.
            # The result is stored in the `env` dictionary, which acts
            # as the memory for subsequent computations.
            try:
                # ast.Module is required to create a valid code block
                code_obj = compile(ast.Module([stmt], type_ignores=[]), '<string>', 'exec')
                exec(code_obj, {}, env)
            except Exception as e:
                # This helps debug issues in the manifest's function_code
                print(f"ERROR: Failed to execute line: {ast.unparse(stmt)}. Error: {e}")
                return None # Halt on error to ensure trace integrity
        
        # We ignore other node types like `ast.Return`

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
    Substitutes variable placeholders in solution templates with their values,
    using normalization for clean formatting.
    """
    reconstructed_mapping = {}
    placeholder_pattern = re.compile(r'\{([a-zA-Z0-9_]+)\}')

    for step in logical_steps:
        line_number = step.get("line_number")
        template = step.get("solution_line_template")

        if not line_number or not template:
            continue

        def replacer(match):
            variable_name = match.group(1)
            value = eval_trace.get(variable_name)

            if value is None:
                return f"{{ERROR: {variable_name} not in trace}}"
            
            # Use the normalization utility for correct string rendering
            value_to_render = normalize_value(value)
            
            return str(value_to_render)

        reconstructed_line = placeholder_pattern.sub(replacer, template)
        reconstructed_mapping[line_number] = reconstructed_line

    return reconstructed_mapping


```

#### Cell 4: Individual Error Generation functions


```python
import random


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


def generate_decimal_shift_error(correct_value: float) -> dict[str, Any]:
    """Multiplies or divides a float by 10 to simulate a decimal shift."""
    choice = random.choice(["multiply", "divide"])
    flawed_value = correct_value * 10 if choice == "multiply" else correct_value / 10
    return {
        "flawed_value": round(flawed_value, 10), # Round to avoid precision issues
        "explanation_type": "It appears the decimal point was misplaced."
    }


def generate_monetary_off_by_cents_error(correct_value: float) -> dict[str, Any]:
    """Adds or subtracts a small, realistic monetary amount."""
    offsets = [0.10, 0.25, 0.50, 1.00, 2.00]
    offset = random.choice(offsets)
    if random.random() < 0.5:
        offset = -offset
    
    flawed_value = correct_value + offset
    return {
        "flawed_value": round(flawed_value, 2), # Ensure result is a valid monetary value
        "explanation_type": "This appears to be a minor miscalculation in cents or dollars."
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


```

#### Cell 5: Error Generation Controller and Helpers


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


# --- IN CELL 5 ---
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

#### Cell 6: Validation Utilities


```python

def get_sign(n) -> int:
    """Returns the sign of a number (1 for positive, -1 for negative, 0 for zero)."""
    if n > 0: return 1
    if n < 0: return -1
    return 0


def normalize_value(value):
    """
    Normalizes a numeric value for consistent comparison and rendering.
    If a float can be represented as an integer (e.g., 20.0), it is cast to int.
    """
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value


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

#### Cell 7: Final Artifact assembly


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

#### Cell 8: Main Orchestrator


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


```python
print(build_solution_mapping(index=4822, dataset=GSM8K_TRAIN))
```

    {'L1': 'He gets 500*.8=$<<500*.8=400>>400 off the cost of lenses', 'L2': 'That means the lenses cost 500-400=$<<500-400=100>>100', 'L3': 'The frames cost 200-50=$<<200-50=150>>150', 'L4': 'So he pays 100+150=$<<100+150=250>>250'}


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
for index in [310, 2300, 2401, 2918, 4822]:
    try:
        run_comprehensive_error_test(tier=example_tier, index=index)
    except Exception as e:
        import traceback
        print(f"\nAN UNCAUGHT ERROR OCCURRED: {e}")
        traceback.print_exc()
```

    ============================================================
    STARTING COMPREHENSIVE TEST FOR: Tier 'tier2', Index '310'
    ============================================================
    
    Found 8 target variables to test: ['hours_per_worker_per_month', 'wage_per_warehouse_worker', 'total_warehouse_wages', 'wage_per_manager', 'total_manager_wages', 'total_wages', 'fica_taxes', 'grand_total']
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'hours_per_worker_per_month' (Correct Value: 200) ---
      -> Found 2 applicable error types: ['generate_off_by_factor_of_10_error', 'generate_digit_transposition_error']
    
      --- Applying Error: generate_off_by_factor_of_10_error ---
    
        --- Flawed Solution (using generate_off_by_factor_of_10_error) ---
    First figure out how many hours each worker works per month by multiplying the number of days they work by the number of hours a day they work: 25 days * 8 hours/day = <<25*8=2000>>2000 hours
    Then calculate how much one warehouse worker makes per month by multiplying their hourly rate by the number of hours they work: 2000 hours * $15/hour = $<<2000*15=30000>>30000
    Then multiply that number by 4 to find out how much all the warehouse workers make: $30000/worker * 4 workers = $<<30000*4=120000>>120000
    Now multiply the hours each manager works (also 2000) by their hourly wage to find out how much one manager makes per month: 2000 hours * $20/hour = $<<2000*20=40000>>40000
    Now multiply one manager's wages by the number of managers (2) to find their total wage amount: $40000/manager * 2 managers = $<<40000*2=80000>>80000
    Now add the wages for the managers and the workers to find the total cost of the wages: $80000 + $120000 = $<<80000+120000=200000>>200000
    Now multiply the total wage bill by 10% to find how much the FICA taxes are: $200000 * 0.1 = $<<200000*0.1=20000>>20000
    Now add the total wage bill to the total tax amount to find the grand total: $20000 + $200000 = $<<20000+200000=220000>>220000
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L1",
        "explanation": "The result of this computation should be 200, not 2000. It appears an extra zero was added to the number."
      }
    }
    
      --- Applying Error: generate_digit_transposition_error ---
        -> Generator returned None (e.g., no valid transposition). Skipping.
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'wage_per_warehouse_worker' (Correct Value: 3000) ---
      -> Found 2 applicable error types: ['generate_off_by_factor_of_10_error', 'generate_digit_transposition_error']
    
      --- Applying Error: generate_off_by_factor_of_10_error ---
    
        --- Flawed Solution (using generate_off_by_factor_of_10_error) ---
    First figure out how many hours each worker works per month by multiplying the number of days they work by the number of hours a day they work: 25 days * 8 hours/day = <<25*8=200>>200 hours
    Then calculate how much one warehouse worker makes per month by multiplying their hourly rate by the number of hours they work: 200 hours * $15/hour = $<<200*15=30000>>30000
    Then multiply that number by 4 to find out how much all the warehouse workers make: $30000/worker * 4 workers = $<<30000*4=120000>>120000
    Now multiply the hours each manager works (also 200) by their hourly wage to find out how much one manager makes per month: 200 hours * $20/hour = $<<200*20=4000>>4000
    Now multiply one manager's wages by the number of managers (2) to find their total wage amount: $4000/manager * 2 managers = $<<4000*2=8000>>8000
    Now add the wages for the managers and the workers to find the total cost of the wages: $8000 + $120000 = $<<8000+120000=128000>>128000
    Now multiply the total wage bill by 10% to find how much the FICA taxes are: $128000 * 0.1 = $<<128000*0.1=12800>>12800
    Now add the total wage bill to the total tax amount to find the grand total: $12800 + $128000 = $<<12800+128000=140800>>140800
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L2",
        "explanation": "The result of this computation should be 3000, not 30000. It appears an extra zero was added to the number."
      }
    }
    
      --- Applying Error: generate_digit_transposition_error ---
        -> Generator returned None (e.g., no valid transposition). Skipping.
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'total_warehouse_wages' (Correct Value: 12000) ---
      -> Found 2 applicable error types: ['generate_off_by_factor_of_10_error', 'generate_digit_transposition_error']
    
      --- Applying Error: generate_off_by_factor_of_10_error ---
    
        --- Flawed Solution (using generate_off_by_factor_of_10_error) ---
    First figure out how many hours each worker works per month by multiplying the number of days they work by the number of hours a day they work: 25 days * 8 hours/day = <<25*8=200>>200 hours
    Then calculate how much one warehouse worker makes per month by multiplying their hourly rate by the number of hours they work: 200 hours * $15/hour = $<<200*15=3000>>3000
    Then multiply that number by 4 to find out how much all the warehouse workers make: $3000/worker * 4 workers = $<<3000*4=1200>>1200
    Now multiply the hours each manager works (also 200) by their hourly wage to find out how much one manager makes per month: 200 hours * $20/hour = $<<200*20=4000>>4000
    Now multiply one manager's wages by the number of managers (2) to find their total wage amount: $4000/manager * 2 managers = $<<4000*2=8000>>8000
    Now add the wages for the managers and the workers to find the total cost of the wages: $8000 + $1200 = $<<8000+1200=9200>>9200
    Now multiply the total wage bill by 10% to find how much the FICA taxes are: $9200 * 0.1 = $<<9200*0.1=920>>920
    Now add the total wage bill to the total tax amount to find the grand total: $920 + $9200 = $<<920+9200=10120>>10120
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L3",
        "explanation": "The result of this computation should be 12000, not 1200. It appears a zero was dropped from the number."
      }
    }
    
      --- Applying Error: generate_digit_transposition_error ---
    
        --- Flawed Solution (using generate_digit_transposition_error) ---
    First figure out how many hours each worker works per month by multiplying the number of days they work by the number of hours a day they work: 25 days * 8 hours/day = <<25*8=200>>200 hours
    Then calculate how much one warehouse worker makes per month by multiplying their hourly rate by the number of hours they work: 200 hours * $15/hour = $<<200*15=3000>>3000
    Then multiply that number by 4 to find out how much all the warehouse workers make: $3000/worker * 4 workers = $<<3000*4=21000>>21000
    Now multiply the hours each manager works (also 200) by their hourly wage to find out how much one manager makes per month: 200 hours * $20/hour = $<<200*20=4000>>4000
    Now multiply one manager's wages by the number of managers (2) to find their total wage amount: $4000/manager * 2 managers = $<<4000*2=8000>>8000
    Now add the wages for the managers and the workers to find the total cost of the wages: $8000 + $21000 = $<<8000+21000=29000>>29000
    Now multiply the total wage bill by 10% to find how much the FICA taxes are: $29000 * 0.1 = $<<29000*0.1=2900>>2900
    Now add the total wage bill to the total tax amount to find the grand total: $2900 + $29000 = $<<2900+29000=31900>>31900
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L3",
        "explanation": "The result of this computation should be 12000, not 21000. It appears two adjacent digits were swapped."
      }
    }
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'wage_per_manager' (Correct Value: 4000) ---
      -> Found 2 applicable error types: ['generate_off_by_factor_of_10_error', 'generate_digit_transposition_error']
    
      --- Applying Error: generate_off_by_factor_of_10_error ---
    
        --- Flawed Solution (using generate_off_by_factor_of_10_error) ---
    First figure out how many hours each worker works per month by multiplying the number of days they work by the number of hours a day they work: 25 days * 8 hours/day = <<25*8=200>>200 hours
    Then calculate how much one warehouse worker makes per month by multiplying their hourly rate by the number of hours they work: 200 hours * $15/hour = $<<200*15=3000>>3000
    Then multiply that number by 4 to find out how much all the warehouse workers make: $3000/worker * 4 workers = $<<3000*4=12000>>12000
    Now multiply the hours each manager works (also 200) by their hourly wage to find out how much one manager makes per month: 200 hours * $20/hour = $<<200*20=40000>>40000
    Now multiply one manager's wages by the number of managers (2) to find their total wage amount: $40000/manager * 2 managers = $<<40000*2=80000>>80000
    Now add the wages for the managers and the workers to find the total cost of the wages: $80000 + $12000 = $<<80000+12000=92000>>92000
    Now multiply the total wage bill by 10% to find how much the FICA taxes are: $92000 * 0.1 = $<<92000*0.1=9200>>9200
    Now add the total wage bill to the total tax amount to find the grand total: $9200 + $92000 = $<<9200+92000=101200>>101200
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L4",
        "explanation": "The result of this computation should be 4000, not 40000. It appears an extra zero was added to the number."
      }
    }
    
      --- Applying Error: generate_digit_transposition_error ---
        -> Generator returned None (e.g., no valid transposition). Skipping.
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'total_manager_wages' (Correct Value: 8000) ---
      -> Found 2 applicable error types: ['generate_off_by_factor_of_10_error', 'generate_digit_transposition_error']
    
      --- Applying Error: generate_off_by_factor_of_10_error ---
    
        --- Flawed Solution (using generate_off_by_factor_of_10_error) ---
    First figure out how many hours each worker works per month by multiplying the number of days they work by the number of hours a day they work: 25 days * 8 hours/day = <<25*8=200>>200 hours
    Then calculate how much one warehouse worker makes per month by multiplying their hourly rate by the number of hours they work: 200 hours * $15/hour = $<<200*15=3000>>3000
    Then multiply that number by 4 to find out how much all the warehouse workers make: $3000/worker * 4 workers = $<<3000*4=12000>>12000
    Now multiply the hours each manager works (also 200) by their hourly wage to find out how much one manager makes per month: 200 hours * $20/hour = $<<200*20=4000>>4000
    Now multiply one manager's wages by the number of managers (2) to find their total wage amount: $4000/manager * 2 managers = $<<4000*2=80000>>80000
    Now add the wages for the managers and the workers to find the total cost of the wages: $80000 + $12000 = $<<80000+12000=92000>>92000
    Now multiply the total wage bill by 10% to find how much the FICA taxes are: $92000 * 0.1 = $<<92000*0.1=9200>>9200
    Now add the total wage bill to the total tax amount to find the grand total: $9200 + $92000 = $<<9200+92000=101200>>101200
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L5",
        "explanation": "The result of this computation should be 8000, not 80000. It appears an extra zero was added to the number."
      }
    }
    
      --- Applying Error: generate_digit_transposition_error ---
        -> Generator returned None (e.g., no valid transposition). Skipping.
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'total_wages' (Correct Value: 20000) ---
      -> Found 3 applicable error types: ['generate_stem_off_by_n_error', 'generate_off_by_factor_of_10_error', 'generate_digit_transposition_error']
    
      --- Applying Error: generate_stem_off_by_n_error ---
    
        --- Flawed Solution (using generate_stem_off_by_n_error) ---
    First figure out how many hours each worker works per month by multiplying the number of days they work by the number of hours a day they work: 25 days * 8 hours/day = <<25*8=200>>200 hours
    Then calculate how much one warehouse worker makes per month by multiplying their hourly rate by the number of hours they work: 200 hours * $15/hour = $<<200*15=3000>>3000
    Then multiply that number by 4 to find out how much all the warehouse workers make: $3000/worker * 4 workers = $<<3000*4=12000>>12000
    Now multiply the hours each manager works (also 200) by their hourly wage to find out how much one manager makes per month: 200 hours * $20/hour = $<<200*20=4000>>4000
    Now multiply one manager's wages by the number of managers (2) to find their total wage amount: $4000/manager * 2 managers = $<<4000*2=8000>>8000
    Now add the wages for the managers and the workers to find the total cost of the wages: $8000 + $12000 = $<<8000+12000=20030>>20030
    Now multiply the total wage bill by 10% to find how much the FICA taxes are: $20030 * 0.1 = $<<20030*0.1=2003>>2003
    Now add the total wage bill to the total tax amount to find the grand total: $2003 + $20030 = $<<2003+20030=22033>>22033
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L6",
        "explanation": "The result of this computation should be 20000, not 20030. It appears there was a miscalculation with the digits before the final zero."
      }
    }
    
      --- Applying Error: generate_off_by_factor_of_10_error ---
    
        --- Flawed Solution (using generate_off_by_factor_of_10_error) ---
    First figure out how many hours each worker works per month by multiplying the number of days they work by the number of hours a day they work: 25 days * 8 hours/day = <<25*8=200>>200 hours
    Then calculate how much one warehouse worker makes per month by multiplying their hourly rate by the number of hours they work: 200 hours * $15/hour = $<<200*15=3000>>3000
    Then multiply that number by 4 to find out how much all the warehouse workers make: $3000/worker * 4 workers = $<<3000*4=12000>>12000
    Now multiply the hours each manager works (also 200) by their hourly wage to find out how much one manager makes per month: 200 hours * $20/hour = $<<200*20=4000>>4000
    Now multiply one manager's wages by the number of managers (2) to find their total wage amount: $4000/manager * 2 managers = $<<4000*2=8000>>8000
    Now add the wages for the managers and the workers to find the total cost of the wages: $8000 + $12000 = $<<8000+12000=200000>>200000
    Now multiply the total wage bill by 10% to find how much the FICA taxes are: $200000 * 0.1 = $<<200000*0.1=20000>>20000
    Now add the total wage bill to the total tax amount to find the grand total: $20000 + $200000 = $<<20000+200000=220000>>220000
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L6",
        "explanation": "The result of this computation should be 20000, not 200000. It appears an extra zero was added to the number."
      }
    }
    
      --- Applying Error: generate_digit_transposition_error ---
        -> Generator returned None (e.g., no valid transposition). Skipping.
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'fica_taxes' (Correct Value: 2000.0) ---
      -> Found 2 applicable error types: ['generate_off_by_factor_of_10_error', 'generate_digit_transposition_error']
    
      --- Applying Error: generate_off_by_factor_of_10_error ---
    
        --- Flawed Solution (using generate_off_by_factor_of_10_error) ---
    First figure out how many hours each worker works per month by multiplying the number of days they work by the number of hours a day they work: 25 days * 8 hours/day = <<25*8=200>>200 hours
    Then calculate how much one warehouse worker makes per month by multiplying their hourly rate by the number of hours they work: 200 hours * $15/hour = $<<200*15=3000>>3000
    Then multiply that number by 4 to find out how much all the warehouse workers make: $3000/worker * 4 workers = $<<3000*4=12000>>12000
    Now multiply the hours each manager works (also 200) by their hourly wage to find out how much one manager makes per month: 200 hours * $20/hour = $<<200*20=4000>>4000
    Now multiply one manager's wages by the number of managers (2) to find their total wage amount: $4000/manager * 2 managers = $<<4000*2=8000>>8000
    Now add the wages for the managers and the workers to find the total cost of the wages: $8000 + $12000 = $<<8000+12000=20000>>20000
    Now multiply the total wage bill by 10% to find how much the FICA taxes are: $20000 * 0.1 = $<<20000*0.1=20000>>20000
    Now add the total wage bill to the total tax amount to find the grand total: $20000 + $20000 = $<<20000+20000=40000>>40000
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L7",
        "explanation": "The result of this computation should be 2000.0, not 20000.0. It appears an extra zero was added to the number."
      }
    }
    
      --- Applying Error: generate_digit_transposition_error ---
        -> Generator returned None (e.g., no valid transposition). Skipping.
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'grand_total' (Correct Value: 22000.0) ---
      -> Found 3 applicable error types: ['generate_off_by_n_error', 'generate_off_by_factor_of_10_error', 'generate_digit_transposition_error']
    
      --- Applying Error: generate_off_by_n_error ---
    
        --- Flawed Solution (using generate_off_by_n_error) ---
    First figure out how many hours each worker works per month by multiplying the number of days they work by the number of hours a day they work: 25 days * 8 hours/day = <<25*8=200>>200 hours
    Then calculate how much one warehouse worker makes per month by multiplying their hourly rate by the number of hours they work: 200 hours * $15/hour = $<<200*15=3000>>3000
    Then multiply that number by 4 to find out how much all the warehouse workers make: $3000/worker * 4 workers = $<<3000*4=12000>>12000
    Now multiply the hours each manager works (also 200) by their hourly wage to find out how much one manager makes per month: 200 hours * $20/hour = $<<200*20=4000>>4000
    Now multiply one manager's wages by the number of managers (2) to find their total wage amount: $4000/manager * 2 managers = $<<4000*2=8000>>8000
    Now add the wages for the managers and the workers to find the total cost of the wages: $8000 + $12000 = $<<8000+12000=20000>>20000
    Now multiply the total wage bill by 10% to find how much the FICA taxes are: $20000 * 0.1 = $<<20000*0.1=2000>>2000
    Now add the total wage bill to the total tax amount to find the grand total: $2000 + $20000 = $<<2000+20000=22004>>22004
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L8",
        "explanation": "The result of this computation should be 22000.0, not 22004.0. This appears to be a minor miscalculation."
      }
    }
    
      --- Applying Error: generate_off_by_factor_of_10_error ---
    
        --- Flawed Solution (using generate_off_by_factor_of_10_error) ---
    First figure out how many hours each worker works per month by multiplying the number of days they work by the number of hours a day they work: 25 days * 8 hours/day = <<25*8=200>>200 hours
    Then calculate how much one warehouse worker makes per month by multiplying their hourly rate by the number of hours they work: 200 hours * $15/hour = $<<200*15=3000>>3000
    Then multiply that number by 4 to find out how much all the warehouse workers make: $3000/worker * 4 workers = $<<3000*4=12000>>12000
    Now multiply the hours each manager works (also 200) by their hourly wage to find out how much one manager makes per month: 200 hours * $20/hour = $<<200*20=4000>>4000
    Now multiply one manager's wages by the number of managers (2) to find their total wage amount: $4000/manager * 2 managers = $<<4000*2=8000>>8000
    Now add the wages for the managers and the workers to find the total cost of the wages: $8000 + $12000 = $<<8000+12000=20000>>20000
    Now multiply the total wage bill by 10% to find how much the FICA taxes are: $20000 * 0.1 = $<<20000*0.1=2000>>2000
    Now add the total wage bill to the total tax amount to find the grand total: $2000 + $20000 = $<<2000+20000=2200>>2200
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L8",
        "explanation": "The result of this computation should be 22000.0, not 2200.0. It appears a zero was dropped from the number."
      }
    }
    
      --- Applying Error: generate_digit_transposition_error ---
    
        --- Flawed Solution (using generate_digit_transposition_error) ---
    First figure out how many hours each worker works per month by multiplying the number of days they work by the number of hours a day they work: 25 days * 8 hours/day = <<25*8=200>>200 hours
    Then calculate how much one warehouse worker makes per month by multiplying their hourly rate by the number of hours they work: 200 hours * $15/hour = $<<200*15=3000>>3000
    Then multiply that number by 4 to find out how much all the warehouse workers make: $3000/worker * 4 workers = $<<3000*4=12000>>12000
    Now multiply the hours each manager works (also 200) by their hourly wage to find out how much one manager makes per month: 200 hours * $20/hour = $<<200*20=4000>>4000
    Now multiply one manager's wages by the number of managers (2) to find their total wage amount: $4000/manager * 2 managers = $<<4000*2=8000>>8000
    Now add the wages for the managers and the workers to find the total cost of the wages: $8000 + $12000 = $<<8000+12000=20000>>20000
    Now multiply the total wage bill by 10% to find how much the FICA taxes are: $20000 * 0.1 = $<<20000*0.1=2000>>2000
    Now add the total wage bill to the total tax amount to find the grand total: $2000 + $20000 = $<<2000+20000=20200>>20200
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L8",
        "explanation": "The result of this computation should be 22000.0, not 20200.0. It appears two adjacent digits were swapped."
      }
    }
    
    ============================================================
    COMPREHENSIVE TEST COMPLETE
    ============================================================
    ============================================================
    STARTING COMPREHENSIVE TEST FOR: Tier 'tier2', Index '2300'
    ============================================================
    
    Found 5 target variables to test: ['josh_hours_per_month', 'josh_monthly_pay', 'carl_hours_per_month', 'carl_monthly_pay', 'total_pay']
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'josh_hours_per_month' (Correct Value: 160) ---
      -> Found 1 applicable error types: ['generate_digit_transposition_error']
    
      --- Applying Error: generate_digit_transposition_error ---
    
        --- Flawed Solution (using generate_digit_transposition_error) ---
    Josh works 8 hours/day * 5 days/week * 4 weeks/month = <<8*5*4=610>>610 hours a month.
    He earns 610 hours/month * $9/month = $<<610*9=5490>>5490 per month.
    Carl works less because he is an intern: 6 hours/day * 5 days/week * 4 weeks/month = <<6*5*4=120>>120 hours per month.
    Carl earns 120 hours * $4.5/hour = $<<120*4.5=540>>540 per month.
    The company pays for the 2 together: $5490 + $540 = $<<5490+540=6030>>6030.
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L1",
        "explanation": "The result of this computation should be 160, not 610. It appears two adjacent digits were swapped."
      }
    }
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'josh_monthly_pay' (Correct Value: 1440) ---
    
        --- Flawed Solution (using generate_digit_transposition_error) ---
    Josh works 8 hours/day * 5 days/week * 4 weeks/month = <<8*5*4=610>>610 hours a month.
    He earns 610 hours/month * $9/month = $<<610*9=5490>>5490 per month.
    Carl works less because he is an intern: 6 hours/day * 5 days/week * 4 weeks/month = <<6*5*4=120>>120 hours per month.
    Carl earns 120 hours * $4.5/hour = $<<120*4.5=540>>540 per month.
    The company pays for the 2 together: $5490 + $540 = $<<5490+540=6030>>6030.
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L1",
        "explanation": "The result of this computation should be 160, not 610. It appears two adjacent digits were swapped."
      }
    }
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'josh_monthly_pay' (Correct Value: 1440) ---
      -> Found 1 applicable error types: ['generate_digit_transposition_error']
    
      --- Applying Error: generate_digit_transposition_error ---
    
        --- Flawed Solution (using generate_digit_transposition_error) ---
    Josh works 8 hours/day * 5 days/week * 4 weeks/month = <<8*5*4=160>>160 hours a month.
    He earns 160 hours/month * $9/month = $<<160*9=4140>>4140 per month.
    Carl works less because he is an intern: 6 hours/day * 5 days/week * 4 weeks/month = <<6*5*4=120>>120 hours per month.
    Carl earns 120 hours * $4.5/hour = $<<120*4.5=540>>540 per month.
    The company pays for the 2 together: $4140 + $540 = $<<4140+540=4680>>4680.
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L2",
        "explanation": "The result of this computation should be 1440, not 4140. It appears two adjacent digits were swapped."
      }
    }
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'carl_hours_per_month' (Correct Value: 120) ---
      -> Found 1 applicable error types: ['generate_digit_transposition_error']
    
      --- Applying Error: generate_digit_transposition_error ---
    
        --- Flawed Solution (using generate_digit_transposition_error) ---
    Josh works 8 hours/day * 5 days/week * 4 weeks/month = <<8*5*4=160>>160 hours a month.
    He earns 160 hours/month * $9/month = $<<160*9=1440>>1440 per month.
    Carl works less because he is an intern: 6 hours/day * 5 days/week * 4 weeks/month = <<6*5*4=210>>210 hours per month.
    Carl earns 210 hours * $4.5/hour = $<<210*4.5=945>>945 per month.
    The company pays for the 2 together: $1440 + $945 = $<<1440+945=2385>>2385.
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L3",
        "explanation": "The result of this computation should be 120, not 210. It appears two adjacent digits were swapped."
      }
    }
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'carl_monthly_pay' (Correct Value: 540.0) ---
      -> Found 1 applicable error types: ['generate_digit_transposition_error']
    
      --- Applying Error: generate_digit_transposition_error ---
    
        --- Flawed Solution (using generate_digit_transposition_error) ---
    Josh works 8 hours/day * 5 days/week * 4 weeks/month = <<8*5*4=160>>160 hours a month.
    He earns 160 hours/month * $9/month = $<<160*9=1440>>1440 per month.
    Carl works less because he is an intern: 6 hours/day * 5 days/week * 4 weeks/month = <<6*5*4=120>>120 hours per month.
    Carl earns 120 hours * $4.5/hour = $<<120*4.5=450>>450 per month.
    The company pays for the 2 together: $1440 + $450 = $<<1440+450=1890>>1890.
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L4",
        "explanation": "The result of this computation should be 540.0, not 450.0. It appears two adjacent digits were swapped."
      }
    }
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'total_pay' (Correct Value: 1980.0) ---
      -> Found 2 applicable error types: ['generate_off_by_n_error', 'generate_digit_transposition_error']
    
      --- Applying Error: generate_off_by_n_error ---
    
        --- Flawed Solution (using generate_off_by_n_error) ---
    Josh works 8 hours/day * 5 days/week * 4 weeks/month = <<8*5*4=160>>160 hours a month.
    He earns 160 hours/month * $9/month = $<<160*9=1440>>1440 per month.
    Carl works less because he is an intern: 6 hours/day * 5 days/week * 4 weeks/month = <<6*5*4=120>>120 hours per month.
    Carl earns 120 hours * $4.5/hour = $<<120*4.5=540>>540 per month.
    The company pays for the 2 together: $1440 + $540 = $<<1440+540=1982>>1982.
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L5",
        "explanation": "The result of this computation should be 1980.0, not 1982.0. This appears to be a minor miscalculation."
      }
    }
    
      --- Applying Error: generate_digit_transposition_error ---
    
        --- Flawed Solution (using generate_digit_transposition_error) ---
    Josh works 8 hours/day * 5 days/week * 4 weeks/month = <<8*5*4=160>>160 hours a month.
    He earns 160 hours/month * $9/month = $<<160*9=1440>>1440 per month.
    Carl works less because he is an intern: 6 hours/day * 5 days/week * 4 weeks/month = <<6*5*4=120>>120 hours per month.
    Carl earns 120 hours * $4.5/hour = $<<120*4.5=540>>540 per month.
    The company pays for the 2 together: $1440 + $540 = $<<1440+540=1908>>1908.
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L5",
        "explanation": "The result of this computation should be 1980.0, not 1908.0. It appears two adjacent digits were swapped."
      }
    }
    
    ============================================================
    COMPREHENSIVE TEST COMPLETE
    ============================================================
    ============================================================
    STARTING COMPREHENSIVE TEST FOR: Tier 'tier2', Index '2401'
    ============================================================
    
    Found 7 target variables to test: ['initial_run_duration', 'distance_before_notice', 'additional_fast_run_duration', 'additional_fast_distance', 'slow_distance', 'chase_distance', 'total_distance']
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'initial_run_duration' (Correct Value: 3) ---
      -> Found 1 applicable error types: ['generate_off_by_n_error']
    
      --- Applying Error: generate_off_by_n_error ---
    
        --- Flawed Solution (using generate_off_by_n_error) ---
    He was running for 4-1=<<4-1=2>>2 hours
    So in that time he runs 2*25=<<2*25=50>>50 miles
    Since he slowed down after 4 hours, the time he spent running at 25mph was an additional 4-2=<<4-2=2>>2 hours
    So in the first hour they were finding him, he ran 2*25=<<2*25=50>>50 miles
    In the second hour they were finding him, he ran 1*10=<<1*10=10>>10 miles
    Finally, during the chase, he ran 50*0.5=<<50*0.5=25>>25 miles
    So he is 50+50+10+25=<<50+50+10+25=135>>135 miles away
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L1",
        "explanation": "The result of this computation should be 3, not 2. This appears to be a minor miscalculation."
      }
    }
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'distance_before_notice' (Correct Value: 75) ---
      -> Found 1 applicable error types: ['generate_digit_transposition_error']
    
      --- Applying Error: generate_digit_transposition_error ---
    
        --- Flawed Solution (using generate_digit_transposition_error) ---
    He was running for 4-1=<<4-1=3>>3 hours
    So in that time he runs 3*25=<<3*25=57>>57 miles
    Since he slowed down after 4 hours, the time he spent running at 25mph was an additional 4-3=<<4-3=1>>1 hours
    So in the first hour they were finding him, he ran 1*25=<<1*25=25>>25 miles
    In the second hour they were finding him, he ran 1*10=<<1*10=10>>10 miles
    Finally, during the chase, he ran 50*0.5=<<50*0.5=25>>25 miles
    So he is 57+25+10+25=<<57+25+10+25=117>>117 miles away
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L2",
        "explanation": "The result of this computation should be 75, not 57. It appears two adjacent digits were swapped."
      }
    }
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'additional_fast_run_duration' (Correct Value: 1) ---
      -> Found 1 applicable error types: ['generate_off_by_n_error']
    
      --- Applying Error: generate_off_by_n_error ---
    
        --- Flawed Solution (using generate_off_by_n_error) ---
    He was running for 4-1=<<4-1=3>>3 hours
    So in that time he runs 3*25=<<3*25=75>>75 miles
    Since he slowed down after 4 hours, the time he spent running at 25mph was an additional 4-3=<<4-3=6>>6 hours
    So in the first hour they were finding him, he ran 6*25=<<6*25=150>>150 miles
    In the second hour they were finding him, he ran 1*10=<<1*10=10>>10 miles
    Finally, during the chase, he ran 50*0.5=<<50*0.5=25>>25 miles
    So he is 75+150+10+25=<<75+150+10+25=260>>260 miles away
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L3",
        "explanation": "The result of this computation should be 1, not 6. This appears to be a minor miscalculation."
      }
    }
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'additional_fast_distance' (Correct Value: 25) ---
      -> Found 1 applicable error types: ['generate_digit_transposition_error']
    
      --- Applying Error: generate_digit_transposition_error ---
    
        --- Flawed Solution (using generate_digit_transposition_error) ---
    He was running for 4-1=<<4-1=3>>3 hours
    So in that time he runs 3*25=<<3*25=75>>75 miles
    Since he slowed down after 4 hours, the time he spent running at 25mph was an additional 4-3=<<4-3=1>>1 hours
    So in the first hour they were finding him, he ran 1*25=<<1*25=52>>52 miles
    In the second hour they were finding him, he ran 1*10=<<1*10=10>>10 miles
    Finally, during the chase, he ran 50*0.5=<<50*0.5=25>>25 miles
    So he is 75+52+10+25=<<75+52+10+25=162>>162 miles away
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L4",
        "explanation": "The result of this computation should be 25, not 52. It appears two adjacent digits were swapped."
      }
    }
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'slow_distance' (Correct Value: 10) ---
      -> Found 1 applicable error types: ['generate_digit_transposition_error']
    
      --- Applying Error: generate_digit_transposition_error ---
        -> Generator returned None (e.g., no valid transposition). Skipping.
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'chase_distance' (Correct Value: 25.0) ---
      -> Found 1 applicable error types: ['generate_digit_transposition_error']
    
      --- Applying Error: generate_digit_transposition_error ---
    
        --- Flawed Solution (using generate_digit_transposition_error) ---
    He was running for 4-1=<<4-1=3>>3 hours
    So in that time he runs 3*25=<<3*25=75>>75 miles
    Since he slowed down after 4 hours, the time he spent running at 25mph was an additional 4-3=<<4-3=1>>1 hours
    So in the first hour they were finding him, he ran 1*25=<<1*25=25>>25 miles
    In the second hour they were finding him, he ran 1*10=<<1*10=10>>10 miles
    Finally, during the chase, he ran 50*0.5=<<50*0.5=52>>52 miles
    So he is 75+25+10+52=<<75+25+10+52=162>>162 miles away
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L6",
        "explanation": "The result of this computation should be 25.0, not 52.0. It appears two adjacent digits were swapped."
      }
    }
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'total_distance' (Correct Value: 135.0) ---
      -> Found 2 applicable error types: ['generate_off_by_n_error', 'generate_digit_transposition_error']
    
      --- Applying Error: generate_off_by_n_error ---
    
        --- Flawed Solution (using generate_off_by_n_error) ---
    He was running for 4-1=<<4-1=3>>3 hours
    So in that time he runs 3*25=<<3*25=75>>75 miles
    Since he slowed down after 4 hours, the time he spent running at 25mph was an additional 4-3=<<4-3=1>>1 hours
    So in the first hour they were finding him, he ran 1*25=<<1*25=25>>25 miles
    In the second hour they were finding him, he ran 1*10=<<1*10=10>>10 miles
    Finally, during the chase, he ran 50*0.5=<<50*0.5=25>>25 miles
    So he is 75+25+10+25=<<75+25+10+25=139>>139 miles away
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L7",
        "explanation": "The result of this computation should be 135.0, not 139.0. This appears to be a minor miscalculation."
      }
    }
    
      --- Applying Error: generate_digit_transposition_error ---
    
        --- Flawed Solution (using generate_digit_transposition_error) ---
    He was running for 4-1=<<4-1=3>>3 hours
    So in that time he runs 3*25=<<3*25=75>>75 miles
    Since he slowed down after 4 hours, the time he spent running at 25mph was an additional 4-3=<<4-3=1>>1 hours
    So in the first hour they were finding him, he ran 1*25=<<1*25=25>>25 miles
    In the second hour they were finding him, he ran 1*10=<<1*10=10>>10 miles
    Finally, during the chase, he ran 50*0.5=<<50*0.5=25>>25 miles
    So he is 75+25+10+25=<<75+25+10+25=315>>315 miles away
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L7",
        "explanation": "The result of this computation should be 135.0, not 315.0. It appears two adjacent digits were swapped."
      }
    }
    
    ============================================================
    COMPREHENSIVE TEST COMPLETE
    ============================================================
    ============================================================
    STARTING COMPREHENSIVE TEST FOR: Tier 'tier2', Index '2918'
    ============================================================
    
    Found 3 target variables to test: ['base_cost', 'discount_amount', 'final_cost']
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'base_cost' (Correct Value: 500.0) ---
      -> Found 2 applicable error types: ['generate_off_by_factor_of_10_error', 'generate_digit_transposition_error']
    
      --- Applying Error: generate_off_by_factor_of_10_error ---
    
        --- Flawed Solution (using generate_off_by_factor_of_10_error) ---
    Phoebe is having 20 guests and Monica charges $25 per person so that’s 20*25 = $<<20*25=50>>50
    Phoebe is a repeat customer so she gets 10% off of $50 so that’s .10*50 = $<<10*0.01*50=5>>5 discount
    Monica is charging $50 minus the repeat customer discount of $5 so she will make 50-5 = $<<50-5=45>>45
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L1",
        "explanation": "The result of this computation should be 500.0, not 50.0. It appears a zero was dropped from the number."
      }
    }
    
      --- Applying Error: generate_digit_transposition_error ---
        -> Generator returned None (e.g., no valid transposition). Skipping.
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'discount_amount' (Correct Value: 50.0) ---
      -> Found 1 applicable error types: ['generate_digit_transposition_error']
    
      --- Applying Error: generate_digit_transposition_error ---
        -> Generator returned None (e.g., no valid transposition). Skipping.
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'final_cost' (Correct Value: 450.0) ---
      -> Found 2 applicable error types: ['generate_off_by_n_error', 'generate_digit_transposition_error']
    
      --- Applying Error: generate_off_by_n_error ---
    
        --- Flawed Solution (using generate_off_by_n_error) ---
    Phoebe is having 20 guests and Monica charges $25 per person so that’s 20*25 = $<<20*25=500>>500
    Phoebe is a repeat customer so she gets 10% off of $500 so that’s .10*500 = $<<10*0.01*500=50>>50 discount
    Monica is charging $500 minus the repeat customer discount of $50 so she will make 500-50 = $<<500-50=453>>453
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L3",
        "explanation": "The result of this computation should be 450.0, not 453.0. This appears to be a minor miscalculation."
      }
    }
    
      --- Applying Error: generate_digit_transposition_error ---
    
        --- Flawed Solution (using generate_digit_transposition_error) ---
    Phoebe is having 20 guests and Monica charges $25 per person so that’s 20*25 = $<<20*25=500>>500
    Phoebe is a repeat customer so she gets 10% off of $500 so that’s .10*500 = $<<10*0.01*500=50>>50 discount
    Monica is charging $500 minus the repeat customer discount of $50 so she will make 500-50 = $<<500-50=405>>405
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L3",
        "explanation": "The result of this computation should be 450.0, not 405.0. It appears two adjacent digits were swapped."
      }
    }
    
    ============================================================
    COMPREHENSIVE TEST COMPLETE
    ============================================================
    ============================================================
    STARTING COMPREHENSIVE TEST FOR: Tier 'tier2', Index '4822'
    ============================================================
    
    Found 4 target variables to test: ['lenses_coverage_amount', 'final_lenses_cost', 'final_frames_cost', 'total_cost']
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'lenses_coverage_amount' (Correct Value: 400.0) ---
      -> Found 2 applicable error types: ['generate_off_by_factor_of_10_error', 'generate_digit_transposition_error']
    
      --- Applying Error: generate_off_by_factor_of_10_error ---
    VALIDATION FAIL (Sign): Var 'final_lenses_cost' changed sign from 100.0 to -3500.0.
        -> FAILED: Generated an invalid trace (sign/type change). Skipping.
    
      --- Applying Error: generate_digit_transposition_error ---
        -> Generator returned None (e.g., no valid transposition). Skipping.
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'final_lenses_cost' (Correct Value: 100.0) ---
      -> Found 3 applicable error types: ['generate_off_by_n_error', 'generate_off_by_factor_of_10_error', 'generate_digit_transposition_error']
    
      --- Applying Error: generate_off_by_n_error ---
    
        --- Flawed Solution (using generate_off_by_n_error) ---
    He gets 500*0.8=$<<500*0.8=400>>400 off the cost of lenses
    That means the lenses cost 500-400=$<<500-400=95>>95
    The frames cost 200-50=$<<200-50=150>>150
    So he pays 95+150=$<<95+150=245>>245
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L2",
        "explanation": "The result of this computation should be 100.0, not 95.0. This appears to be a minor miscalculation."
      }
    }
    
      --- Applying Error: generate_off_by_factor_of_10_error ---
    
        --- Flawed Solution (using generate_off_by_factor_of_10_error) ---
    He gets 500*0.8=$<<500*0.8=400>>400 off the cost of lenses
    That means the lenses cost 500-400=$<<500-400=10>>10
    The frames cost 200-50=$<<200-50=150>>150
    So he pays 10+150=$<<10+150=160>>160
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L2",
        "explanation": "The result of this computation should be 100.0, not 10.0. It appears a zero was dropped from the number."
      }
    }
    
      --- Applying Error: generate_digit_transposition_error ---
        -> Generator returned None (e.g., no valid transposition). Skipping.
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'final_frames_cost' (Correct Value: 150) ---
      -> Found 2 applicable error types: ['generate_stem_off_by_n_error', 'generate_digit_transposition_error']
    
      --- Applying Error: generate_stem_off_by_n_error ---
    
        --- Flawed Solution (using generate_stem_off_by_n_error) ---
    He gets 500*0.8=$<<500*0.8=400>>400 off the cost of lenses
    That means the lenses cost 500-400=$<<500-400=100>>100
    The frames cost 200-50=$<<200-50=170>>170
    So he pays 100+170=$<<100+170=270>>270
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L3",
        "explanation": "The result of this computation should be 150, not 170. It appears there was a miscalculation with the digits before the final zero."
      }
    }
    
      --- Applying Error: generate_digit_transposition_error ---
    
        --- Flawed Solution (using generate_digit_transposition_error) ---
    He gets 500*0.8=$<<500*0.8=400>>400 off the cost of lenses
    That means the lenses cost 500-400=$<<500-400=100>>100
    The frames cost 200-50=$<<200-50=105>>105
    So he pays 100+105=$<<100+105=205>>205
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L3",
        "explanation": "The result of this computation should be 150, not 105. It appears two adjacent digits were swapped."
      }
    }
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    --- TESTING VARIABLE: 'total_cost' (Correct Value: 250.0) ---
      -> Found 2 applicable error types: ['generate_off_by_n_error', 'generate_digit_transposition_error']
    
      --- Applying Error: generate_off_by_n_error ---
    
        --- Flawed Solution (using generate_off_by_n_error) ---
    He gets 500*0.8=$<<500*0.8=400>>400 off the cost of lenses
    That means the lenses cost 500-400=$<<500-400=100>>100
    The frames cost 200-50=$<<200-50=150>>150
    So he pays 100+150=$<<100+150=247>>247
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L4",
        "explanation": "The result of this computation should be 250.0, not 247.0. This appears to be a minor miscalculation."
      }
    }
    
      --- Applying Error: generate_digit_transposition_error ---
    
        --- Flawed Solution (using generate_digit_transposition_error) ---
    He gets 500*0.8=$<<500*0.8=400>>400 off the cost of lenses
    That means the lenses cost 500-400=$<<500-400=100>>100
    The frames cost 200-50=$<<200-50=150>>150
    So he pays 100+150=$<<100+150=205>>205
    
        --- Target JSON Label ---
    {
      "verdict": "Flawed",
      "error_details": {
        "error_type": "computational_error",
        "erroneous_line_number": "L4",
        "explanation": "The result of this computation should be 250.0, not 205.0. It appears two adjacent digits were swapped."
      }
    }
    
    ============================================================
    COMPREHENSIVE TEST COMPLETE
    ============================================================



```python
