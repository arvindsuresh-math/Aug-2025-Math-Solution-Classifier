### Cell 1: Imports and Path Definitions


```python
import json
import re
import ast
import inspect
import importlib.util
from pathlib import Path
from types import ModuleType
from typing import Callable, Any
from fractions import Fraction as BuiltinFraction

import pandas as pd
from tqdm.notebook import tqdm
from datasets import load_dataset, Dataset

# --- Path and Directory Definitions ---
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
PROCESSED_TEMPLATE_DIR = DATA_DIR / "template-generated-processed"
MODELS = ['openai_gpt-4.1', 'google_gemini-2.5-flash']

print(f"Project root: {PROJECT_ROOT}")
print(f"Validation Input Directory: {PROCESSED_TEMPLATE_DIR}")

if not PROCESSED_TEMPLATE_DIR.is_dir():
    raise FileNotFoundError(f"INPUT DIRECTORY NOT FOUND: {PROCESSED_TEMPLATE_DIR}")
```

    Project root: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math
    Validation Input Directory: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/template-generated-processed


### Cell 2: Data Loaders and Ground Truth Utilities


```python
# --- Load GSM8K Dataset for ground truth answers and solution text ---
GSM8K_TRAIN: Dataset = load_dataset("gsm8k", "main")["train"]

def load_function_module(tier: str, index: int, model: str) -> ModuleType | None:
    """Dynamically loads the 'solve.py' module for a given template."""
    py_file_path = PROCESSED_TEMPLATE_DIR / tier / str(index) / f"{model}.py"
    if not py_file_path.exists(): return None
    module_name = f"templates.val.t{tier}.i{index}.m_{model.replace('.', '_')}"
    spec = importlib.util.spec_from_file_location(module_name, py_file_path)
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    return None

def load_logical_steps(tier: str, index: int, model: str) -> list[dict] | None:
    """Loads the 'logical_steps.json' for a given template."""
    json_file_path = PROCESSED_TEMPLATE_DIR / tier / str(index) / f"{model}.json"
    try:
        return json.loads(json_file_path.read_text(encoding='utf-8'))
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def get_ground_truth_answer(index: int) -> float | None:
    """Extracts the final numeric answer from the GSM8K dataset."""
    try:
        answer_text = GSM8K_TRAIN[int(index)]['answer']
        final_answer_str = answer_text.split('####')[-1].strip().replace(',', '')
        return float(final_answer_str)
    except (ValueError, IndexError):
        return None

def get_original_solution_lines(index: int) -> dict[str, str] | None:
    """Extracts the original solution into a line-numbered dictionary."""
    try:
        solution_text = GSM8K_TRAIN[int(index)]["answer"]
        lines = [ln.strip() for ln in solution_text.splitlines() if ln.strip()]
        if lines and re.match(r"^####\s*[\d\.,]+$", lines[-1]):
            lines.pop(-1)
        return {f"L{i+1}": line for i, line in enumerate(lines)}
    except IndexError:
        return None

print("Data loading utilities defined.")
```

    Data loading utilities defined.


### Cell 3: Core Validation Functions


```python
class NonSimplifyingFraction(BuiltinFraction):
    """
    A subclass of fractions.Fraction that does not simplify when converted
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

def normalize_numeric_string(s: str) -> str:
    """Converts a string representing a number into a canonical form."""
    if not isinstance(s, str): s = str(s)
    cleaned = s.strip()
    cleaned = re.sub(r'[\$,]', '', cleaned)
    if cleaned.startswith('.'): cleaned = '0' + cleaned
    elif cleaned.startswith('-.') or cleaned.startswith('+.'): cleaned = cleaned[0] + '0' + cleaned[1:]
    try:
        num = float(cleaned)
        if num.is_integer(): return str(int(num))
        return str(num)
    except (ValueError, TypeError):
        return cleaned

def check_answer(solve_function: Callable, ground_truth_answer: float) -> dict:
    """
    Executes a solve() function and compares its result against the ground truth.
    Returns a dictionary with a descriptive status.
    """
    try:
        result = solve_function()
    except Exception as e:
        return {"status": "fail_not_executable", "details": str(e), "computed_answer": None}
    
    norm_result = normalize_value(result) if isinstance(result, (int, float, BuiltinFraction)) else result
    norm_truth = normalize_value(ground_truth_answer)
    
    if norm_result == norm_truth:
        return {"status": "pass", "details": None, "computed_answer": result}
    else:
        details = f"Expected {ground_truth_answer}, but got {result}."
        return {"status": "fail_wrong_answer", "details": details, "computed_answer": result}

def validate_structural_integrity(logical_steps: list[dict], original_lines: dict[str, str]) -> dict:
    """
    Validates the structural integrity of the templates line-by-line.
    Returns a dictionary containing the score and a list of mismatched line numbers.
    """
    structural_matches, mismatched_lines = 0, []
    for step in logical_steps:
        template, line_num = step.get('solution_line_template', ''), step.get('line_number')
        original_line = original_lines.get(line_num, "")
        ambient_fragments = re.split(r'\{[a-zA-Z0-9_]+\}', template)
        current_pos, line_is_ok = 0, True
        for fragment in ambient_fragments:
            found_pos = original_line.find(fragment, current_pos)
            if found_pos == -1:
                line_is_ok = False
                break
            current_pos = found_pos + len(fragment)
        if line_is_ok: structural_matches += 1
        else: mismatched_lines.append(line_num)
            
    score = structural_matches / len(logical_steps) if logical_steps else 1.0
    return {"score": score, "mismatched_lines": mismatched_lines}

def validate_semantic_integrity(logical_steps: list[dict], correct_trace: dict, original_lines: dict[str, str]) -> dict:
    """
    Validates the semantic (numeric value) integrity of the templates.
    ASSUMES the template structure is already a perfect match.
    Returns a dictionary containing the score and a list of mismatched variable names.
    """
    total_placeholders, semantic_matches, mismatched_variables = 0, 0, []
    for step in logical_steps:
        template, line_num = step.get('solution_line_template', ''), step.get('line_number')
        original_line = original_lines.get(line_num, "")
        placeholders = re.findall(r'\{([a-zA-Z0-9_]+)\}', template)
        ambient_fragments = re.split(r'\{[a-zA-Z0-9_]+\}', template)
        current_pos = 0
        for i, placeholder_var in enumerate(placeholders):
            total_placeholders += 1
            start_ambient, end_ambient = ambient_fragments[i], ambient_fragments[i+1]
            start_val_pos = original_line.find(start_ambient, current_pos) + len(start_ambient)
            end_frag_pos = original_line.find(end_ambient, start_val_pos) if end_ambient else len(original_line)
            extracted_str = original_line[start_val_pos:end_frag_pos]
            ground_truth_val = correct_trace.get(placeholder_var)
            if ground_truth_val is not None:
                if normalize_numeric_string(extracted_str) == normalize_numeric_string(ground_truth_val):
                    semantic_matches += 1
                else: mismatched_variables.append(placeholder_var)
            else: mismatched_variables.append(placeholder_var)
            current_pos = end_frag_pos
            
    score = semantic_matches / total_placeholders if total_placeholders > 0 else 1.0
    return {"score": score, "mismatched_variables": mismatched_variables}

print("Core validation functions defined.")
```

    Core validation functions defined.


### Cell 4: Validation orchestrator


```python
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

def validate_template(tier: str, index: int, model: str) -> dict | None:
    """
    Orchestrates the complete validation process for a single template,
    calling checks sequentially and returning a summary report dictionary.
    """
    # 1. Load all components; exit if any are missing.
    solve_module = load_function_module(tier, index, model)
    logical_steps = load_logical_steps(tier, index, model)
    ground_truth_answer = get_ground_truth_answer(index)
    original_lines = get_original_solution_lines(index)
    
    if not all([solve_module, logical_steps, ground_truth_answer, original_lines]):
        return None

    solve_function = solve_module.solve
    
    # 2. Run the primary validation checks.
    answer_check_result = check_answer(solve_function, ground_truth_answer)
    structural_results = validate_structural_integrity(logical_steps, original_lines)
    
    # 3. Semantic check is only performed if structure is perfect and code is executable.
    semantic_results = {"score": None, "mismatched_variables": None}
    correct_trace = execution_trace(solve_function)
    if structural_results["score"] == 1.0 and correct_trace:
        semantic_results = validate_semantic_integrity(logical_steps, correct_trace, original_lines)

    # 4. Compile the final report.
    report = {
        "index": index,
        "tier": tier,
        "model": model,
        "answer_check_status": answer_check_result["status"],
        "structural_score": structural_results["score"],
        "semantic_score": semantic_results["score"],
        "structural_mismatches": structural_results["mismatched_lines"],
        "semantic_mismatches": semantic_results["mismatched_variables"],
    }
    return report

print("Validation orchestrator defined.")
```

    Validation orchestrator defined.


### Cell 5: Main driver and report generation


```python
def run_full_validation_pipeline():
    """
    Drives the entire validation pipeline for all processed templates,
    compiles the results, and saves a final CSV report with summary statistics.
    """
    print("--- Starting Full Template Validation ---")
    all_reports = []
    
    tier_dirs = sorted([d for d in PROCESSED_TEMPLATE_DIR.iterdir() if d.is_dir() and d.name.startswith('tier')])
    for tier_dir in tqdm(tier_dirs, desc="Validating Tiers"):
        index_dirs = sorted([d for d in tier_dir.iterdir() if d.is_dir() and d.name.isdigit()], key=lambda p: int(p.name))
        for index_dir in tqdm(index_dirs, desc=f"Processing {tier_dir.name}", leave=False):
            for model in MODELS:
                report = validate_template(tier_dir.name, int(index_dir.name), model)
                if report:
                    all_reports.append(report)

    if all_reports:
        report_df = pd.DataFrame(all_reports)
        report_path = PROCESSED_TEMPLATE_DIR / "template_validation_report.csv"
        report_df.to_csv(report_path, index=False)
        
        print("\n--- Validation Complete ---")
        print(f"Validated {len(report_df)} templates.")
        print(f"Report saved to: {report_path}")
        
        # Display Final Summary Statistics
        print("\n--- Summary Report ---")
        
        # Answer Correctness Breakdown
        answer_counts = report_df['answer_check_status'].value_counts()
        total_templates = len(report_df)
        pass_count = answer_counts.get('pass', 0)
        wrong_answer_count = answer_counts.get('fail_wrong_answer', 0)
        not_executable_count = answer_counts.get('fail_not_executable', 0)
        
        print("Answer Correctness Breakdown:")
        print(f"  - Pass (Correct Answer): {pass_count:>4} / {total_templates} ({pass_count/total_templates:.2%})")
        print(f"  - Fail (Wrong Answer):   {wrong_answer_count:>4} / {total_templates} ({wrong_answer_count/total_templates:.2%})")
        print(f"  - Fail (Not Executable): {not_executable_count:>4} / {total_templates} ({not_executable_count/total_templates:.2%})")
        
        # Define the subset eligible for semantic validation
        eligible_for_semantic_check = report_df[
            (report_df['answer_check_status'] != 'fail_not_executable') &
            (report_df['structural_score'] == 1.0)
        ]
        
        # Calculate integrity rates based on the appropriate populations (file-based)
        perfect_structure_count = (report_df['structural_score'] == 1.0).sum()
        total_eligible = len(eligible_for_semantic_check)
        perfect_semantic_count = (eligible_for_semantic_check['semantic_score'] == 1.0).sum() if not eligible_for_semantic_check.empty else 0
        
        print(f"\n--- Integrity Rates (file-based) ---")
        print(f"Perfect Structural Match: {perfect_structure_count} / {total_templates} ({perfect_structure_count/total_templates:.2%}) of all templates")
        print(f"Perfect Semantic Match:   {perfect_semantic_count} / {total_eligible} ({perfect_semantic_count/total_eligible:.2%}) of eligible templates")

        # Calculate integrity rates based on the index-based population
        structural_pass_df = report_df[report_df['structural_score'] == 1.0].copy()
        semantic_pass_df = report_df[report_df['semantic_score'] == 1.0].copy()

        structural_pass_indices = list(set(structural_pass_df['index'].tolist()))
        semantic_pass_indices = list(set(semantic_pass_df['index'].tolist()))
        total_indices = list(set(report_df['index'].tolist()))

        print(f"\n--- Integrity Rates (index-based) ---")
        print(f"Perfect Structural Match: {len(structural_pass_indices)} / {len(total_indices)} ({len(structural_pass_indices)/len(total_indices):.2%}) of all indices")
        print(f"Perfect Semantic Match:   {len(semantic_pass_indices)} / {len(total_indices)} ({len(semantic_pass_indices)/len(total_indices):.2%}) of all indices")
    else:
        print("\nNo templates were found to validate.")
```

### Cell 6: Running the full validation pipeline


```python
run_full_validation_pipeline()
```

    --- Starting Full Template Validation ---



    Validating Tiers:   0%|          | 0/4 [00:00<?, ?it/s]



    Processing tier1:   0%|          | 0/1138 [00:00<?, ?it/s]



    Processing tier2:   0%|          | 0/332 [00:00<?, ?it/s]



    Processing tier3:   0%|          | 0/1262 [00:00<?, ?it/s]



    Processing tier4:   0%|          | 0/185 [00:00<?, ?it/s]


    
    --- Validation Complete ---
    Validated 4794 templates.
    Report saved to: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/template-generated-processed/template_validation_report.csv
    
    --- Summary Report ---
    Answer Correctness Breakdown:
      - Pass (Correct Answer): 4751 / 4794 (99.10%)
      - Fail (Wrong Answer):     42 / 4794 (0.88%)
      - Fail (Not Executable):    1 / 4794 (0.02%)
    
    --- Integrity Rates (file-based) ---
    Perfect Structural Match: 4482 / 4794 (93.49%) of all templates
    Perfect Semantic Match:   4182 / 4481 (93.33%) of eligible templates
    
    --- Integrity Rates (index-based) ---
    Perfect Structural Match: 2766 / 2916 (94.86%) of all indices
    Perfect Semantic Match:   2598 / 2916 (89.09%) of all indices



```python
# Cell 7: Diagnostic Tool for Individual Indices

def find_tier_for_index(index: int) -> str | None:
    """Helper function to find the tier for a given problem index."""
    for tier, indices in TIER_LISTS.items():
        if index in indices:
            return tier
    return None

def reconstruct_solution_for_model(tier: str, index: int, model: str) -> dict[str, str]:
    """
    Reconstructs the solution lines for a single template.
    
    Returns a dictionary mapping line numbers to the reconstructed text.
    """
    logical_steps = load_logical_steps(tier, index, model)
    solve_module = load_function_module(tier, index, model)
    
    if not (logical_steps and solve_module):
        return {}
        
    correct_trace = execution_trace(solve_module.solve)
    if not correct_trace:
        return {ln: "ERROR: Could not execute trace" for ln in original_lines}

    reconstructed_lines = {}
    for step in logical_steps:
        ln = step["line_number"]
        template = step["solution_line_template"]
        try:
            reconstructed_lines[ln] = template.format_map(correct_trace)
        except (KeyError, ValueError):
            reconstructed_lines[ln] = "ERROR: Formatting failed"
            
    return reconstructed_lines

def normalize_line_text(text: str) -> str:
    """
    Normalizes a full line of text by normalizing all numbers found within it.
    """
    # This pattern finds integers, comma-separated numbers, and decimals.
    number_pattern = r'[\d,]+\.?\d*'
    # Use re.sub with a lambda to apply our string normalizer to each number found.
    return re.sub(number_pattern, lambda m: normalize_numeric_string(m.group(0)), text)

def diagnose_index(index: int):
    """
    Provides a full diagnostic report for a single problem index, comparing
    the original solution against the templates from all models.
    """
    print("="*80)
    print(f"DIAGNOSTIC REPORT FOR INDEX: {index}")
    print("="*80)

    # 1. Load ground truth data
    tier = find_tier_for_index(index)
    original_lines = get_original_solution_lines(index)
    if not tier or not original_lines:
        print(f"ERROR: Could not find tier or original solution for index {index}.")
        return

    # --- Part 1: Print Mismatch Lists ---
    print("\n--- Mismatch Analysis ---")
    full_report = report_df[report_df['index'] == index]
    for _, row in full_report.iterrows():
        model = row['model']
        print(f"\nModel: {model}")
        
        # Safely evaluate the string representation of lists in the DataFrame
        structural_mismatches = ast.literal_eval(row['structural_mismatches'])
        semantic_mismatches = ast.literal_eval(row['semantic_mismatches'])
        
        if structural_mismatches:
            print(f"  - Structural Mismatches on Lines: {structural_mismatches}")
        else:
            print("  - No Structural Mismatches.")
            
        if semantic_mismatches:
            print(f"  - Semantic Mismatches for Variables: {semantic_mismatches}")
        else:
            print("  - No Semantic Mismatches (or not applicable).")

    # --- Part 2: Display Visual Diff DataFrame ---
    print("\n" + "="*80)
    print("--- Visual Diff of Reconstructed Lines (with Normalized Values) ---")
    
    # Start with the original solution
    df = pd.DataFrame.from_dict(original_lines, orient='index', columns=['Original'])
    
    # Add a column for each model's reconstruction
    for model in MODELS:
        reconstructed = reconstruct_solution_for_model(tier, index, model)
        df[f'Recon_{model}'] = df.index.map(reconstructed)

    # Create the final normalized DataFrame by applying the normalization function
    normalized_df = df.map(lambda x: normalize_line_text(str(x)) if pd.notna(x) else "")
    
    display(normalized_df)
```
