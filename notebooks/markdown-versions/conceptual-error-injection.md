# Conceptual Error Candidate Generation

This notebook contains the end-to-end pipeline for generating conceptual error "candidates" from validated `Formalization Templates`. The process involves programmatically applying logical mutations to the Abstract Syntax Tree (AST) of the correct `function_code`, executing the mutated code to generate a flawed numerical trace, and then packaging all relevant information for a human-in-the-loop validation and annotation stage.

#### **Cell 1: Imports and Setup**
*   **Functionality:** Standard project setup.
*   **Logic:**
    *   Imports necessary libraries (`json`, `ast`, `pathlib`, etc.).
    *   Defines a robust `find_project_root` function to make path definitions portable.
    *   Sets up key `Path` objects for input (`PROCESSED_TEMPLATE_DIR`) and output (`CONCEPTUAL_CANDIDATES_DIR`).
    *   Ensures the output directory exists.


```python
# --- Imports and Path Definitions ---

import json
import re
import ast
import inspect
import importlib.util
from pathlib import Path
from types import ModuleType
from typing import Callable, Any, Dict, List, Set
from fractions import Fraction as BuiltinFraction
import copy
import datetime

import pandas as pd
from tqdm.notebook import tqdm
from datasets import load_dataset, Dataset
from joblib import Parallel, delayed

def find_project_root(marker: str = ".git"):
    """
    Traverses the directory structure upwards from the current working directory
    to locate the project's root, which is identified by the presence of a
    specific marker file or directory (e.g., '.git').

    Args:
        marker: The filename or directory name that marks the project root.

    Returns:
        A Path object to the project root directory.
    
    Raises:
        FileNotFoundError: If the project root cannot be found.
    """
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
MODELS = ['google_gemini-2.5-flash', 'openai_gpt-4.1']

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


#### **Cell 2: Load Dataset and Tiers**
*   **Functionality:** Loads the ground-truth dataset and categorizes problems into tiers.
*   **Logic:**
    *   Loads the `gsm8k` training set.
    *   Defines several helper functions (`has_computational_division`, `has_float`, `is_symbolic`) that use regular expressions to classify the solution text of each problem.
    *   `mutually_disjoint_tiers` uses these helpers to partition all problem indices into distinct tiers (e.g., `tier1` for simple integer arithmetic, `tier5` for symbolic algebra). This organizes the data generation process.


```python
# --- Load GSM8K Dataset ---
GSM8K_TRAIN: Dataset = load_dataset("gsm8k", "main")["train"]

# --- Tier Definition Functions ---
def has_computational_division(solution_text: str):
    """Checks if a solution text contains a division operation."""
    pattern = re.compile(r'/\s*\d')
    return bool(pattern.search(solution_text))

def has_float(solution_text: str):
    """Checks if a solution text contains a float value."""
    pattern = re.compile(r'(?<!\d)\.\d+|\d+\.\d+')
    return bool(pattern.search(solution_text))

def is_symbolic(solution_text: str):
    """Checks if a solution text uses symbolic algebra (e.g., 'Let x...')."""
    pattern = re.compile(r'^Let [a-zA-Z] ', re.MULTILINE)
    return bool(pattern.search(solution_text))

def mutually_disjoint_tiers(dataset: Dataset):
    """
    Categorizes all problems in the dataset into mutually disjoint tiers
    based on the mathematical operations present in their solution text.
    """
    tiers = {}
    symbolic_set = {idx for idx, sample in enumerate(dataset) if is_symbolic(sample.get("answer", ""))}
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


#### **Cell 3: Template Loading Utilities**
*   **Functionality:** Provides helper functions to load the validated `Formalization Template` components.
*   **Logic:**
    *   `load_function_module`: Takes a tier, index, and model name. It constructs the path to the `.py` file and uses `importlib.util` to dynamically load the file as a Python module, making its `solve` function accessible.
    *   `load_logical_steps`: Takes the same inputs, constructs the path to the `.json` file, and returns the parsed list of dictionaries representing the solution's logical steps.


```python
def load_function_module(
    tier: str,
    index: int,
    model_name: str
):
    """
    Dynamically loads the 'solve.py' module for a given template using its
    path, which is constructed from the tier, index, and model name.
    """
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

def load_logical_steps(
    tier: str,
    index: int,
    model_name: str
):
    """Loads the 'logical_steps.json' for a given template."""
    json_file_path = PROCESSED_TEMPLATE_DIR / tier / str(index) / f"{model_name}.json"
    try:
        return json.loads(json_file_path.read_text(encoding='utf-8'))
    except (FileNotFoundError, json.JSONDecodeError):
        return None

print("Template loading functions defined.")
```

    Template loading functions defined.


#### **Cell 4: Sanitization and solution mapping**


```python
def sanitize_text(text: str):
    """
    Replaces a comprehensive set of problematic Unicode characters with their
    ASCII equivalents to prevent model generation and string parsing errors.
    """
    replacements = {
        "\u2212": "-", "\u00d7": "*", "\u00f7": "/", "\u22c5": "*",
        "\u201c": '"', "\u201d": '"', "\u2018": "'", "\u2019": "'",
        "\u2014": "-", "\u2013": "-", "\u2026": "...", "\u00a0": " ",
    }
    for uni, ascii_char in replacements.items():
        text = text.replace(uni, ascii_char)
    return text

def build_solution_mapping(index: int):
    """
    Extracts the original natural language solution from the dataset, sanitizes
    it, and structures it into a line-numbered dictionary including the 'FA'
    (Final Answer) line.
    """
    try:
        solution_text = GSM8K_TRAIN[index]["answer"]
        sanitized_text = sanitize_text(solution_text)
        lines = [ln.strip() for ln in sanitized_text.splitlines() if ln.strip()]

        solution_mapping = {}
        if lines and re.match(r"^####\s*[\d\.,]+$", lines[-1]):
            solution_mapping["FA"] = lines.pop(-1).strip()
        
        for i, line in enumerate(lines, 1):
            solution_mapping[f"L{i}"] = line
            
        return solution_mapping
    except IndexError:
        return {}

print("Sanitization and Solution Mapping utilities defined.")
```

    Sanitization and Solution Mapping utilities defined.


#### **Cell 5: Core AST and Trace Utilities**


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

def _execute_ast_statements(stmts: List[ast.stmt]):
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

def execution_trace(func: Callable[[], Any]):
    """Executes a function's source code line by line to build a full variable trace."""
    try:
        src = inspect.getsource(func)
        tree = ast.parse(src)
        func_def = tree.body[0]
        if isinstance(func_def, ast.FunctionDef):
            return _execute_ast_statements(func_def.body)
        return None
    except (FileNotFoundError, TypeError, IndexError):
        return None

def get_scope_at_node(
    func: Callable,
    target_assign_node: ast.Assign
):
    """Executes a function's AST up to a specific node to get the current variable scope."""
    try:
        src = inspect.getsource(func)
        tree = ast.parse(src)
        func_def = tree.body[0]
        if not isinstance(func_def, ast.FunctionDef):
            return None

        statements_before = []
        for stmt in func_def.body:
            if isinstance(stmt, ast.Assign) and stmt.lineno == target_assign_node.lineno:
                return _execute_ast_statements(statements_before)
            statements_before.append(stmt)
        return None
    except (FileNotFoundError, TypeError, IndexError):
        return None

def is_plausible_trace(
    correct_trace: dict,
    flawed_trace: dict
):
    """
    Validates a flawed trace against a correct one for type and value integrity.
    A trace is considered implausible if any numeric variable becomes non-numeric,
    flips its sign, or incorrectly becomes zero.
    """
    for key, correct_val in correct_trace.items():
        if not isinstance(correct_val, (int, float, BuiltinFraction)):
            continue

        flawed_val = flawed_trace.get(key)
        if not isinstance(flawed_val, (int, float, BuiltinFraction)):
            return False

        is_correct_int_like = isinstance(correct_val, int) or (isinstance(correct_val, float) and correct_val.is_integer())
        is_flawed_int_like = isinstance(flawed_val, int) or (isinstance(flawed_val, float) and flawed_val.is_integer())
        if is_correct_int_like and not is_flawed_int_like:
            return False

        correct_sign = (correct_val > 0) - (correct_val < 0)
        flawed_sign = (flawed_val > 0) - (flawed_val < 0)
        if correct_val != 0 and correct_sign != flawed_sign:
            return False
        if correct_val != 0 and flawed_val == 0:
            return False
    return True

def apply_mutation(
    func: Callable,
    mutation_details: Dict[str, Any]
):
    """
    Applies a single logical mutation to a function's AST and returns the
    mutated code and resulting flawed trace.
    """
    try:
        src = inspect.getsource(func)
        tree = ast.parse(src)

        class ASTMutator(ast.NodeTransformer):
            def __init__(self, details):
                self.details = details
                self.mutation_applied = False

            def visit_Assign(self, node):
                if not (isinstance(node.targets[0], ast.Name) and node.targets[0].id == self.details['target_variable']):
                    return node

                mutation_type = self.details['type']
                if mutation_type == 'incomplete_calculation' and isinstance(node.value, ast.BinOp):
                    unrolled = _unroll_binop(node.value)
                    if unrolled:
                        operands, op_type = unrolled
                        operand_to_remove = self.details['operand_to_remove']
                        new_operands = [op for op in operands if not (isinstance(op, ast.Name) and op.id == operand_to_remove)]
                        if len(new_operands) >= 2:
                            node.value = _build_binop_tree_from_list(new_operands, op_type)
                            self.mutation_applied = True
                elif mutation_type == 'operator_swap' and isinstance(node.value, ast.BinOp):
                    node.value.op = self.details['new_op']
                    self.mutation_applied = True
                elif mutation_type in ['incorrect_operand', 'input_misrepresentation', 'incorrect_final_answer_selection']:
                    class OperandSwapper(ast.NodeTransformer):
                        def __init__(self, to_replace, new_name):
                            self.to_replace = to_replace
                            self.new_name = new_name
                        def visit_Name(self, name_node):
                            if name_node.id == self.to_replace:
                                return ast.Name(id=self.new_name, ctx=name_node.ctx)
                            return name_node
                    swapper = OperandSwapper(self.details['operand_to_replace'], self.details['replacement_variable'])
                    node.value = swapper.visit(node.value)
                    self.mutation_applied = True
                return node

        mutator = ASTMutator(mutation_details)
        mutated_tree = mutator.visit(copy.deepcopy(tree))
        if not mutator.mutation_applied:
            return None, None

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


#### **Cell 6: Mutation Discovery**


```python
def get_variable_dependencies(node: ast.Assign):
    """Extracts the names of variables used as operands in an assignment's value."""
    return sorted([n.id for n in ast.walk(node.value) if isinstance(n, ast.Name) and n.id != 'int'])

def _unroll_binop(node: ast.BinOp):
    """
    Recursively unrolls a nested ast.BinOp structure into a flat list of operands.
    Returns None if operators are inconsistent (e.g., A + B * C).
    """
    op_type = type(node.op)
    def recurse(n):
        if isinstance(n, ast.BinOp) and type(n.op) == op_type:
            yield from recurse(n.left)
            yield from recurse(n.right)
        else:
            yield n
    operands = list(recurse(node))
    return operands, op_type

def _build_binop_tree_from_list(
    operands: list[ast.AST],
    op_constructor: type[ast.operator]
):
    """Reconstructs a left-associative ast.BinOp tree from a list of operand nodes."""
    if len(operands) < 2:
        raise ValueError("Cannot build a BinOp tree with fewer than 2 operands.")
    tree = ast.BinOp(left=operands[0], op=op_constructor(), right=operands[1])
    for i in range(2, len(operands)):
        tree = ast.BinOp(left=tree, op=op_constructor(), right=operands[i])
    return tree

def _discover_operator_swaps(node: ast.Assign):
    """Finds all valid OperatorSwap mutations for a given assignment node."""
    if not (isinstance(node.value, ast.BinOp) and hasattr(node.targets[0], 'id') and
            isinstance(node.value.left, (ast.Name, ast.Constant)) and isinstance(node.value.right, (ast.Name, ast.Constant))):
        return []

    target_variable, original_op_node = node.targets[0].id, node.value.op
    swap_map = {
        ast.Add: [ast.Sub, ast.Mult], ast.Sub: [ast.Add, ast.Div],
        ast.Mult: [ast.Div, ast.Add], ast.Div: [ast.Mult, ast.Sub]
    }
    mutations = []
    if type(original_op_node) in swap_map:
        for new_op_constructor in swap_map[type(original_op_node)]:
            mutations.append({"type": "operator_swap", "target_variable": target_variable, "original_op_type": type(original_op_node),
                              "new_op": new_op_constructor()})
    return mutations

def _discover_plausible_wrong_references(
    func: Callable,
    node: ast.Assign,
    all_input_vars: Set[str],
    debug: bool = False
):
    """
    Discovers plausible operand substitution mutations, excluding the 'answer' variable.
    """
    mutations = []
    if not hasattr(node.targets[0], 'id'):
        return []
    target_variable = node.targets[0].id
    if target_variable == 'answer':
        return []

    scope = get_scope_at_node(func, node)
    if scope is None:
        return []

    operands = [n.id for n in ast.walk(node.value) if isinstance(n, ast.Name) and n.id != 'int']
    for operand_to_replace in set(operands):
        if operand_to_replace not in scope:
            continue
        for replacement_candidate in scope:
            if replacement_candidate in (operand_to_replace, 'Fraction'):
                continue
            if isinstance(scope.get(operand_to_replace), (int, float, BuiltinFraction)) and isinstance(scope.get(replacement_candidate), (int, float, BuiltinFraction)):
                mutation_type = "input_misrepresentation" if operand_to_replace in all_input_vars else "incorrect_operand"
                mutations.append({"type": mutation_type, "target_variable": target_variable, "operand_to_replace": operand_to_replace, "replacement_variable": replacement_candidate})
    return [dict(t) for t in {tuple(d.items()) for d in mutations}]

def _discover_incomplete_calculations(node: ast.Assign):
    """Discovers opportunities for an Incomplete Calculation error by omitting one operand."""
    if not (isinstance(node.value, ast.BinOp) and hasattr(node.targets[0], 'id')):
        return []
    target_variable = node.targets[0].id
    unrolled = _unroll_binop(node.value)
    if not unrolled:
        return []
    operands, op_type = unrolled
    if len(operands) < 3 or op_type not in [ast.Add, ast.Mult]:
        return []
        
    mutations = []
    operand_names = [op.id for op in operands if isinstance(op, ast.Name)]
    for operand_node in operands:
        if isinstance(operand_node, ast.Name):
            mutations.append({"type": "incomplete_calculation", "target_variable": target_variable, "operand_to_remove": operand_node.id, "original_operands": tuple(sorted(operand_names))})
    return mutations

def _discover_incorrect_final_answer_selections(
    node: ast.Assign,
    logical_steps: List[Dict],
    all_output_vars: Set[str],
    debug: bool = False
):
    """
    Discovers opportunities to select an incorrect final answer from recently
    computed intermediate variables.
    """
    if not hasattr(node.targets[0], 'id') or node.targets[0].id != 'answer':
        return []

    correct_operands = [n.id for n in ast.walk(node.value) if isinstance(n, ast.Name)]
    if not correct_operands:
        return []
    correct_final_var = correct_operands[0]

    mutations = []
    num_steps = len(logical_steps)
    line_threshold = max(1, num_steps - 2)

    for var_name in all_output_vars:
        if var_name == correct_final_var:
            continue
        step_info = next((s for s in logical_steps if s.get('output_variable') == var_name), None)
        if step_info and step_info.get('line_number'):
            line_num = int(step_info['line_number'][1:])
            if line_num >= line_threshold:
                mutations.append({"type": "incorrect_final_answer_selection", "target_variable": "answer", "operand_to_replace": correct_final_var, "replacement_variable": var_name})
    return mutations

def discover_mutation_opportunities(
    func: Callable,
    logical_steps: list,
    correct_trace: dict,
    debug_mode: bool = False
):
    """Analyzes a function's AST to find all possible conceptual error mutations."""
    all_mutations = []
    try:
        src = inspect.getsource(func)
        tree = ast.parse(src)
        func_def = tree.body[0]
        if not isinstance(func_def, ast.FunctionDef):
            return []
    except (FileNotFoundError, TypeError, IndexError):
        return []

    assign_nodes = [node for node in func_def.body if isinstance(node, ast.Assign)]
    all_input_vars = {v for s in logical_steps for k in ('question_inputs', 'WK_inputs') for v in s.get(k, [])}
    all_output_vars = {s['output_variable'] for s in logical_steps if 'output_variable' in s}

    for node in assign_nodes:
        all_mutations.extend(_discover_operator_swaps(node))
        all_mutations.extend(_discover_plausible_wrong_references(func, node, all_input_vars, debug=debug_mode))
        all_mutations.extend(_discover_incomplete_calculations(node))
        all_mutations.extend(_discover_incorrect_final_answer_selections(node, logical_steps, all_output_vars, debug=debug_mode))
    return [dict(t) for t in {tuple(d.items()) for d in all_mutations}]

print("Mutation Discovery functions defined.")
```

    Mutation Discovery functions defined.


#### **Cell 7: Candidate Generation and Reconstruction**


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
        
def _cap_candidates(
    candidates: List[Dict],
    repro_seed: int
):
    """Applies constraints to the list of generated candidates to ensure variety."""
    from collections import Counter
    import random

    type_counts, line_counts = Counter(), Counter()
    filtered_candidates = []
    for cand in candidates:
        m_type, err_line = cand['mutation_details']['type'], cand['erroneous_line_number']
        type_counts[m_type] += 1
        line_counts[err_line] += 1
        if type_counts[m_type] <= 2 and line_counts[err_line] <= 2:
            filtered_candidates.append(cand)

    if len(filtered_candidates) > 5:
        random.seed(repro_seed)
        random.shuffle(filtered_candidates)
        return filtered_candidates[:5]
    return filtered_candidates

def _get_mutated_template(
    original_template: str,
    mutation: dict
):
    """Modifies a template string to reflect a variable swap or operator swap."""
    mutation_type = mutation['type']
    if mutation_type == 'operator_swap':
        # This part of the function is not currently used by the active discovery
        # functions but is kept for potential future use.
        return original_template
    elif mutation_type in ['incorrect_operand', 'input_misrepresentation', 'incorrect_final_answer_selection']:
        to_replace_ph, new_name_ph = f"{{{mutation['operand_to_replace']}}}", f"{{{mutation['replacement_variable']}}}"
        return original_template.replace(to_replace_ph, new_name_ph)
    return original_template

def _reconstruct_incomplete_calc_template(
    original_template: str,
    mutation: dict
):
    """
    Reconstructs the solution line template for an 'incomplete_calculation' error,
    modifying both the outer text and the inner calculator annotation.
    """
    placeholder_to_remove = f"{{{mutation['operand_to_remove']}}}"
    target_variable = mutation['target_variable']
    pattern_after = re.compile(re.escape(placeholder_to_remove) + r'\s*[x*×+]\s*')
    pattern_before = re.compile(r'\s*[x*×+]\s*' + re.escape(placeholder_to_remove))

    mutated_template = original_template
    annotation_match = re.search(r'<<(.*?)>>', mutated_template)
    if annotation_match:
        full_annotation_str, inner_expr_str = annotation_match.group(0), annotation_match.group(1)
        modified_inner_expr = pattern_after.sub('', inner_expr_str, count=1)
        if modified_inner_expr == inner_expr_str:
            modified_inner_expr = pattern_before.sub('', modified_inner_expr, count=1)
        new_annotation_str = f"<<{modified_inner_expr}>>"
        mutated_template = mutated_template.replace(full_annotation_str, new_annotation_str)

    final_template = pattern_after.sub('', mutated_template, count=1)
    if final_template == mutated_template:
        final_template = pattern_before.sub('', final_template, count=1)
    return final_template

def _generate_explanation(
    mutation: dict,
    correct_trace: dict
):
    """Generates a human-readable explanation with values for a given mutation."""
    m_type = mutation['type']
    def get_val(var_name): return correct_trace.get(var_name, 'N/A')

    if m_type == 'incomplete_calculation':
        return f"Incomplete calculation. The term '{mutation['operand_to_remove']}' (value: {get_val(mutation['operand_to_remove'])}) was omitted from the operation."
    elif m_type == 'operator_swap':
        op_map = {ast.Add: '+', ast.Sub: '-', ast.Mult: '*', ast.Div: '/'}
        original_op_str, new_op_str = op_map.get(mutation['original_op_type'], '?'), op_map.get(type(mutation['new_op']), '?')
        return f"Incorrect operation. The calculation should use '{original_op_str}' but used '{new_op_str}' instead."
    elif m_type == 'incorrect_operand':
        original, replacement = mutation['operand_to_replace'], mutation['replacement_variable']
        return f"Incorrect operand. The variable '{replacement}' (value: {get_val(replacement)}) was used instead of '{original}' (value: {get_val(original)})."
    elif m_type == 'input_misrepresentation':
        original, replacement = mutation['operand_to_replace'], mutation['replacement_variable']
        return f"Input misrepresentation. The value for '{replacement}' ({get_val(replacement)}) was used instead of '{original}' ({get_val(original)})."
    elif m_type == 'incorrect_final_answer_selection':
        original, replacement = mutation['operand_to_replace'], mutation['replacement_variable']
        return f"Incorrect final answer. An intermediate value '{replacement}' (value: {get_val(replacement)}) was reported instead of '{original}' (value: {get_val(original)})."
    return "An unknown conceptual error occurred."

def reconstruct_solution_from_trace(
    logical_steps: list[dict],
    eval_trace: dict[str, Any],
    candidate_mutation: dict | None = None
):
    """Reconstructs NL solution lines, truncates if necessary, and adds the FA line."""
    formatted_trace, reconstructed_mapping = FormattingTrace(eval_trace), {}
    cutoff_line = None
    if candidate_mutation and candidate_mutation['type'] == 'incorrect_final_answer_selection':
        incorrect_answer_var = candidate_mutation['replacement_variable']
        cutoff_line_info = next((s for s in logical_steps if s.get('output_variable') == incorrect_answer_var), None)
        if cutoff_line_info:
            cutoff_line = cutoff_line_info['line_number']

    for step in logical_steps:
        ln, template = step.get("line_number"), step.get("solution_line_template")
        if not (ln and template):
            continue

        if candidate_mutation and candidate_mutation['type'] != 'incorrect_final_answer_selection':
            if step.get("output_variable") == candidate_mutation['target_variable']:
                if candidate_mutation['type'] == 'incomplete_calculation':
                    template = _reconstruct_incomplete_calc_template(template, candidate_mutation)
                else:
                    template = _get_mutated_template(template, candidate_mutation)
        try:
            reconstructed_mapping[ln] = template.format_map(formatted_trace)
        except (KeyError, ValueError):
            return None
        if ln == cutoff_line:
            break

    flawed_final_answer = eval_trace.get('answer')
    if flawed_final_answer is not None:
        if isinstance(flawed_final_answer, float) and flawed_final_answer.is_integer():
            formatted_answer = int(flawed_final_answer)
        else:
            formatted_answer = round(flawed_final_answer, 2) if isinstance(flawed_final_answer, float) else flawed_final_answer
        reconstructed_mapping['FA'] = f"#### {formatted_answer}"
    return reconstructed_mapping

def generate_candidates_for_template(
    func: Callable,
    logical_steps: list,
    correct_trace: dict,
    original_solution_mapping: dict,
    index: int,
    debug_mode: bool = False
):
    """Orchestrates the generation of all possible conceptual error candidates for a single template."""
    mutations = discover_mutation_opportunities(func, logical_steps, correct_trace, debug_mode=debug_mode)
    candidates, original_code = [], inspect.getsource(func)
    repro_seed = hash(f"conceptual_{index}")

    for mutation in mutations:
        mutated_code, flawed_trace = apply_mutation(func, mutation)
        if not flawed_trace or not is_plausible_trace(correct_trace, flawed_trace):
            continue
        correct_answer, flawed_answer = correct_trace.get('answer'), flawed_trace.get('answer')
        norm_correct = str(float(correct_answer)) if isinstance(correct_answer, (int, float)) else str(correct_answer)
        norm_flawed = str(float(flawed_answer)) if isinstance(flawed_answer, (int, float)) else str(flawed_answer)
        if correct_answer is None or flawed_answer is None or norm_correct == norm_flawed:
            continue
        try:
            flawed_nl_reconstruction = reconstruct_solution_from_trace(logical_steps, flawed_trace, candidate_mutation=mutation)
            if not flawed_nl_reconstruction:
                continue
        except AttributeError as e:
            if "'str' object has no attribute 'numerator'" in str(e):
                print(f"\n[DEBUG] Caught AttributeError on index {index}. Skipping mutation: {mutation}")
                continue
            else:
                raise e

        if mutation['type'] == 'incorrect_final_answer_selection':
            erroneous_line_number = "FA"
        else:
            erroneous_line_number = next((s['line_number'] for s in logical_steps if s.get('output_variable') == mutation['target_variable']), None)
        target_var = mutation['target_variable']
        
        candidate_package = {
            "index": index, "original_solution_mapping": original_solution_mapping,
            "original_function_code": original_code, "mutation_details": mutation,
            "correct_trace": correct_trace, "flawed_trace": flawed_trace,
            "correct_value": correct_trace.get(target_var), "flawed_value": flawed_trace.get(target_var),
            "logical_steps": logical_steps, "flawed_nl_reconstruction": flawed_nl_reconstruction,
            "erroneous_line_number": erroneous_line_number,
            "explanation": _generate_explanation(mutation, correct_trace)
        }
        candidates.append(candidate_package)
        
    capped_candidates = _cap_candidates(candidates, repro_seed)
    for cand in capped_candidates:
        cand['repro_seed'] = repro_seed
    return capped_candidates

print("Candidate Generation and Reconstruction functions defined.")
```

    Candidate Generation and Reconstruction functions defined.


#### **Cell 7: Main Driver**
*   **Functionality:** Executes the entire pipeline in parallel for a specified range of problem indices.
*   **Logic:**
    *   `run_candidate_generation_pipeline_parallel`: The entry point. It defines a list of tasks (indices to process) and uses the `joblib` library to run them in parallel across all available CPU cores.
    *   `process_single_index`: The worker function executed by each parallel job. It contains the model fallback logic: it tries to load a template from the preferred model (`gemini-2.5-flash`), and if that fails or produces no candidates, it tries the next model (`gpt-4.1`).
    *   `save_candidates_and_get_metadata`: A utility to save the generated candidate packages to disk as individual JSON files and compile their metadata into a list for the final CSV catalog. The logic for generating a unique filename is a good safeguard.


```python
def process_single_index(
    index_info: tuple,
    model_preference: list
):
    """
    Worker function to process a single problem index for candidate generation.
    It loads a template, validates it, and orchestrates the generation of
    conceptual error candidates.
    """
    tier, index = index_info
    original_solution_mapping = build_solution_mapping(index)
    if not original_solution_mapping:
        return []

    for model_name in model_preference:
        solve_module = load_function_module(tier, index, model_name)
        logical_steps = load_logical_steps(tier, index, model_name)
        if solve_module and logical_steps:
            is_brittle = False
            for step in logical_steps:
                template = step.get('solution_line_template', '')
                placeholders = re.findall(r'\{([^}]+)\}', template)
                if any('.' in p for p in placeholders):
                    print(f"[INFO] Skipping brittle template for index {index} (model: {model_name}) due to attribute access in placeholder.")
                    is_brittle = True
                    break
            if is_brittle:
                continue

            solve_function, correct_trace = solve_module.solve, execution_trace(solve_module.solve)
            if not correct_trace:
                continue
            
            candidates = generate_candidates_for_template(
                func=solve_function, logical_steps=logical_steps,
                correct_trace=correct_trace, original_solution_mapping=original_solution_mapping,
                index=index
            )
            
            if candidates:
                for cand in candidates:
                    cand['model_name'] = model_name
                return candidates
    return []

def run_candidate_generation_pipeline_parallel(indices_to_generate: List[int]):
    """Drives the conceptual error candidate generation pipeline in parallel using joblib."""
    print("--- Starting Conceptual Error Candidate Generation (PARALLEL MODE) ---")
    
    tasks = []
    for tier, indices in TIER_LISTS.items():
        for index in indices:
            if index in indices_to_generate:
                tasks.append((tier, index))
    
    print(f"Prepared {len(tasks)} indices for processing across all available CPU cores.")

    results_list = Parallel(n_jobs=-1)(
        delayed(process_single_index)(task, MODELS) 
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
        repro_seed = cand.get('repro_seed')
        now_utc = datetime.datetime.now(datetime.timezone.utc)
        
        output_dir = CONCEPTUAL_CANDIDATES_DIR / tier / str(index)
        output_dir.mkdir(parents=True, exist_ok=True)
        replacement_var = mutation.get('replacement_variable', '')
        filename = f"{model_name}_{m_type}_{target_var}_{replacement_var}.json"
        filepath = output_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(cand, f, indent=2, default=str)
        
        record = {
            "index": index, "tier": tier, "model": model_name, "mutation_type": m_type, 
            "target_variable": target_var, "correct_value": str(cand.get('correct_value')), 
            "flawed_value": str(cand.get('flawed_value')), "repro_seed": repro_seed,
            "date_utc": now_utc.strftime('%Y-%m-%d'), "time_utc": now_utc.strftime('%H:%M:%S'),
            "mutation_details": json.dumps(mutation, default=str), "filepath": str(filepath.relative_to(PROJECT_ROOT))
        }
        all_candidate_metadata.append(record)

    if all_candidate_metadata:
        catalog_df = pd.DataFrame(all_candidate_metadata)
        cols = ['index', 'tier', 'model', 'mutation_type', 'target_variable', 'correct_value', 'flawed_value', 'repro_seed', 'date_utc', 'time_utc', 'mutation_details', 'filepath']
        catalog_df = catalog_df.reindex(columns=[c for c in cols if c in catalog_df.columns])
        catalog_path = CONCEPTUAL_CANDIDATES_DIR / "conceptual_candidate_catalog.csv"
        catalog_df.to_csv(catalog_path, index=False)
        print(f"\n--- Pipeline Complete ---")
        print(f"Generated and saved {len(all_candidate_metadata)} conceptual error candidates.")
        print(f"Catalog saved to: {catalog_path}")

print("Main Driver and supporting functions defined.")
```

    Main Driver and supporting functions defined.


## Cell 8: Execute Pipeline

This final cell executes the main driver function to run the entire test pipeline.


```python
run_candidate_generation_pipeline_parallel(indices_to_generate=list(range(3000)))
```

    --- Starting Conceptual Error Candidate Generation (PARALLEL MODE) ---
    Prepared 3000 indices for processing across all available CPU cores.



    Processing Indices:   0%|          | 0/3000 [00:00<?, ?it/s]


    [INFO] Skipping brittle template for index 1484 (model: google_gemini-2.5-flash) due to attribute access in placeholder.
    
    --- Parallel processing complete. Saving artifacts... ---



    Saving Candidates:   0%|          | 0/13499 [00:00<?, ?it/s]


    
    --- Pipeline Complete ---
    Generated and saved 13499 conceptual error candidates.
    Catalog saved to: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/conceptual-error-candidates/conceptual_candidate_catalog.csv

