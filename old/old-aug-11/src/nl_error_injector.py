import re
import json
import importlib.util
import copy
import ast
from pathlib import Path
from typing import Dict, Any, Tuple, Optional, List

# You must install this library: pip install num2words
from num2words import num2words

# ==============================================================================
# ASSUMPTION: The following utility functions are defined elsewhere in your
# project and are available for import.
# ==============================================================================

# from your_utils import execution_trace, build_solution_mapping

# For this script to be self-contained, I will include placeholder implementations
# based on the code you have provided.

def execution_trace(func):
    """Placeholder: Simulates execution and returns a variable-to-value map."""
    src = inspect.getsource(func)
    tree = ast.parse(src)
    func_def = tree.body[0]
    env = {}
    # Get default args
    arg_names = [arg.arg for arg in func_def.args.args]
    defaults = func_def.args.defaults
    for name, val_node in zip(arg_names[-len(defaults):], defaults):
        env[name] = eval(compile(ast.Expression(val_node), '', 'eval'))

    # Execute body
    for stmt in func_def.body:
        if isinstance(stmt, ast.Assign):
            code_obj = compile(ast.Module([stmt], []), '', 'exec')
            exec(code_obj, {}, env)
    return env

# ==============================================================================
# Main Class for Natural Language Error Injection
# ==============================================================================

class NaturalLanguageErrorInjector:
    """
    Generates a flawed natural language (NL) solution and its corresponding
    structured JSON label by injecting a programmatic error from a source
    code function.

    This class orchestrates the loading of correct and flawed code,
    analyzing their execution traces, and programmatically modifying the
    original NL solution text to reflect the injected error.
    """

    def __init__(self, problem_index: int, model_name: str, error_type: str, project_root: Path):
        """
        Initializes the injector for a specific error instance.

        Args:
            problem_index: The GSM8K index of the problem.
            model_name: The name of the model that generated the code.
            error_type: The type of error to inject (e.g., 'computational_error').
            project_root: The root path of the project directory.
        """
        self.problem_index = problem_index
        self.model_name = model_name
        self.error_type = error_type
        self.project_root = project_root

        # Define paths
        self.correct_code_dir = self.project_root / 'data' / 'code_gen_outputs_traced'
        self.flawed_code_dir = self.project_root / 'data' / 'code_with_error'
        self.metadata_dir = self.project_root / 'data' / 'injection_metadata' # Assuming this path

        # Initialize data attributes
        self.f_oracle = None
        self.f_flawed = None
        self.correct_trace = None
        self.flawed_trace = None
        self.metadata = None
        self.original_nl_solution = None
        self.deleted_nl_line_text = "" # For skipped_step

        # Map AST op classes to symbols for explanations
        self.op_map = {ast.Add: '+', ast.Sub: '-', ast.Mult: '*', ast.Div: '/'}

    def _load_module_from_path(self, file_path: Path, module_name: str):
        """Loads a Python module from a given file path."""
        if not file_path.exists():
            print(f"❌ Error: File not found at {file_path}")
            return None
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        return None

    def _load_data_sources(self) -> bool:
        """
        Loads all necessary inputs from disk into instance attributes.
        """
        # 1. Load correct/oracle code and trace
        correct_path = self.correct_code_dir / str(self.problem_index) / f"{self.model_name}.py"
        self.f_oracle = self._load_module_from_path(correct_path, "f_oracle")
        if not self.f_oracle: return False
        self.correct_trace = execution_trace(self.f_oracle.solve)

        # 2. Load flawed code and trace
        flawed_path = self.flawed_code_dir / self.error_type / str(self.problem_index) / f"{self.model_name}.py"
        self.f_flawed = self._load_module_from_path(flawed_path, "f_flawed")
        # For skipped_step, the flawed code may be non-runnable.
        if self.f_flawed:
            try:
                self.flawed_trace = execution_trace(self.f_flawed.solve)
            except Exception:
                if self.error_type != 'skipped_step':
                    print(f"⚠️ Warning: Could not trace flawed function for {self.error_type}")
                self.flawed_trace = {} # Ensure it exists
        else:
             if self.error_type != 'skipped_step': return False
             self.flawed_trace = {}

        # 3. Load injection metadata
        metadata_path = self.metadata_dir / f"metadata_{self.problem_index}_{self.error_type}.json"
        if not metadata_path.exists():
            print(f"❌ Error: Metadata file not found at {metadata_path}")
            return False
        with open(metadata_path, 'r') as f:
            full_metadata = json.load(f)
            self.metadata = full_metadata.get(self.model_name)
        if not self.metadata:
            print(f"❌ Error: No metadata found for model '{self.model_name}' in {metadata_path}")
            return False

        # 4. Load original NL solution
        # This requires the gsm8k dataset to be available.
        # self.original_nl_solution = build_solution_mapping(self.problem_index, gsm8k_train)
        # For a self-contained example, I will use a placeholder:
        if self.problem_index == 0:
            self.original_nl_solution = {
                "L1": 'Natalia sold 48/2 = <<48/2=24>>24 clips in May.',
                "L2": 'Natalia sold 48+24 = <<48+24=72>>72 clips altogether in April and May.',
                "FA": '#### 72'
            }
        else:
            # In a real scenario, you would load this from the dataset
            print(f"⚠️ Warning: No placeholder NL solution for index {self.problem_index}")
            self.original_nl_solution = {}
            
        return True

    def _replace_number_in_string(self, text: str, old_num: float, new_num: float) -> str:
        """A robust helper to replace a number within a string, handling int/float and word forms."""
        if old_num == new_num:
            return text
        
        # Format the new number (e.g., 72.0 becomes "72")
        new_num_str = str(int(new_num)) if new_num.is_integer() else str(new_num)
        
        # Try replacing the word form first for integers
        if old_num.is_integer():
            old_num_int = int(old_num)
            old_num_word = num2words(old_num_int)
            # Use regex for whole-word replacement
            word_pattern = re.compile(r'\b' + re.escape(old_num_word) + r'\b', re.IGNORECASE)
            text = word_pattern.sub(new_num_str, text)

        # Then, replace the numeral form
        old_num_str = str(int(old_num)) if old_num.is_integer() else str(old_num)
        numeral_pattern = re.compile(r'\b' + re.escape(old_num_str) + r'\b')
        text = numeral_pattern.sub(new_num_str, text)
        
        return text

    def _modify_nl_line(self, line_text: str) -> str:
        """Modifies a single NL line by replacing its result with the flawed value from the trace."""
        # Regex to find the result in a calculator annotation, e.g., <<...=24>>
        match = re.search(r'<<.*?=([\d\.]+)>>', line_text)
        if not match:
            return line_text

        original_result = float(match.group(1))
        
        # Find the variable in the correct trace that produced this result
        variable_name = None
        for var, val in self.correct_trace.items():
            # Using a tolerance for float comparison
            if isinstance(val, (int, float)) and abs(val - original_result) < 1e-6:
                variable_name = var
                break
        
        if not variable_name:
            return line_text # Could not map result to a variable

        # Find the new, flawed value of this variable
        new_flawed_value = self.flawed_trace.get(variable_name)
        if new_flawed_value is None:
            return line_text
            
        # Replace the original result with the flawed one in the NL text
        return self._replace_number_in_string(line_text, original_result, new_flawed_value)

    def _generate_flawed_nl_solution(self) -> Dict[str, str]:
        """Creates the flawed NL solution mapping based on the error type."""
        flawed_nl = copy.deepcopy(self.original_nl_solution)
        
        if self.error_type == 'skipped_step':
            line_to_delete = self.metadata['line_label']
            if line_to_delete in flawed_nl:
                # Store the deleted text for the JSON label generation
                self.deleted_nl_line_text = flawed_nl[line_to_delete]
                del flawed_nl[line_to_delete]
            return flawed_nl

        # For other errors, iterate and propagate changes
        # Sorting keys ensures 'L1' is processed before 'L2', etc.
        sorted_keys = sorted(flawed_nl.keys(), key=lambda k: (k[0] != 'L', int(k[1:]) if k.startswith('L') else 0))
        for key in sorted_keys:
            if key.startswith('L'):
                flawed_nl[key] = self._modify_nl_line(flawed_nl[key])
        
        return flawed_nl

    def _generate_json_label(self) -> Dict[str, Any]:
        """Constructs the final structured JSON label using metadata-driven templates."""
        m = self.metadata
        explanation = "Error: Could not generate explanation."
        correction = "Error: Could not generate correction."

        if self.error_type == 'computational_error':
            explanation = f"There is a computational error. The solution states the result is {m['new_value']}, but the correct value is {m['original_value']}."
            correction = f"To correct this, replace the incorrect value {m['new_value']} with the correct value {m['original_value']}."

        elif self.error_type == 'incorrect_operation':
            # Safely get operator symbols
            original_op_symbol = self.op_map.get(ast.parse(m['original_op']).body[0].value.__class__, '?')
            new_op_symbol = self.op_map.get(ast.parse(m['new_op']).body[0].value.__class__, '?')
            
            explanation = f"The solution incorrectly uses a '{new_op_symbol}' operation where a '{original_op_symbol}' operation was needed."
            correction = f"To correct this, the operator should be changed from '{new_op_symbol}' to '{original_op_symbol}'."

        elif self.error_type == 'skipped_step':
            explanation = f"A necessary calculation step is missing. The solution fails to perform the step that would have defined the variable '{m['deleted_variable']}'."
            correction = f"To correct this, the following step must be inserted back into the solution: '{self.deleted_nl_line_text}'"
        
        elif self.error_type == 'incorrect_operand':
            explanation = f"The calculation uses an incorrect variable. It incorrectly references '{m['new_operand']}' instead of '{m['original_operand']}'."
            correction = f"To correct this, the variable '{m['new_operand']}' should be replaced with the correct variable, '{m['original_operand']}'."

        return {
            "verdict": "Flawed",
            "error_details": {
                "error_type": self.error_type,
                "erroneous_line_number": m['line_label'],
                "explanation": explanation,
                "correction": correction
            }
        }

    def inject_nl_error(self) -> Optional[Tuple[Dict[str, str], Dict[str, Any]]]:
        """
        Orchestrates the end-to-end process of generating a flawed NL solution
        and its corresponding JSON label.
        """
        if not self._load_data_sources():
            print("--- Process halted due to data loading failure. ---")
            return None
        
        flawed_nl_solution = self._generate_flawed_nl_solution()
        json_label = self._generate_json_label()
        
        return flawed_nl_solution, json_label


# ==============================================================================
# Example Usage
# ==============================================================================
if __name__ == '__main__':
    import inspect
    
    # Define project root relative to this script's location
    # In a real scenario, you might use a more robust method like find_project_root()
    try:
        PROJECT_ROOT = Path(__file__).parent.parent
    except NameError:
        PROJECT_ROOT = Path.cwd() # Fallback for interactive environments

    print(f"Using project root: {PROJECT_ROOT}\n")

    # --- Configuration for the example ---
    test_problem_index = 0
    test_model = "anthropic_claude-3-5-haiku-20241022"
    
    # We will test all relevant error types
    # NOTE: 'incorrect_operand' is excluded as per the instructions.
    test_error_types = ['computational_error', 'incorrect_operation', 'skipped_step']

    for error_type in test_error_types:
        print(f"============================================================")
        print(f"  Testing Injection for: {error_type.upper()}")
        print(f"============================================================\n")

        # 1. Instantiate the injector
        injector = NaturalLanguageErrorInjector(
            problem_index=test_problem_index,
            model_name=test_model,
            error_type=error_type,
            project_root=PROJECT_ROOT
        )

        # 2. Run the injection process
        result = injector.inject_nl_error()

        if result:
            flawed_solution, final_label = result
            
            # 3. Print the results
            print("--- Original NL Solution ---")
            print(json.dumps(injector.original_nl_solution, indent=4))
            
            print("\n--- Generated Flawed NL Solution ---")
            print(json.dumps(flawed_solution, indent=4))
            
            print("\n--- Generated JSON Label ---")
            print(json.dumps(final_label, indent=4))
            print("\n")
        else:
            print(f"Injection failed for {error_type}.\n")