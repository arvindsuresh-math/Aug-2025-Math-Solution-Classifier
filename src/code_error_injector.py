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