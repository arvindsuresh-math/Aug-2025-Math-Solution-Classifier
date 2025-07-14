# Conceptual Error Candidate Generation

This notebook contains the end-to-end pipeline for generating conceptual error "candidates" from validated `Formalization Templates`. The process involves programmatically applying logical mutations to the Abstract Syntax Tree (AST) of the correct `function_code`, executing the mutated code to generate a flawed numerical trace, and then packaging all relevant information for a human-in-the-loop validation and annotation stage.

## Cell 1: Imports and setup


```python
# --- Imports and Path Definitions ---

import json
import re
import ast
import inspect
import importlib.util
from pathlib import Path
from types import ModuleType
from typing import Callable, Any, Dict, List
from fractions import Fraction as BuiltinFraction
import copy

import pandas as pd
from tqdm.notebook import tqdm
from datasets import load_dataset, Dataset

def find_project_root(marker: str = ".git") -> Path:
    """Traverse upwards to find the project root, marked by the git repository."""
    current_path = Path.cwd().resolve()
    while current_path != current_path.parent:
        if (current_path / marker).exists():
            return current_path
        current_path = current_path.parent
    raise FileNotFoundError(f"Could not find project root. Marker '{marker}' not found.")

PROJECT_ROOT = find_project_root()
DATA_DIR = PROJECT_ROOT / 'data'

# --- Directory Paths ---
PROCESSED_TEMPLATE_DIR = DATA_DIR / "template-generated-processed"
CONCEPTUAL_CANDIDATES_DIR = DATA_DIR / "conceptual-error-candidates"

# --- Models ---
MODELS = ['openai_gpt-4.1', 'google_gemini-2.5-flash']

print(f"Project root: {PROJECT_ROOT}")
print(f"Input (Processed Templates): {PROCESSED_TEMPLATE_DIR}")
print(f"Output (Conceptual Candidates): {CONCEPTUAL_CANDIDATES_DIR}")

# --- Ensure Directories Exist ---
PROCESSED_TEMPLATE_DIR.mkdir(parents=True, exist_ok=True)
CONCEPTUAL_CANDIDATES_DIR.mkdir(parents=True, exist_ok=True)
```

    Project root: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math
    Input (Processed Templates): /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/template-generated-processed
    Output (Conceptual Candidates): /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/conceptual-error-candidates


## Cell 2: Load Dataset and Tiers

This cell loads the GSM8K dataset, which is used to access the original problem text and solution for context. It also defines and applies the tiering system to categorize problems, which helps in organizing the processing flow.


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


## Cell 3: Template Loading Utilities

These functions handle loading the two key components of a validated `Formalization Template` from disk: the `function_code` from the `.py` file and the `logical_steps` from the `.json` file.


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


## Cell 4: Core AST and Trace Utilities

This cell contains the foundational utilities for AST manipulation and execution.

1.  `_execute_ast_statements`: A low-level helper that executes a list of assignment statements and returns the resulting variable scope.
2.  `execution_trace`: Gets a complete trace of all variables at the end of a function's execution.
3.  `get_scope_at_node`: Executes a function only *up to* a specified node, returning the variable scope at that point.
4.  `apply_mutation`: The core mutation engine. It takes a function and a `mutation_details` dictionary, applies the logical mutation to a copy of the AST, and then returns both the mutated code as a string and the resulting `flawed_trace`.


```python
class NonSimplifyingFraction(BuiltinFraction):
    """A subclass of fractions.Fraction that preserves original representation for printing."""
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

def _execute_ast_statements(stmts: List[ast.stmt]) -> Dict[str, Any] | None:
    """Executes a list of AST assignment statements and returns the final local environment."""
    try:
        global_namespace = {'Fraction': NonSimplifyingFraction}
        local_env = {}
        for stmt in stmts:
            if isinstance(stmt, ast.Assign):
                module_node = ast.Module([stmt], type_ignores=[])
                code_obj = compile(module_node, '<string>', 'exec')
                exec(code_obj, global_namespace, local_env)
        return local_env
    except Exception:
        return None

def execution_trace(func: Callable[[], Any]) -> dict[str, Any] | None:
    """Executes a function's source code line by line to build a full variable trace."""
    try:
        src = inspect.getsource(func)
        tree = ast.parse(src)
        func_def = tree.body[0]
        if not isinstance(func_def, ast.FunctionDef): return None
        return _execute_ast_statements(func_def.body)
    except (FileNotFoundError, TypeError, IndexError):
        return None

def get_scope_at_node(func: Callable, target_assign_node: ast.Assign) -> Dict[str, Any] | None:
    """Executes a function's AST up to a specific node to get the current variable scope."""
    try:
        src = inspect.getsource(func)
        tree = ast.parse(src)
        func_def = tree.body[0]
        if not isinstance(func_def, ast.FunctionDef): return None

        statements_before = []
        for stmt in func_def.body:
            if isinstance(stmt, ast.Assign) and stmt.lineno == target_assign_node.lineno:
                return _execute_ast_statements(statements_before)
            statements_before.append(stmt)
        return None
    except (FileNotFoundError, TypeError, IndexError):
        return None

def is_plausible_trace(correct_trace: dict, flawed_trace: dict) -> bool:
    """Validates a flawed trace against a correct one for type, sign, and zero-value integrity."""
    for key, correct_val in correct_trace.items():
        if not isinstance(correct_val, (int, float, BuiltinFraction)): continue
        flawed_val = flawed_trace.get(key)
        if flawed_val is None or not isinstance(flawed_val, (int, float, BuiltinFraction)): # FIX: Handle non-numeric flawed values
            continue
        is_correct_int_like = isinstance(correct_val, int) or (isinstance(correct_val, float) and correct_val.is_integer())
        is_flawed_int_like = isinstance(flawed_val, int) or (isinstance(flawed_val, float) and flawed_val.is_integer())
        if is_correct_int_like and not is_flawed_int_like: 
            return False
        correct_sign = 1 if correct_val > 0 else -1 if correct_val < 0 else 0
        flawed_sign = 1 if flawed_val > 0 else -1 if flawed_val < 0 else 0
        if correct_sign != 0 and correct_sign != flawed_sign: 
            return False
        if correct_val != 0 and flawed_val == 0: 
            return False
    return True

def apply_mutation(func: Callable, mutation_details: Dict[str, Any]) -> tuple[str | None, Dict[str, Any] | None]:
    """Applies a single logical mutation to a function's AST and returns the mutated code and trace."""
    try:
        src = inspect.getsource(func)
        tree = ast.parse(src)
        
        class ASTMutator(ast.NodeTransformer):
            def __init__(self, details):
                self.details = details
                self.mutation_applied = False
            def visit_Assign(self, node):
                if isinstance(node.targets[0], ast.Name) and node.targets[0].id == self.details['target_variable']:
                    mutation_type = self.details['type']
                    if mutation_type == 'operator_swap' and isinstance(node.value, ast.BinOp):
                        node.value.op = self.details['new_op']
                        self.mutation_applied = True
                    elif mutation_type in ['incorrect_operand', 'input_misrepresentation', 'skipped_step']:
                        class OperandSwapper(ast.NodeTransformer):
                            def __init__(self, to_replace, new_name):
                                self.to_replace = to_replace
                                self.new_name = new_name
                            def visit_Name(self, name_node):
                                if name_node.id == self.to_replace: return ast.Name(id=self.new_name, ctx=name_node.ctx)
                                return name_node
                        swapper = OperandSwapper(self.details['operand_to_replace'], self.details['replacement_variable'])
                        node.value = swapper.visit(node.value)
                        self.mutation_applied = True
                return node

        mutator = ASTMutator(mutation_details)
        mutated_tree = mutator.visit(copy.deepcopy(tree))
        if not mutator.mutation_applied: return None, None
        
        ast.fix_missing_locations(mutated_tree)
        mutated_code_str = ast.unparse(mutated_tree)
        
        func_def = mutated_tree.body[0]
        flawed_trace = _execute_ast_statements(func_def.body) if isinstance(func_def, ast.FunctionDef) else None
        return mutated_code_str, flawed_trace
    except Exception:
        return None, None

print("Core AST and Trace Utilities defined.")
```

    Core AST and Trace Utilities defined.


## Cell 5: Mutation Discovery

This section contains the logic for discovering all valid mutation opportunities within a `function_code`'s AST. The main function `discover_mutation_opportunities` orchestrates calls to specialized helper functions for each error type.


```python
def get_variable_dependencies(node: ast.Assign) -> List[str]:
    """Extracts the names of variables used as operands in an assignment's value."""
    return sorted([n.id for n in ast.walk(node.value) if isinstance(n, ast.Name) and n.id != 'int'])

def _discover_operator_swaps(node: ast.Assign) -> List[Dict[str, Any]]:
    """Finds all valid OperatorSwap mutations, capturing the operand names."""
    if not (isinstance(node.value, ast.BinOp) and hasattr(node.targets[0], 'id') and
            isinstance(node.value.left, ast.Name) and isinstance(node.value.right, ast.Name)):
        return []

    target_variable, original_op_node = node.targets[0].id, node.value.op
    swap_map = {
        ast.Add: [ast.Sub, ast.Mult], ast.Sub: [ast.Add, ast.Div],
        ast.Mult: [ast.Div, ast.Add], ast.Div: [ast.Mult, ast.Sub]
    }
    original_op_type = type(original_op_node)
    mutations = []
    if original_op_type in swap_map:
        for new_op_constructor in swap_map[original_op_type]:
            mutations.append({"type": "operator_swap", "target_variable": target_variable, "original_op_type": original_op_type,
                              "new_op": new_op_constructor(), "left_operand": node.value.left.id, "right_operand": node.value.right.id})
    return mutations

def _discover_plausible_wrong_references(
    func: Callable, node: ast.Assign, all_input_vars: set, debug: bool = False
) -> List[Dict[str, Any]]:
    """Discovers and classifies plausible operand substitution mutations."""
    mutations = []
    if not hasattr(node.targets[0], 'id'): return []
    target_variable = node.targets[0].id
    
    scope = get_scope_at_node(func, node)
    if scope is None: return []

    operands = [n.id for n in ast.walk(node.value) if isinstance(n, ast.Name) and n.id != 'int']
    
    for operand_to_replace in set(operands):
        if operand_to_replace not in scope: continue
        
        for replacement_candidate in scope:
            if replacement_candidate in (operand_to_replace, 'Fraction'): continue
            if isinstance(scope[operand_to_replace], (int, float, BuiltinFraction)) and \
               isinstance(scope.get(replacement_candidate), (int, float, BuiltinFraction)):
                
                mutation_type = "input_misrepresentation" if operand_to_replace in all_input_vars else "incorrect_operand"
                mutations.append({"type": mutation_type, "target_variable": target_variable,
                                  "operand_to_replace": operand_to_replace, "replacement_variable": replacement_candidate})
                
    return [dict(t) for t in {tuple(d.items()) for d in mutations}]

def _discover_omitted_final_steps(node: ast.Assign, dependency_map: Dict[str, List[str]], debug: bool = False) -> List[Dict[str, Any]]:
    """Discovers opportunities to skip the final step by returning an intermediate value."""
    mutations = []
    if not hasattr(node.targets[0], 'id') or node.targets[0].id != 'answer':
        return []

    target_variable = node.targets[0].id
    
    # FIX: Check if the dependency list is empty before accessing an element.
    answer_dependencies = dependency_map.get(target_variable, [])
    if not answer_dependencies:
        return [] # This happens if answer is assigned a constant, e.g., answer = 0
        
    correct_final_var = answer_dependencies[0]

    if debug:
        print(f"\n[DEBUG SS] Target: {target_variable}")
        print(f"  > Correct final operand: {correct_final_var}")

    for var_name in dependency_map.keys():
        if var_name not in ['answer', correct_final_var] and dependency_map.get(var_name):
            if debug:
                print(f"    * SUCCESS: Found Omitted Final Step. Swapping '{correct_final_var}' with '{var_name}'")
            mutations.append({"type": "skipped_step", "target_variable": target_variable,
                              "operand_to_replace": correct_final_var, "replacement_variable": var_name})
            
    return mutations

def discover_mutation_opportunities(
    func: Callable, logical_steps: list, correct_trace: dict, debug_mode: bool = False
) -> list:
    """Analyzes a function's AST to find all possible conceptual error mutations."""
    all_mutations = []
    try:
        src = inspect.getsource(func)
        tree = ast.parse(src)
        func_def = tree.body[0]
        if not isinstance(func_def, ast.FunctionDef): return []
    except (FileNotFoundError, TypeError, IndexError): return []

    assign_nodes = [node for node in func_def.body if isinstance(node, ast.Assign)]
    
    all_input_vars = set(v for s in logical_steps for k in ('question_inputs', 'WK_inputs') for v in s.get(k, []))
    dependency_map = {node.targets[0].id: get_variable_dependencies(node) 
                      for node in assign_nodes if hasattr(node.targets[0], 'id')}

    for node in assign_nodes:
        all_mutations.extend(_discover_operator_swaps(node))
        all_mutations.extend(_discover_plausible_wrong_references(func, node, all_input_vars, debug=debug_mode))
        all_mutations.extend(_discover_omitted_final_steps(node, dependency_map, debug=debug_mode))
        
    return [dict(t) for t in {tuple(d.items()) for d in all_mutations}]

print("Mutation Discovery functions defined.")
```

    Mutation Discovery functions defined.


## Cell 6: Candidate Generation and Reconstruction

This section contains the logic for orchestrating the generation pipeline and reconstructing the natural language solutions from the flawed numerical traces.


```python
class FormattingTrace(dict):
    """A dictionary subclass that formats numbers for clean reconstruction."""
    def __getitem__(self, key):
        val = super().__getitem__(key)
        if isinstance(val, float) and val.is_integer():
            return str(int(val))
        if isinstance(val, float):
            return str(round(val, 2))
        return str(val)
    
def _cap_candidates(candidates: List[Dict]) -> List[Dict]:
    """
    Applies constraints to the list of generated candidates to ensure variety.
    
    Constraints:
    1. No more than 2 of any individual mutation type per sample.
    2. No more than 2 errors targeting any individual line per sample.
    3. No more than 5 errors in total per sample.
    """
    from collections import Counter
    
    # Apply type and line constraints
    type_counts = Counter()
    line_counts = Counter()
    
    filtered_candidates = []
    for cand in candidates:
        m_type = cand['mutation_details']['type']
        err_line = cand['erroneous_line_number']
        
        type_counts[m_type] += 1
        line_counts[err_line] += 1
        
        if type_counts[m_type] <= 2 and line_counts[err_line] <= 2:
            filtered_candidates.append(cand)
            
    # Apply total constraint, prioritizing a mix of types if possible
    if len(filtered_candidates) > 5:
        # A simple shuffle and truncate is a good heuristic to get a mix.
        import random
        random.seed(42) # for reproducibility
        random.shuffle(filtered_candidates)
        return filtered_candidates[:5]
        
    return filtered_candidates

def _generate_explanation(mutation: dict, correct_trace: dict) -> str:
    """Generates a human-readable explanation for a given mutation."""
    m_type = mutation['type']
    
    if m_type == 'operator_swap':
        op_map = {ast.Add: '+', ast.Sub: '-', ast.Mult: '*', ast.Div: '/'}
        original_op_str, new_op_str = op_map.get(mutation['original_op_type'], '?'), op_map.get(type(mutation['new_op']), '?')
        return f"Incorrect operation. The calculation should use '{original_op_str}' but used '{new_op_str}' instead."
    
    elif m_type == 'incorrect_operand':
        replacement_var, original_var = mutation['replacement_variable'], mutation['operand_to_replace']
        replacement_val, original_val = correct_trace.get(replacement_var, 'N/A'), correct_trace.get(original_var, 'N/A')
        return (f"Incorrect operand. The variable '{replacement_var}' (value: {replacement_val}) was used "
                f"instead of the correct variable '{original_var}' (value: {original_val}).")

    elif m_type == 'input_misrepresentation':
        replacement_var, original_var = mutation['replacement_variable'], mutation['operand_to_replace']
        replacement_val, original_val = correct_trace.get(replacement_var, 'N/A'), correct_trace.get(original_var, 'N/A')
        return (f"Input misrepresentation. The value for '{replacement_var}' ({replacement_val}) was used "
                f"instead of the correct input value for '{original_var}' ({original_val}).")

    elif m_type == 'skipped_step':
        return (f"Skipped final step. An intermediate value ('{mutation['replacement_variable']}') was returned "
                f"instead of the correct final answer ('{mutation['operand_to_replace']}').")
    
    return "An unknown conceptual error occurred."

def _get_mutated_template(original_template: str, mutation: dict) -> str:
    """Modifies a template string using a context-aware regex to handle intervening text."""
    mutation_type = mutation['type']

    if mutation_type == 'operator_swap':
        op_map = {ast.Add: '+', ast.Sub: '-', ast.Mult: '*', ast.Div: '/'}
        original_op_str, new_op_str = op_map.get(mutation['original_op_type']), op_map.get(type(mutation['new_op']))
        left_ph, right_ph = f"{{{mutation['left_operand']}}}", f"{{{mutation['right_operand']}}}"
        if not (original_op_str and new_op_str): return original_template

        patterns = [
            re.compile(f"({re.escape(left_ph)})(.*?)({re.escape(original_op_str)})(.*?)({re.escape(right_ph)})"),
            re.compile(f"({re.escape(right_ph)})(.*?)({re.escape(original_op_str)})(.*?)({re.escape(left_ph)})")
        ]
        
        mutated_template = original_template
        for pattern in patterns:
            mutated_template = pattern.sub(f"\\1\\2{new_op_str}\\4\\5", mutated_template)
        return mutated_template

    elif mutation_type in ['incorrect_operand', 'input_misrepresentation', 'skipped_step']:
        to_replace_ph, new_name_ph = f"{{{mutation['operand_to_replace']}}}", f"{{{mutation['replacement_variable']}}}"
        return original_template.replace(to_replace_ph, new_name_ph)
        
    return original_template

def reconstruct_solution_from_trace(logical_steps: list[dict], eval_trace: dict[str, Any], candidate_mutation: dict | None = None) -> dict[str, str] | None:
    """Reconstructs NL solution lines, using a mutated template and custom formatting."""
    formatted_trace = FormattingTrace(eval_trace)
    reconstructed_mapping = {}
    mutated_ln = None
    if candidate_mutation:
        mutated_var = candidate_mutation['target_variable']
        for step in logical_steps:
            if step.get("output_variable") == mutated_var:
                mutated_ln = step.get("line_number")
                break
    for step in logical_steps:
        ln, template = step.get("line_number"), step.get("solution_line_template")
        if not (ln and template): continue
        if ln == mutated_ln and candidate_mutation:
            template = _get_mutated_template(template, candidate_mutation)
        try:
            reconstructed_mapping[ln] = template.format_map(formatted_trace)
        except (KeyError, ValueError):
            return None
    return reconstructed_mapping

def generate_candidates_for_template(
    func: Callable, logical_steps: list, correct_trace: dict, index: int, debug_mode: bool = False
) -> list[dict]:
    """Orchestrates the generation of all possible conceptual error candidates."""
    mutations = discover_mutation_opportunities(func, logical_steps, correct_trace, debug_mode=debug_mode)
    candidates = []
    original_code = inspect.getsource(func)

    for mutation in mutations:
        if mutation['target_variable'] == 'answer' and mutation['type'] != 'skipped_step':
            continue

        mutated_code, flawed_trace = apply_mutation(func, mutation)
        if not flawed_trace or not is_plausible_trace(correct_trace, flawed_trace): continue
        
        correct_answer, flawed_answer = correct_trace.get('answer'), flawed_trace.get('answer')
        norm_correct = str(float(correct_answer)) if isinstance(correct_answer, (int, float)) else str(correct_answer)
        norm_flawed = str(float(flawed_answer)) if isinstance(flawed_answer, (int, float)) else str(flawed_answer)
        if correct_answer is None or flawed_answer is None or norm_correct == norm_flawed: continue

        flawed_nl_reconstruction = reconstruct_solution_from_trace(logical_steps, flawed_trace, candidate_mutation=mutation)
        if not flawed_nl_reconstruction: continue
            
        # --- FIX: Intelligent Erroneous Line Number Assignment ---
        if mutation['target_variable'] == 'answer':
            # For answer-level mutations, the error is on the last logical step.
            erroneous_line_number = logical_steps[-1]['line_number'] if logical_steps else None
        else:
            # For other mutations, find the line where the variable was calculated.
            erroneous_line_number = next((s['line_number'] for s in logical_steps if s.get('output_variable') == mutation['target_variable']), None)

        candidate_package = {
            "index": index,
            "original_function_code": original_code,
            "mutation_details": mutation,
            "correct_trace": correct_trace,
            "flawed_trace": flawed_trace,
            "logical_steps": logical_steps,
            "flawed_nl_reconstruction": flawed_nl_reconstruction,
            "erroneous_line_number": erroneous_line_number,
            "explanation": _generate_explanation(mutation, correct_trace)
        }
        candidates.append(candidate_package)
        
    return _cap_candidates(candidates)
```

## Cell 7: Main Driver

This is the main execution block. It iterates through a small, targeted set of test indices, loads each template, and passes it to the `generate_candidates_for_template` orchestrator. It then prints the results for direct inspection and debugging.


```python
def process_single_index(index_info: tuple, model_preference: list) -> List[Dict]:
    """
    Worker function to process a single problem index. Returns candidates with model_name.
    """
    tier, index = index_info
    
    for model_name in model_preference:
        solve_module = load_function_module(tier, index, model_name)
        logical_steps = load_logical_steps(tier, index, model_name)
        
        if solve_module and logical_steps:
            solve_function = solve_module.solve
            correct_trace = execution_trace(solve_function)
            if not correct_trace:
                continue
            
            candidates = generate_candidates_for_template(
                solve_function, logical_steps, correct_trace, index
            )
            
            if candidates:
                # Add the successful model_name to each candidate package for later use.
                for cand in candidates:
                    cand['model_name'] = model_name
                return candidates
            
    return []

def save_candidates_and_get_metadata(tier: str, index: int, model_name: str, candidates: List[Dict]) -> List[Dict]:
    """Saves candidate packages to JSON files and returns a list of metadata records."""
    output_dir = CONCEPTUAL_CANDIDATES_DIR / tier / str(index)
    output_dir.mkdir(parents=True, exist_ok=True)
    metadata_records = []
    
    for cand in candidates:
        mutation = cand['mutation_details']
        m_type = mutation['type']
        target_var = mutation['target_variable']
        
        # Use a more descriptive filename including the error type
        filename = f"{model_name}_{m_type}_{target_var}.json"
        filepath = output_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(cand, f, indent=2, default=str)
        
        record = {
            "index": index, "tier": tier, "model": model_name,
            "mutation_type": m_type, "target_variable": target_var,
            "mutation_details": json.dumps(mutation, default=str),
            "filepath": str(filepath.relative_to(PROJECT_ROOT))
        }
        metadata_records.append(record)
        
    return metadata_records

from joblib import Parallel, delayed

def run_candidate_generation_pipeline_parallel():
    """Drives the conceptual error candidate generation pipeline in parallel using joblib."""
    print("--- Starting Conceptual Error Candidate Generation (PARALLEL MODE) ---")
    
    model_preference = ['google_gemini-2.5-flash', 'openai_gpt-4.1']
    tasks = []
    for tier, indices in TIER_LISTS.items():
        for index in indices:
            if 0 <= index <= 3000:
                tasks.append((tier, index))
    
    print(f"Prepared {len(tasks)} indices for processing across all available CPU cores.")

    results_list = Parallel(n_jobs=-1)(
        delayed(process_single_index)(task, model_preference) 
        for task in tqdm(tasks, desc="Processing Indices")
    )

    print("\n--- Parallel processing complete. Saving artifacts... ---")
    
    all_candidates = [candidate for sublist in results_list if sublist for candidate in sublist]
    all_candidate_metadata = []

    if not all_candidates:
        print("No valid conceptual error candidates were generated.")
        return

    for cand in tqdm(all_candidates, desc="Saving Candidates"):
        mutation, index, model_name = cand['mutation_details'], cand['index'], cand['model_name']
        m_type, target_var = mutation['type'], mutation['target_variable']
        tier = next((t for t, ids in TIER_LISTS.items() if index in ids), 'unknown')

        output_dir = CONCEPTUAL_CANDIDATES_DIR / tier / str(index)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Use a unique identifier to prevent overwrites
        replacement_var = mutation.get('replacement_variable', '')
        filename = f"{model_name}_{m_type}_{target_var}_{replacement_var}.json"
        filepath = output_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(cand, f, indent=2, default=str)
        
        record = {"index": index, "tier": tier, "model": model_name, "mutation_type": m_type, 
                  "target_variable": target_var, "mutation_details": json.dumps(mutation, default=str),
                  "filepath": str(filepath.relative_to(PROJECT_ROOT))}
        all_candidate_metadata.append(record)

    if all_candidate_metadata:
        catalog_df = pd.DataFrame(all_candidate_metadata)
        cols = ['index', 'tier', 'model', 'mutation_type', 'target_variable', 'mutation_details', 'filepath']
        catalog_df = catalog_df.reindex(columns=[c for c in cols if c in catalog_df.columns])
        catalog_path = CONCEPTUAL_CANDIDATES_DIR / "conceptual_candidate_catalog.csv"
        catalog_df.to_csv(catalog_path, index=False)
        print(f"\n--- Pipeline Complete ---")
        print(f"Generated and saved {len(all_candidate_metadata)} conceptual error candidates.")
        print(f"Catalog saved to: {catalog_path}")

print("Parallel Main Driver defined.")

# def run_candidate_generation_pipeline():
#     """
#     Drives the conceptual error candidate generation pipeline with model fallback logic.
#     """
#     print("--- Starting Conceptual Error Candidate Generation ---")
#     all_candidate_metadata = []
    
#     model_preference = ['google_gemini-2.5-flash', 'openai_gpt-4.1']
    
#     # Define the range of indices to process
#     indices_to_process = range(0, 3001)

#     for index in tqdm(indices_to_process, desc="Processing Indices"):
#         # Find the tier for the current index
#         tier = next((t for t, ids in TIER_LISTS.items() if index in ids), None)
#         if not tier:
#             continue

#         # Try to load a template using the model preference order
#         loaded_template = False
#         for model_name in model_preference:
#             solve_module = load_function_module(tier, index, model_name)
#             logical_steps = load_logical_steps(tier, index, model_name)
            
#             if solve_module and logical_steps:
#                 solve_function = solve_module.solve
#                 correct_trace = execution_trace(solve_function)
#                 if not correct_trace:
#                     continue
                
#                 # Successfully loaded and traced a template, now generate candidates
#                 candidates = generate_candidates_for_template(
#                     solve_function, logical_steps, correct_trace, index
#                 )
                
#                 if candidates:
#                     records = save_candidates_and_get_metadata(tier, index, model_name, candidates)
#                     all_candidate_metadata.extend(records)
                
#                 loaded_template = True
#                 break # Stop trying models once one succeeds
        
#         if not loaded_template:
#             # Optional: Log indices for which no valid template was found
#             pass

#     # Save the final master catalog
#     if all_candidate_metadata:
#         catalog_df = pd.DataFrame(all_candidate_metadata)
#         cols = ['index', 'tier', 'model', 'mutation_type', 'target_variable', 'mutation_details', 'filepath']
#         catalog_df = catalog_df.reindex(columns=[c for c in cols if c in catalog_df.columns])
        
#         catalog_path = CONCEPTUAL_CANDIDATES_DIR / "conceptual_candidate_catalog.csv"
#         catalog_df.to_csv(catalog_path, index=False)
        
#         print(f"\n--- Pipeline Complete ---")
#         print(f"Generated {len(catalog_df)} conceptual error candidates.")
#         print(f"Catalog saved to: {catalog_path}")
#     else:
#         print("\n--- Pipeline Complete ---")
#         print("No valid conceptual error candidates were generated.")


# print("Main Driver and Artifact Saving functions defined.")
```

    Parallel Main Driver defined.


## Cell 8: Execute Pipeline

This final cell executes the main driver function to run the entire test pipeline.


```python
run_candidate_generation_pipeline_parallel()
```

    --- Starting Conceptual Error Candidate Generation (PARALLEL MODE) ---
    Prepared 3001 indices for processing across all available CPU cores.



    Processing Indices:   0%|          | 0/3001 [00:00<?, ?it/s]



    ---------------------------------------------------------------------------

    _RemoteTraceback                          Traceback (most recent call last)

    _RemoteTraceback: 
    """
    Traceback (most recent call last):
      File "/opt/miniconda3/envs/erdos-dl/lib/python3.12/site-packages/joblib/externals/loky/process_executor.py", line 490, in _process_worker
        r = call_item()
            ^^^^^^^^^^^
      File "/opt/miniconda3/envs/erdos-dl/lib/python3.12/site-packages/joblib/externals/loky/process_executor.py", line 291, in __call__
        return self.fn(*self.args, **self.kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/opt/miniconda3/envs/erdos-dl/lib/python3.12/site-packages/joblib/parallel.py", line 607, in __call__
        return [func(*args, **kwargs) for func, args, kwargs in self.items]
                ^^^^^^^^^^^^^^^^^^^^^
      File "/var/folders/yk/x70ww_h95d3fgd5spjp1s0780000gn/T/ipykernel_14041/3839294663.py", line 17, in process_single_index
      File "/var/folders/yk/x70ww_h95d3fgd5spjp1s0780000gn/T/ipykernel_14041/1117982106.py", line 142, in generate_candidates_for_template
      File "/var/folders/yk/x70ww_h95d3fgd5spjp1s0780000gn/T/ipykernel_14041/1117982106.py", line 117, in reconstruct_solution_from_trace
    AttributeError: 'str' object has no attribute 'numerator'
    """

    
    The above exception was the direct cause of the following exception:


    AttributeError                            Traceback (most recent call last)

    Cell In[24], line 1
    ----> 1 run_candidate_generation_pipeline_parallel()


    Cell In[23], line 72, in run_candidate_generation_pipeline_parallel()
         68             tasks.append((tier, index))
         70 print(f"Prepared {len(tasks)} indices for processing across all available CPU cores.")
    ---> 72 results_list = Parallel(n_jobs=-1)(
         73     delayed(process_single_index)(task, model_preference) 
         74     for task in tqdm(tasks, desc="Processing Indices")
         75 )
         77 print("\n--- Parallel processing complete. Saving artifacts... ---")
         79 all_candidates = [candidate for sublist in results_list if sublist for candidate in sublist]


    File /opt/miniconda3/envs/erdos-dl/lib/python3.12/site-packages/joblib/parallel.py:2072, in Parallel.__call__(self, iterable)
       2066 # The first item from the output is blank, but it makes the interpreter
       2067 # progress until it enters the Try/Except block of the generator and
       2068 # reaches the first `yield` statement. This starts the asynchronous
       2069 # dispatch of the tasks to the workers.
       2070 next(output)
    -> 2072 return output if self.return_generator else list(output)


    File /opt/miniconda3/envs/erdos-dl/lib/python3.12/site-packages/joblib/parallel.py:1682, in Parallel._get_outputs(self, iterator, pre_dispatch)
       1679     yield
       1681     with self._backend.retrieval_context():
    -> 1682         yield from self._retrieve()
       1684 except GeneratorExit:
       1685     # The generator has been garbage collected before being fully
       1686     # consumed. This aborts the remaining tasks if possible and warn
       1687     # the user if necessary.
       1688     self._exception = True


    File /opt/miniconda3/envs/erdos-dl/lib/python3.12/site-packages/joblib/parallel.py:1784, in Parallel._retrieve(self)
       1778 while self._wait_retrieval():
       1779     # If the callback thread of a worker has signaled that its task
       1780     # triggered an exception, or if the retrieval loop has raised an
       1781     # exception (e.g. `GeneratorExit`), exit the loop and surface the
       1782     # worker traceback.
       1783     if self._aborting:
    -> 1784         self._raise_error_fast()
       1785         break
       1787     nb_jobs = len(self._jobs)


    File /opt/miniconda3/envs/erdos-dl/lib/python3.12/site-packages/joblib/parallel.py:1859, in Parallel._raise_error_fast(self)
       1855 # If this error job exists, immediately raise the error by
       1856 # calling get_result. This job might not exists if abort has been
       1857 # called directly or if the generator is gc'ed.
       1858 if error_job is not None:
    -> 1859     error_job.get_result(self.timeout)


    File /opt/miniconda3/envs/erdos-dl/lib/python3.12/site-packages/joblib/parallel.py:758, in BatchCompletionCallBack.get_result(self, timeout)
        752 backend = self.parallel._backend
        754 if backend.supports_retrieve_callback:
        755     # We assume that the result has already been retrieved by the
        756     # callback thread, and is stored internally. It's just waiting to
        757     # be returned.
    --> 758     return self._return_or_raise()
        760 # For other backends, the main thread needs to run the retrieval step.
        761 try:


    File /opt/miniconda3/envs/erdos-dl/lib/python3.12/site-packages/joblib/parallel.py:773, in BatchCompletionCallBack._return_or_raise(self)
        771 try:
        772     if self.status == TASK_ERROR:
    --> 773         raise self._result
        774     return self._result
        775 finally:


    AttributeError: 'str' object has no attribute 'numerator'



```python

```
