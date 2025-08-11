"""
# The `ErrorInjector` Pipeline: Algorithm Details

This document outlines the algorithm for each of the four error injection strategies. The central design principle is a **hybrid AST/string-manipulation approach**. We use Python's Abstract Syntax Tree (`ast`) module for robustly and accurately *finding* a target for modification, but then perform the actual modification using string operations on the original source code.

This hybrid approach gives us the best of both worlds:
1.  **Robustness (from AST):** The AST understands the code's structure, so we can reliably find, for example, "the third binary operation" or "an assignment to the variable `x`" without brittle regular expressions.
2.  **Format Preservation (from Strings):** By only changing the specific line of code in the original source string, we preserve all comments, indentation, and blank lines, which is critical for our project.

---

### 1. `incorrect_operation`

**Goal:** To replace a mathematical operator (e.g., `+`) in an expression with a different, incorrect one (e.g., `*`).

**Algorithm:**
1.  **Parse & Map:** The source code is parsed into an AST. A `swap_map` dictionary is defined, mapping operators like `+` to a list of possible valid replacements, such as `*` or `-`.
2.  **Find Candidates:** The AST is traversed to find all binary operation nodes (`ast.BinOp`) whose operator type exists as a key in our `swap_map`. All such nodes are collected into a list of candidates.
3.  **Random Selection:**
    *   One candidate operation node is randomly selected from the list.
    *   A new replacement operator is randomly selected from the list of valid swaps for that specific operator (e.g., if `+` was chosen, the new operator could be `*` or `-`).
4.  **Targeted String Replacement:**
    *   The line number of the selected operation is retrieved from the AST node (`node.lineno`).
    *   The corresponding line is located in the original source code.
    *   A simple, one-time string `.replace()` is used to swap the original operator symbol (e.g., `+`) with the new one (e.g., `*`).

**Key Safeguards & Rationale:**
*   We deliberately **exclude division (`/`)** as a potential replacement for `+` or `*`. This is a critical safeguard to prevent two common sources of bad data:
    1.  **`ZeroDivisionError`:** A swap could easily result in a division by zero, making the flawed code un-runnable.
    2.  **Unintended Type Conversion:** Swapping an integer operation for division can silently convert the result to a `float` (e.g., `5+2` is `7`, but `5/2` is `2.5`), which introduces a second, uncontrolled error.

---

### 2. `computational_error`

**Goal:** To replace the result of a calculation with a fixed, incorrect numerical value.

**Algorithm:**
1.  **Parse & Find Candidates:** The code is parsed into an AST. All assignment nodes (`ast.Assign`) are collected as candidates, **except for assignments to the final `answer` variable**.
2.  **Simulate Execution:** For each candidate assignment, the script simulates the function's execution up to that point. It does this by:
    *   Creating a dictionary (`env`) with the function's default arguments.
    *   Executing each preceding line of code using `exec()` to populate `env` with the correct values of all intermediate variables.
3.  **Evaluate & Perturb:**
    *   The right-hand side of the candidate assignment is evaluated using `eval()` within the context of the simulated environment to get its correct `original_value`.
    *   This value is then "perturbed" by adding a small, random integer (e.g., +1, -10) to get a `new_value`.
4.  **Hybrid Replacement:**
    *   A new, temporary `ast.Assign` node is created, assigning the `new_value` to the same target variable.
    *   We use `ast.unparse()` on *only this new node* to generate a clean string of the flawed code line (e.g., `total_cost = 51.0`).
    *   This new string replaces the original line in the source code, preserving indentation.

**Key Safeguards & Rationale:**
*   We **exclude the final `answer = ...` line** from the candidate pool. This prevents the injector from simply hard-coding a wrong final answer, which is not a true "computational error" and provides a low-quality, ambiguous training signal. The error must occur in the reasoning steps.
*   The script uses `ast.copy_location()` to prevent a crash when un-parsing the newly created AST node, a bug we discovered during testing.

---

### 3. `incorrect_operand`

**Goal:** To replace a variable in a calculation with a different, incorrect variable.

**Algorithm:**
1.  **Parse & Find Candidates:** The AST is traversed to find all variables (`ast.Name` nodes) that are used as operands inside a binary operation. These are collected as candidates.
2.  **Dynamic Scope Calculation:** The candidates are shuffled, and the script iterates through them. For *each candidate*, it performs the following critical step:
    *   It determines the set of all variables that are **in scope at that specific line**. This is done by a helper that collects all function arguments plus any variables assigned on *previous* lines.
3.  **Select Replacement:** A replacement variable is randomly chosen from this correctly-scoped set, ensuring it is different from the original operand.
4.  **Targeted String Replacement:** The line containing the original operand is modified using `re.sub()` with word boundaries (`\b... \b`). This is more robust than a simple `.replace()` as it prevents accidentally changing parts of longer variable names (e.g., changing `x` in `x_offset`).

**Key Safeguards & Rationale:**
*   The **dynamic scope calculation** is the most important safeguard. It guarantees that we never replace a variable with one that hasn't been defined yet, which would cause the program to crash with an `UnboundLocalError`. This was a critical bug that was fixed during testing.

---

### 4. `skipped_step`

**Goal:** To delete an entire line of code (an assignment) and patch subsequent code to prevent it from crashing.

**Algorithm:**
1.  **Parse & Find Candidates:** The script collects all assignment statements as potential lines to delete, once again **excluding the final `answer = ...` assignment**.
2.  **Select Line and Replacement:**
    *   One candidate line is randomly chosen for deletion. The name of the variable it defined is stored (e.g., `deleted_var`).
    *   A plausible `replacement_var` is chosen to substitute for `deleted_var` in the rest of the code. The function prefers to use one of the original function arguments for this, as they are always in scope and often represent root values in the problem.
3.  **Patch and Delete:**
    *   The script iterates through all *subsequent* lines of the source code and uses `re.sub()` to replace every occurrence of the `deleted_var` with the `replacement_var`.
    *   Finally, the original candidate line is deleted from the source code.

**Key Safeguards & Rationale:**
*   As with the other injectors, excluding the `answer` assignment is critical to ensure the error is a genuine "skipped step" in reasoning, not a broken return statement.
*   The patching of subsequent lines is essential to prevent the flawed code from raising a `NameError` when it tries to use the `deleted_var` that was never defined. This ensures all generated examples are runnable.
"""


# ---------------------------------------------------------------------- #
#  Global constants & Configuration
# ---------------------------------------------------------------------- #

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
BASE_INPUT_DIR = PROJECT_ROOT / 'data' / 'code_gen_outputs_formatted'
BASE_OUTPUT_DIR = PROJECT_ROOT / 'data' / 'code_with_error'

#Make the output directory if it doesn't exist
if not BASE_OUTPUT_DIR.exists():
    BASE_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Created output directory: {BASE_OUTPUT_DIR}")

# Confirm the paths
print(f"Project root found: {PROJECT_ROOT}")
print(f"Base input directory set to: {BASE_INPUT_DIR}")
print(f"Base output directory set to: {BASE_OUTPUT_DIR}")

MODEL_DICT = {
  "anthropic": ["claude-3-5-haiku-20241022"], 
  "openai": ["gpt-4.1-mini"],
  "google": ["gemini-2.0-flash-thinking-exp", 
             "gemini-2.5-flash-lite-preview-06-17",
             "gemini-2.5-flash"]
}

MODELS = [f"{provider}_{model}" for provider, sublist in MODEL_DICT.items() for model in sublist]
print(f"Available models: {MODELS}")

INDICES = list(range(100))

import ast
import random
import re
from typing import Dict, Any, Tuple, Optional, List

class ErrorInjector:
    """
    A class to programmatically inject specific, controlled errors into
    the source code of a Python function using a hybrid AST and string
    manipulation approach to preserve formatting.
    """

    def inject(self, source_code: str, error_type: str, seed: Optional[int] = None) -> Optional[Tuple[str, Dict[str, Any]]]:
        """
        Main method to inject an error of a specified type into the source code.
        The provided seed makes the injection process deterministic.

        Args:
            source_code: A string containing the source code of a single function.
            error_type: The type of error to inject.
            seed: An optional integer to seed the random number generator for reproducibility.

        Returns:
            A tuple containing:
            - The modified source code as a string.
            - A dictionary with metadata about the injected error, including the seed.
            Returns None if an error of the specified type could not be injected.
        """
        if seed is not None:
            random.seed(seed)
        
        injection_methods = {
            "incorrect_operation": self.inject_incorrect_operation,
            "computational_error": self.inject_computational_error,
            "incorrect_operand": self.inject_incorrect_operand,
            "skipped_step": self.inject_skipped_step,
        }
        if error_type not in injection_methods:
            raise ValueError(f"Unknown error type: {error_type}")

        # Call the appropriate injection method
        result = injection_methods[error_type](source_code)

        # --- METADATA MODIFICATION ---
        # If injection was successful, add the seed to the metadata before returning.
        if result:
            modified_code, metadata = result
            metadata['seed'] = seed
            return modified_code, metadata
        
        # If injection failed, return None
        return None

    # --------------------------------------------------------------------------
    # Error Injection Strategies (Format-Preserving)
    # --------------------------------------------------------------------------

    def inject_incorrect_operation(self, source_code: str) -> Optional[Tuple[str, Dict[str, Any]]]:
        """Replaces a binary mathematical operator (+, -, *) with a different one."""
        tree = ast.parse(source_code)
        lines = source_code.splitlines()
        line_map = self._map_lines_to_labels(lines)
        
        op_map = {ast.Add: '+', ast.Sub: '-', ast.Mult: '*'}
        swap_map = {
            ast.Add: [(ast.Sub, '-'), (ast.Mult, '*')],
            ast.Sub: [(ast.Add, '+')],
            ast.Mult: [(ast.Add, '+'), (ast.Sub, '-')]
        }

        candidates = []
        for node in ast.walk(tree):
            if isinstance(node, ast.BinOp) and type(node.op) in swap_map:
                candidates.append(node)
        
        if not candidates:
            return None

        target_node = random.choice(candidates)
        original_op_node = target_node.op

        # Randomly choose one of the possible replacements from the list
        new_op_node_type, new_op_symbol = random.choice(swap_map[type(original_op_node)])
        
        original_op_symbol = op_map[type(original_op_node)]
        
        line_idx = target_node.lineno - 1
        lines[line_idx] = lines[line_idx].replace(original_op_symbol, new_op_symbol, 1)

        metadata = {
            "line_label": line_map.get(target_node.lineno),
            "original_op": original_op_node.__class__.__name__,
            # Use the new variable to get the name of the chosen operator
            "new_op": new_op_node_type.__name__
        }
        
        return "\n".join(lines), metadata

    def inject_computational_error(self, source_code: str) -> Optional[Tuple[str, Dict[str, Any]]]:
        """Replaces an assignment's result with a perturbed value."""
        tree = ast.parse(source_code)
        lines = source_code.splitlines()
        line_map = self._map_lines_to_labels(lines)
        func_def = tree.body[0]
        
        candidates = [
            node for node in ast.walk(func_def)
            if isinstance(node, ast.Assign) and
            # Exclude assignments to the final 'answer' variable
            (isinstance(node.targets[0], ast.Name) and node.targets[0].id != 'answer')
        ]
        if not candidates:
            return None

        env = self._get_default_args(func_def)
        random.shuffle(candidates)

        for target_node in candidates:
            temp_env = env.copy()
            successful_exec = True
            for stmt in func_def.body:
                if stmt.lineno >= target_node.lineno: break
                try: exec(ast.unparse(stmt), globals(), temp_env)
                except Exception: successful_exec = False; break
            if not successful_exec: continue

            try:
                original_value = eval(ast.unparse(target_node.value), globals(), temp_env)
                if not isinstance(original_value, (int, float)): continue
            except Exception: continue
            
            perturbed_value = original_value + random.choice([-10, -1, 1, 10])
            if perturbed_value == original_value: perturbed_value += 1

            # Create a modified copy of the node to unparse
            modified_node = ast.Assign(targets=target_node.targets, value=ast.Constant(value=perturbed_value))
            
            ### FIX ###
            # Copy line number and other location data from the original node.
            ast.copy_location(modified_node, target_node)

            new_line_code = ast.unparse(modified_node)

            line_idx = target_node.lineno - 1
            indentation = re.match(r"^\s*", lines[line_idx]).group(0)
            lines[line_idx] = indentation + new_line_code
            
            metadata = {
                "line_label": line_map.get(target_node.lineno),
                "original_value": original_value,
                "new_value": perturbed_value
            }
            return "\n".join(lines), metadata
            
        return None

    def inject_incorrect_operand(self, source_code: str) -> Optional[Tuple[str, Dict[str, Any]]]:
        """
        Replaces a variable in an expression with another variable from the correct
        scope using `re.sub`. Ensures replacement vars are defined before use.
        """
        tree = ast.parse(source_code)
        lines = source_code.splitlines()
        line_map = self._map_lines_to_labels(lines)
        func_def = tree.body[0]

        # Find all variables used as operands in binary operations
        candidates = []
        for node in ast.walk(tree):
            if isinstance(node, ast.BinOp):
                for operand in [node.left, node.right]:
                    if isinstance(operand, ast.Name):
                        candidates.append(operand)
        
        if not candidates: return None

        # Shuffle candidates to ensure random selection on different runs
        random.shuffle(candidates)

        for target_node in candidates:
            # For each candidate, determine the variables in scope AT THAT LINE
            available_vars = self._get_vars_in_scope_at_line(func_def, target_node.lineno)
            
            original_operand = target_node.id
            
            # The replacement must be a different variable that is already in scope
            possible_replacements = list(available_vars - {original_operand})
            
            if not possible_replacements:
                continue # No valid variable to swap with at this location

            new_operand = random.choice(possible_replacements)
            line_idx = target_node.lineno - 1
            line_content = lines[line_idx]

            # Use regex with word boundaries to avoid partial matches
            # We replace only the first occurrence on a line to be conservative
            new_line_content, num_subs = re.subn(
                r'\b' + re.escape(original_operand) + r'\b',
                new_operand,
                line_content,
                count=1
            )

            if num_subs > 0:
                lines[line_idx] = new_line_content
                metadata = {
                    "line_label": line_map.get(target_node.lineno),
                    "original_operand": original_operand,
                    "new_operand": new_operand
                }
                return "\n".join(lines), metadata

        # If loop finishes without finding any valid swap
        return None

    def inject_skipped_step(self, source_code: str) -> Optional[Tuple[str, Dict[str, Any]]]:
        """Deletes an assignment and patches subsequent uses of the variable."""
        tree = ast.parse(source_code)
        lines = source_code.splitlines()
        line_map = self._map_lines_to_labels(lines)
        func_def = tree.body[0]

        candidates = []
        for node in func_def.body:
            if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                # Exclude assignments to the final 'answer' variable
                if node.targets[0].id != 'answer':
                    candidates.append(node)
        
        if not candidates: return None
            
        target_node = random.choice(candidates)
        deleted_var_name = target_node.targets[0].id
        line_idx_to_delete = target_node.lineno - 1

        scope_vars = self._get_scope_vars(func_def, args_only=True)
        replacement_pool = list(scope_vars - {deleted_var_name})
        if not replacement_pool:
             replacement_pool = list(self._get_scope_vars(func_def) - {deleted_var_name})
        if not replacement_pool: return None
        replacement_var_name = random.choice(replacement_pool)

        # Patch subsequent lines
        for i in range(line_idx_to_delete + 1, len(lines)):
            lines[i] = re.sub(r'\b' + re.escape(deleted_var_name) + r'\b', replacement_var_name, lines[i])

        # Delete the target line
        del lines[line_idx_to_delete]

        metadata = {
            "line_label": line_map.get(target_node.lineno),
            "deleted_variable": deleted_var_name,
            "replacement_variable": replacement_var_name
        }

        return "\n".join(lines), metadata

    # --------------------------------------------------------------------------
    # Helper classes and methods
    # --------------------------------------------------------------------------
    
    def _get_vars_in_scope_at_line(self, func_def: ast.FunctionDef, line_number: int) -> set:
        """
        Returns a set of variable names that are in scope (defined) at the
        beginning of a specific line number.
        """
        # Arguments are always in scope
        scope_vars = {arg.arg for arg in func_def.args.args}
        
        # Add variables defined in lines prior to the target line
        for stmt in func_def.body:
            if stmt.lineno >= line_number:
                break
            if isinstance(stmt, ast.Assign):
                for target in stmt.targets:
                    if isinstance(target, ast.Name):
                        scope_vars.add(target.id)
        return scope_vars

    def _map_lines_to_labels(self, lines: List[str]) -> Dict[int, str]:
        """Creates a map from 1-based line number to its logical step label (e.g., 'L1')."""
        mapping = {}
        current_label = None
        label_re = re.compile(r"^\s*#:\s*(L\d+|FA)\s*")
        for i, line in enumerate(lines, 1):
            match = label_re.match(line)
            if match:
                current_label = match.group(1)
            if current_label:
                mapping[i] = current_label
        return mapping
        
    def _get_default_args(self, func_def: ast.FunctionDef) -> Dict[str, Any]:
        """Extracts a dictionary of arguments and their default values."""
        env = {}
        # This is a simplified eval; robust parsing would require ast.literal_eval
        # but the formatted code should be safe.
        for arg, default in zip(func_def.args.args[::-1], func_def.args.defaults[::-1]):
            try:
                env[arg.arg] = eval(ast.unparse(default))
            except:
                # Fallback for complex defaults that can't be easily eval'd
                env[arg.arg] = None 
        return env
        
    def _get_scope_vars(self, func_def: ast.FunctionDef, args_only=False) -> set:
        """Returns a set of all variable names in the function's scope."""
        scope_vars = {arg.arg for arg in func_def.args.args}
        if not args_only:
            for node in func_def.body:
                if isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            scope_vars.add(target.id)
        return scope_vars
    

# ==============================================================================
# Function to test and debug error injection
# ==============================================================================

import traceback
import hashlib

def test_and_inject_error(
    problem_index: int,
    error_type: str,
    base_input_dir: Path = BASE_INPUT_DIR,
    base_output_dir: Path = BASE_OUTPUT_DIR,
    save_output: bool = True,
    master_seed: Optional[int] = 42  # Add master_seed parameter
):
    """
    Loads formatted code files, injects a specified error with a deterministic seed,
    prints the results, and saves the modified code.
    """
    results = {}
    for model_name in MODELS:
        input_file = base_input_dir / str(problem_index) / f"{model_name}.py"
        
        try:
            source_code = input_file.read_text(encoding="utf-8")
            print(f"--- Loaded Source File: {input_file} ---")
        except FileNotFoundError:
            print(f"❌ ERROR: Source file not found at {input_file}")
            continue  # Use continue to proceed to the next model
        except Exception as e:
            print(f"❌ ERROR: Failed to read source file {input_file}")
            traceback.print_exc()
            continue

        # --- SEED GENERATION BLOCK ---
        file_seed = None
        if master_seed is not None:
            # Create a deterministic seed unique to this file and error type
            seed_str = f"{master_seed}_{problem_index}_{model_name}_{error_type}"
            # Use a hash to convert the unique string into a consistent integer seed
            seed_hash = hashlib.sha256(seed_str.encode()).hexdigest()
            file_seed = int(seed_hash, 16) % (2**32) # Ensure seed is within valid range

        try:
            injector = ErrorInjector()
            # Pass the generated seed to the inject method
            result = injector.inject(source_code, error_type, seed=file_seed)
        except Exception as e:
            print(f"❌ ERROR: The ErrorInjector failed for '{model_name}'.")
            traceback.print_exc()
            continue

        if result is None:
            print(f"\n--- ⚠️ Injection Failed for {model_name} ---")
            continue

        modified_code, metadata = result
        
        print(f"\n--- ✅ Injected '{error_type}' Error into {model_name} ---")
        print("METADATA:", metadata)
        # To aid debugging, print the seed that was used
        if file_seed is not None:
            print(f"SEED USED: {file_seed}")
        print("\n--- MODIFIED CODE ---")
        print(modified_code)

        results[model_name] = (modified_code, metadata)

        if save_output:
            output_dir = base_output_dir / error_type / str(problem_index)
            output_dir.mkdir(parents=True, exist_ok=True)
            output_file = output_dir / f"{model_name}.py"
            try:
                output_file.write_text(modified_code, encoding="utf-8")
                print(f"\n✓ Saved modified code to {output_file}")
            except Exception as e:
                print(f"❌ ERROR: Failed to write output file to {output_file}")
                traceback.print_exc()

    return results