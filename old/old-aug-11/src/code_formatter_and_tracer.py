import re
from pathlib import Path

# ---------------------------------------------------------------------- #
#  Global constants & Configuration
# ---------------------------------------------------------------------- #

def find_project_root():
    """Traverse upwards to find the project root, marked by the .git folder."""
    current_path = Path.cwd()
    while current_path != current_path.parent:
        if (current_path / ".git").is_dir():
            return current_path
        current_path = current_path.parent
    raise FileNotFoundError("Could not find project root. Is this a git repository?")


PROJECT_ROOT = find_project_root()
BASE_INPUT_DIR = PROJECT_ROOT / 'data' / 'code_gen_outputs_cleaned'
BASE_OUTPUT_DIR = PROJECT_ROOT / 'data' / 'code_gen_outputs_formatted'
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

# ---------------------------------------------------------------------- #
#  Code Formatter
# ---------------------------------------------------------------------- #

def get_code_lines_dict(
        problem_index: int, 
        model_name: str, 
        base_input_dir: Path = BASE_INPUT_DIR):
    """
    Returns a dict mapping line numbers (0-based) to the verbatim lines of code
    for the given problem index and model name.
    """
    import sys
    problem_dir = base_input_dir / str(problem_index)
    file_path = problem_dir / f"{model_name}.py"
    if not file_path.exists():
        print(f"[Error] File not found: {file_path}", file=sys.stderr)
        return None
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return {i: line.rstrip("\n") for i, line in enumerate(lines)}


def replace_final_answer_comment(code_lines_dict):
    """
    Returns a new dict where any line that begins with 'answer =' (ignoring leading whitespace)
    is preceded by a '#: FA' comment line.
    """
    new_dict = {}
    new_idx = 0
    for idx in range(len(code_lines_dict)):
        line = code_lines_dict[idx]
        if line.lstrip().startswith("answer ="):
            new_dict[new_idx] = "#: FA"
            new_dict[new_idx + 1] = line
            new_idx += 2
        else:
            new_dict[new_idx] = line
            new_idx += 1
    return new_dict

def format_comment(comment_line):
    """
    Accepts a comment string. Returns '\n' if not in the format '#: ... Ln' or '#: FA'.
    If correct, returns '#: Ln' or '#: FA' (ignoring everything between).
    """
    comment_line = comment_line.strip()
    if comment_line.startswith("#:") and comment_line.endswith("FA"):
        return "#: FA"
    m = re.match(r"^#:(.*)L(\d+)\s*$", comment_line)
    if m:
        return f"#: L{m.group(2)}"
    return "\n"

def remove_trailing_comment(code_line):
    """
    Removes trailing comment from a code line.
    If it finds the trailing comment '# FINAL ANSWER', then it returns ': FA' on one line and the code on the next. If it finds any other comment, it just removes the comment and returns the code line.
    """
    if "#" not in code_line:
        return code_line
    code, _ = code_line.split("#", 1)
    return code.rstrip()

def remove_redundant_comments(lines):
    """
    Removes any comment line that is immediately followed by another comment line.
    But keeps '#: FA' comments even if followed by 'answer =' lines.
    """
    result = []
    for i, line in enumerate(lines):
        if line.startswith("#:"):
            # If next line is also a comment, skip this one
            if i + 1 < len(lines) and lines[i + 1].startswith("#:"):
                continue
            # If next line begins with "answer" and this is NOT a FA comment, skip this one
            if (i + 1 < len(lines) and 
                lines[i + 1].lstrip().startswith("answer") and 
                line.strip() != "#: FA"):
                continue
        result.append(line)
    return result

def format_generated_code(code_lines_dict):
    """
    Cleans and formats generated code according to the specified rules.
    """

    # Format the final answer portion
    code_lines_dict = replace_final_answer_comment(code_lines_dict)

    # Split into lines for further processing
    lines = list(code_lines_dict.values())

    # Find the end of the func signature/docstring
    sig_end = 0
    for i, line in enumerate(lines):
        if line.strip().endswith('"""'):
            sig_end = i
            break
    signature = lines[:sig_end + 1]
    body = lines[sig_end + 1:]

    # Format comments and remove trailing comments
    processed = []
    for line in body:
        stripped = line.strip()
        if stripped.startswith("#"):
            processed.append(format_comment(stripped))
        elif stripped == "":
            processed.append("\n")
        else:
            processed.append(remove_trailing_comment(line))

    # Remove all line breaks, keep only comments or code
    processed = [l for l in processed if l.strip() != ""]

    # Third pass: remove redundant comments
    processed = remove_redundant_comments(processed)

    # Assemble final code: signature, then body with correct indentation and blank lines before comments
    final_lines = signature.copy()
    indent = "    "
    for line in processed:
        if line.startswith("#:"):
            final_lines.append("")  # blank line before comment
            final_lines.append(f"{indent}{line}")
        else:
            final_lines.append(f"{indent}{line.strip()}")

    # Remove any extra blank lines at the end
    while final_lines and final_lines[-1].strip() == "":
        final_lines.pop()

    return "\n".join(final_lines)

def batch_format_and_write(
    indices,
    models = MODELS,
    base_input_dir = BASE_INPUT_DIR,
    base_output_dir = BASE_OUTPUT_DIR,
    get_code_lines_dict=get_code_lines_dict,
    format_generated_code=format_generated_code
):
    """
    For each (index, model), generate formatted code and write to {base_output_dir}/{index}/{model}.py
    """
    for idx in indices:
        for model in models:
            code_lines_dict = get_code_lines_dict(idx, model, base_input_dir)
            if code_lines_dict is None:
                print(f"[Warning] No code for index={idx}, model={model}")
                continue
            formatted_code = format_generated_code(code_lines_dict)
            out_dir = base_output_dir / str(idx)
            out_dir.mkdir(parents=True, exist_ok=True)
            out_path = out_dir / f"{model}.py"
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(formatted_code)
            print(f"Wrote formatted code to {out_path}")


# ---------------------------------------------------------------------- #
# Code Tracer
# ---------------------------------------------------------------------- #

def execution_trace(func):
    import inspect, ast
    src = inspect.getsource(func)
    tree = ast.parse(src)
    func_def = tree.body[0]
    env = {}
    for arg, default in zip(
        func_def.args.args[::-1], 
        func_def.args.defaults[::-1]
    ):
        env[arg.arg] = eval(compile(ast.Expression(default), '', 'eval'))
    for stmt in func_def.body:
        if isinstance(stmt, ast.Assign):
            code = compile(ast.Module([stmt], []), '', 'exec')
            exec(code, {}, env)
    # Return all variables, including arguments
    return env

def augment_code_with_trace(
    problem_index: int,
    model_name: str,
    input_dir: Path,
    output_dir: Path,
    verbose: bool = True
):
    """
    Augment a single Python file with execution trace comments using simple string replacement.
    """
    # Step 1: Get the individual lines of code
    code_lines_dict = get_code_lines_dict(problem_index, model_name, input_dir)
    if code_lines_dict is None:
        if verbose:
            print(f"Could not get code lines for problem {problem_index}, model {model_name}")
        return False
    
    try:
        # Load the module and get execution trace
        input_file = input_dir / str(problem_index) / f"{model_name}.py"
        spec = importlib.util.spec_from_file_location("module.name", input_file)
        if spec is None or spec.loader is None:
            if verbose:
                print(f"Could not load module spec for {input_file}")
            return False
                
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Get execution trace
        trace_dict = execution_trace(module.solve)
        
        # Step 2: Find the end of function signature (including docstring)
        lines = list(code_lines_dict.values())
        sig_end = -1
        for i, line in enumerate(lines):
            if line.strip().endswith('"""'):
                sig_end = i
                break
        
        if sig_end == -1:
            if verbose:
                print(f"Could not find end of docstring for {model_name}")
            return False
        
        # Split into signature and body
        signature_lines = lines[:sig_end + 1]
        body_lines = lines[sig_end + 1:]
        
        # Step 3-5: Process body lines
        processed_body = ""  # Start as empty string instead of list
        for line in body_lines:
            # Step 3: Add comment lines
            if line.strip().startswith('#'):
                processed_body += '\n'  # Add a blank line before comments
                processed_body += line + '\n'  # Append line with newline
                continue
            elif line.strip().startswith('answer ='):
                processed_body += line + '\n' # Do not add eval comment for answer lines
                continue
            
            # Step 4: For code lines, do search and replace
            if line.strip():  # Non-empty line
                eval_line = line
                sorted_trace_dict = sorted(trace_dict.items(), key=lambda x: len(x[0]), reverse=True)
                
                # Replace each variable with its value
                substituted = False
                for variable, value in sorted_trace_dict:
                    if variable in eval_line:
                        eval_line = eval_line.replace(variable, str(value))
                        substituted = True
                
                # Step 5: Append eval comment if any substitution happened
                if substituted:
                    # Get indentation from original line
                    new_line = line + " # eval: " + eval_line.lstrip()
                    processed_body += new_line + '\n'  # Append with newline
                else:
                    # If no substitution, just append the original line
                    processed_body += line + '\n'  # Append with newline
        
        # Step 6: Concatenate and save
        # Convert signature_lines to string and concatenate with processed_body
        signature_code = '\n'.join(signature_lines) + '\n'
        final_code = signature_code + processed_body
        
        # Write to output file
        output_file = output_dir / str(problem_index) / f"{model_name}.py"
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_code)
        
        if verbose:
            print(f"Augmented {model_name} for problem {problem_index}")
        return True
        
    except Exception as e:
        if verbose:
            print(f"Error processing problem {problem_index}, model {model_name}: {e}")
        return False

def batch_augment_with_trace(
    indices: list,
    models: list = MODELS,
    input_dir: Path = PROJECT_ROOT / 'data' / 'code_gen_outputs_formatted',
    output_dir: Path = PROJECT_ROOT / 'data' / 'code_gen_outputs_traced',
    verbose: bool = True
):
    """
    Batch process multiple problems and models to augment code with execution traces.
    """
    success_count = 0
    total_count = 0
    
    for idx in indices:
        if verbose:
            print(f"Processing problem {idx}...")
        
        for model in models:
            total_count += 1
            if augment_code_with_trace(idx, model, input_dir, output_dir, verbose):
                success_count += 1
    
    if verbose:
        print(f"Completed: {success_count}/{total_count} files processed successfully")
