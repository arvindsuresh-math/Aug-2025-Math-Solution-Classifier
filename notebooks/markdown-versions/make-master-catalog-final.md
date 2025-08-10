```python
import json
import random
import re
from pathlib import Path
from typing import List, Dict, Set, Tuple

import pandas as pd
from datasets import load_dataset, Dataset, DatasetDict
from tqdm.auto import tqdm

# --- Path and Directory Definitions ---

def find_project_root(marker: str = ".git") -> Path:
    """Traverse upwards to find the project root, marked by the git repository."""
    current_path = Path.cwd().resolve()
    while current_path != current_path.parent:
        if (current_path / marker).exists():
            return current_path
        current_path = current_path.parent
    raise FileNotFoundError(f"Could not find project root. Marker '{marker}' not found.")

VALIDATORS = ["ali", "arvind", "mauro", "ling", "yewei"]

PROJECT_ROOT = find_project_root()
DATA_DIR = PROJECT_ROOT / 'data'
CONCEPTUAL_ERRORS_DIR = DATA_DIR / 'conceptual-errors-accepted'
COMPUTATIONAL_ERRORS_DIR = DATA_DIR / 'computational-errors-generated'
CONCEPTUAL_CATALOG_DIR = DATA_DIR / 'conceptual-error-candidates'

# load all catalog filepaths into a dict
CATALOG_FILEPATH_DICT = {
    "manual": DATA_DIR / 'manually_generated_errors_final.csv',
    "computational": COMPUTATIONAL_ERRORS_DIR / 'computational_error_catalog.csv'
}
for name in VALIDATORS:
    CATALOG_FILEPATH_DICT[f"conceptual_{name}"] = CONCEPTUAL_CATALOG_DIR / f'validation_catalog_{name}.csv'

# Display the filepaths
for name, path in CATALOG_FILEPATH_DICT.items():
    print(f"{name}: {path}")

# make dictionary with all catalogs
CATALOG_DICT = {key: pd.read_csv(path) for key, path in CATALOG_FILEPATH_DICT.items()}
```

    manual: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/manually_generated_errors_final.csv
    computational: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/computational-errors-generated/computational_error_catalog.csv
    conceptual_ali: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/conceptual-error-candidates/validation_catalog_ali.csv
    conceptual_arvind: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/conceptual-error-candidates/validation_catalog_arvind.csv
    conceptual_mauro: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/conceptual-error-candidates/validation_catalog_mauro.csv
    conceptual_ling: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/conceptual-error-candidates/validation_catalog_ling.csv
    conceptual_yewei: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/conceptual-error-candidates/validation_catalog_yewei.csv



```python
for key, df in CATALOG_DICT.items():
    print(f"{key}: {len(df)} rows")
    print("columns:", df.columns.tolist())
```

    manual: 1963 rows
    columns: ['answer', 'erroneous_line_number', 'error_type', 'explanation', 'filepath', 'index', 'question', 'wrong_answer']
    computational: 22623 rows
    columns: ['index', 'tier', 'model', 'erroneous_line_number', 'explanation', 'wrong_answer', 'correct_trace_generated', 'target_variable', 'error_type', 'correct_value', 'flawed_value', 'repro_seed', 'date_utc', 'time_utc', 'filepath']
    conceptual_ali: 398 rows
    columns: ['index', 'tier', 'model', 'mutation_type', 'target_variable', 'correct_value', 'flawed_value', 'repro_seed', 'decision_date_utc', 'decision_time_utc', 'status', 'manual_edits', 'filepath', 'validator', 'tier_numeric', 'priority']
    conceptual_arvind: 394 rows
    columns: ['index', 'tier', 'model', 'mutation_type', 'target_variable', 'correct_value', 'flawed_value', 'repro_seed', 'decision_date_utc', 'decision_time_utc', 'status', 'manual_edits', 'filepath', 'validator', 'tier_numeric', 'priority']
    conceptual_mauro: 381 rows
    columns: ['index', 'tier', 'model', 'mutation_type', 'target_variable', 'correct_value', 'flawed_value', 'repro_seed', 'decision_date_utc', 'decision_time_utc', 'status', 'manual_edits', 'filepath', 'validator', 'tier_numeric', 'priority']
    conceptual_ling: 388 rows
    columns: ['index', 'tier', 'model', 'mutation_type', 'target_variable', 'correct_value', 'flawed_value', 'repro_seed', 'decision_date_utc', 'decision_time_utc', 'status', 'manual_edits', 'filepath', 'validator', 'tier_numeric', 'priority']
    conceptual_yewei: 381 rows
    columns: ['index', 'tier', 'model', 'mutation_type', 'target_variable', 'correct_value', 'flawed_value', 'repro_seed', 'decision_date_utc', 'decision_time_utc', 'status', 'manual_edits', 'filepath', 'validator', 'tier_numeric', 'priority']



```python
GSM8K_TRAIN = load_dataset("gsm8k", "main")["train"]
```


```python
# --- Tier Definition Functions (copied from arvind-july-25.ipynb) ---

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

def mutually_disjoint_tiers(dataset):
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

# --- Create Tier Mappings ---

def add_tier_column(df, tier_lists):
    """
    Adds a 'tier' column to the dataframe based on the TIER_LISTS dictionary.
    Maps each GSM8K index to its corresponding tier.
    """
    index_to_tier = {}
    for tier_name, indices in tier_lists.items():
        for idx in indices:
            index_to_tier[idx] = tier_name
    
    df['tier'] = df['index'].map(index_to_tier)
    
    missing_tiers = df['tier'].isna().sum()
    if missing_tiers > 0:
        print(f"Warning: {missing_tiers} indices could not be mapped to tiers")
        df['tier'] = df['tier'].fillna('unknown')
    
    return df

# Generate tier mappings for the entire GSM8K dataset
TIER_LISTS = mutually_disjoint_tiers(GSM8K_TRAIN)
print("Tier distribution in GSM8K:")
for tier, indices in TIER_LISTS.items():
    print(f"  {tier}: {len(indices)} problems")
```

    Tier distribution in GSM8K:
      tier1: 2767 problems
      tier2: 837 problems
      tier3: 3113 problems
      tier4: 544 problems
      tier5: 212 problems



```python
def sanitize_text(text: str) -> str:
    """
    Comprehensive text sanitization function that:
    1. Converts literal \n to actual newlines
    2. Replaces problematic Unicode characters with ASCII equivalents
    3. Removes comma separators from numbers
    
    This prevents model generation and string parsing errors.
    """
    text = text.replace('\\n', '\n')

    replacements = {
        "\u2212": "-",    # Minus Sign
        "\u00d7": "*",    # Multiplication Sign
        "\u00f7": "/",    # Division Sign
        "\u22c5": "*",    # Dot Operator
        "\u201c": '"',    # Left Double Quotation Mark
        "\u201d": '"',    # Right Double Quotation Mark
        "\u2018": "'",    # Left Single Quotation Mark
        "\u2019": "'",    # Right Single Quotation Mark
        "\u2014": "-",    # Em Dash
        "\u2013": "-",    # En Dash
        "\u2026": "...",  # Horizontal Ellipsis
        "\u00a0": " ",    # No-Break Space
        "\u00f1": "n",    # Spanish ñ -> n
        "\u200b": "",     # Zero Width Space -> remove completely
    }
    for uni, ascii_char in replacements.items():
        text = text.replace(uni, ascii_char)

    text = re.sub(r'(\d),(\d)', r'\1\2', text)
    
    return text

def make_answer_mapping(answer: str) -> Dict[str, str]:
    """
    Create a mapping from line numbers to solution lines from sanitized answer text.
    Returns a dict mapping line identifiers ("L1", "L2", ..., "FA") to solution lines
    WITHOUT calculator annotations.
    """
    lines = answer.split('\n')
    final_answer = None
    answer_mapping = {}

    if lines and re.match(r'^\s*####\s*.*$', lines[-1]):
        final_answer_line = lines.pop().strip()
        match = re.search(r'####\s*(.*)', final_answer_line)
        if match:
            final_answer = match.group(1).strip()

    cleaned_lines = [line.strip() for line in lines if line.strip()]
    for i, line in enumerate(cleaned_lines):
        # Remove calculator annotations from each line
        clean_line = re.sub(r'<<.*?>>', '', line).strip()
        answer_mapping[f"L{i+1}"] = clean_line
    
    if final_answer is not None:
        answer_mapping["FA"] = final_answer
    
    return answer_mapping

def make_separate_mappings(answer: str) -> Tuple[Dict[str, str], Dict[str, str]]:
    """
    Extract calculator equations and create clean answer mapping without annotations.
    Takes the original answer text and returns both equation mapping and clean answer mapping.
    """
    lines = answer.split('\n')
    final_answer = None
    
    # Handle final answer line
    if lines and re.match(r'^\s*####\s*.*$', lines[-1]):
        final_answer_line = lines.pop().strip()
        match = re.search(r'####\s*(.*)', final_answer_line)
        if match:
            final_answer = match.group(1).strip()

    cleaned_lines = [line.strip() for line in lines if line.strip()]
    
    eqn_mapping = {}
    clean_answer_mapping = {}
    
    for i, line in enumerate(cleaned_lines):
        line_id = f"L{i+1}"
        
        # Extract calculator equations
        calculator_matches = re.findall(r'<<(.*?)>>', line)
        if calculator_matches:
            eqn_mapping[line_id] = calculator_matches[0]
        else:
            eqn_mapping[line_id] = ""
        
        # Create clean text without calculator annotations
        clean_text = re.sub(r'<<.*?>>', '', line).strip()
        clean_answer_mapping[line_id] = clean_text
    
    # Handle final answer
    if final_answer is not None:
        clean_answer_mapping["FA"] = final_answer
        eqn_mapping["FA"] = ""
    
    return eqn_mapping, clean_answer_mapping

def reconstruct_answer_from_clean_mapping(clean_mapping: Dict[str, str]) -> str:
    """
    Returns a reconstructed answer text from clean mapping with FINAL ANSWER: prefix.
    """
    if not clean_mapping:
        return ""
    
    lines = []
    i = 1
    while f"L{i}" in clean_mapping:
        line_text = clean_mapping[f"L{i}"].strip()
        if line_text:
            lines.append(line_text)
        i += 1
    
    if "FA" in clean_mapping and clean_mapping["FA"].strip():
        lines.append(f"FINAL ANSWER: {clean_mapping['FA'].strip()}")
    
    return '\n'.join(lines)

def process_answer_with_full_mappings(
        answer_text: str,
        answer_prefix: str) -> Dict[str, any]:
    """
    Process an answer text and extract all mappings and derived information.
    
    Args:
        answer_text: Raw answer text
        answer_prefix: "correct" or "flawed"
    
    Returns:
        Dict containing all processed information or None if processing fails
    """
    try:
        sanitized_text = sanitize_text(answer_text)
        
        # Extract equations and clean mappings from original text
        eqn_mapping, clean_answer_mapping = make_separate_mappings(sanitized_text)
        
        if not clean_answer_mapping:
            return None

        # Reconstruct clean answer
        reconstructed_answer = reconstruct_answer_from_clean_mapping(clean_answer_mapping)
        
        # Store the CLEAN mapping as the main answer mapping
        answer_mapping_json = json.dumps(clean_answer_mapping, ensure_ascii=False, indent=2)
        eqn_mapping_json = json.dumps(eqn_mapping, ensure_ascii=False, indent=2)

        return {
            answer_prefix + '_answer': reconstructed_answer,
            answer_prefix + '_mapping': answer_mapping_json,  # Now clean
            answer_prefix + '_eqn_mapping': eqn_mapping_json,
            answer_prefix + '_answer_length': len(clean_answer_mapping)
        }
        
    except Exception as e:
        # Any processing error returns None, will be handled as problematic
        return None

def validate_line_number_with_mapping(erroneous_line_number: str, answer_mapping: Dict[str, str]) -> bool:
    """
    Returns True if the erroneous line number exists in the answer mapping, False otherwise.
    """
    if not erroneous_line_number or not answer_mapping:
        return False
    return erroneous_line_number in answer_mapping
```


```python
def process_single_catalog_row(
        gsm8k_problem: Dict, 
        wrong_answer_text: str,
        erroneous_line_number: str, 
        explanation: str,
        error_type: str, 
        error_subtype: str, 
        source: str,
        tier_lists: Dict,
        catalog_index: int) -> Tuple[Dict[str, any], bool]:
    """
    Process a single catalog row and return all required columns.
    
    Args:
        gsm8k_problem: GSM8K problem data
        wrong_answer_text: Wrong answer text
        erroneous_line_number: Line identifier with error
        explanation: Error explanation
        error_type: Type of error (computational_error/conceptual_error)
        error_subtype: Subtype of error
        source: Source of data (manual/programmatic)
        tier_lists: Tier mapping dictionary
        catalog_index: The GSM8K index from the source catalog
    
    Returns:
        Tuple of (processed_row_dict, is_successful)
    """
    try:
        problem_index = catalog_index
        
        # Determine tier
        problem_tier = None
        for tier_name, indices in tier_lists.items():
            if problem_index in indices:
                problem_tier = tier_name
                break
        
        # Process question
        cleaned_question = sanitize_text(gsm8k_problem['question'])
        
        # Process correct answer
        correct_processed = process_answer_with_full_mappings(gsm8k_problem['answer'], "correct")
        if not correct_processed:
            return {}, False
        
        # Process wrong answer
        wrong_processed = process_answer_with_full_mappings(wrong_answer_text, "wrong")
        if not wrong_processed:
            return {}, False
        
        # Parse the clean mappings for validation and line extraction
        correct_mapping = json.loads(correct_processed['correct_mapping'])
        wrong_mapping = json.loads(wrong_processed['wrong_mapping'])
        wrong_eqn_mapping = json.loads(wrong_processed['wrong_eqn_mapping'])
        
        # Validate erroneous line number against correct answer
        if not validate_line_number_with_mapping(erroneous_line_number, correct_mapping):
            return {}, False
        
        # Extract erroneous line information from wrong answer (already clean)
        if erroneous_line_number == "FA":
            # For final answer, reconstruct with "FINAL ANSWER:" prefix
            fa_content = wrong_mapping.get("FA", "")
            erroneous_line = f"FINAL ANSWER: {fa_content}" if fa_content else ""
        else:
            # For regular lines, use the clean version directly
            erroneous_line = wrong_mapping.get(erroneous_line_number, "")

        erroneous_line_eqn = wrong_eqn_mapping.get(erroneous_line_number, "")
        
        # Build the complete row
        processed_row = {
            'index': problem_index,
            'tier': problem_tier,
            'question': cleaned_question,
            'correct_answer': correct_processed['correct_answer'],
            'wrong_answer': wrong_processed['wrong_answer'],
            'error_type': error_type,
            'explanation': explanation,
            'erroneous_line_number': erroneous_line_number,
            'erroneous_line': erroneous_line,
            'erroneous_line_eqn': erroneous_line_eqn,
            'correct_answer_mapping': correct_processed['correct_mapping'],
            'wrong_answer_mapping': wrong_processed['wrong_mapping'],
            'correct_eqn_mapping': correct_processed['correct_eqn_mapping'],
            'wrong_eqn_mapping': wrong_processed['wrong_eqn_mapping'],
            'correct_answer_length': correct_processed['correct_answer_length'],
            'wrong_answer_length': wrong_processed['wrong_answer_length'],
            'source': source,
            'error_subtype': error_subtype
        }
        
        return processed_row, True
        
    except Exception as e:
        return {}, False
```


```python
def process_manual_catalog_with_new_pipeline(catalog_dict, gsm8k_train, tier_lists) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Process manual catalog using the new pipeline with full mappings.
    """
    print("=== Processing Manual Catalog with New Pipeline ===")
    
    df = catalog_dict['manual'].copy()
    print(f"Initial rows: {len(df)}")
    
    clean_rows = []
    problematic_rows = []
    
    for idx, row in tqdm(df.iterrows(), total=len(df), desc="Processing manual catalog"):
        try:
            problem_index = int(row['index'])
            
            # Check if erroneous_line_number is missing
            if pd.isna(row['erroneous_line_number']):
                problematic_rows.append({
                    **row.to_dict(),
                    'error_reason': 'Missing erroneous_line_number',
                    'source_catalog': 'manual'
                })
                continue
            
            # Get GSM8K data
            if problem_index >= len(gsm8k_train):
                problematic_rows.append({
                    **row.to_dict(),
                    'error_reason': f'Index {problem_index} out of range',
                    'source_catalog': 'manual'
                })
                continue
                
            gsm8k_problem = gsm8k_train[problem_index]
            
            # Process using the new pipeline
            processed_row, success = process_single_catalog_row(
                gsm8k_problem=gsm8k_problem,
                wrong_answer_text=row['wrong_answer'],
                erroneous_line_number=row['erroneous_line_number'],
                explanation=row['explanation'],
                error_type=row['error_type'] + '_error',
                error_subtype='NA',
                source='manual',
                tier_lists=tier_lists,
                catalog_index=problem_index  # Add this line
            )
            
            if success:
                clean_rows.append(processed_row)
            else:
                problematic_rows.append({
                    **row.to_dict(),
                    'error_reason': 'Processing failed in pipeline',
                    'source_catalog': 'manual'
                })
            
        except Exception as e:
            problematic_rows.append({
                **row.to_dict(),
                'error_reason': f'Processing error: {str(e)}',
                'source_catalog': 'manual'
            })
    
    clean_df = pd.DataFrame(clean_rows)
    problematic_df = pd.DataFrame(problematic_rows)
    
    print(f"Clean rows: {len(clean_df)}")
    print(f"Problematic rows: {len(problematic_df)}")
    
    return clean_df, problematic_df

def process_computational_catalog_with_new_pipeline(catalog_dict, gsm8k_train, tier_lists) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Process computational catalog using the new pipeline with full mappings.
    """
    print("=== Processing Computational Catalog with New Pipeline ===")
    
    df = catalog_dict['computational'].copy()
    print(f"Initial rows: {len(df)}")
    
    clean_rows = []
    problematic_rows = []
    
    for idx, row in tqdm(df.iterrows(), total=len(df), desc="Processing computational catalog"):
        try:
            problem_index = int(row['index'])
            
            # Check if erroneous_line_number is missing
            if pd.isna(row['erroneous_line_number']):
                problematic_rows.append({
                    **row.to_dict(),
                    'error_reason': 'Missing erroneous_line_number',
                    'source_catalog': 'computational'
                })
                continue
            
            # Get GSM8K data
            if problem_index >= len(gsm8k_train):
                problematic_rows.append({
                    **row.to_dict(),
                    'error_reason': f'Index {problem_index} out of range',
                    'source_catalog': 'computational'
                })
                continue
                
            gsm8k_problem = gsm8k_train[problem_index]
            
            # Check if this is tier5 and exclude it
            problem_tier = None
            for tier_name, indices in tier_lists.items():
                if problem_index in indices:
                    problem_tier = tier_name
                    break
            
            if problem_tier == 'tier5':
                problematic_rows.append({
                    **row.to_dict(),
                    'error_reason': 'Excluded tier5 problem',
                    'source_catalog': 'computational'
                })
                continue
            
            # Process using the new pipeline
            processed_row, success = process_single_catalog_row(
                gsm8k_problem=gsm8k_problem,
                wrong_answer_text=row['wrong_answer'],
                erroneous_line_number=row['erroneous_line_number'],
                explanation=row['explanation'],
                error_type='computational_error',
                error_subtype=row['error_type'],
                source='programmatic',
                tier_lists=tier_lists,
                catalog_index=problem_index  # Add this line
            )
            
            if success:
                clean_rows.append(processed_row)
            else:
                problematic_rows.append({
                    **row.to_dict(),
                    'error_reason': 'Processing failed in pipeline',
                    'source_catalog': 'computational'
                })
            
        except Exception as e:
            problematic_rows.append({
                **row.to_dict(),
                'error_reason': f'Processing error: {str(e)}',
                'source_catalog': 'computational'
            })
    
    clean_df = pd.DataFrame(clean_rows)
    problematic_df = pd.DataFrame(problematic_rows)
    
    print(f"Clean rows: {len(clean_df)}")
    print(f"Problematic rows: {len(problematic_df)}")
    
    return clean_df, problematic_df

def process_validator_catalogs_with_new_pipeline(catalog_dict, gsm8k_train, tier_lists, validators, project_root) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Process all validator catalogs using the new pipeline with full mappings.
    """
    print("=== Processing Validator Catalogs with New Pipeline ===")
    
    all_clean_rows = []
    all_problematic_rows = []
    
    def check_file_exists_and_get_path(filepath, base_dir=None):
        """
        Check if a file exists and return the correct path, handling cross-platform path issues.
        """
        if pd.isna(filepath) or filepath == "":
            return None, False
        
        normalized_filepath = str(filepath).replace('\\', '/')
        file_path = Path(normalized_filepath)
        
        if not file_path.is_absolute():
            full_path = project_root / file_path
        else:
            full_path = file_path
        
        return full_path, full_path.exists()
    
    def fix_answer_formatting(wrong_answer: str) -> str:
        """
        Fixes the formatting of wrong answers by moving the final answer line
        from the beginning to the end if it's misplaced.
        """
        if not isinstance(wrong_answer, str):
            return wrong_answer
        
        lines = wrong_answer.strip().split('\n')
        final_answer_line = None
        other_lines = []
        
        for line in lines:
            if re.match(r'^\s*####\s*.*$', line.strip()):
                final_answer_line = line.strip()
            elif line.strip():
                other_lines.append(line)
        
        if final_answer_line and other_lines:
            return '\n'.join(other_lines) + '\n' + final_answer_line
        elif final_answer_line:
            return final_answer_line
        else:
            return wrong_answer
    
    for validator in validators:
        print(f"\nProcessing validator: {validator}")
        df = catalog_dict[f'conceptual_{validator}'].copy()
        
        # Filter to only accepted samples
        df = df[df['status'] == 'accepted']
        print(f"Accepted rows for {validator}: {len(df)}")
        
        for idx, row in tqdm(df.iterrows(), total=len(df), desc=f"Processing {validator}"):
            try:
                problem_index = int(row['index'])
                
                # Get GSM8K data
                if problem_index >= len(gsm8k_train):
                    all_problematic_rows.append({
                        **row.to_dict(),
                        'error_reason': f'Index {problem_index} out of range',
                        'source_catalog': f'conceptual_{validator}'
                    })
                    continue
                    
                gsm8k_problem = gsm8k_train[problem_index]
                
                # Check if this is tier5 and exclude it
                problem_tier = None
                for tier_name, indices in tier_lists.items():
                    if problem_index in indices:
                        problem_tier = tier_name
                        break
                
                if problem_tier == 'tier5':
                    all_problematic_rows.append({
                        **row.to_dict(),
                        'error_reason': 'Excluded tier5 problem',
                        'source_catalog': f'conceptual_{validator}'
                    })
                    continue
                
                # Load JSON file with proper path handling
                try:
                    filepath, file_exists = check_file_exists_and_get_path(row['filepath'])
                    
                    if not file_exists or filepath is None:
                        all_problematic_rows.append({
                            **row.to_dict(),
                            'error_reason': f'JSON file not found: {row["filepath"]}',
                            'source_catalog': f'conceptual_{validator}'
                        })
                        continue
                    
                    with open(filepath, 'r', encoding='utf-8') as f:
                        json_data = json.load(f)
                        
                except Exception as e:
                    all_problematic_rows.append({
                        **row.to_dict(),
                        'error_reason': f'JSON loading error: {str(e)}',
                        'source_catalog': f'conceptual_{validator}'
                    })
                    continue
                
                # Extract data from JSON
                try:
                    raw_wrong_answer = json_data['context']['flawed_solution']
                    explanation = json_data['error_details']['explanation']
                    erroneous_line_number = json_data['error_details']['erroneous_line_number']
                    error_subtype = json_data['error_details']['error_type']
                except KeyError as e:
                    all_problematic_rows.append({
                        **row.to_dict(),
                        'error_reason': f'Missing JSON field: {str(e)}',
                        'source_catalog': f'conceptual_{validator}'
                    })
                    continue
                
                # Fix the answer formatting
                wrong_answer = fix_answer_formatting(raw_wrong_answer)
                
                # Check for null erroneous_line_number
                if erroneous_line_number is None or erroneous_line_number == "null":
                    all_problematic_rows.append({
                        **row.to_dict(),
                        'error_reason': f'Null erroneous_line_number in JSON',
                        'source_catalog': f'conceptual_{validator}'
                    })
                    continue
                
                # Process using the new pipeline
                processed_row, success = process_single_catalog_row(
                    gsm8k_problem=gsm8k_problem,
                    wrong_answer_text=wrong_answer,
                    erroneous_line_number=erroneous_line_number,
                    explanation=explanation,
                    error_type='conceptual_error',
                    error_subtype=error_subtype,
                    source='programmatic',
                    tier_lists=tier_lists,
                    catalog_index=problem_index  # Add this line
                )
                
                if success:
                    all_clean_rows.append(processed_row)
                else:
                    all_problematic_rows.append({
                        **row.to_dict(),
                        'error_reason': 'Processing failed in pipeline',
                        'source_catalog': f'conceptual_{validator}'
                    })
                
            except Exception as e:
                all_problematic_rows.append({
                    **row.to_dict(),
                    'error_reason': f'Processing error: {str(e)}',
                    'source_catalog': f'conceptual_{validator}'
                })
    
    clean_df = pd.DataFrame(all_clean_rows)
    problematic_df = pd.DataFrame(all_problematic_rows)
    
    print(f"\nTotal clean rows: {len(clean_df)}")
    print(f"Total problematic rows: {len(problematic_df)}")
    
    return clean_df, problematic_df
```


```python
MASTER_CATALOG_COLUMNS = [
    'index', 
    'tier', 
    'question', 
    'correct_answer', 
    'wrong_answer', 
    'error_type', 
    'explanation', 
    'erroneous_line_number', 
    'erroneous_line', 
    'erroneous_line_eqn', 
    'correct_answer_mapping', 
    'wrong_answer_mapping',
    'correct_eqn_mapping', 
    'wrong_eqn_mapping', 
    'correct_answer_length',
    'wrong_answer_length', 
    'source', 
    'error_subtype'
]

def create_master_catalogs_with_new_structure(manual_clean, computational_clean, validator_clean, 
                          manual_problematic, computational_problematic, validator_problematic):
    """
    Combines all clean and problematic dataframes into final master catalogs with new structure.
    """
    print("=== Creating Master Catalogs with New Structure ===")
    
    # Combine all clean dataframes
    all_clean_dfs = []
    if not manual_clean.empty:
        all_clean_dfs.append(manual_clean)
    if not computational_clean.empty:
        all_clean_dfs.append(computational_clean)
    if not validator_clean.empty:
        all_clean_dfs.append(validator_clean)
    
    master_catalog = pd.concat(all_clean_dfs, ignore_index=True) if all_clean_dfs else pd.DataFrame()
    
    # Combine all problematic dataframes
    all_problematic_dfs = []
    if not manual_problematic.empty:
        all_problematic_dfs.append(manual_problematic)
    if not computational_problematic.empty:
        all_problematic_dfs.append(computational_problematic)
    if not validator_problematic.empty:
        all_problematic_dfs.append(validator_problematic)
    
    catalog_problematic = pd.concat(all_problematic_dfs, ignore_index=True) if all_problematic_dfs else pd.DataFrame()
    
    # Ensure consistent column order for master catalog
    if not master_catalog.empty:
        master_catalog = master_catalog[MASTER_CATALOG_COLUMNS]
    
    print(f"Master catalog rows: {len(master_catalog)}")
    print(f"Problematic rows: {len(catalog_problematic)}")
    
    return master_catalog, catalog_problematic
```


```python
# 1. Run the full pipeline
print("🚀 Starting Full Pipeline Execution")
print("=" * 80)

# Process manual catalog
manual_clean, manual_problematic = process_manual_catalog_with_new_pipeline(
    CATALOG_DICT, GSM8K_TRAIN, TIER_LISTS
)

# Process computational catalog  
computational_clean, computational_problematic = process_computational_catalog_with_new_pipeline(
    CATALOG_DICT, GSM8K_TRAIN, TIER_LISTS
)

# Process validator catalogs
validator_clean, validator_problematic = process_validator_catalogs_with_new_pipeline(
    CATALOG_DICT, GSM8K_TRAIN, TIER_LISTS, VALIDATORS, PROJECT_ROOT
)

# Create master catalogs
master_catalog, catalog_problematic = create_master_catalogs_with_new_structure(
    manual_clean, computational_clean, validator_clean,
    manual_problematic, computational_problematic, validator_problematic
)

print("\n🎉 Pipeline Execution Complete!")
print(f"✅ Master catalog: {len(master_catalog):,} rows")
print(f"❌ Problematic rows: {len(catalog_problematic):,} rows")
```

    🚀 Starting Full Pipeline Execution
    ================================================================================
    === Processing Manual Catalog with New Pipeline ===
    Initial rows: 1963



    Processing manual catalog:   0%|          | 0/1963 [00:00<?, ?it/s]


    Clean rows: 1740
    Problematic rows: 223
    === Processing Computational Catalog with New Pipeline ===
    Initial rows: 22623



    Processing computational catalog:   0%|          | 0/22623 [00:00<?, ?it/s]


    Clean rows: 21768
    Problematic rows: 855
    === Processing Validator Catalogs with New Pipeline ===
    
    Processing validator: ali
    Accepted rows for ali: 341



    Processing ali:   0%|          | 0/341 [00:00<?, ?it/s]


    
    Processing validator: arvind
    Accepted rows for arvind: 91



    Processing arvind:   0%|          | 0/91 [00:00<?, ?it/s]


    
    Processing validator: mauro
    Accepted rows for mauro: 312



    Processing mauro:   0%|          | 0/312 [00:00<?, ?it/s]


    
    Processing validator: ling
    Accepted rows for ling: 110



    Processing ling:   0%|          | 0/110 [00:00<?, ?it/s]


    
    Processing validator: yewei
    Accepted rows for yewei: 290



    Processing yewei:   0%|          | 0/290 [00:00<?, ?it/s]


    
    Total clean rows: 1144
    Total problematic rows: 0
    === Creating Master Catalogs with New Structure ===
    Master catalog rows: 24652
    Problematic rows: 1078
    
    🎉 Pipeline Execution Complete!
    ✅ Master catalog: 24,652 rows
    ❌ Problematic rows: 1,078 rows



```python
# 2. Pretty print one randomly chosen row from each catalog source
import json

def pretty_print_sample_rows_by_source(master_catalog):
    """
    Pretty prints one randomly chosen row from each source catalog.
    """
    print("🎲 RANDOM SAMPLE FROM EACH SOURCE CATALOG")
    print("=" * 80)
    
    if master_catalog.empty:
        print("❌ Master catalog is empty!")
        return
    
    # Define source mappings
    source_mappings = {
        'manual': 'Manual Catalog',
        'computational': 'Computational Catalog', 
        'conceptual_ali': 'Conceptual Validator - Ali',
        'conceptual_arvind': 'Conceptual Validator - Arvind',
        'conceptual_mauro': 'Conceptual Validator - Mauro',
        'conceptual_ling': 'Conceptual Validator - Ling',
        'conceptual_yewei': 'Conceptual Validator - Yewei'
    }
    
    # Get available sources in the data
    available_sources = master_catalog['source'].unique()
    error_types = master_catalog['error_type'].unique()
    
    # Sample one row from each available source/error_type combination
    sampled_sources = set()
    
    # First priority: manual source
    if 'manual' in available_sources:
        manual_samples = master_catalog[master_catalog['source'] == 'manual']
        if not manual_samples.empty:
            sample = manual_samples.sample(1).iloc[0]
            sampled_sources.add('manual')
            print_sample_row(sample, 'Manual Catalog')
    
    # Second priority: computational (programmatic source + computational_error)
    programmatic_computational = master_catalog[
        (master_catalog['source'] == 'programmatic') & 
        (master_catalog['error_type'] == 'computational_error')
    ]
    if not programmatic_computational.empty:
        sample = programmatic_computational.sample(1).iloc[0]
        sampled_sources.add('computational')
        print_sample_row(sample, 'Computational Catalog')
    
    # Third priority: conceptual validators (programmatic source + conceptual_error)
    programmatic_conceptual = master_catalog[
        (master_catalog['source'] == 'programmatic') & 
        (master_catalog['error_type'] == 'conceptual_error')
    ]
    
    # Try to get one sample from each validator if possible
    validators_sampled = set()
    for _ in range(5):  # Try up to 5 times to get different validators
        if not programmatic_conceptual.empty and len(validators_sampled) < 5:
            sample = programmatic_conceptual.sample(1).iloc[0]
            
            # Determine which validator this likely came from based on patterns
            # This is approximate since we don't store validator info directly
            validator_name = f"Conceptual Validator #{len(validators_sampled) + 1}"
            if validator_name not in validators_sampled:
                validators_sampled.add(validator_name)
                print_sample_row(sample, validator_name)
    
    print(f"\n📊 Summary: Displayed samples from {len(sampled_sources) + len(validators_sampled)} source categories")

def print_sample_row(sample, source_name):
    """Helper function to pretty print a single sample row with full content."""
    print(f"\n🔍 {source_name.upper()}")
    print("-" * 60)
    print(f"📋 Index: {sample['index']} | Tier: {sample['tier']} | Error Type: {sample['error_type']}")
    print(f"📝 Error Subtype: {sample['error_subtype']}")
    print(f"🎯 Erroneous Line Number: {sample['erroneous_line_number']}")
    print(f"🔴 Erroneous Line: {sample['erroneous_line']}")
    print(f"🧮 Erroneous Line Equation: {sample['erroneous_line_eqn']}")
    
    print(f"\n❓ Question:")
    print(f"{sample['question']}")
    
    print(f"\n✅ Correct Answer (Full):")
    print(f"{sample['correct_answer']}")
    
    print(f"\n❌ Wrong Answer (Full):")
    print(f"{sample['wrong_answer']}")
    
    print(f"\n💡 Explanation:")
    print(f"{sample['explanation']}")
    
    print(f"\n📊 Answer Lengths:")
    print(f"   Correct: {sample['correct_answer_length']} lines")
    print(f"   Wrong: {sample['wrong_answer_length']} lines")
    
    print(f"\n🗂️ Correct Answer Mapping (JSON):")
    print(f"{sample['correct_answer_mapping']}")
    
    print(f"\n🗂️ Wrong Answer Mapping (JSON):")
    print(f"{sample['wrong_answer_mapping']}")
    
    print(f"\n🧮 Correct Equation Mapping (JSON):")
    print(f"{sample['correct_eqn_mapping']}")
    
    print(f"\n🧮 Wrong Equation Mapping (JSON):")
    print(f"{sample['wrong_eqn_mapping']}")
    
    print(f"\n🏷️ Source: {sample['source']}")
    
    print("=" * 80)

# Run the pretty printer
pretty_print_sample_rows_by_source(master_catalog)
```

    🎲 RANDOM SAMPLE FROM EACH SOURCE CATALOG
    ================================================================================
    
    🔍 MANUAL CATALOG
    ------------------------------------------------------------
    📋 Index: 1184 | Tier: tier1 | Error Type: computational_error
    📝 Error Subtype: NA
    🎯 Erroneous Line Number: L3
    🔴 Erroneous Line: A medium bed can hold 3 rows with 20 seeds sown per row, 3 * 20=50 seeds per medium bed.
    🧮 Erroneous Line Equation: 3*20=50
    
    ❓ Question:
    Grace is looking to plant some lettuce in her raised bed garden. Her raised bed is comprised of 2 large beds on top with 2 medium beds on the bottom. The top bed can hold 4 rows of lettuce with 25 seeds being sown per row. The medium bed can house 3 rows with 20 seeds being sown per row. How many seeds can Grace plant in all four beds of her raised bed garden?
    
    ✅ Correct Answer (Full):
    A large bed can hold 4 rows with 25 seeds per row, 4 * 25=100 seeds per large bed
    100 seeds per large bed and there are 2 beds, 100 * 2= 200 seeds needed in total for both large beds.
    A medium bed can hold 3 rows with 20 seeds sown per row, 3 * 20=60 seeds per medium bed.
    60 seeds per medium bed and there are 2 medium beds, 60 * 2=120 seeds needed in total for both medium beds.
    200 seeds needed for the large beds combined with 120 seeds needed for the medium beds comes to 200 +120= 320 seeds needed to plant all four beds of the raised garden bed.
    FINAL ANSWER: 320
    
    ❌ Wrong Answer (Full):
    A large bed can hold 4 rows with 25 seeds per row, 4 * 25=100 seeds per large bed
    100 seeds per large bed and there are 2 beds, 100 * 2= 200 seeds needed in total for both large beds.
    A medium bed can hold 3 rows with 20 seeds sown per row, 3 * 20=50 seeds per medium bed.
    50 seeds per medium bed and there are 2 medium beds, 50 * 2=100 seeds needed in total for both medium beds.
    200 seeds needed for the large beds combined with 100 seeds needed for the medium beds comes to 200 +100= 300 seeds needed to plant all four beds of the raised garden bed.
    FINAL ANSWER: 300
    
    💡 Explanation:
    computational error: A medium bed can hold 3 rows with 20 seeds sown per row, 3 * 20 = 60 seeds per medium bed (the calculation of 3*20 was incorrect).
    
    📊 Answer Lengths:
       Correct: 6 lines
       Wrong: 6 lines
    
    🗂️ Correct Answer Mapping (JSON):
    {
      "L1": "A large bed can hold 4 rows with 25 seeds per row, 4 * 25=100 seeds per large bed",
      "L2": "100 seeds per large bed and there are 2 beds, 100 * 2= 200 seeds needed in total for both large beds.",
      "L3": "A medium bed can hold 3 rows with 20 seeds sown per row, 3 * 20=60 seeds per medium bed.",
      "L4": "60 seeds per medium bed and there are 2 medium beds, 60 * 2=120 seeds needed in total for both medium beds.",
      "L5": "200 seeds needed for the large beds combined with 120 seeds needed for the medium beds comes to 200 +120= 320 seeds needed to plant all four beds of the raised garden bed.",
      "FA": "320"
    }
    
    🗂️ Wrong Answer Mapping (JSON):
    {
      "L1": "A large bed can hold 4 rows with 25 seeds per row, 4 * 25=100 seeds per large bed",
      "L2": "100 seeds per large bed and there are 2 beds, 100 * 2= 200 seeds needed in total for both large beds.",
      "L3": "A medium bed can hold 3 rows with 20 seeds sown per row, 3 * 20=50 seeds per medium bed.",
      "L4": "50 seeds per medium bed and there are 2 medium beds, 50 * 2=100 seeds needed in total for both medium beds.",
      "L5": "200 seeds needed for the large beds combined with 100 seeds needed for the medium beds comes to 200 +100= 300 seeds needed to plant all four beds of the raised garden bed.",
      "FA": "300"
    }
    
    🧮 Correct Equation Mapping (JSON):
    {
      "L1": "4*25=100",
      "L2": "100*2=200",
      "L3": "3*20=60",
      "L4": "60*2=120",
      "L5": "200+120=320",
      "FA": ""
    }
    
    🧮 Wrong Equation Mapping (JSON):
    {
      "L1": "4*25=100",
      "L2": "100*2=200",
      "L3": "3*20=50",
      "L4": "50*2=100",
      "L5": "200+100=300",
      "FA": ""
    }
    
    🏷️ Source: manual
    ================================================================================
    
    🔍 COMPUTATIONAL CATALOG
    ------------------------------------------------------------
    📋 Index: 6725 | Tier: tier1 | Error Type: computational_error
    📝 Error Subtype: generate_digit_transposition_error
    🎯 Erroneous Line Number: L1
    🔴 Erroneous Line: Janice can earn $30 x 5 = $105 per week.
    🧮 Erroneous Line Equation: 30*5=105
    
    ❓ Question:
    Janice has been working part-time at a convenience store 5 days a week. She can earn $30 per day and can earn $15 more when she works a 2 hour overtime shift. If she works three overtime shifts this week, how much will she earn this week?
    
    ✅ Correct Answer (Full):
    Janice can earn $30 x 5 = $150 per week.
    She will earn $15 x 3 = $45 more if she works three overtime shifts.
    Therefore, Janice will earn $150 + $45 = $195 this week.
    FINAL ANSWER: 195
    
    ❌ Wrong Answer (Full):
    Janice can earn $30 x 5 = $105 per week.
    She will earn $15 x 3 = $45 more if she works three overtime shifts.
    Therefore, Janice will earn $105 + $45 = $150 this week.
    FINAL ANSWER: 150
    
    💡 Explanation:
    The result of this computation should be 150, not 105. It appears two adjacent digits were swapped.
    
    📊 Answer Lengths:
       Correct: 4 lines
       Wrong: 4 lines
    
    🗂️ Correct Answer Mapping (JSON):
    {
      "L1": "Janice can earn $30 x 5 = $150 per week.",
      "L2": "She will earn $15 x 3 = $45 more if she works three overtime shifts.",
      "L3": "Therefore, Janice will earn $150 + $45 = $195 this week.",
      "FA": "195"
    }
    
    🗂️ Wrong Answer Mapping (JSON):
    {
      "L1": "Janice can earn $30 x 5 = $105 per week.",
      "L2": "She will earn $15 x 3 = $45 more if she works three overtime shifts.",
      "L3": "Therefore, Janice will earn $105 + $45 = $150 this week.",
      "FA": "150"
    }
    
    🧮 Correct Equation Mapping (JSON):
    {
      "L1": "30*5=150",
      "L2": "15*3=45",
      "L3": "150+45=195",
      "FA": ""
    }
    
    🧮 Wrong Equation Mapping (JSON):
    {
      "L1": "30*5=105",
      "L2": "15*3=45",
      "L3": "105+45=150",
      "FA": ""
    }
    
    🏷️ Source: programmatic
    ================================================================================
    
    🔍 CONCEPTUAL VALIDATOR #1
    ------------------------------------------------------------
    📋 Index: 3224 | Tier: tier4 | Error Type: conceptual_error
    📝 Error Subtype: operator_swap
    🎯 Erroneous Line Number: L2
    🔴 Erroneous Line: Traveling 15 minutes at 16 miles per hour, Stephen travels 16/0.25 = 64 miles.
    🧮 Erroneous Line Equation: 
    
    ❓ Question:
    Stephen rides his bicycle to church.  During the first third of his trip, he travels at a speed of 16 miles per hour. During the second third of his trip, riding uphill, he travels a speed of 12 miles per hour.  During the last third of his trip, he rides downhill at a speed of 20 miles per hour.  If each third of his trip takes 15 minutes, what is the distance Stephen rides his bicycle to church, in miles?
    
    ✅ Correct Answer (Full):
    15 minutes is 15/60=0.25 hours.
    Traveling 15 minutes at 16 miles per hour, Stephen travels 16*0.25 = 4 miles.
    Traveling 15 minutes at 12 miles per hour, Stephen travels 12*0.25 = 3 miles.
    Traveling 15 minutes at 20 miles per hour, Stephen travels 20*0.25 = 5 miles.
    All together, Stephen travels 4+3+5=12 miles.
    FINAL ANSWER: 12
    
    ❌ Wrong Answer (Full):
    15 minutes is 15/60=0.25 hours.
    Traveling 15 minutes at 16 miles per hour, Stephen travels 16/0.25 = 64 miles.
    Traveling 15 minutes at 12 miles per hour, Stephen travels 12*0.25 = 3 miles.
    Traveling 15 minutes at 20 miles per hour, Stephen travels 20*0.25 = 5 miles.
    All together, Stephen travels 64+3+5=72 miles.
    FINAL ANSWER: 72
    
    💡 Explanation:
    Incorrect operation. The calculation should use '*' but used '/' instead.
    
    📊 Answer Lengths:
       Correct: 6 lines
       Wrong: 6 lines
    
    🗂️ Correct Answer Mapping (JSON):
    {
      "L1": "15 minutes is 15/60=0.25 hours.",
      "L2": "Traveling 15 minutes at 16 miles per hour, Stephen travels 16*0.25 = 4 miles.",
      "L3": "Traveling 15 minutes at 12 miles per hour, Stephen travels 12*0.25 = 3 miles.",
      "L4": "Traveling 15 minutes at 20 miles per hour, Stephen travels 20*0.25 = 5 miles.",
      "L5": "All together, Stephen travels 4+3+5=12 miles.",
      "FA": "12"
    }
    
    🗂️ Wrong Answer Mapping (JSON):
    {
      "L1": "15 minutes is 15/60=0.25 hours.",
      "L2": "Traveling 15 minutes at 16 miles per hour, Stephen travels 16/0.25 = 64 miles.",
      "L3": "Traveling 15 minutes at 12 miles per hour, Stephen travels 12*0.25 = 3 miles.",
      "L4": "Traveling 15 minutes at 20 miles per hour, Stephen travels 20*0.25 = 5 miles.",
      "L5": "All together, Stephen travels 64+3+5=72 miles.",
      "FA": "72"
    }
    
    🧮 Correct Equation Mapping (JSON):
    {
      "L1": "15/60=0.25",
      "L2": "",
      "L3": "",
      "L4": "",
      "L5": "4+3+5=12",
      "FA": ""
    }
    
    🧮 Wrong Equation Mapping (JSON):
    {
      "L1": "15/60=0.25",
      "L2": "",
      "L3": "",
      "L4": "",
      "L5": "64+3+5=72",
      "FA": ""
    }
    
    🏷️ Source: programmatic
    ================================================================================
    
    🔍 CONCEPTUAL VALIDATOR #2
    ------------------------------------------------------------
    📋 Index: 4241 | Tier: tier3 | Error Type: conceptual_error
    📝 Error Subtype: operator_swap
    🎯 Erroneous Line Number: L2
    🔴 Erroneous Line: The total number of marbles that Ludo bought is 16 marbles + 4 marbles = 12 marbles
    🧮 Erroneous Line Equation: 16+4=12
    
    ❓ Question:
    Three friends Wolfgang, Ludo, and Michael, went to Walmart and bought marbles. Wolfgang bought 16 marbles, Ludo bought 1/4 times more marbles than Wolfgang, and Michael bought 2/3 times as many marbles as the number of marbles both Wolfgang and Ludo bought. If they combined their marbles and decided to share them equally, how many marbles did each get?
    
    ✅ Correct Answer (Full):
    Ludo bought 1/4 more marbles than Wolfgang, which is 1/4 * 16 marbles = 4 marbles
    The total number of marbles that Ludo bought is 16 marbles + 4 marbles = 20 marbles
    Wolfgang and Ludo purchased a total of 20 marbles + 16 marbles = 36 marbles.
    If Michael bought 2/3 times the total number of marbles bought by Wolfgang and Ludo, he bought 2/3 * 36 marbles = 24 marbles.
    The three friends purchased a total of 24 marbles + 36 marbles = 60 marbles.
    When they shared the marbles equally, each got 60 marbles / 3 people = 20 marbles/person.
    FINAL ANSWER: 20
    
    ❌ Wrong Answer (Full):
    Ludo bought 1/4 more marbles than Wolfgang, which is 1/4 * 16 marbles = 4 marbles
    The total number of marbles that Ludo bought is 16 marbles + 4 marbles = 12 marbles
    Wolfgang and Ludo purchased a total of 12 marbles + 16 marbles = 28 marbles.
    If Michael bought 2/3 times the total number of marbles bought by Wolfgang and Ludo, he bought 2/3 * 28 marbles = 56/3 marbles.
    The three friends purchased a total of 56/3 marbles + 28 marbles = 140/3 marbles.
    When they shared the marbles equally, each got 140/3 marbles / 3 people = 140/9 marbles/person.
    FINAL ANSWER: 140/9
    
    💡 Explanation:
    Incorrect operation. The calculation should use '+' but used '-' instead.
    
    📊 Answer Lengths:
       Correct: 7 lines
       Wrong: 7 lines
    
    🗂️ Correct Answer Mapping (JSON):
    {
      "L1": "Ludo bought 1/4 more marbles than Wolfgang, which is 1/4 * 16 marbles = 4 marbles",
      "L2": "The total number of marbles that Ludo bought is 16 marbles + 4 marbles = 20 marbles",
      "L3": "Wolfgang and Ludo purchased a total of 20 marbles + 16 marbles = 36 marbles.",
      "L4": "If Michael bought 2/3 times the total number of marbles bought by Wolfgang and Ludo, he bought 2/3 * 36 marbles = 24 marbles.",
      "L5": "The three friends purchased a total of 24 marbles + 36 marbles = 60 marbles.",
      "L6": "When they shared the marbles equally, each got 60 marbles / 3 people = 20 marbles/person.",
      "FA": "20"
    }
    
    🗂️ Wrong Answer Mapping (JSON):
    {
      "L1": "Ludo bought 1/4 more marbles than Wolfgang, which is 1/4 * 16 marbles = 4 marbles",
      "L2": "The total number of marbles that Ludo bought is 16 marbles + 4 marbles = 12 marbles",
      "L3": "Wolfgang and Ludo purchased a total of 12 marbles + 16 marbles = 28 marbles.",
      "L4": "If Michael bought 2/3 times the total number of marbles bought by Wolfgang and Ludo, he bought 2/3 * 28 marbles = 56/3 marbles.",
      "L5": "The three friends purchased a total of 56/3 marbles + 28 marbles = 140/3 marbles.",
      "L6": "When they shared the marbles equally, each got 140/3 marbles / 3 people = 140/9 marbles/person.",
      "FA": "140/9"
    }
    
    🧮 Correct Equation Mapping (JSON):
    {
      "L1": "1/4*16=4",
      "L2": "16+4=20",
      "L3": "20+16=36",
      "L4": "2/3*36=24",
      "L5": "24+36=60",
      "L6": "60/3=20",
      "FA": ""
    }
    
    🧮 Wrong Equation Mapping (JSON):
    {
      "L1": "1/4*16=4",
      "L2": "16+4=12",
      "L3": "12+16=28",
      "L4": "2/3*28=56/3",
      "L5": "56/3+28=140/3",
      "L6": "140/3/3=140/9",
      "FA": ""
    }
    
    🏷️ Source: programmatic
    ================================================================================
    
    🔍 CONCEPTUAL VALIDATOR #3
    ------------------------------------------------------------
    📋 Index: 2135 | Tier: tier4 | Error Type: conceptual_error
    📝 Error Subtype: incomplete_calculation
    🎯 Erroneous Line Number: L1
    🔴 Erroneous Line: The four cats weigh 36 pounds in total because 12 plus 14.7 plus 9.3 equals 36.
    🧮 Erroneous Line Equation: 12+14.7+9.3=36
    
    ❓ Question:
    Janele wants to figure out the average weight of her cats. She has 4 of them. The first two weigh 12 pounds each. The third weighs 14.7 pounds and the fourth weighs 9.3 pounds. What is their average weight?
    
    ✅ Correct Answer (Full):
    The four cats weigh 48 pounds in total because 12 plus 12 plus 14.7 plus 9.3 equals 48.
    The average weight is 12 pounds because 48 divided by 4 is 12.
    FINAL ANSWER: 12
    
    ❌ Wrong Answer (Full):
    The four cats weigh 36 pounds in total because 12 plus 14.7 plus 9.3 equals 36.
    The average weight is 9 pounds because 36 divided by 4 is 9.
    FINAL ANSWER: 9
    
    💡 Explanation:
    Incomplete calculation. The term 'cat2_weight' (value: 12.0) was omitted from the operation.
    
    📊 Answer Lengths:
       Correct: 3 lines
       Wrong: 3 lines
    
    🗂️ Correct Answer Mapping (JSON):
    {
      "L1": "The four cats weigh 48 pounds in total because 12 plus 12 plus 14.7 plus 9.3 equals 48.",
      "L2": "The average weight is 12 pounds because 48 divided by 4 is 12.",
      "FA": "12"
    }
    
    🗂️ Wrong Answer Mapping (JSON):
    {
      "L1": "The four cats weigh 36 pounds in total because 12 plus 14.7 plus 9.3 equals 36.",
      "L2": "The average weight is 9 pounds because 36 divided by 4 is 9.",
      "FA": "9"
    }
    
    🧮 Correct Equation Mapping (JSON):
    {
      "L1": "12+12+14.7+9.3=48",
      "L2": "48/4=12",
      "FA": ""
    }
    
    🧮 Wrong Equation Mapping (JSON):
    {
      "L1": "12+14.7+9.3=36",
      "L2": "36/4=9",
      "FA": ""
    }
    
    🏷️ Source: programmatic
    ================================================================================
    
    🔍 CONCEPTUAL VALIDATOR #4
    ------------------------------------------------------------
    📋 Index: 4809 | Tier: tier2 | Error Type: conceptual_error
    📝 Error Subtype: incomplete_calculation
    🎯 Erroneous Line Number: L3
    🔴 Erroneous Line: Now multiply the new total by 10% to find out how much Jerry owes the loan shark in interest the second month: $220 * 10% = $2200
    🧮 Erroneous Line Equation: 220*10=2200
    
    ❓ Question:
    Jerry owes a loan shark $200. The loan shark charges Jerry 10% interest compounded monthly. (This means that every month the loan shark adds Jerry's interest amount to his loan, and the next month Jerry has to pay 10% on the new total). If Jerry doesn't make any payments, how much (in dollars) does the loan shark charge in interest the second month?
    
    ✅ Correct Answer (Full):
    First calculate how much the loan shark charges in interest the first month by multiplying the loan amount by the interest rate: $200 * 10% = $20
    Now add the interest amount to the original amount of the loan to find Jerry's new total: $200 + $20 = $220
    Now multiply the new total by 10% to find out how much Jerry owes the loan shark in interest the second month: $220 * 10% = $22
    FINAL ANSWER: 22
    
    ❌ Wrong Answer (Full):
    First calculate how much the loan shark charges in interest the first month by multiplying the loan amount by the interest rate: $200 * 10% = $20
    Now add the interest amount to the original amount of the loan to find Jerry's new total: $200 + $20 = $220
    Now multiply the new total by 10% to find out how much Jerry owes the loan shark in interest the second month: $220 * 10% = $2200
    FINAL ANSWER: 2200
    
    💡 Explanation:
    Incomplete calculation. The term 'percent_factor' (value: 0.01) was omitted from the operation.
    
    📊 Answer Lengths:
       Correct: 4 lines
       Wrong: 4 lines
    
    🗂️ Correct Answer Mapping (JSON):
    {
      "L1": "First calculate how much the loan shark charges in interest the first month by multiplying the loan amount by the interest rate: $200 * 10% = $20",
      "L2": "Now add the interest amount to the original amount of the loan to find Jerry's new total: $200 + $20 = $220",
      "L3": "Now multiply the new total by 10% to find out how much Jerry owes the loan shark in interest the second month: $220 * 10% = $22",
      "FA": "22"
    }
    
    🗂️ Wrong Answer Mapping (JSON):
    {
      "L1": "First calculate how much the loan shark charges in interest the first month by multiplying the loan amount by the interest rate: $200 * 10% = $20",
      "L2": "Now add the interest amount to the original amount of the loan to find Jerry's new total: $200 + $20 = $220",
      "L3": "Now multiply the new total by 10% to find out how much Jerry owes the loan shark in interest the second month: $220 * 10% = $2200",
      "FA": "2200"
    }
    
    🧮 Correct Equation Mapping (JSON):
    {
      "L1": "200*10*.01=20",
      "L2": "200+20=220",
      "L3": "220*10*.01=22",
      "FA": ""
    }
    
    🧮 Wrong Equation Mapping (JSON):
    {
      "L1": "200*10*0.01=20",
      "L2": "200+20=220",
      "L3": "220*10=2200",
      "FA": ""
    }
    
    🏷️ Source: programmatic
    ================================================================================
    
    🔍 CONCEPTUAL VALIDATOR #5
    ------------------------------------------------------------
    📋 Index: 5132 | Tier: tier1 | Error Type: conceptual_error
    📝 Error Subtype: incomplete_calculation
    🎯 Erroneous Line Number: L4
    🔴 Erroneous Line: Therefore, Cid earned a total of $$300 + $75 = $375.
    🧮 Erroneous Line Equation: 300+75=375
    
    ❓ Question:
    Cid owns a mechanic shop, he charges $20 for an oil change, $30 for a repair, and $5 for a car wash. How much money did he earn if he changed the oil of 5 cars, repaired 10 cars, and washed 15 cars?
    
    ✅ Correct Answer (Full):
    The money he earned from an oil change is $20 x 5 =$ 100.
    The money he earned from the repair is $30 x 10 = $300.
    The money he earned from the car wash is $15 x 5 = $75.
    Therefore, Cid earned a total of $100 + $300 + $75 = $475.
    FINAL ANSWER: 475
    
    ❌ Wrong Answer (Full):
    The money he earned from an oil change is $20 x 5 =$ 100.
    The money he earned from the repair is $30 x 10 = $300.
    The money he earned from the car wash is $15 x 5 = $75.
    Therefore, Cid earned a total of $$300 + $75 = $375.
    FINAL ANSWER: 375
    
    💡 Explanation:
    Incomplete calculation. The term 'earned_from_oil_change' (value: 100) was omitted from the operation.
    
    📊 Answer Lengths:
       Correct: 5 lines
       Wrong: 5 lines
    
    🗂️ Correct Answer Mapping (JSON):
    {
      "L1": "The money he earned from an oil change is $20 x 5 =$ 100.",
      "L2": "The money he earned from the repair is $30 x 10 = $300.",
      "L3": "The money he earned from the car wash is $15 x 5 = $75.",
      "L4": "Therefore, Cid earned a total of $100 + $300 + $75 = $475.",
      "FA": "475"
    }
    
    🗂️ Wrong Answer Mapping (JSON):
    {
      "L1": "The money he earned from an oil change is $20 x 5 =$ 100.",
      "L2": "The money he earned from the repair is $30 x 10 = $300.",
      "L3": "The money he earned from the car wash is $15 x 5 = $75.",
      "L4": "Therefore, Cid earned a total of $$300 + $75 = $375.",
      "FA": "375"
    }
    
    🧮 Correct Equation Mapping (JSON):
    {
      "L1": "20*5=100",
      "L2": "30*10=300",
      "L3": "15*5=75",
      "L4": "100+300+75=475",
      "FA": ""
    }
    
    🧮 Wrong Equation Mapping (JSON):
    {
      "L1": "20*5=100",
      "L2": "30*10=300",
      "L3": "15*5=75",
      "L4": "300+75=375",
      "FA": ""
    }
    
    🏷️ Source: programmatic
    ================================================================================
    
    📊 Summary: Displayed samples from 7 source categories



```python
# 3. Save the master catalog to a new folder "../data/aug-5-dataset"
from pathlib import Path
import shutil

# Create the new directory
AUG_5_DATASET_DIR = DATA_DIR / "aug-5-dataset"
AUG_5_DATASET_DIR.mkdir(parents=True, exist_ok=True)

print(f"💾 SAVING MASTER CATALOG TO: {AUG_5_DATASET_DIR}")
print("=" * 80)

# Save master catalog
master_catalog_path = AUG_5_DATASET_DIR / "master_catalog.csv"
master_catalog.to_csv(master_catalog_path, index=False)
print(f"✅ Master catalog saved: {master_catalog_path}")
print(f"   📊 {len(master_catalog):,} rows with {len(MASTER_CATALOG_COLUMNS)} columns")

# Save problematic catalog
problematic_catalog_path = AUG_5_DATASET_DIR / "catalog_problematic.csv"
catalog_problematic.to_csv(problematic_catalog_path, index=False)
print(f"✅ Problematic catalog saved: {problematic_catalog_path}")
print(f"   📊 {len(catalog_problematic):,} problematic rows")

# Save summary statistics
summary_path = AUG_5_DATASET_DIR / "dataset_summary.txt"
with open(summary_path, 'w') as f:
    f.write("AUG-5 DATASET SUMMARY\n")
    f.write("=" * 50 + "\n\n")
    f.write(f"Generated on: August 5, 2025\n")
    f.write(f"Total master catalog rows: {len(master_catalog):,}\n")
    f.write(f"Total problematic rows: {len(catalog_problematic):,}\n")
    f.write(f"Unique GSM8K indices: {master_catalog['index'].nunique():,}\n\n")
    
    f.write("SOURCE DISTRIBUTION:\n")
    source_counts = master_catalog['source'].value_counts()
    for source, count in source_counts.items():
        pct = (count / len(master_catalog)) * 100
        f.write(f"  {source}: {count:,} ({pct:.1f}%)\n")
    
    f.write("\nERROR TYPE DISTRIBUTION:\n")
    error_type_counts = master_catalog['error_type'].value_counts()
    for error_type, count in error_type_counts.items():
        pct = (count / len(master_catalog)) * 100
        f.write(f"  {error_type}: {count:,} ({pct:.1f}%)\n")
    
    f.write("\nTIER DISTRIBUTION:\n")
    tier_counts = master_catalog['tier'].value_counts().sort_index()
    for tier, count in tier_counts.items():
        pct = (count / len(master_catalog)) * 100
        f.write(f"  {tier}: {count:,} ({pct:.1f}%)\n")
    
    f.write(f"\nCOLUMNS ({len(MASTER_CATALOG_COLUMNS)}):\n")
    for i, col in enumerate(MASTER_CATALOG_COLUMNS, 1):
        f.write(f"  {i:2d}. {col}\n")

print(f"✅ Summary statistics saved: {summary_path}")

def get_column_description(col_name):
    """Get description for each column."""
    descriptions = {
        'index': 'GSM8K problem index',
        'tier': 'Problem difficulty tier (tier1-tier5)',
        'question': 'Math problem question text',
        'correct_answer': 'Correct solution with FINAL ANSWER prefix',
        'wrong_answer': 'Flawed solution with FINAL ANSWER prefix', 
        'error_type': 'Type of error (computational_error/conceptual_error)',
        'explanation': 'Human explanation of the error',
        'erroneous_line_number': 'Line identifier containing the error (L1, L2, FA)',
        'erroneous_line': 'Text content of the erroneous line',
        'erroneous_line_eqn': 'Calculator equation from erroneous line',
        'correct_answer_mapping': 'JSON mapping of line IDs to correct solution lines',
        'wrong_answer_mapping': 'JSON mapping of line IDs to wrong solution lines',
        'correct_eqn_mapping': 'JSON mapping of line IDs to correct calculator equations',
        'wrong_eqn_mapping': 'JSON mapping of line IDs to wrong calculator equations', 
        'correct_answer_length': 'Number of lines in correct solution',
        'wrong_answer_length': 'Number of lines in wrong solution',
        'source': 'Data source (manual/programmatic)',
        'error_subtype': 'Detailed error subtype classification'
    }
    return descriptions.get(col_name, 'No description available')

# Save column schema
schema_path = AUG_5_DATASET_DIR / "column_schema.json"
schema_info = {
    "dataset_name": "aug-5-dataset", 
    "creation_date": "2025-08-05",
    "total_columns": len(MASTER_CATALOG_COLUMNS),
    "columns": {
        col: {
            "position": i + 1,
            "data_type": str(master_catalog[col].dtype) if col in master_catalog.columns else "unknown",
            "description": get_column_description(col)
        }
        for i, col in enumerate(MASTER_CATALOG_COLUMNS)
    }
}

with open(schema_path, 'w') as f:
    json.dump(schema_info, f, indent=2)

print(f"✅ Column schema saved: {schema_path}")

# List all files in the new directory
print(f"\n📁 FILES IN {AUG_5_DATASET_DIR.name}/:")
for file_path in sorted(AUG_5_DATASET_DIR.iterdir()):
    file_size = file_path.stat().st_size / (1024 * 1024)  # Size in MB
    print(f"   📄 {file_path.name} ({file_size:.1f} MB)")

print(f"\n🎉 Dataset successfully saved to: {AUG_5_DATASET_DIR}")
print("✨ Ready for downstream processing and analysis!")
```

    💾 SAVING MASTER CATALOG TO: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/aug-5-dataset
    ================================================================================
    ✅ Master catalog saved: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/aug-5-dataset/master_catalog.csv
       📊 24,652 rows with 18 columns
    ✅ Problematic catalog saved: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/aug-5-dataset/catalog_problematic.csv
       📊 1,078 problematic rows
    ✅ Summary statistics saved: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/aug-5-dataset/dataset_summary.txt
    ✅ Column schema saved: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/aug-5-dataset/column_schema.json
    
    📁 FILES IN aug-5-dataset/:
       📄 catalog_problematic.csv (0.4 MB)
       📄 column_schema.json (0.0 MB)
       📄 dataset_summary.txt (0.0 MB)
       📄 manual_length_mismatch.csv (0.3 MB)
       📄 master_catalog.csv (47.0 MB)
    
    🎉 Dataset successfully saved to: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/aug-5-dataset
    ✨ Ready for downstream processing and analysis!



```python
# Read the CSV and examine the data types and a sample row
import pandas as pd
import json

# Read the saved master catalog
df = pd.read_csv(master_catalog_path)

print("📊 DATAFRAME INFO:")
print("=" * 50)
df.info()

print("\n📋 COLUMN DTYPES:")
print("=" * 50)
for col in df.columns:
    print(f"{col}: {df[col].dtype}")

print("\n🔍 SAMPLE ROW (First Row):")
print("=" * 50)
sample_row = df.iloc[0]
for col, value in sample_row.items():
    print(f"\n{col}:")
    print(f"  Type: {type(value)}")
    print(f"  Value: {repr(value)}")  # repr shows the actual string representation
    
    # Special handling for JSON columns
    if col.endswith('_mapping'):
        print(f"  First 100 chars: {str(value)[:100]}...")
        try:
            parsed = json.loads(value)
            print(f"  JSON Parse: SUCCESS - {type(parsed)}")
        except Exception as e:
            print(f"  JSON Parse: FAILED - {str(e)}")

print("\n🧪 JSON PARSING TEST:")
print("=" * 50)
# Test parsing the JSON columns
json_columns = ['correct_answer_mapping', 'wrong_answer_mapping', 'correct_eqn_mapping', 'wrong_eqn_mapping']

for col in json_columns:
    print(f"\nTesting {col}:")
    test_value = df.iloc[0][col]
    print(f"Raw value: {repr(test_value)}")
    
    try:
        parsed = json.loads(test_value)
        print(f"✅ Parsed successfully: {type(parsed)}")
        print(f"   Sample content: {list(parsed.keys())[:3]}")
    except json.JSONDecodeError as e:
        print(f"❌ JSON parsing failed: {e}")
        
        # Try to fix the escaping issue
        try:
            fixed_value = test_value.replace('""', '"')
            parsed = json.loads(fixed_value)
            print(f"✅ Fixed and parsed: {type(parsed)}")
        except Exception as e2:
            print(f"❌ Still failed after fixing: {e2}")
```

    📊 DATAFRAME INFO:
    ==================================================
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 24652 entries, 0 to 24651
    Data columns (total 18 columns):
     #   Column                  Non-Null Count  Dtype 
    ---  ------                  --------------  ----- 
     0   index                   24652 non-null  int64 
     1   tier                    24652 non-null  object
     2   question                24652 non-null  object
     3   correct_answer          24652 non-null  object
     4   wrong_answer            24652 non-null  object
     5   error_type              24652 non-null  object
     6   explanation             24651 non-null  object
     7   erroneous_line_number   24652 non-null  object
     8   erroneous_line          24382 non-null  object
     9   erroneous_line_eqn      22616 non-null  object
     10  correct_answer_mapping  24652 non-null  object
     11  wrong_answer_mapping    24652 non-null  object
     12  correct_eqn_mapping     24652 non-null  object
     13  wrong_eqn_mapping       24652 non-null  object
     14  correct_answer_length   24652 non-null  int64 
     15  wrong_answer_length     24652 non-null  int64 
     16  source                  24652 non-null  object
     17  error_subtype           22912 non-null  object
    dtypes: int64(3), object(15)
    memory usage: 3.4+ MB
    
    📋 COLUMN DTYPES:
    ==================================================
    index: int64
    tier: object
    question: object
    correct_answer: object
    wrong_answer: object
    error_type: object
    explanation: object
    erroneous_line_number: object
    erroneous_line: object
    erroneous_line_eqn: object
    correct_answer_mapping: object
    wrong_answer_mapping: object
    correct_eqn_mapping: object
    wrong_eqn_mapping: object
    correct_answer_length: int64
    wrong_answer_length: int64
    source: object
    error_subtype: object
    
    🔍 SAMPLE ROW (First Row):
    ==================================================
    
    index:
      Type: <class 'numpy.int64'>
      Value: 1000
    
    tier:
      Type: <class 'str'>
      Value: 'tier3'
    
    question:
      Type: <class 'str'>
      Value: 'John buys a heating pad for $30.  He uses it 3 times a week for 2 weeks.  How much does he spend on each use?'
    
    correct_answer:
      Type: <class 'str'>
      Value: 'He uses it 3*2=6 times\nSo he pays 30/6=$5\nFINAL ANSWER: 5'
    
    wrong_answer:
      Type: <class 'str'>
      Value: 'He uses it 3*2=5 times\nSo he pays 30/5=$6\nFINAL ANSWER: 6'
    
    error_type:
      Type: <class 'str'>
      Value: 'computational_error'
    
    explanation:
      Type: <class 'str'>
      Value: 'computational error: John uses it 3*2=<<3*2=6>>6 times.'
    
    erroneous_line_number:
      Type: <class 'str'>
      Value: 'L1'
    
    erroneous_line:
      Type: <class 'str'>
      Value: 'He uses it 3*2=5 times'
    
    erroneous_line_eqn:
      Type: <class 'str'>
      Value: '3*2=5'
    
    correct_answer_mapping:
      Type: <class 'str'>
      Value: '{\n  "L1": "He uses it 3*2=6 times",\n  "L2": "So he pays 30/6=$5",\n  "FA": "5"\n}'
      First 100 chars: {
      "L1": "He uses it 3*2=6 times",
      "L2": "So he pays 30/6=$5",
      "FA": "5"
    }...
      JSON Parse: SUCCESS - <class 'dict'>
    
    wrong_answer_mapping:
      Type: <class 'str'>
      Value: '{\n  "L1": "He uses it 3*2=5 times",\n  "L2": "So he pays 30/5=$6",\n  "FA": "6"\n}'
      First 100 chars: {
      "L1": "He uses it 3*2=5 times",
      "L2": "So he pays 30/5=$6",
      "FA": "6"
    }...
      JSON Parse: SUCCESS - <class 'dict'>
    
    correct_eqn_mapping:
      Type: <class 'str'>
      Value: '{\n  "L1": "3*2=6",\n  "L2": "30/6=5",\n  "FA": ""\n}'
      First 100 chars: {
      "L1": "3*2=6",
      "L2": "30/6=5",
      "FA": ""
    }...
      JSON Parse: SUCCESS - <class 'dict'>
    
    wrong_eqn_mapping:
      Type: <class 'str'>
      Value: '{\n  "L1": "3*2=5",\n  "L2": "30/5=6",\n  "FA": ""\n}'
      First 100 chars: {
      "L1": "3*2=5",
      "L2": "30/5=6",
      "FA": ""
    }...
      JSON Parse: SUCCESS - <class 'dict'>
    
    correct_answer_length:
      Type: <class 'numpy.int64'>
      Value: 3
    
    wrong_answer_length:
      Type: <class 'numpy.int64'>
      Value: 3
    
    source:
      Type: <class 'str'>
      Value: 'manual'
    
    error_subtype:
      Type: <class 'float'>
      Value: nan
    
    🧪 JSON PARSING TEST:
    ==================================================
    
    Testing correct_answer_mapping:
    Raw value: '{\n  "L1": "He uses it 3*2=6 times",\n  "L2": "So he pays 30/6=$5",\n  "FA": "5"\n}'
    ✅ Parsed successfully: <class 'dict'>
       Sample content: ['L1', 'L2', 'FA']
    
    Testing wrong_answer_mapping:
    Raw value: '{\n  "L1": "He uses it 3*2=5 times",\n  "L2": "So he pays 30/5=$6",\n  "FA": "6"\n}'
    ✅ Parsed successfully: <class 'dict'>
       Sample content: ['L1', 'L2', 'FA']
    
    Testing correct_eqn_mapping:
    Raw value: '{\n  "L1": "3*2=6",\n  "L2": "30/6=5",\n  "FA": ""\n}'
    ✅ Parsed successfully: <class 'dict'>
       Sample content: ['L1', 'L2', 'FA']
    
    Testing wrong_eqn_mapping:
    Raw value: '{\n  "L1": "3*2=5",\n  "L2": "30/5=6",\n  "FA": ""\n}'
    ✅ Parsed successfully: <class 'dict'>
       Sample content: ['L1', 'L2', 'FA']



```python
# Enhanced comprehensive JSON validation across the entire dataset
import pandas as pd
import json
from tqdm.auto import tqdm

def comprehensive_json_validation(df):
    """
    Check all JSON columns across the entire dataset for parsing errors.
    Only prints output if errors are found.
    """
    print("🔍 COMPREHENSIVE JSON VALIDATION")
    print("=" * 60)
    
    json_columns = ['correct_answer_mapping', 'wrong_answer_mapping', 'correct_eqn_mapping', 'wrong_eqn_mapping']
    total_rows = len(df)
    total_cells = total_rows * len(json_columns)
    
    print(f"📊 Checking {total_cells:,} JSON cells across {total_rows:,} rows...")
    
    error_summary = {col: [] for col in json_columns}
    successful_parses = 0
    
    for idx in tqdm(range(len(df)), desc="Validating JSON cells"):
        row = df.iloc[idx]
        
        for col in json_columns:
            cell_value = row[col]
            
            # Skip if NaN or empty
            if pd.isna(cell_value) or cell_value == "":
                continue
                
            try:
                parsed = json.loads(cell_value)
                successful_parses += 1
                
                # Basic validation - should be a dict with expected keys
                if not isinstance(parsed, dict):
                    error_summary[col].append({
                        'row_idx': idx, 
                        'gsm8k_idx': row['index'],
                        'error': 'Not a dictionary',
                        'preview': str(cell_value)[:100]
                    })
                elif not any(key.startswith(('L', 'FA')) for key in parsed.keys()):
                    error_summary[col].append({
                        'row_idx': idx, 
                        'gsm8k_idx': row['index'],
                        'error': 'Missing expected keys (L1, L2, FA, etc.)',
                        'keys_found': list(parsed.keys())[:5]
                    })
                    
            except json.JSONDecodeError as e:
                error_summary[col].append({
                    'row_idx': idx, 
                    'gsm8k_idx': row['index'],
                    'error': f'JSON decode error: {str(e)}',
                    'preview': str(cell_value)[:100]
                })
            except Exception as e:
                error_summary[col].append({
                    'row_idx': idx, 
                    'gsm8k_idx': row['index'],
                    'error': f'Unexpected error: {str(e)}',
                    'preview': str(cell_value)[:100]
                })
    
    # Report results
    total_errors = sum(len(errors) for errors in error_summary.values())
    
    if total_errors == 0:
        print(f"✅ VALIDATION SUCCESSFUL!")
        print(f"   📊 {successful_parses:,} JSON cells parsed successfully")
        print(f"   📊 0 parsing errors found")
        print(f"   🎉 All JSON data is properly formatted and parseable!")
        return True
    else:
        print(f"❌ VALIDATION FAILED!")
        print(f"   📊 {successful_parses:,} successful parses")
        print(f"   📊 {total_errors:,} parsing errors found")
        
        for col, errors in error_summary.items():
            if errors:
                print(f"\n🔴 {col} - {len(errors)} errors:")
                for i, error in enumerate(errors[:3]):  # Show first 3 errors
                    print(f"   {i+1}. Row {error['row_idx']} (GSM8K {error['gsm8k_idx']}): {error['error']}")
                    if 'preview' in error:
                        print(f"      Preview: {error['preview']}...")
                if len(errors) > 3:
                    print(f"   ... and {len(errors) - 3} more errors")
        
        return False

# Run the comprehensive validation
validation_passed = comprehensive_json_validation(df)

if validation_passed:
    print(f"\n🎯 DATASET QUALITY SUMMARY:")
    print(f"   📂 File: {master_catalog_path.name}")
    print(f"   📊 Rows: {len(df):,}")
    print(f"   📋 Columns: {len(df.columns)}")
    print(f"   ✅ JSON Format: All valid")
    print(f"   🚀 Ready for downstream processing!")
else:
    print(f"\n⚠️  DATASET NEEDS ATTENTION:")
    print(f"   📂 File: {master_catalog_path.name}")
    print(f"   📊 JSON parsing errors detected")
    print(f"   🔧 Consider regenerating or fixing the problematic entries")
```

    🔍 COMPREHENSIVE JSON VALIDATION
    ============================================================
    📊 Checking 98,608 JSON cells across 24,652 rows...



    Validating JSON cells:   0%|          | 0/24652 [00:00<?, ?it/s]


    ✅ VALIDATION SUCCESSFUL!
       📊 98,608 JSON cells parsed successfully
       📊 0 parsing errors found
       🎉 All JSON data is properly formatted and parseable!
    
    🎯 DATASET QUALITY SUMMARY:
       📂 File: master_catalog.csv
       📊 Rows: 24,652
       📋 Columns: 18
       ✅ JSON Format: All valid
       🚀 Ready for downstream processing!



```python
# Fixed Enhanced Data Quality Analysis with Correct Counting
import pandas as pd
import json
from collections import defaultdict

def analyze_data_quality_enhanced_fixed(df):
    """
    Comprehensive data quality analysis with breakdowns by source and error_type.
    Fixed to avoid overcounting rows with multiple issues.
    """
    print("📊 ENHANCED DATA QUALITY ANALYSIS (FIXED)")
    print("=" * 80)
    
    sources = df['source'].unique()
    error_types = df['error_type'].unique()
    total_rows = len(df)
    
    print(f"📋 Total rows: {total_rows:,}")
    print(f"📋 Sources: {', '.join(sources)}")
    print(f"📋 Error types: {', '.join(error_types)}")
    print(f"📋 Source distribution: {dict(df['source'].value_counts())}")
    print(f"📋 Error type distribution: {dict(df['error_type'].value_counts())}")
    
    # Initialize results with nested dictionaries for source -> error_type -> count
    quality_metrics = {
        'missing_erroneous_line': defaultdict(lambda: defaultdict(int)),
        'missing_explanation': defaultdict(lambda: defaultdict(int)), 
        'length_mismatch_non_fa': defaultdict(lambda: defaultdict(int)),
        'correct_missing_equations': defaultdict(lambda: defaultdict(int)),
        'wrong_missing_equations': defaultdict(lambda: defaultdict(int))
    }
    
    # Track rows with ANY issues for proper summary calculations
    rows_with_any_issues = defaultdict(lambda: defaultdict(set))  # source -> error_type -> set of row indices
    
    print(f"\n🔍 Analyzing {total_rows:,} rows...")
    
    for idx, row in df.iterrows():
        source = row['source']
        error_type = row['error_type']
        has_any_issue = False
        
        # 1. Check for missing erroneous_line
        if pd.isna(row['erroneous_line']) or str(row['erroneous_line']).strip() == '' or str(row['erroneous_line']) == 'nan':
            quality_metrics['missing_erroneous_line'][source][error_type] += 1
            has_any_issue = True
        
        # 2. Check for missing explanation
        if pd.isna(row['explanation']) or str(row['explanation']).strip() == '' or str(row['explanation']) == 'nan':
            quality_metrics['missing_explanation'][source][error_type] += 1
            has_any_issue = True
        
        # 3. Check length mismatch for non-FA erroneous lines
        if row['erroneous_line_number'] != 'FA':
            if row['correct_answer_length'] != row['wrong_answer_length']:
                quality_metrics['length_mismatch_non_fa'][source][error_type] += 1
                has_any_issue = True
        
        # 4. & 5. Check for missing calculator equations
        try:
            # Parse the equation mappings
            correct_eqn_mapping = json.loads(row['correct_eqn_mapping'])
            wrong_eqn_mapping = json.loads(row['wrong_eqn_mapping'])
            
            correct_length = row['correct_answer_length']
            wrong_length = row['wrong_answer_length']
            
            # Count non-empty equations in correct mapping
            correct_non_empty_eqns = sum(1 for v in correct_eqn_mapping.values() if v and str(v).strip())
            
            # Count non-empty equations in wrong mapping  
            wrong_non_empty_eqns = sum(1 for v in wrong_eqn_mapping.values() if v and str(v).strip())
            
            # Check if correct equations are missing (should have at least length-1 non-empty equations)
            if correct_non_empty_eqns < (correct_length - 1):
                quality_metrics['correct_missing_equations'][source][error_type] += 1
                has_any_issue = True
            
            # Check if wrong equations are missing
            if wrong_non_empty_eqns < (wrong_length - 1):
                quality_metrics['wrong_missing_equations'][source][error_type] += 1
                has_any_issue = True
                
        except (json.JSONDecodeError, KeyError, TypeError) as e:
            # If we can't parse the JSON, count as missing equations
            quality_metrics['correct_missing_equations'][source][error_type] += 1
            quality_metrics['wrong_missing_equations'][source][error_type] += 1
            has_any_issue = True
        
        # Track this row if it has any issues
        if has_any_issue:
            rows_with_any_issues[source][error_type].add(idx)
    
    # Print detailed results
    print(f"\n📊 QUALITY METRICS SUMMARY (BY SOURCE AND ERROR TYPE)")
    print("=" * 80)
    
    metrics_descriptions = {
        'missing_erroneous_line': '1. Missing Erroneous Line',
        'missing_explanation': '2. Missing Explanation', 
        'length_mismatch_non_fa': '3. Length Mismatch (Non-FA)',
        'correct_missing_equations': '4. Missing Correct Equations',
        'wrong_missing_equations': '5. Missing Wrong Equations'
    }
    
    for metric_key, description in metrics_descriptions.items():
        print(f"\n🔍 {description}:")
        print("-" * 60)
        
        metric_data = quality_metrics[metric_key]
        
        # Calculate total issues for this metric
        total_issues = sum(sum(error_counts.values()) for error_counts in metric_data.values())
        
        if total_issues == 0:
            print("   ✅ No issues found!")
        else:
            print(f"   ⚠️  Total issues: {total_issues:,}")
            
            # Show breakdown by source and error type
            for source in sources:
                source_total = len(df[df['source'] == source])
                source_issues = sum(metric_data[source].values())
                
                if source_issues > 0:
                    source_pct = (source_issues / source_total) * 100
                    print(f"\n      📌 {source.upper()}: {source_issues:,} / {source_total:,} ({source_pct:.1f}%)")
                    
                    for error_type in error_types:
                        count = metric_data[source][error_type]
                        if count > 0:
                            error_type_total = len(df[(df['source'] == source) & (df['error_type'] == error_type)])
                            if error_type_total > 0:
                                error_type_pct = (count / error_type_total) * 100
                                print(f"         └─ {error_type}: {count:,} / {error_type_total:,} ({error_type_pct:.1f}%)")
                else:
                    print(f"\n      ✅ {source.upper()}: 0 / {source_total:,} (0.0%)")
    
    # Overall summary table
    print(f"\n📋 SUMMARY TABLE")
    print("=" * 80)
    print(f"{'Metric':<30} {'Total Issues':<15} {'% of Dataset':<15}")
    print("-" * 80)
    
    for metric_key, description in metrics_descriptions.items():
        short_desc = description.split('. ')[1]  # Remove number prefix
        total_issues = sum(sum(error_counts.values()) for error_counts in quality_metrics[metric_key].values())
        pct = (total_issues / total_rows) * 100
        print(f"{short_desc:<30} {total_issues:<15,} {pct:<15.1f}%")
    
    # FIXED: Enhanced source breakdown summary using unique row counts
    print(f"\n📋 SOURCE × ERROR TYPE BREAKDOWN (UNIQUE ROWS WITH ANY ISSUES)")
    print("=" * 80)
    print(f"{'Source':<15} {'Error Type':<20} {'Total Rows':<12} {'Rows w/Issues':<14} {'Quality %':<12}")
    print("-" * 80)
    
    for source in sources:
        for error_type in error_types:
            subset_df = df[(df['source'] == source) & (df['error_type'] == error_type)]
            subset_total = len(subset_df)
            
            if subset_total > 0:
                # Count UNIQUE rows with any issues (not sum of individual issue counts)
                unique_rows_with_issues = len(rows_with_any_issues[source][error_type])
                
                # Calculate quality percentage based on unique problematic rows
                issue_pct = (unique_rows_with_issues / subset_total) * 100 if subset_total > 0 else 0
                quality_pct = max(0, 100 - issue_pct)
                
                print(f"{source:<15} {error_type:<20} {subset_total:<12,} {unique_rows_with_issues:<14,} {quality_pct:<12.1f}%")
    
    # FIXED: Additional insights using unique row counts
    print(f"\n🔬 ADDITIONAL INSIGHTS (BASED ON UNIQUE ROWS)")
    print("=" * 80)
    
    # Find the most problematic source×error_type combinations based on unique rows with issues
    problematic_combinations = []
    for source in sources:
        for error_type in error_types:
            subset_df = df[(df['source'] == source) & (df['error_type'] == error_type)]
            subset_total = len(subset_df)
            
            if subset_total > 0:
                unique_rows_with_issues = len(rows_with_any_issues[source][error_type])
                issue_rate = (unique_rows_with_issues / subset_total) * 100
                
                if issue_rate > 0:
                    problematic_combinations.append({
                        'source': source,
                        'error_type': error_type,
                        'total_rows': subset_total,
                        'unique_problematic_rows': unique_rows_with_issues,
                        'issue_rate': issue_rate
                    })
    
    # Sort by issue rate
    problematic_combinations.sort(key=lambda x: x['issue_rate'], reverse=True)
    
    if problematic_combinations:
        print("🚨 Most problematic combinations (by % of rows with ANY issues):")
        for i, combo in enumerate(problematic_combinations[:5], 1):
            print(f"   {i}. {combo['source']} × {combo['error_type']}: "
                  f"{combo['unique_problematic_rows']:,} problematic rows out of {combo['total_rows']:,} total "
                  f"({combo['issue_rate']:.1f}% have issues)")
    else:
        print("✅ No problematic combinations found!")
    
    # Additional breakdown showing issue distribution
    print(f"\n📊 ISSUE DISTRIBUTION BREAKDOWN")
    print("=" * 80)
    
    total_unique_issues = sum(len(error_type_sets) for source_dict in rows_with_any_issues.values() 
                             for error_type_sets in source_dict.values())
    
    print(f"📋 Total unique rows with any issues: {total_unique_issues:,}")
    print(f"📋 Rows with perfect quality: {total_rows - total_unique_issues:,} ({((total_rows - total_unique_issues) / total_rows * 100):.1f}%)")
    
    return quality_metrics, rows_with_any_issues

# Run the fixed enhanced analysis
quality_results, issue_tracking = analyze_data_quality_enhanced_fixed(df)

print(f"\n🎯 FIXED ENHANCED ANALYSIS COMPLETE")
print(f"💡 Now shows correct unique row counts without overcounting.")
```

    📊 ENHANCED DATA QUALITY ANALYSIS (FIXED)
    ================================================================================
    📋 Total rows: 24,652
    📋 Sources: manual, programmatic
    📋 Error types: computational_error, conceptual_error
    📋 Source distribution: {'programmatic': 22912, 'manual': 1740}
    📋 Error type distribution: {'computational_error': 22542, 'conceptual_error': 2110}
    
    🔍 Analyzing 24,652 rows...
    
    📊 QUALITY METRICS SUMMARY (BY SOURCE AND ERROR TYPE)
    ================================================================================
    
    🔍 1. Missing Erroneous Line:
    ------------------------------------------------------------
       ⚠️  Total issues: 270
    
          📌 MANUAL: 34 / 1,740 (2.0%)
             └─ conceptual_error: 34 / 966 (3.5%)
    
          📌 PROGRAMMATIC: 236 / 22,912 (1.0%)
             └─ computational_error: 232 / 21,768 (1.1%)
             └─ conceptual_error: 4 / 1,144 (0.3%)
    
    🔍 2. Missing Explanation:
    ------------------------------------------------------------
       ⚠️  Total issues: 1
    
          📌 MANUAL: 1 / 1,740 (0.1%)
             └─ computational_error: 1 / 774 (0.1%)
    
          ✅ PROGRAMMATIC: 0 / 22,912 (0.0%)
    
    🔍 3. Length Mismatch (Non-FA):
    ------------------------------------------------------------
       ⚠️  Total issues: 1,137
    
          📌 MANUAL: 201 / 1,740 (11.6%)
             └─ computational_error: 3 / 774 (0.4%)
             └─ conceptual_error: 198 / 966 (20.5%)
    
          📌 PROGRAMMATIC: 936 / 22,912 (4.1%)
             └─ computational_error: 914 / 21,768 (4.2%)
             └─ conceptual_error: 22 / 1,144 (1.9%)
    
    🔍 4. Missing Correct Equations:
    ------------------------------------------------------------
       ⚠️  Total issues: 4,828
    
          📌 MANUAL: 375 / 1,740 (21.6%)
             └─ computational_error: 171 / 774 (22.1%)
             └─ conceptual_error: 204 / 966 (21.1%)
    
          📌 PROGRAMMATIC: 4,453 / 22,912 (19.4%)
             └─ computational_error: 4,238 / 21,768 (19.5%)
             └─ conceptual_error: 215 / 1,144 (18.8%)
    
    🔍 5. Missing Wrong Equations:
    ------------------------------------------------------------
       ⚠️  Total issues: 4,305
    
          📌 MANUAL: 478 / 1,740 (27.5%)
             └─ computational_error: 172 / 774 (22.2%)
             └─ conceptual_error: 306 / 966 (31.7%)
    
          📌 PROGRAMMATIC: 3,827 / 22,912 (16.7%)
             └─ computational_error: 3,650 / 21,768 (16.8%)
             └─ conceptual_error: 177 / 1,144 (15.5%)
    
    📋 SUMMARY TABLE
    ================================================================================
    Metric                         Total Issues    % of Dataset   
    --------------------------------------------------------------------------------
    Missing Erroneous Line         270             1.1            %
    Missing Explanation            1               0.0            %
    Length Mismatch (Non-FA)       1,137           4.6            %
    Missing Correct Equations      4,828           19.6           %
    Missing Wrong Equations        4,305           17.5           %
    
    📋 SOURCE × ERROR TYPE BREAKDOWN (UNIQUE ROWS WITH ANY ISSUES)
    ================================================================================
    Source          Error Type           Total Rows   Rows w/Issues  Quality %   
    --------------------------------------------------------------------------------
    manual          computational_error  774          173            77.6        %
    manual          conceptual_error     966          443            54.1        %
    programmatic    computational_error  21,768       4,387          79.8        %
    programmatic    conceptual_error     1,144        215            81.2        %
    
    🔬 ADDITIONAL INSIGHTS (BASED ON UNIQUE ROWS)
    ================================================================================
    🚨 Most problematic combinations (by % of rows with ANY issues):
       1. manual × conceptual_error: 443 problematic rows out of 966 total (45.9% have issues)
       2. manual × computational_error: 173 problematic rows out of 774 total (22.4% have issues)
       3. programmatic × computational_error: 4,387 problematic rows out of 21,768 total (20.2% have issues)
       4. programmatic × conceptual_error: 215 problematic rows out of 1,144 total (18.8% have issues)
    
    📊 ISSUE DISTRIBUTION BREAKDOWN
    ================================================================================
    📋 Total unique rows with any issues: 5,218
    📋 Rows with perfect quality: 19,434 (78.8%)
    
    🎯 FIXED ENHANCED ANALYSIS COMPLETE
    💡 Now shows correct unique row counts without overcounting.



```python
df = df.dropna(subset=['erroneous_line', 'explanation'])
```


```python
# 1. All rows with manual source and missing erroneous line
manual_missing_erroneous_line = df[
    (df['source'] == 'manual') & 
    (
        pd.isna(df['erroneous_line']) | 
        (df['erroneous_line'].astype(str).str.strip() == '') |
        (df['erroneous_line'].astype(str) == 'nan')
    )
].copy()

print("📊 MANUAL SOURCE + MISSING ERRONEOUS LINE")
print("=" * 60)
print(f"Total rows found: {len(manual_missing_erroneous_line):,}")

if len(manual_missing_erroneous_line) > 0:
    print(f"Sample GSM8K indices: {manual_missing_erroneous_line['index'].head(10).tolist()}")
    print(f"Error types: {manual_missing_erroneous_line['error_type'].value_counts().to_dict()}")
    print(f"Tiers: {manual_missing_erroneous_line['tier'].value_counts().to_dict()}")
    
    # Show a sample row
    print(f"\n🔍 SAMPLE ROW:")
    print("-" * 40)
    sample_row = manual_missing_erroneous_line.iloc[0]
    print(f"Index: {sample_row['index']}")
    print(f"Tier: {sample_row['tier']}")
    print(f"Error Type: {sample_row['error_type']}")
    print(f"Erroneous Line Number: {sample_row['erroneous_line_number']}")
    print(f"Erroneous Line: {repr(sample_row['erroneous_line'])}")
    print(f"Explanation: {sample_row['explanation'][:100]}...")
else:
    print("✅ No rows found with this combination")

# 2. All rows with manual source and non-FA length mismatch
manual_length_mismatch = df[
    (df['source'] == 'manual') & 
    (df['erroneous_line_number'] != 'FA') &
    (df['correct_answer_length'] != df['wrong_answer_length'])
].copy()

print(f"\n📊 MANUAL SOURCE + NON-FA LENGTH MISMATCH")
print("=" * 60)
print(f"Total rows found: {len(manual_length_mismatch):,}")

if len(manual_length_mismatch) > 0:
    print(f"Sample GSM8K indices: {manual_length_mismatch['index'].head(10).tolist()}")
    print(f"Error types: {manual_length_mismatch['error_type'].value_counts().to_dict()}")
    print(f"Tiers: {manual_length_mismatch['tier'].value_counts().to_dict()}")
    print(f"Erroneous line numbers: {manual_length_mismatch['erroneous_line_number'].value_counts().to_dict()}")
    
    # Show length difference statistics
    manual_length_mismatch['length_diff'] = manual_length_mismatch['correct_answer_length'] - manual_length_mismatch['wrong_answer_length']
    print(f"Length differences: {manual_length_mismatch['length_diff'].value_counts().to_dict()}")
    
    # Show a sample row
    print(f"\n🔍 SAMPLE ROW:")
    print("-" * 40)
    sample_row = manual_length_mismatch.iloc[0]
    print(f"Index: {sample_row['index']}")
    print(f"Tier: {sample_row['tier']}")
    print(f"Error Type: {sample_row['error_type']}")
    print(f"Erroneous Line Number: {sample_row['erroneous_line_number']}")
    print(f"Correct Answer Length: {sample_row['correct_answer_length']}")
    print(f"Wrong Answer Length: {sample_row['wrong_answer_length']}")
    print(f"Length Difference: {sample_row['length_diff']}")
    print(f"Explanation: {sample_row['explanation'][:100]}...")
else:
    print("✅ No rows found with this combination")

# Summary of both dataframes
print(f"\n📋 SUMMARY")
print("=" * 60)
print(f"Manual source total rows: {len(df[df['source'] == 'manual']):,}")
print(f"Rows with missing erroneous line: {len(manual_missing_erroneous_line):,}")
print(f"Rows with non-FA length mismatch: {len(manual_length_mismatch):,}")

# Check for overlap between the two issues
if len(manual_missing_erroneous_line) > 0 and len(manual_length_mismatch) > 0:
    overlap_indices = set(manual_missing_erroneous_line['index']) & set(manual_length_mismatch['index'])
    print(f"Rows with BOTH issues: {len(overlap_indices):,}")
    if len(overlap_indices) > 0:
        print(f"Overlapping GSM8K indices: {list(overlap_indices)[:10]}")
```

    📊 MANUAL SOURCE + MISSING ERRONEOUS LINE
    ============================================================
    Total rows found: 0
    ✅ No rows found with this combination
    
    📊 MANUAL SOURCE + NON-FA LENGTH MISMATCH
    ============================================================
    Total rows found: 167
    Sample GSM8K indices: [1087, 1003, 1004, 1007, 1008, 1016, 1019, 1020, 1023, 1024]
    Error types: {'conceptual_error': 164, 'computational_error': 3}
    Tiers: {'tier1': 65, 'tier3': 59, 'tier2': 22, 'tier4': 12, 'tier5': 9}
    Erroneous line numbers: {'L1': 82, 'L2': 45, 'L3': 28, 'L4': 10, 'L5': 1, 'L6': 1}
    Length differences: {1: 115, -1: 24, 2: 13, 3: 10, -2: 4, 4: 1}
    
    🔍 SAMPLE ROW:
    ----------------------------------------
    Index: 1087
    Tier: tier5
    Error Type: computational_error
    Erroneous Line Number: L5
    Correct Answer Length: 7
    Wrong Answer Length: 8
    Length Difference: -1
    Explanation: computational error: In the equation 100 - x + 40 - 30 = 60, the calculation of 40 - 30 was incorrec...
    
    📋 SUMMARY
    ============================================================
    Manual source total rows: 1,705
    Rows with missing erroneous line: 0
    Rows with non-FA length mismatch: 167



```python
manual_length_mismatch.head()
```




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
      <th>question</th>
      <th>correct_answer</th>
      <th>wrong_answer</th>
      <th>error_type</th>
      <th>explanation</th>
      <th>erroneous_line_number</th>
      <th>erroneous_line</th>
      <th>erroneous_line_eqn</th>
      <th>correct_answer_mapping</th>
      <th>wrong_answer_mapping</th>
      <th>correct_eqn_mapping</th>
      <th>wrong_eqn_mapping</th>
      <th>correct_answer_length</th>
      <th>wrong_answer_length</th>
      <th>source</th>
      <th>error_subtype</th>
      <th>length_diff</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>69</th>
      <td>1087</td>
      <td>tier5</td>
      <td>Hadley loves to do volunteer work at the local...</td>
      <td>Let x be the number of books borrowed by lunch...</td>
      <td>Let x be the number of books borrowed by lunch...</td>
      <td>computational_error</td>
      <td>computational error: In the equation 100 - x +...</td>
      <td>L5</td>
      <td>Thus 100 - x + 20 = 60</td>
      <td>NaN</td>
      <td>{\n  "L1": "Let x be the number of books borro...</td>
      <td>{\n  "L1": "Let x be the number of books borro...</td>
      <td>{\n  "L1": "",\n  "L2": "",\n  "L3": "",\n  "L...</td>
      <td>{\n  "L1": "",\n  "L2": "",\n  "L3": "",\n  "L...</td>
      <td>7</td>
      <td>8</td>
      <td>manual</td>
      <td>NaN</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>83</th>
      <td>1003</td>
      <td>tier3</td>
      <td>Cheryl is signing up for a golf tournament tha...</td>
      <td>If the electricity bill costs $800, and Cheryl...</td>
      <td>If the electricity bill costs $800, and Cheryl...</td>
      <td>conceptual_error</td>
      <td>misunderstanding of problem: The student calcu...</td>
      <td>L2</td>
      <td>Since the cost to enter the tournament is 20% ...</td>
      <td>20/100*1200=240</td>
      <td>{\n  "L1": "If the electricity bill costs $800...</td>
      <td>{\n  "L1": "If the electricity bill costs $800...</td>
      <td>{\n  "L1": "800+400=1200",\n  "L2": "20/100*12...</td>
      <td>{\n  "L1": "800+400=1200",\n  "L2": "20/100*12...</td>
      <td>4</td>
      <td>3</td>
      <td>manual</td>
      <td>NaN</td>
      <td>1</td>
    </tr>
    <tr>
      <th>84</th>
      <td>1004</td>
      <td>tier1</td>
      <td>Kamil wants to renovate his kitchen at home. F...</td>
      <td>Two professionals work together 6 * 2 = 12 hou...</td>
      <td>One professional works 6 hours a day for 7 day...</td>
      <td>conceptual_error</td>
      <td>misunderstanding of problem: The calculation f...</td>
      <td>L1</td>
      <td>One professional works 6 hours a day for 7 day...</td>
      <td>6*7=42</td>
      <td>{\n  "L1": "Two professionals work together 6 ...</td>
      <td>{\n  "L1": "One professional works 6 hours a d...</td>
      <td>{\n  "L1": "6*2=12",\n  "L2": "7*12=84",\n  "L...</td>
      <td>{\n  "L1": "6*7=42",\n  "L2": "42*15=630",\n  ...</td>
      <td>4</td>
      <td>3</td>
      <td>manual</td>
      <td>NaN</td>
      <td>1</td>
    </tr>
    <tr>
      <th>87</th>
      <td>1007</td>
      <td>tier5</td>
      <td>Rajesh walked 10 kilometers less than 4 times ...</td>
      <td>Let H = distance Hiro walked\n4H - 10 = distan...</td>
      <td>Let H = distance Hiro walked\n4(H - 10) = dist...</td>
      <td>conceptual_error</td>
      <td>misinterpretation of phrase: The phrase "10 ki...</td>
      <td>L2</td>
      <td>4(H - 10) = distance Rajesh walked</td>
      <td>NaN</td>
      <td>{\n  "L1": "Let H = distance Hiro walked",\n  ...</td>
      <td>{\n  "L1": "Let H = distance Hiro walked",\n  ...</td>
      <td>{\n  "L1": "",\n  "L2": "",\n  "L3": "",\n  "L...</td>
      <td>{\n  "L1": "",\n  "L2": "",\n  "L3": "",\n  "L...</td>
      <td>8</td>
      <td>9</td>
      <td>manual</td>
      <td>NaN</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>88</th>
      <td>1008</td>
      <td>tier1</td>
      <td>Lana aims to sell 20 muffins at the bake sale....</td>
      <td>Lana sold 12 muffins and has to sell 20 - 12 =...</td>
      <td>Lana sold another 4 in the afternoon. So Lana ...</td>
      <td>conceptual_error</td>
      <td>skipped step: The step where the 12 muffins so...</td>
      <td>L1</td>
      <td>Lana sold another 4 in the afternoon. So Lana ...</td>
      <td>20-4=16</td>
      <td>{\n  "L1": "Lana sold 12 muffins and has to se...</td>
      <td>{\n  "L1": "Lana sold another 4 in the afterno...</td>
      <td>{\n  "L1": "",\n  "L2": "8-4=4",\n  "FA": ""\n}</td>
      <td>{\n  "L1": "20-4=16",\n  "FA": ""\n}</td>
      <td>3</td>
      <td>2</td>
      <td>manual</td>
      <td>NaN</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
manual_length_mismatch.to_csv(AUG_5_DATASET_DIR / "manual_length_mismatch.csv", index=False)
```


```python
# Load the manually edited CSV
manual_edited = pd.read_csv(AUG_5_DATASET_DIR / "manual_length_mismatch.csv")

print("🔄 SIMPLE MERGE: MANUALLY EDITED DATA BACK TO MASTER CATALOG")
print("=" * 70)

# Display initial state
print(f"📊 Initial master catalog rows: {len(df):,}")
print(f"📊 Manual edits to merge: {len(manual_edited):,}")

# Track changes
rows_updated = 0
rows_not_found = 0
not_found_details = []

# Loop over each manually edited row
for _, edited_row in manual_edited.iterrows():
    edit_index = edited_row['index']
    edit_error_type = edited_row['error_type']
    
    # Find the matching row in df (same index, error_type, and manual source)
    mask = (df['index'] == edit_index) & \
           (df['error_type'] == edit_error_type) & \
           (df['source'] == 'manual')
    
    matching_rows = df[mask]
    
    if len(matching_rows) == 1:
        # Found exactly one match - replace it
        row_idx = matching_rows.index[0]
        
        # Replace the entire row with the edited version
        for col in df.columns:
            if col in edited_row:
                df.at[row_idx, col] = edited_row[col]
        
        rows_updated += 1
        
    elif len(matching_rows) == 0:
        # No match found
        rows_not_found += 1
        not_found_details.append({
            'index': edit_index,
            'error_type': edit_error_type
        })
        
    else:
        # Multiple matches found (shouldn't happen)
        print(f"⚠️  WARNING: Multiple matches found for index={edit_index}, error_type={edit_error_type}")
        rows_not_found += 1
        not_found_details.append({
            'index': edit_index,
            'error_type': edit_error_type,
            'issue': f'Multiple matches ({len(matching_rows)})'
        })

# Report results
print(f"\n📊 MERGE RESULTS:")
print(f"   Rows successfully updated: {rows_updated:,}")
print(f"   Rows not found/problematic: {rows_not_found:,}")

if rows_not_found > 0:
    print(f"\n❌ PROBLEMATIC ROWS:")
    for detail in not_found_details[:5]:  # Show first 5
        issue = detail.get('issue', 'Not found')
        print(f"   Index {detail['index']}, Error Type {detail['error_type']}: {issue}")
    if len(not_found_details) > 5:
        print(f"   ... and {len(not_found_details) - 5} more")
else:
    print("✅ All edited rows were successfully merged!")

# Verification
manual_rows_in_df = len(df[df['source'] == 'manual'])
print(f"\n📋 VERIFICATION:")
print(f"   Total rows in master catalog: {len(df):,}")
print(f"   Manual source rows: {manual_rows_in_df:,}")

# Show sample of updated data
if rows_updated > 0:
    print(f"\n🔍 SAMPLE OF UPDATED ROWS:")
    sample_indices = manual_edited['index'].head(3).tolist()
    for idx in sample_indices:
        sample_row = df[(df['index'] == idx) & (df['source'] == 'manual')]
        if not sample_row.empty:
            row = sample_row.iloc[0]
            print(f"   Index {idx}: {row['error_type']} | Tier: {row['tier']}")

print(f"\n🎉 SIMPLE MERGE COMPLETE!")
print(f"✅ {rows_updated:,} rows updated in master catalog")
```

    🔄 SIMPLE MERGE: MANUALLY EDITED DATA BACK TO MASTER CATALOG
    ======================================================================
    📊 Initial master catalog rows: 24,376
    📊 Manual edits to merge: 167
    
    📊 MERGE RESULTS:
       Rows successfully updated: 167
       Rows not found/problematic: 0
    ✅ All edited rows were successfully merged!
    
    📋 VERIFICATION:
       Total rows in master catalog: 24,376
       Manual source rows: 1,700
    
    🔍 SAMPLE OF UPDATED ROWS:
       Index 1087: conceptual_error | Tier: tier5
       Index 1003: computational_error | Tier: tier3
       Index 1004: computational_error | Tier: tier1
    
    🎉 SIMPLE MERGE COMPLETE!
    ✅ 167 rows updated in master catalog
    
    📋 VERIFICATION:
       Total rows in master catalog: 24,376
       Manual source rows: 1,700
    
    🔍 SAMPLE OF UPDATED ROWS:
       Index 1087: conceptual_error | Tier: tier5
       Index 1003: computational_error | Tier: tier3
       Index 1004: computational_error | Tier: tier1
    
    🎉 SIMPLE MERGE COMPLETE!
    ✅ 167 rows updated in master catalog



```python
df.to_csv(AUG_5_DATASET_DIR / "master_catalog.csv", index=False)
```


```python
# Check for rows where erroneous_line_number is not in wrong_answer_mapping
import json
import pandas as pd

def check_erroneous_line_in_mapping(df):
    """
    Check for rows where the erroneous_line_number is not found in the wrong_answer_mapping.
    """
    print("🔍 CHECKING ERRONEOUS LINE NUMBER vs WRONG ANSWER MAPPING")
    print("=" * 70)
    
    problematic_rows = []
    
    for idx, row in df.iterrows():
        try:
            erroneous_line_number = row['erroneous_line_number']
            wrong_mapping_json = row['wrong_answer_mapping']
            
            # Skip if either field is missing
            if pd.isna(erroneous_line_number) or pd.isna(wrong_mapping_json):
                continue
            
            # Parse the wrong answer mapping
            wrong_mapping = json.loads(wrong_mapping_json)
            
            # Check if erroneous line number exists in the mapping
            if erroneous_line_number not in wrong_mapping:
                problematic_rows.append({
                    'row_index': idx,
                    'gsm8k_index': row['index'],
                    'source': row['source'],
                    'error_type': row['error_type'],
                    'tier': row['tier'],
                    'erroneous_line_number': erroneous_line_number,
                    'available_line_numbers': list(wrong_mapping.keys()),
                    'wrong_answer_length': row['wrong_answer_length'],
                    'explanation': row['explanation'][:100] + "..." if len(str(row['explanation'])) > 100 else row['explanation']
                })
                
        except json.JSONDecodeError as e:
            # JSON parsing error
            problematic_rows.append({
                'row_index': idx,
                'gsm8k_index': row['index'],
                'source': row['source'],
                'error_type': row['error_type'],
                'tier': row['tier'],
                'erroneous_line_number': erroneous_line_number,
                'available_line_numbers': 'JSON_PARSE_ERROR',
                'wrong_answer_length': row['wrong_answer_length'],
                'explanation': f"JSON Error: {str(e)}"
            })
        except Exception as e:
            # Other errors
            problematic_rows.append({
                'row_index': idx,
                'gsm8k_index': row['index'],
                'source': row['source'],
                'error_type': row['error_type'],
                'tier': row['tier'],
                'erroneous_line_number': erroneous_line_number,
                'available_line_numbers': 'OTHER_ERROR',
                'wrong_answer_length': row['wrong_answer_length'],
                'explanation': f"Error: {str(e)}"
            })
    
    # Convert to DataFrame for easier analysis
    problematic_df = pd.DataFrame(problematic_rows)
    
    print(f"📊 RESULTS:")
    print(f"   Total rows checked: {len(df):,}")
    print(f"   Problematic rows found: {len(problematic_rows):,}")
    
    if len(problematic_rows) > 0:
        print(f"\n📋 BREAKDOWN BY SOURCE:")
        source_counts = problematic_df['source'].value_counts()
        for source, count in source_counts.items():
            total_source_rows = len(df[df['source'] == source])
            pct = (count / total_source_rows) * 100
            print(f"   {source}: {count:,} / {total_source_rows:,} ({pct:.1f}%)")
        
        print(f"\n📋 BREAKDOWN BY ERROR TYPE:")
        error_type_counts = problematic_df['error_type'].value_counts()
        for error_type, count in error_type_counts.items():
            total_error_type_rows = len(df[df['error_type'] == error_type])
            pct = (count / total_error_type_rows) * 100
            print(f"   {error_type}: {count:,} / {total_error_type_rows:,} ({pct:.1f}%)")
        
        print(f"\n🔍 SAMPLE PROBLEMATIC ROWS:")
        print("-" * 70)
        for i, row in enumerate(problematic_df.head(5).itertuples(), 1):
            print(f"\n{i}. GSM8K Index {row.gsm8k_index} (Source: {row.source}, Type: {row.error_type})")
            print(f"   Erroneous Line Number: {row.erroneous_line_number}")
            print(f"   Available Line Numbers: {row.available_line_numbers}")
            print(f"   Wrong Answer Length: {row.wrong_answer_length}")
            print(f"   Explanation: {row.explanation}")
        
        if len(problematic_rows) > 5:
            print(f"\n   ... and {len(problematic_rows) - 5} more problematic rows")
    else:
        print("\n✅ All erroneous line numbers are properly found in their wrong answer mappings!")
    
    return problematic_df

# Run the check
problematic_mappings = check_erroneous_line_in_mapping(df)

# Save problematic rows if any found
if len(problematic_mappings) > 0:
    output_path = AUG_5_DATASET_DIR / "problematic_line_mappings.csv"
    problematic_mappings.to_csv(output_path, index=False)
    print(f"\n💾 Problematic rows saved to: {output_path}")
```

    🔍 CHECKING ERRONEOUS LINE NUMBER vs WRONG ANSWER MAPPING
    ======================================================================
    📊 RESULTS:
       Total rows checked: 24,376
       Problematic rows found: 0
    
    ✅ All erroneous line numbers are properly found in their wrong answer mappings!



```python
import pandas as pd
import json
import numpy as np
from collections import defaultdict

def create_equation_extraction_dataset_refined(df):
    """
    Create equation extraction dataset with distinct samples and unified error_type column.
    """
    print("🔧 CREATING EQUATION EXTRACTION DATASET (REFINED)")
    print("=" * 70)
    
    # Define sample types and their criteria
    sample_configs = {
        'computational_error': {
            'criteria': lambda row: row['error_type'] == 'computational_error',
            'answer_mapping_col': 'wrong_answer_mapping', 
            'eqn_mapping_col': 'wrong_eqn_mapping'
        },
        'conceptual_error': {
            'criteria': lambda row: row['error_type'] == 'conceptual_error',
            'answer_mapping_col': 'wrong_answer_mapping',
            'eqn_mapping_col': 'wrong_eqn_mapping'
        }
    }
    
    # Tier priorities: tier4 (100), tier2 (50), tier3 (100), tier1 (remaining)
    tier_priorities = [
        ('tier4', 100),
        ('tier2', 50), 
        ('tier3', 100),
        ('tier1', None)  # Fill remaining slots
    ]
    
    target_samples_per_type = 300
    
    def has_complete_annotation_coverage(row, eqn_mapping_col):
        """Check if all solution lines except FA have calculator annotations."""
        try:
            eqn_mapping = json.loads(row[eqn_mapping_col])
            
            # Count total lines (excluding FA)
            answer_length = row['correct_answer_length'] if 'correct' in eqn_mapping_col else row['wrong_answer_length']
            expected_lines = answer_length - 1 if 'FA' in eqn_mapping else answer_length
            
            # Count non-empty equations (excluding FA)
            non_empty_equations = sum(1 for key, value in eqn_mapping.items() 
                                    if key != 'FA' and value and str(value).strip())
            
            return non_empty_equations == expected_lines
            
        except (json.JSONDecodeError, KeyError, TypeError):
            return False
    
    selected_samples = []
    used_indices = set()  # Track used GSM8K indices to ensure distinctness
    
    # First, process error samples (computational and conceptual)
    for sample_type, config in sample_configs.items():
        print(f"\n📋 Processing {sample_type.upper()} samples...")
        
        # Filter candidates based on criteria
        candidates = df[df.apply(config['criteria'], axis=1)].copy()
        
        print(f"   Initial candidates: {len(candidates):,}")
        
        # Filter for complete annotation coverage
        candidates = candidates[
            candidates.apply(lambda row: has_complete_annotation_coverage(row, config['eqn_mapping_col']), axis=1)
        ].copy()
        
        print(f"   With complete annotation coverage: {len(candidates):,}")
        
        if len(candidates) == 0:
            print(f"   ❌ No candidates found for {sample_type}")
            continue
        
        # Select samples by tier priority
        selected_for_type = []
        remaining_slots = target_samples_per_type
        
        for tier, target_count in tier_priorities:
            if remaining_slots <= 0:
                break
                
            tier_candidates = candidates[candidates['tier'] == tier]
            
            if target_count is None:  # tier1 - fill remaining slots
                target_count = remaining_slots
            
            available_count = len(tier_candidates)
            actual_count = min(target_count, available_count, remaining_slots)
            
            if actual_count > 0:
                # Randomly sample from this tier
                tier_selected = tier_candidates.sample(n=actual_count, random_state=42).copy()
                selected_for_type.append(tier_selected)
                remaining_slots -= actual_count
                
                # Track used indices
                used_indices.update(tier_selected['index'].tolist())
                
                print(f"   {tier}: {actual_count:,} selected (available: {available_count:,}, target: {target_count})")
        
        # Combine all selected samples for this type
        if selected_for_type:
            type_samples = pd.concat(selected_for_type, ignore_index=True)
            
            # Add train/test split (4:1 ratio)
            np.random.seed(42 + len(selected_samples))  # Different seed per type
            n_samples = len(type_samples)
            n_train = int(0.8 * n_samples)  # 4:1 ratio
            
            indices = np.random.permutation(n_samples)
            train_indices = indices[:n_train]
            test_indices = indices[n_train:]
            
            type_samples['split'] = 'test'  # Default to test
            type_samples.iloc[train_indices, type_samples.columns.get_loc('split')] = 'train'
            
            selected_samples.append(type_samples)
            
            print(f"   ✅ Final selection: {len(type_samples):,} samples")
            print(f"      Train: {len(type_samples[type_samples['split'] == 'train']):,}")
            print(f"      Test: {len(type_samples[type_samples['split'] == 'test']):,}")
            
            # Show tier distribution
            tier_dist = type_samples['tier'].value_counts().sort_index()
            print(f"      Tier distribution: {dict(tier_dist)}")
    
    # Now process correct samples, excluding used indices
    print(f"\n📋 Processing CORRECT samples...")
    print(f"   Excluding {len(used_indices):,} indices already used in error samples")
    
    # Filter out used indices to ensure distinctness
    correct_candidates = df[~df['index'].isin(used_indices)].copy()
    
    print(f"   Initial distinct candidates: {len(correct_candidates):,}")
    
    # Filter for complete annotation coverage using correct mappings
    correct_candidates = correct_candidates[
        correct_candidates.apply(lambda row: has_complete_annotation_coverage(row, 'correct_eqn_mapping'), axis=1)
    ].copy()
    
    print(f"   With complete annotation coverage: {len(correct_candidates):,}")
    
    if len(correct_candidates) > 0:
        # Select correct samples by tier priority
        selected_correct = []
        remaining_slots = target_samples_per_type
        
        for tier, target_count in tier_priorities:
            if remaining_slots <= 0:
                break
                
            tier_candidates = correct_candidates[correct_candidates['tier'] == tier]
            
            if target_count is None:  # tier1 - fill remaining slots
                target_count = remaining_slots
            
            available_count = len(tier_candidates)
            actual_count = min(target_count, available_count, remaining_slots)
            
            if actual_count > 0:
                # Randomly sample from this tier
                tier_selected = tier_candidates.sample(n=actual_count, random_state=43).copy()
                selected_correct.append(tier_selected)
                remaining_slots -= actual_count
                
                print(f"   {tier}: {actual_count:,} selected (available: {available_count:,}, target: {target_count})")
        
        # Combine all selected correct samples
        if selected_correct:
            correct_samples = pd.concat(selected_correct, ignore_index=True)
            
            # Set error_type to "correct" for these samples
            correct_samples['error_type'] = 'correct'
            
            # Add train/test split (4:1 ratio)
            np.random.seed(44)  # Different seed for correct samples
            n_samples = len(correct_samples)
            n_train = int(0.8 * n_samples)  # 4:1 ratio
            
            indices = np.random.permutation(n_samples)
            train_indices = indices[:n_train]
            test_indices = indices[n_train:]
            
            correct_samples['split'] = 'test'  # Default to test
            correct_samples.iloc[train_indices, correct_samples.columns.get_loc('split')] = 'train'
            
            selected_samples.append(correct_samples)
            
            print(f"   ✅ Final selection: {len(correct_samples):,} samples")
            print(f"      Train: {len(correct_samples[correct_samples['split'] == 'train']):,}")
            print(f"      Test: {len(correct_samples[correct_samples['split'] == 'test']):,}")
            
            # Show tier distribution
            tier_dist = correct_samples['tier'].value_counts().sort_index()
            print(f"      Tier distribution: {dict(tier_dist)}")
    else:
        print(f"   ❌ No distinct correct samples found")
    
    # Combine all sample types
    if selected_samples:
        final_dataset = pd.concat(selected_samples, ignore_index=True)
        
        print(f"\n🎯 FINAL DATASET SUMMARY")
        print("=" * 50)
        print(f"Total samples: {len(final_dataset):,}")
        
        # Verify distinctness
        unique_indices = final_dataset['index'].nunique()
        total_samples = len(final_dataset)
        print(f"Unique GSM8K indices: {unique_indices:,} (should equal total samples: {total_samples:,})")
        if unique_indices == total_samples:
            print("✅ All samples are distinct!")
        else:
            print(f"❌ WARNING: {total_samples - unique_indices} duplicate indices found!")
        
        # Summary by error type (now unified)
        print(f"\nBy Error Type:")
        for error_type in ['correct', 'computational_error', 'conceptual_error']:
            type_data = final_dataset[final_dataset['error_type'] == error_type]
            if len(type_data) > 0:
                train_count = len(type_data[type_data['split'] == 'train'])
                test_count = len(type_data[type_data['split'] == 'test'])
                print(f"  {error_type}: {len(type_data):,} (train: {train_count:,}, test: {test_count:,})")
        
        # Summary by split
        print(f"\nBy Split:")
        split_counts = final_dataset['split'].value_counts()
        for split, count in split_counts.items():
            pct = (count / len(final_dataset)) * 100
            print(f"  {split}: {count:,} ({pct:.1f}%)")
        
        # Summary by tier
        print(f"\nBy Tier:")
        tier_counts = final_dataset['tier'].value_counts().sort_index()
        for tier, count in tier_counts.items():
            pct = (count / len(final_dataset)) * 100
            print(f"  {tier}: {count:,} ({pct:.1f}%)")
        
        # Summary by source
        print(f"\nBy Source:")
        source_counts = final_dataset['source'].value_counts()
        for source, count in source_counts.items():
            pct = (count / len(final_dataset)) * 100
            print(f"  {source}: {count:,} ({pct:.1f}%)")
        
        return final_dataset
    else:
        print("\n❌ No samples could be selected!")
        return pd.DataFrame()

# Create the refined equation extraction dataset
equation_extraction_dataset = create_equation_extraction_dataset_refined(df)

# Save the dataset
if not equation_extraction_dataset.empty:
    output_path = AUG_5_DATASET_DIR / "equation_extraction_dataset.csv"
    equation_extraction_dataset.to_csv(output_path, index=False)
    print(f"\n💾 Dataset saved to: {output_path}")
    
    # # Save metadata
    # metadata = {
    #     "dataset_name": "equation_extraction_dataset",
    #     "creation_date": "2025-08-05",
    #     "total_samples": len(equation_extraction_dataset),
    #     "error_type_distribution": dict(equation_extraction_dataset['error_type'].value_counts()),
    #     "split_distribution": dict(equation_extraction_dataset['split'].value_counts()),
    #     "tier_distribution": dict(equation_extraction_dataset['tier'].value_counts()),
    #     "source_distribution": dict(equation_extraction_dataset['source'].value_counts()),
    #     "columns": list(equation_extraction_dataset.columns),
    #     "distinctness_verified": equation_extraction_dataset['index'].nunique() == len(equation_extraction_dataset),
    #     "description": "Dataset for fine-tuning equation extraction task with distinct samples and complete annotation coverage"
    # }
    
    # metadata_path = AUG_5_DATASET_DIR / "equation_extraction_metadata.json"
    # with open(metadata_path, 'w') as f:
    #     json.dump(metadata, f, indent=2)
    
    # print(f"💾 Metadata saved to: {metadata_path}")
    
else:
    print("❌ Dataset creation failed!")
```

    🔧 CREATING EQUATION EXTRACTION DATASET (REFINED)
    ======================================================================
    
    📋 Processing COMPUTATIONAL_ERROR samples...
       Initial candidates: 22,309
       With complete annotation coverage: 18,576
       tier4: 100 selected (available: 969, target: 100)
       tier2: 50 selected (available: 2,617, target: 50)
       tier3: 100 selected (available: 5,983, target: 100)
       tier1: 50 selected (available: 9,007, target: 50)
       ✅ Final selection: 300 samples
          Train: 240
          Test: 60
          Tier distribution: {'tier1': 50, 'tier2': 50, 'tier3': 100, 'tier4': 100}
    
    📋 Processing CONCEPTUAL_ERROR samples...
       Initial candidates: 2,067
       With complete annotation coverage: 1,591
       tier4: 100 selected (available: 169, target: 100)
       tier2: 50 selected (available: 261, target: 50)
       tier3: 100 selected (available: 605, target: 100)
       tier1: 50 selected (available: 556, target: 50)
       ✅ Final selection: 300 samples
          Train: 240
          Test: 60
          Tier distribution: {'tier1': 50, 'tier2': 50, 'tier3': 100, 'tier4': 100}
    
    📋 Processing CORRECT samples...
       Excluding 538 indices already used in error samples
       Initial distinct candidates: 21,953
       With complete annotation coverage: 17,424
       tier4: 100 selected (available: 534, target: 100)
       tier2: 50 selected (available: 2,307, target: 50)
       tier3: 100 selected (available: 5,762, target: 100)
       tier1: 50 selected (available: 8,821, target: 50)
       ✅ Final selection: 300 samples
          Train: 240
          Test: 60
          Tier distribution: {'tier1': 50, 'tier2': 50, 'tier3': 100, 'tier4': 100}
    
    🎯 FINAL DATASET SUMMARY
    ==================================================
    Total samples: 900
    Unique GSM8K indices: 815 (should equal total samples: 900)
    ❌ WARNING: 85 duplicate indices found!
    
    By Error Type:
      correct: 300 (train: 240, test: 60)
      computational_error: 300 (train: 240, test: 60)
      conceptual_error: 300 (train: 240, test: 60)
    
    By Split:
      train: 720 (80.0%)
      test: 180 (20.0%)
    
    By Tier:
      tier1: 150 (16.7%)
      tier2: 150 (16.7%)
      tier3: 300 (33.3%)
      tier4: 300 (33.3%)
    
    By Source:
      programmatic: 783 (87.0%)
      manual: 117 (13.0%)
    
    💾 Dataset saved to: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/aug-5-dataset/equation_extraction_dataset.csv



```python
import pandas as pd
import json
import numpy as np
from collections import defaultdict

def create_error_detection_dataset(df):
    """
    Create error detection dataset with specified design requirements.
    """
    print("🔧 CREATING ERROR DETECTION DATASET")
    print("=" * 70)
    
    # Tier priorities: tier4 (500), tier2 (500), tier3 (500), tier1 (500)
    tier_priorities = [
        ('tier4', 500),
        ('tier2', 500), 
        ('tier3', 500),
        ('tier1', 500)
    ]
    
    used_indices = set()  # Track used GSM8K indices to ensure distinctness
    selected_samples = []
    
    # Step 1: Get all conceptual error samples
    print(f"\n📋 Step 1: Processing CONCEPTUAL ERROR samples...")
    conceptual_samples = df[df['error_type'] == 'conceptual_error'].copy()
    N = len(conceptual_samples)
    
    print(f"   Found N = {N:,} conceptual error samples")
    
    # Track conceptual indices
    conceptual_indices = set(conceptual_samples['index'].tolist())
    used_indices.update(conceptual_indices)
    
    # Add split column (will assign later)
    conceptual_samples['split'] = 'train'  # Default, will be reassigned
    selected_samples.append(conceptual_samples)
    
    print(f"   ✅ Added {len(conceptual_samples):,} conceptual error samples")
    
    # Step 2: Add N computational error samples (distinct problem indices)
    print(f"\n📋 Step 2: Processing COMPUTATIONAL ERROR samples...")
    print(f"   Target: {N:,} samples with distinct indices from conceptual samples")
    
    # Get computational candidates excluding conceptual indices
    computational_candidates = df[
        (df['error_type'] == 'computational_error') & 
        (~df['index'].isin(used_indices))
    ].copy()
    
    print(f"   Available distinct computational candidates: {len(computational_candidates):,}")
    
    # Select computational samples by tier priority
    selected_computational = []
    remaining_slots = N
    
    for tier, tier_limit in tier_priorities:
        if remaining_slots <= 0:
            break
            
        tier_candidates = computational_candidates[computational_candidates['tier'] == tier]
        available_count = len(tier_candidates)
        actual_count = min(tier_limit, available_count, remaining_slots)
        
        if actual_count > 0:
            # Randomly sample from this tier
            tier_selected = tier_candidates.sample(n=actual_count, random_state=42).copy()
            selected_computational.append(tier_selected)
            remaining_slots -= actual_count
            
            # Track used indices
            used_indices.update(tier_selected['index'].tolist())
            
            print(f"   {tier}: {actual_count:,} selected (available: {available_count:,}, limit: {tier_limit:,})")
    
    # Combine computational samples
    if selected_computational:
        computational_samples = pd.concat(selected_computational, ignore_index=True)
        computational_samples['split'] = 'train'  # Default, will be reassigned
        selected_samples.append(computational_samples)
        
        print(f"   ✅ Added {len(computational_samples):,} computational error samples")
        
        # Show tier distribution
        tier_dist = computational_samples['tier'].value_counts().sort_index()
        print(f"      Tier distribution: {dict(tier_dist)}")
    else:
        print(f"   ❌ Could not select enough computational samples")
        computational_samples = pd.DataFrame()
    
    # Step 3: Add N//4 correct samples corresponding to random conceptual/computational samples
    print(f"\n📋 Step 3: Processing CORRESPONDING CORRECT samples...")
    
    target_corresponding = N // 4
    print(f"   Target: {target_corresponding:,} corresponding correct samples each for conceptual and computational")
    
    # Randomly select N//4 conceptual and computational samples
    np.random.seed(42)
    
    # Get corresponding correct samples for random conceptual samples
    if len(conceptual_samples) >= target_corresponding:
        random_conceptual_indices = np.random.choice(
            conceptual_samples['index'].values, 
            size=target_corresponding, 
            replace=False
        )
        
        # Find corresponding correct samples
        conceptual_correct_samples = df[df['index'].isin(random_conceptual_indices)].copy()
        conceptual_correct_samples['error_type'] = 'correct'
        conceptual_correct_samples['split'] = 'train'
        selected_samples.append(conceptual_correct_samples)
        
        print(f"   ✅ Added {len(conceptual_correct_samples):,} correct samples corresponding to conceptual errors")
    
    # Get corresponding correct samples for random computational samples  
    if len(computational_samples) >= target_corresponding:
        random_computational_indices = np.random.choice(
            computational_samples['index'].values,
            size=target_corresponding,
            replace=False
        )
        
        # Find corresponding correct samples
        computational_correct_samples = df[df['index'].isin(random_computational_indices)].copy()
        computational_correct_samples['error_type'] = 'correct'
        computational_correct_samples['split'] = 'train'
        selected_samples.append(computational_correct_samples)
        
        print(f"   ✅ Added {len(computational_correct_samples):,} correct samples corresponding to computational errors")
    
    # Step 4: Add N//2 entirely separate correct samples
    print(f"\n📋 Step 4: Processing SEPARATE CORRECT samples...")
    
    target_separate = N // 2
    print(f"   Target: {target_separate:,} entirely separate correct samples")
    print(f"   Excluding {len(used_indices):,} indices already used")
    
    # Get correct candidates excluding all used indices
    separate_correct_candidates = df[~df['index'].isin(used_indices)].copy()
    
    print(f"   Available distinct correct candidates: {len(separate_correct_candidates):,}")
    
    # Select separate correct samples by tier priority
    selected_separate_correct = []
    remaining_slots = target_separate
    
    for tier, tier_limit in tier_priorities:
        if remaining_slots <= 0:
            break
            
        tier_candidates = separate_correct_candidates[separate_correct_candidates['tier'] == tier]
        available_count = len(tier_candidates)
        actual_count = min(tier_limit, available_count, remaining_slots)
        
        if actual_count > 0:
            # Randomly sample from this tier
            tier_selected = tier_candidates.sample(n=actual_count, random_state=43).copy()
            selected_separate_correct.append(tier_selected)
            remaining_slots -= actual_count
            
            print(f"   {tier}: {actual_count:,} selected (available: {available_count:,}, limit: {tier_limit:,})")
    
    # Combine separate correct samples
    if selected_separate_correct:
        separate_correct_samples = pd.concat(selected_separate_correct, ignore_index=True)
        separate_correct_samples['error_type'] = 'correct'
        separate_correct_samples['split'] = 'train'  # Default, will be reassigned
        selected_samples.append(separate_correct_samples)
        
        print(f"   ✅ Added {len(separate_correct_samples):,} separate correct samples")
        
        # Show tier distribution
        tier_dist = separate_correct_samples['tier'].value_counts().sort_index()
        print(f"      Tier distribution: {dict(tier_dist)}")
    else:
        print(f"   ❌ Could not select enough separate correct samples")
    
    # Combine all samples
    if selected_samples:
        final_dataset = pd.concat(selected_samples, ignore_index=True)
        
        # Add proper train/test split (4:1 ratio within each error type)
        print(f"\n📋 Adding train/test splits...")
        
        for error_type in ['correct', 'conceptual_error', 'computational_error']:
            type_mask = final_dataset['error_type'] == error_type
            type_indices = final_dataset[type_mask].index.tolist()
            
            if len(type_indices) > 0:
                np.random.seed(44 + hash(error_type) % 100)  # Different seed per type
                n_samples = len(type_indices)
                n_train = int(0.8 * n_samples)  # 4:1 ratio
                
                shuffled_indices = np.random.permutation(type_indices)
                train_indices = shuffled_indices[:n_train]
                test_indices = shuffled_indices[n_train:]
                
                final_dataset.loc[train_indices, 'split'] = 'train'
                final_dataset.loc[test_indices, 'split'] = 'test'
        
        print(f"\n🎯 FINAL DATASET SUMMARY")
        print("=" * 50)
        print(f"Total samples: {len(final_dataset):,}")
        print(f"Expected total (3N): {3 * N:,}")
        
        # Verify distinctness within error types where expected
        total_unique = final_dataset['index'].nunique()
        print(f"Unique GSM8K indices: {total_unique:,}")
        
        # Summary by error type
        print(f"\nBy Error Type:")
        for error_type in ['correct', 'conceptual_error', 'computational_error']:
            type_data = final_dataset[final_dataset['error_type'] == error_type]
            if len(type_data) > 0:
                train_count = len(type_data[type_data['split'] == 'train'])
                test_count = len(type_data[type_data['split'] == 'test'])
                unique_indices = type_data['index'].nunique()
                print(f"  {error_type}: {len(type_data):,} (train: {train_count:,}, test: {test_count:,}, unique indices: {unique_indices:,})")
        
        # Summary by split
        print(f"\nBy Split:")
        split_counts = final_dataset['split'].value_counts()
        for split, count in split_counts.items():
            pct = (count / len(final_dataset)) * 100
            print(f"  {split}: {count:,} ({pct:.1f}%)")
        
        # Summary by tier
        print(f"\nBy Tier:")
        tier_counts = final_dataset['tier'].value_counts().sort_index()
        for tier, count in tier_counts.items():
            pct = (count / len(final_dataset)) * 100
            print(f"  {tier}: {count:,} ({pct:.1f}%)")
        
        # Summary by source
        print(f"\nBy Source:")
        source_counts = final_dataset['source'].value_counts()
        for source, count in source_counts.items():
            pct = (count / len(final_dataset)) * 100
            print(f"  {source}: {count:,} ({pct:.1f}%)")
        
        return final_dataset
    else:
        print("\n❌ No samples could be selected!")
        return pd.DataFrame()

# Create the error detection dataset
error_detection_dataset = create_error_detection_dataset(df)

# Save the dataset
if not error_detection_dataset.empty:
    output_path = AUG_5_DATASET_DIR / "error_detection_dataset.csv"
    error_detection_dataset.to_csv(output_path, index=False)
    print(f"\n💾 Dataset saved to: {output_path}")
    
    # # Save metadata
    # metadata = {
    #     "dataset_name": "error_detection_dataset",
    #     "creation_date": "2025-08-05",
    #     "total_samples": len(error_detection_dataset),
    #     "N_conceptual": len(error_detection_dataset[error_detection_dataset['error_type'] == 'conceptual_error']),
    #     "error_type_distribution": dict(error_detection_dataset['error_type'].value_counts()),
    #     "split_distribution": dict(error_detection_dataset['split'].value_counts()),
    #     "tier_distribution": dict(error_detection_dataset['tier'].value_counts()),
    #     "source_distribution": dict(error_detection_dataset['source'].value_counts()),
    #     "columns": list(error_detection_dataset.columns),
    #     "unique_indices": error_detection_dataset['index'].nunique(),
    #     "description": "Dataset for fine-tuning error detection task with structure: N conceptual + N computational + N correct (3N total)"
    # }
    
    # metadata_path = AUG_5_DATASET_DIR / "error_detection_metadata.json"
    # with open(metadata_path, 'w') as f:
    #     json.dump(metadata, f, indent=2)
    
    # print(f"💾 Metadata saved to: {metadata_path}")
    
else:
    print("❌ Dataset creation failed!")
```

    🔧 CREATING ERROR DETECTION DATASET
    ======================================================================
    
    📋 Step 1: Processing CONCEPTUAL ERROR samples...
       Found N = 2,067 conceptual error samples
       ✅ Added 2,067 conceptual error samples
    
    📋 Step 2: Processing COMPUTATIONAL ERROR samples...
       Target: 2,067 samples with distinct indices from conceptual samples
       Available distinct computational candidates: 16,204
       tier4: 500 selected (available: 787, limit: 500)
       tier2: 500 selected (available: 2,051, limit: 500)
       tier3: 500 selected (available: 5,505, limit: 500)
       tier1: 500 selected (available: 7,851, limit: 500)
       ✅ Added 2,000 computational error samples
          Tier distribution: {'tier1': 500, 'tier2': 500, 'tier3': 500, 'tier4': 500}
    
    📋 Step 3: Processing CORRESPONDING CORRECT samples...
       Target: 516 corresponding correct samples each for conceptual and computational
       ✅ Added 2,238 correct samples corresponding to conceptual errors
       ✅ Added 2,010 correct samples corresponding to computational errors
    
    📋 Step 4: Processing SEPARATE CORRECT samples...
       Target: 1,033 entirely separate correct samples
       Excluding 3,271 indices already used
       Available distinct correct candidates: 10,287
       tier4: 58 selected (available: 58, limit: 500)
       tier2: 500 selected (available: 627, limit: 500)
       tier3: 475 selected (available: 3,835, limit: 500)
       ✅ Added 1,033 separate correct samples
          Tier distribution: {'tier2': 500, 'tier3': 475, 'tier4': 58}
    
    📋 Adding train/test splits...
    
    🎯 FINAL DATASET SUMMARY
    ==================================================
    Total samples: 9,348
    Expected total (3N): 6,201
    Unique GSM8K indices: 3,941
    
    By Error Type:
      correct: 5,281 (train: 4,224, test: 1,057, unique indices: 1,637)
      conceptual_error: 2,067 (train: 1,653, test: 414, unique indices: 1,847)
      computational_error: 2,000 (train: 1,600, test: 400, unique indices: 1,424)
    
    By Split:
      train: 7,477 (80.0%)
      test: 1,871 (20.0%)
    
    By Tier:
      tier1: 2,658 (28.4%)
      tier2: 2,274 (24.3%)
      tier3: 2,914 (31.2%)
      tier4: 1,461 (15.6%)
      tier5: 41 (0.4%)
    
    By Source:
      programmatic: 7,955 (85.1%)
      manual: 1,393 (14.9%)
    
    💾 Dataset saved to: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/aug-5-dataset/error_detection_dataset.csv



```python
import pandas as pd
import json
import numpy as np
from collections import defaultdict

def create_error_detection_dataset_simplified(df):
    """
    Create error detection dataset with simplified correct sample logic.
    """
    print("🔧 CREATING ERROR DETECTION DATASET (SIMPLIFIED)")
    print("=" * 70)
    
    # Tier priorities: tier4 (500), tier2 (500), tier3 (500), tier1 (500)
    tier_priorities = [
        ('tier4', 500),
        ('tier2', 500), 
        ('tier3', 500),
        ('tier1', 500)
    ]
    
    used_indices = set()  # Track used GSM8K indices for conceptual/computational
    selected_samples = []
    
    # Step 1: Get all conceptual error samples
    print(f"\n📋 Step 1: Processing CONCEPTUAL ERROR samples...")
    conceptual_samples = df[df['error_type'] == 'conceptual_error'].copy()
    N = len(conceptual_samples)
    
    print(f"   Found N = {N:,} conceptual error samples")
    
    # Track conceptual indices
    conceptual_indices = set(conceptual_samples['index'].tolist())
    used_indices.update(conceptual_indices)
    
    # Add split column (will assign later)
    conceptual_samples['split'] = 'train'  # Default, will be reassigned
    selected_samples.append(conceptual_samples)
    
    print(f"   ✅ Added {len(conceptual_samples):,} conceptual error samples")
    
    # Step 2: Add N computational error samples (distinct problem indices)
    print(f"\n📋 Step 2: Processing COMPUTATIONAL ERROR samples...")
    print(f"   Target: {N:,} samples with distinct indices from conceptual samples")
    
    # Get computational candidates excluding conceptual indices
    computational_candidates = df[
        (df['error_type'] == 'computational_error') & 
        (~df['index'].isin(used_indices))
    ].copy()
    
    print(f"   Available distinct computational candidates: {len(computational_candidates):,}")
    
    # Select computational samples by tier priority
    selected_computational = []
    remaining_slots = N
    
    for tier, tier_limit in tier_priorities:
        if remaining_slots <= 0:
            break
            
        tier_candidates = computational_candidates[computational_candidates['tier'] == tier]
        available_count = len(tier_candidates)
        actual_count = min(tier_limit, available_count, remaining_slots)
        
        if actual_count > 0:
            # Randomly sample from this tier
            tier_selected = tier_candidates.sample(n=actual_count, random_state=42).copy()
            selected_computational.append(tier_selected)
            remaining_slots -= actual_count
            
            # Track used indices
            used_indices.update(tier_selected['index'].tolist())
            
            print(f"   {tier}: {actual_count:,} selected (available: {available_count:,}, limit: {tier_limit:,})")
    
    # Combine computational samples
    if selected_computational:
        computational_samples = pd.concat(selected_computational, ignore_index=True)
        computational_samples['split'] = 'train'  # Default, will be reassigned
        selected_samples.append(computational_samples)
        
        print(f"   ✅ Added {len(computational_samples):,} computational error samples")
        
        # Show tier distribution
        tier_dist = computational_samples['tier'].value_counts().sort_index()
        print(f"      Tier distribution: {dict(tier_dist)}")
    else:
        print(f"   ❌ Could not select enough computational samples")
        computational_samples = pd.DataFrame()
    
    # Step 3: Add 2000 randomly chosen correct samples (following tier priority)
    print(f"\n📋 Step 3: Processing CORRECT samples...")
    print(f"   Target: 2000 randomly chosen correct samples (following tier priority)")
    
    # Get all available candidates (don't worry about used indices)
    correct_candidates = df.copy()
    
    print(f"   Available correct candidates: {len(correct_candidates):,}")
    
    # Select correct samples by tier priority
    selected_correct = []
    remaining_slots = 2000
    
    for tier, tier_limit in tier_priorities:
        if remaining_slots <= 0:
            break
            
        tier_candidates = correct_candidates[correct_candidates['tier'] == tier]
        available_count = len(tier_candidates)
        actual_count = min(tier_limit, available_count, remaining_slots)
        
        if actual_count > 0:
            # Randomly sample from this tier
            tier_selected = tier_candidates.sample(n=actual_count, random_state=45).copy()
            selected_correct.append(tier_selected)
            remaining_slots -= actual_count
            
            print(f"   {tier}: {actual_count:,} selected (available: {available_count:,}, limit: {tier_limit:,})")
    
    # Combine correct samples
    if selected_correct:
        correct_samples = pd.concat(selected_correct, ignore_index=True)
        correct_samples['error_type'] = 'correct'
        correct_samples['split'] = 'train'  # Default, will be reassigned
        selected_samples.append(correct_samples)
        
        print(f"   ✅ Added {len(correct_samples):,} correct samples")
        
        # Show tier distribution
        tier_dist = correct_samples['tier'].value_counts().sort_index()
        print(f"      Tier distribution: {dict(tier_dist)}")
        
        # Check for distinctness within correct samples
        unique_correct_indices = correct_samples['index'].nunique()
        total_correct_samples = len(correct_samples)
        print(f"      Unique indices in correct samples: {unique_correct_indices:,} / {total_correct_samples:,}")
        if unique_correct_indices == total_correct_samples:
            print("      ✅ All correct samples have distinct indices")
        else:
            print(f"      ⚠️  {total_correct_samples - unique_correct_indices} duplicate indices in correct samples")
    else:
        print(f"   ❌ Could not select correct samples")
    
    # Combine all samples
    if selected_samples:
        final_dataset = pd.concat(selected_samples, ignore_index=True)
        
        # Add proper train/test split (4:1 ratio within each error type)
        print(f"\n📋 Adding train/test splits...")
        
        for error_type in ['correct', 'conceptual_error', 'computational_error']:
            type_mask = final_dataset['error_type'] == error_type
            type_indices = final_dataset[type_mask].index.tolist()
            
            if len(type_indices) > 0:
                np.random.seed(44 + hash(error_type) % 100)  # Different seed per type
                n_samples = len(type_indices)
                n_train = int(0.8 * n_samples)  # 4:1 ratio
                
                shuffled_indices = np.random.permutation(type_indices)
                train_indices = shuffled_indices[:n_train]
                test_indices = shuffled_indices[n_train:]
                
                final_dataset.loc[train_indices, 'split'] = 'train'
                final_dataset.loc[test_indices, 'split'] = 'test'
        
        print(f"\n🎯 FINAL DATASET SUMMARY")
        print("=" * 50)
        print(f"Total samples: {len(final_dataset):,}")
        
        # Summary by error type
        print(f"\nBy Error Type:")
        for error_type in ['correct', 'conceptual_error', 'computational_error']:
            type_data = final_dataset[final_dataset['error_type'] == error_type]
            if len(type_data) > 0:
                train_count = len(type_data[type_data['split'] == 'train'])
                test_count = len(type_data[type_data['split'] == 'test'])
                unique_indices = type_data['index'].nunique()
                print(f"  {error_type}: {len(type_data):,} (train: {train_count:,}, test: {test_count:,}, unique indices: {unique_indices:,})")
        
        # Summary by split
        print(f"\nBy Split:")
        split_counts = final_dataset['split'].value_counts()
        for split, count in split_counts.items():
            pct = (count / len(final_dataset)) * 100
            print(f"  {split}: {count:,} ({pct:.1f}%)")
        
        # Summary by tier
        print(f"\nBy Tier:")
        tier_counts = final_dataset['tier'].value_counts().sort_index()
        for tier, count in tier_counts.items():
            pct = (count / len(final_dataset)) * 100
            print(f"  {tier}: {count:,} ({pct:.1f}%)")
        
        # Summary by source
        print(f"\nBy Source:")
        source_counts = final_dataset['source'].value_counts()
        for source, count in source_counts.items():
            pct = (count / len(final_dataset)) * 100
            print(f"  {source}: {count:,} ({pct:.1f}%)")
        
        # Check overlap between error types
        conceptual_idx = set(final_dataset[final_dataset['error_type'] == 'conceptual_error']['index'])
        computational_idx = set(final_dataset[final_dataset['error_type'] == 'computational_error']['index'])
        correct_idx = set(final_dataset[final_dataset['error_type'] == 'correct']['index'])
        
        print(f"\nIndex Overlap Analysis:")
        conceptual_computational_overlap = len(conceptual_idx & computational_idx)
        conceptual_correct_overlap = len(conceptual_idx & correct_idx)
        computational_correct_overlap = len(computational_idx & correct_idx)
        
        print(f"  Conceptual ∩ Computational: {conceptual_computational_overlap:,} indices")
        print(f"  Conceptual ∩ Correct: {conceptual_correct_overlap:,} indices")
        print(f"  Computational ∩ Correct: {computational_correct_overlap:,} indices")
        
        return final_dataset
    else:
        print("\n❌ No samples could be selected!")
        return pd.DataFrame()

# Create the simplified error detection dataset
error_detection_dataset = create_error_detection_dataset_simplified(df)

# Save the dataset
if not error_detection_dataset.empty:
    output_path = AUG_5_DATASET_DIR / "error_detection_dataset.csv"
    error_detection_dataset.to_csv(output_path, index=False)
    print(f"\n💾 Dataset saved to: {output_path}")
    
    # # Save metadata
    # metadata = {
    #     "dataset_name": "error_detection_dataset_simplified",
    #     "creation_date": "2025-08-05",
    #     "total_samples": len(error_detection_dataset),
    #     "N_conceptual": len(error_detection_dataset[error_detection_dataset['error_type'] == 'conceptual_error']),
    #     "N_computational": len(error_detection_dataset[error_detection_dataset['error_type'] == 'computational_error']),
    #     "N_correct": len(error_detection_dataset[error_detection_dataset['error_type'] == 'correct']),
    #     "error_type_distribution": dict(error_detection_dataset['error_type'].value_counts()),
    #     "split_distribution": dict(error_detection_dataset['split'].value_counts()),
    #     "tier_distribution": dict(error_detection_dataset['tier'].value_counts()),
    #     "source_distribution": dict(error_detection_dataset['source'].value_counts()),
    #     "columns": list(error_detection_dataset.columns),
    #     "total_unique_indices": error_detection_dataset['index'].nunique(),
    #     "description": "Simplified dataset for error detection: all conceptual + equal computational (distinct) + 2000 correct (following tier priority)"
    # }
    
    # metadata_path = AUG_5_DATASET_DIR / "error_detection_metadata.json"
    # with open(metadata_path, 'w') as f:
    #     json.dump(metadata, f, indent=2)
    
    # print(f"💾 Metadata saved to: {metadata_path}")
    
else:
    print("❌ Dataset creation failed!")
```

    🔧 CREATING ERROR DETECTION DATASET (SIMPLIFIED)
    ======================================================================
    
    📋 Step 1: Processing CONCEPTUAL ERROR samples...
       Found N = 2,067 conceptual error samples
       ✅ Added 2,067 conceptual error samples
    
    📋 Step 2: Processing COMPUTATIONAL ERROR samples...
       Target: 2,067 samples with distinct indices from conceptual samples
       Available distinct computational candidates: 16,204
       tier4: 500 selected (available: 787, limit: 500)
       tier2: 500 selected (available: 2,051, limit: 500)
       tier3: 500 selected (available: 5,505, limit: 500)
       tier1: 500 selected (available: 7,851, limit: 500)
       ✅ Added 2,000 computational error samples
          Tier distribution: {'tier1': 500, 'tier2': 500, 'tier3': 500, 'tier4': 500}
    
    📋 Step 3: Processing CORRECT samples...
       Target: 2000 randomly chosen correct samples (following tier priority)
       Available correct candidates: 24,376
       tier4: 500 selected (available: 1,637, limit: 500)
       tier2: 500 selected (available: 3,436, limit: 500)
       tier3: 500 selected (available: 8,198, limit: 500)
       tier1: 500 selected (available: 11,050, limit: 500)
       ✅ Added 2,000 correct samples
          Tier distribution: {'tier1': 500, 'tier2': 500, 'tier3': 500, 'tier4': 500}
          Unique indices in correct samples: 1,607 / 2,000
          ⚠️  393 duplicate indices in correct samples
    
    📋 Adding train/test splits...
    
    🎯 FINAL DATASET SUMMARY
    ==================================================
    Total samples: 6,067
    
    By Error Type:
      correct: 2,000 (train: 1,600, test: 400, unique indices: 1,607)
      conceptual_error: 2,067 (train: 1,653, test: 414, unique indices: 1,847)
      computational_error: 2,000 (train: 1,600, test: 400, unique indices: 1,424)
    
    By Split:
      train: 4,853 (80.0%)
      test: 1,214 (20.0%)
    
    By Tier:
      tier1: 1,690 (27.9%)
      tier2: 1,321 (21.8%)
      tier3: 1,794 (29.6%)
      tier4: 1,234 (20.3%)
      tier5: 28 (0.5%)
    
    By Source:
      programmatic: 4,948 (81.6%)
      manual: 1,119 (18.4%)
    
    Index Overlap Analysis:
      Conceptual ∩ Computational: 0 indices
      Conceptual ∩ Correct: 577 indices
      Computational ∩ Correct: 467 indices
    
    💾 Dataset saved to: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/aug-5-dataset/error_detection_dataset.csv



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[110], line 249
        247     metadata_path = AUG_5_DATASET_DIR / "error_detection_metadata.json"
        248     with open(metadata_path, 'w') as f:
    --> 249         json.dump(metadata, f, indent=2)
        251     print(f"💾 Metadata saved to: {metadata_path}")
        253 else:


    File /opt/miniconda3/envs/erdos-dl/lib/python3.12/json/__init__.py:179, in dump(obj, fp, skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, separators, default, sort_keys, **kw)
        173     iterable = cls(skipkeys=skipkeys, ensure_ascii=ensure_ascii,
        174         check_circular=check_circular, allow_nan=allow_nan, indent=indent,
        175         separators=separators,
        176         default=default, sort_keys=sort_keys, **kw).iterencode(obj)
        177 # could accelerate with writelines in some versions of Python, at
        178 # a debuggability cost
    --> 179 for chunk in iterable:
        180     fp.write(chunk)


    File /opt/miniconda3/envs/erdos-dl/lib/python3.12/json/encoder.py:432, in _make_iterencode.<locals>._iterencode(o, _current_indent_level)
        430     yield from _iterencode_list(o, _current_indent_level)
        431 elif isinstance(o, dict):
    --> 432     yield from _iterencode_dict(o, _current_indent_level)
        433 else:
        434     if markers is not None:


    File /opt/miniconda3/envs/erdos-dl/lib/python3.12/json/encoder.py:406, in _make_iterencode.<locals>._iterencode_dict(dct, _current_indent_level)
        404         else:
        405             chunks = _iterencode(value, _current_indent_level)
    --> 406         yield from chunks
        407 if newline_indent is not None:
        408     _current_indent_level -= 1


    File /opt/miniconda3/envs/erdos-dl/lib/python3.12/json/encoder.py:406, in _make_iterencode.<locals>._iterencode_dict(dct, _current_indent_level)
        404         else:
        405             chunks = _iterencode(value, _current_indent_level)
    --> 406         yield from chunks
        407 if newline_indent is not None:
        408     _current_indent_level -= 1


    File /opt/miniconda3/envs/erdos-dl/lib/python3.12/json/encoder.py:439, in _make_iterencode.<locals>._iterencode(o, _current_indent_level)
        437         raise ValueError("Circular reference detected")
        438     markers[markerid] = o
    --> 439 o = _default(o)
        440 yield from _iterencode(o, _current_indent_level)
        441 if markers is not None:


    File /opt/miniconda3/envs/erdos-dl/lib/python3.12/json/encoder.py:180, in JSONEncoder.default(self, o)
        161 def default(self, o):
        162     """Implement this method in a subclass such that it returns
        163     a serializable object for ``o``, or calls the base implementation
        164     (to raise a ``TypeError``).
       (...)    178 
        179     """
    --> 180     raise TypeError(f'Object of type {o.__class__.__name__} '
        181                     f'is not JSON serializable')


    TypeError: Object of type int64 is not JSON serializable



```python
def check_annotation_coverage(dataset_df, verbose=True):
    """
    Check how many samples in the dataset are missing complete calculator annotation coverage.
    
    Args:
        dataset_df: DataFrame containing the dataset to check
        verbose: Whether to print detailed breakdown
    
    Returns:
        dict: Summary of annotation coverage statistics
    """
    
    def has_complete_annotation_coverage(row, eqn_mapping_col):
        """Check if all solution lines except FA have calculator annotations."""
        try:
            eqn_mapping = json.loads(row[eqn_mapping_col])
            
            # Count total lines (excluding FA)
            answer_length = row['correct_answer_length'] if 'correct' in eqn_mapping_col else row['wrong_answer_length']
            expected_lines = answer_length - 1 if 'FA' in eqn_mapping else answer_length
            
            # Count non-empty equations (excluding FA)
            non_empty_equations = sum(1 for key, value in eqn_mapping.items() 
                                    if key != 'FA' and value and str(value).strip())
            
            return non_empty_equations == expected_lines
            
        except (json.JSONDecodeError, KeyError, TypeError):
            return False
    
    # Initialize results
    results = {
        'total_samples': len(dataset_df),
        'by_error_type': {},
        'missing_coverage': {
            'total': 0,
            'by_error_type': {}
        }
    }
    
    # Group by error_type for analysis
    for error_type in dataset_df['error_type'].unique():
        type_data = dataset_df[dataset_df['error_type'] == error_type]
        
        # Determine which equation mapping column to use
        if error_type == 'correct':
            eqn_col = 'correct_eqn_mapping'
        else:
            eqn_col = 'wrong_eqn_mapping'
        
        # Check coverage for this error type
        has_coverage = type_data.apply(
            lambda row: has_complete_annotation_coverage(row, eqn_col), axis=1
        )
        
        # Count missing coverage
        missing_count = (~has_coverage).sum()
        total_count = len(type_data)
        
        results['by_error_type'][error_type] = {
            'total': total_count,
            'with_coverage': has_coverage.sum(),
            'missing_coverage': missing_count,
            'coverage_rate': has_coverage.sum() / total_count if total_count > 0 else 0
        }
        
        results['missing_coverage']['by_error_type'][error_type] = missing_count
        results['missing_coverage']['total'] += missing_count
    
    # Print results if verbose
    if verbose:
        print("🔍 Calculator Annotation Coverage Analysis")
        print("=" * 50)
        print(f"Total samples in dataset: {results['total_samples']:,}")
        print(f"Total samples missing coverage: {results['missing_coverage']['total']:,}")
        print(f"Overall coverage rate: {((results['total_samples'] - results['missing_coverage']['total']) / results['total_samples'] * 100):.1f}%")
        print()
        
        print("By Error Type:")
        for error_type, stats in results['by_error_type'].items():
            print(f"  {error_type}:")
            print(f"    Total samples: {stats['total']:,}")
            print(f"    With complete coverage: {stats['with_coverage']:,}")
            print(f"    Missing coverage: {stats['missing_coverage']:,}")
            print(f"    Coverage rate: {stats['coverage_rate']:.1%}")
            print()
    
    return results

coverage_results = check_annotation_coverage(error_detection_dataset)
```

    🔍 Calculator Annotation Coverage Analysis
    ==================================================
    Total samples in dataset: 6,067
    Total samples missing coverage: 1,297
    Overall coverage rate: 78.6%
    
    By Error Type:
      conceptual_error:
        Total samples: 2,067
        With complete coverage: 1,591
        Missing coverage: 476
        Coverage rate: 77.0%
    
      computational_error:
        Total samples: 2,000
        With complete coverage: 1,571
        Missing coverage: 429
        Coverage rate: 78.5%
    
      correct:
        Total samples: 2,000
        With complete coverage: 1,608
        Missing coverage: 392
        Coverage rate: 80.4%
    



```python
def filter_error_detection_dataset_for_coverage(dataset_df):
    """
    Filter error detection dataset to keep only rows with complete calculator annotation coverage.
    
    Args:
        dataset_df: The error detection dataset DataFrame
        
    Returns:
        DataFrame: Filtered dataset with only complete coverage samples
    """
    
    def has_complete_annotation_coverage(row, eqn_mapping_col):
        """Check if all solution lines except FA have calculator annotations."""
        try:
            eqn_mapping = json.loads(row[eqn_mapping_col])
            
            # Count total lines (excluding FA)
            answer_length = row['correct_answer_length'] if 'correct' in eqn_mapping_col else row['wrong_answer_length']
            expected_lines = answer_length - 1 if 'FA' in eqn_mapping else answer_length
            
            # Count non-empty equations (excluding FA)
            non_empty_equations = sum(1 for key, value in eqn_mapping.items() 
                                    if key != 'FA' and value and str(value).strip())
            
            return non_empty_equations == expected_lines
            
        except (json.JSONDecodeError, KeyError, TypeError):
            return False
    
    print("🔍 Filtering error detection dataset for complete annotation coverage...")
    print(f"Original dataset size: {len(dataset_df):,} samples")
    
    # Create coverage mask for each error type
    coverage_masks = []
    
    for error_type in dataset_df['error_type'].unique():
        type_mask = dataset_df['error_type'] == error_type
        type_data = dataset_df[type_mask]
        
        # Determine which equation mapping column to use
        if error_type == 'correct':
            eqn_col = 'correct_eqn_mapping'
        else:
            eqn_col = 'wrong_eqn_mapping'
        
        # Check coverage for this error type
        type_coverage = type_data.apply(
            lambda row: has_complete_annotation_coverage(row, eqn_col), axis=1
        )
        
        # Count and report
        with_coverage = type_coverage.sum()
        total_type = len(type_data)
        print(f"  {error_type}: {with_coverage:,} / {total_type:,} samples have complete coverage ({with_coverage/total_type:.1%})")
        
        # Add to overall mask
        coverage_masks.append(type_coverage)
    
    # Combine all coverage masks
    full_coverage_mask = pd.concat(coverage_masks, ignore_index=False)
    
    # Filter the dataset
    filtered_dataset = dataset_df[full_coverage_mask].copy()
    
    print(f"\nFiltered dataset size: {len(filtered_dataset):,} samples")
    print(f"Removed {len(dataset_df) - len(filtered_dataset):,} samples without complete coverage")
    
    # Show final composition
    print("\nFinal dataset composition:")
    final_counts = filtered_dataset['error_type'].value_counts()
    for error_type, count in final_counts.items():
        print(f"  {error_type}: {count:,} samples")
    
    return filtered_dataset

# Apply the filter to your error detection dataset
# Replace 'error_detection_dataset' with your actual variable name
error_detection_dataset_filtered = filter_error_detection_dataset_for_coverage(error_detection_dataset)

# Optionally, update the original variable
# error_detection_dataset = error_detection_dataset_filtered
```

    🔍 Filtering error detection dataset for complete annotation coverage...
    Original dataset size: 6,067 samples
      conceptual_error: 1,591 / 2,067 samples have complete coverage (77.0%)
      computational_error: 1,571 / 2,000 samples have complete coverage (78.5%)
      correct: 1,608 / 2,000 samples have complete coverage (80.4%)
    
    Filtered dataset size: 4,770 samples
    Removed 1,297 samples without complete coverage
    
    Final dataset composition:
      correct: 1,608 samples
      conceptual_error: 1,591 samples
      computational_error: 1,571 samples



```python

```


```python
error_detection_dataset.columns
```




    Index(['index', 'tier', 'question', 'correct_answer', 'wrong_answer',
           'error_type', 'explanation', 'erroneous_line_number', 'erroneous_line',
           'erroneous_line_eqn', 'correct_answer_mapping', 'wrong_answer_mapping',
           'correct_eqn_mapping', 'wrong_eqn_mapping', 'correct_answer_length',
           'wrong_answer_length', 'source', 'error_subtype', 'split'],
          dtype='object')




```python
def generate_thinking_trace_for_error_detection(row):
    """
    Generate thinking trace and JSON output for error detection task.
    Stops the trace immediately after finding the error.
    
    Returns:
        tuple: (thinking_trace_text, json_output_dict)
    """
    
    # Determine which mappings to use based on error_type
    if row['error_type'] == 'correct':
        answer_mapping = json.loads(row['correct_answer_mapping'])
        verdict = "correct"
        erroneous_line = None
    else:
        answer_mapping = json.loads(row['wrong_answer_mapping'])
        verdict = "flawed"
        erroneous_line = row['erroneous_line']  # Already available in dataset
    
    # Get explanation from the dataset
    explanation = row['explanation']
    
    # Count total lines (including FA if present)
    line_keys = [k for k in answer_mapping.keys() if k.startswith('L')]
    num_lines = len(line_keys)
    if 'FA' in answer_mapping:
        num_lines += 1
    
    # Build thinking trace
    thinking_lines = [
        f"There are {num_lines} lines in the solution, including the final answer line. Let's examine the lines one-by-one."
    ]
    
    # Sort line keys to ensure proper order (L1, L2, L3, ...)
    sorted_line_keys = sorted(line_keys, key=lambda x: int(x[1:]))
    
    # Examine each line - STOP when error is found
    error_found = False
    
    # Go through each solution line
    for line_key in sorted_line_keys:
        line_num = line_key[1:]  # Extract number from L1, L2, etc.
        line_text = answer_mapping[line_key]
        
        # Check if this line contains the error
        if (row['error_type'] != 'correct' and 
            not error_found and 
            erroneous_line and 
            line_text.strip() == erroneous_line.strip()):
            thinking_lines.append(f"Line {line_num}: Aha! I see the error. I will now prepare the output json.")
            error_found = True
            break  # STOP HERE - don't continue checking more lines
        else:
            thinking_lines.append(f"Line {line_num}: no errors")
    
    # Only check final answer if error hasn't been found yet
    if not error_found and 'FA' in answer_mapping:
        fa_text = answer_mapping['FA']
        if (row['error_type'] != 'correct' and 
            erroneous_line and 
            fa_text.strip() == erroneous_line.strip()):
            thinking_lines.append(f"Final Answer: Aha! I see the error. I will now prepare the output json.")
            error_found = True
        else:
            thinking_lines.append(f"Final Answer: no errors")
    
    # If no error was found (for correct samples or if error line wasn't matched)
    if not error_found and row['error_type'] == 'correct':
        thinking_lines.append("I found no errors! I will now prepare the output json.")
    elif not error_found and row['error_type'] != 'correct':
        # Fallback for cases where erroneous_line doesn't exactly match any line
        thinking_lines.append("Aha! I see the error. I will now prepare the output json.")
    
    # Construct thinking trace with tags
    thinking_trace = "<think>\n" + "\n".join(thinking_lines) + "\n</think>"
    
    # Construct JSON output dictionary
    json_output = {
        "verdict": verdict,
        "erroneous_line": erroneous_line,
        "explanation": explanation
    }
    
    return thinking_trace, json_output
```


```python
# Apply to your error detection dataset
print("Generating thinking traces and JSON outputs...")

# Apply the function and split the results into two columns
results = error_detection_dataset.apply(generate_thinking_trace_for_error_detection, axis=1)

# Split the tuple results into separate columns
error_detection_dataset['thinking_trace'] = results.apply(lambda x: x[0])
error_detection_dataset['json_output'] = results.apply(lambda x: x[1])

print(f"Added thinking_trace and json_output columns to {len(error_detection_dataset)} samples")
```

    Generating thinking traces and JSON outputs...
    Added thinking_trace and json_output columns to 6067 samples



```python
# Clean up correct samples - set error-related fields to null
print("🧹 Cleaning correct samples...")

# Identify error-related columns that should be null for correct samples
error_columns = [
    'explanation', 
    'erroneous_line', 
    'error_line_numeric',
    'mutation_type',  # if this exists
    'wrong_answer_mapping',
    'wrong_eqn_mapping'
]

# Clean correct samples
correct_mask = error_detection_dataset['error_type'] == 'correct'
print(f"Found {correct_mask.sum()} correct samples to clean")

for col in error_columns:
    if col in error_detection_dataset.columns:
        before_count = error_detection_dataset.loc[correct_mask, col].notna().sum()
        error_detection_dataset.loc[correct_mask, col] = None
        print(f"  Cleaned {col}: {before_count} non-null values set to null")

print("✅ Correct samples cleaned")

# Verify the cleanup
sample_correct = error_detection_dataset[error_detection_dataset['error_type'] == 'correct'].iloc[0]
print("\n🔍 Sample correct row after cleanup:")
print(f"explanation: {sample_correct.get('explanation')}")
print(f"erroneous_line: {sample_correct.get('erroneous_line')}")
print(f"error_line_numeric: {sample_correct.get('error_line_numeric')}")
```

    🧹 Cleaning correct samples...
    Found 2000 correct samples to clean
      Cleaned explanation: 2000 non-null values set to null
      Cleaned erroneous_line: 2000 non-null values set to null
      Cleaned wrong_answer_mapping: 2000 non-null values set to null
      Cleaned wrong_eqn_mapping: 2000 non-null values set to null
    ✅ Correct samples cleaned
    
    🔍 Sample correct row after cleanup:
    explanation: None
    erroneous_line: None
    error_line_numeric: None



```python
# Regenerate thinking traces with clean data
def generate_thinking_trace_for_error_detection_fixed(row):
    """Fixed version that properly handles null values for correct samples"""
    
    # Determine which mappings to use based on error_type
    if row['error_type'] == 'correct':
        answer_mapping = json.loads(row['correct_answer_mapping'])
        verdict = "correct"
        erroneous_line = None
        explanation = "All calculations and reasoning steps are correct."
    else:
        answer_mapping = json.loads(row['wrong_answer_mapping'])
        verdict = "flawed"
        erroneous_line = row['erroneous_line'] if pd.notna(row['erroneous_line']) else None
        explanation = row['explanation'] if pd.notna(row['explanation']) else "Error detected in reasoning."
    
    # Rest of the function remains the same...
    line_keys = [k for k in answer_mapping.keys() if k.startswith('L')]
    num_lines = len(line_keys)
    if 'FA' in answer_mapping:
        num_lines += 1
    
    thinking_lines = [
        f"There are {num_lines} lines in the solution, including the final answer line. Let's examine the lines one-by-one."
    ]
    
    sorted_line_keys = sorted(line_keys, key=lambda x: int(x[1:]))
    error_found = False
    
    for line_key in sorted_line_keys:
        line_num = line_key[1:]
        line_text = answer_mapping[line_key]
        
        if (row['error_type'] != 'correct' and 
            not error_found and 
            erroneous_line and 
            line_text.strip() == erroneous_line.strip()):
            thinking_lines.append(f"Line {line_num}: Aha! I see the error. I will now prepare the output json.")
            error_found = True
            break
        else:
            thinking_lines.append(f"Line {line_num}: no errors")
    
    if not error_found and 'FA' in answer_mapping:
        fa_text = answer_mapping['FA']
        if (row['error_type'] != 'correct' and 
            erroneous_line and 
            fa_text.strip() == erroneous_line.strip()):
            thinking_lines.append(f"Final Answer: Aha! I see the error. I will now prepare the output json.")
            error_found = True
        else:
            thinking_lines.append(f"Final Answer: no errors")
    
    if not error_found and row['error_type'] == 'correct':
        thinking_lines.append("I found no errors! I will now prepare the output json.")
    elif not error_found and row['error_type'] != 'correct':
        thinking_lines.append("Aha! I see the error. I will now prepare the output json.")
    
    thinking_trace = "<think>\n" + "\n".join(thinking_lines) + "\n</think>"
    
    json_output = {
        "verdict": verdict,
        "erroneous_line": erroneous_line,
        "explanation": explanation
    }
    
    return thinking_trace, json_output

# Regenerate with fixed function
print("🔄 Regenerating thinking traces with clean data...")
results = error_detection_dataset.apply(generate_thinking_trace_for_error_detection_fixed, axis=1)
error_detection_dataset['thinking_trace'] = results.apply(lambda x: x[0])
error_detection_dataset['json_output'] = results.apply(lambda x: x[1])
print("✅ Thinking traces regenerated")
```

    🔄 Regenerating thinking traces with clean data...
    ✅ Thinking traces regenerated



```python

```

    🎲 Random Sample from Each Error Type
    ============================================================
    
    📋 CORRECT SAMPLE
    ----------------------------------------
    index:
    6467
    
    tier:
    tier3
    
    question:
    The temperature in New York in June 2020 was 80 degrees. If the temperature in Miami on this day was 10 degrees hotter than the temperature in New York, and 25 degrees cooler than the temperature in San Diego, what was the average temperature for the three cities?
    
    correct_answer:
    If it was 10 degrees hotter on this day in Miami than in New York, then the temperature in Miami was 80+10 = 90 degrees.
    If it was 25 degrees cooler in Miami than in San Diego, then the temperature in San Diego was 90+25 = 115 degrees.
    The total temperature for all the cities is 115+90+80 = 285 degrees
    The average temperature of the three cities is 285/3 = 95 degrees
    FINAL ANSWER: 95
    
    wrong_answer:
    If it was 10 degrees hotter on this day in Miami than in New York, then the temperature in Miami was 80+10 = 90 degrees.
    If it was 25 degrees cooler in Miami than in San Diego, then the temperature in San Diego was 90+25 = 151 degrees.
    The total temperature for all the cities is 151+90+80 = 321 degrees
    The average temperature of the three cities is 321/3 = 107 degrees
    FINAL ANSWER: 107
    
    error_type:
    correct
    
    explanation:
    None
    
    erroneous_line_number:
    L2
    
    erroneous_line:
    None
    
    erroneous_line_eqn:
    90+25=151
    
    correct_answer_mapping:
    {
      "L1": "If it was 10 degrees hotter on this day in Miami than in New York, then the temperature in Miami was 80+10 = 90 degrees.",
      "L2": "If it was 25 degrees cooler in Miami than in San Diego, then the temperature in San Diego was 90+25 = 115 degrees.",
      "L3": "The total temperature for all the cities is 115+90+80 = 285 degrees",
      "L4": "The average temperature of the three cities is 285/3 = 95 degrees",
      "FA": "95"
    }
    
    wrong_answer_mapping:
    None
    
    correct_eqn_mapping:
    {
      "L1": "",
      "L2": "90+25=115",
      "L3": "115+90+80=285",
      "L4": "285/3=95",
      "FA": ""
    }
    
    wrong_eqn_mapping:
    None
    
    correct_answer_length:
    5
    
    wrong_answer_length:
    5
    
    source:
    programmatic
    
    error_subtype:
    generate_digit_transposition_error
    
    split:
    train
    
    thinking_trace:
    <think>
    There are 5 lines in the solution, including the final answer line. Let's examine the lines one-by-one.
    Line 1: no errors
    Line 2: no errors
    Line 3: no errors
    Line 4: no errors
    Final Answer: no errors
    I found no errors! I will now prepare the output json.
    </think>
    
    json_output:
    {'verdict': 'correct', 'erroneous_line': None, 'explanation': 'All calculations and reasoning steps are correct.'}
    
    
    📋 CONCEPTUAL_ERROR SAMPLE
    ----------------------------------------
    index:
    6253
    
    tier:
    tier3
    
    question:
    Dan can get to the center of a lollipop in 58 licks.  Micheal does it in 63 licks.  Sam & David each take 70 licks to get to the center of a lollipop while Lance only needs 39 licks.  What is the average amount of licks it takes to get to the center of a lollipop?
    
    correct_answer:
    Dan takes 58 licks, Michael takes 63, Sam takes 70, David takes 70 and Lance takes 39 for a total of 58+63+70+70+39 = 300 licks
    There are 5 people and the total amount of licks is 300 so the average is 300/5 = 60 licks to get to the center of a lollipop
    FINAL ANSWER: 60
    
    wrong_answer:
    Dan takes 58 licks, Michael takes 63, David takes 70 and Lance takes 39 for a total of 58+63+70+39 = 230 licks
    There are 5 people and the total amount of licks is 230 so the average is 230/5 = 46 licks to get to the center of a lollipop
    FINAL ANSWER: 46
    
    error_type:
    conceptual_error
    
    explanation:
    Incomplete calculation. The term 'sam_licks' (value: 70) was omitted from the operation.
    
    erroneous_line_number:
    L1
    
    erroneous_line:
    Dan takes 58 licks, Michael takes 63, David takes 70 and Lance takes 39 for a total of 58+63+70+39 = 230 licks
    
    erroneous_line_eqn:
    58+63+70+39=230
    
    correct_answer_mapping:
    {
      "L1": "Dan takes 58 licks, Michael takes 63, Sam takes 70, David takes 70 and Lance takes 39 for a total of 58+63+70+70+39 = 300 licks",
      "L2": "There are 5 people and the total amount of licks is 300 so the average is 300/5 = 60 licks to get to the center of a lollipop",
      "FA": "60"
    }
    
    wrong_answer_mapping:
    {
      "L1": "Dan takes 58 licks, Michael takes 63, David takes 70 and Lance takes 39 for a total of 58+63+70+39 = 230 licks",
      "L2": "There are 5 people and the total amount of licks is 230 so the average is 230/5 = 46 licks to get to the center of a lollipop",
      "FA": "46"
    }
    
    correct_eqn_mapping:
    {
      "L1": "58+63+70+70+39=300",
      "L2": "300/5=60",
      "FA": ""
    }
    
    wrong_eqn_mapping:
    {
      "L1": "58+63+70+39=230",
      "L2": "230/5=46",
      "FA": ""
    }
    
    correct_answer_length:
    3
    
    wrong_answer_length:
    3
    
    source:
    programmatic
    
    error_subtype:
    incomplete_calculation
    
    split:
    train
    
    thinking_trace:
    <think>
    There are 3 lines in the solution, including the final answer line. Let's examine the lines one-by-one.
    Line 1: Aha! I see the error. I will now prepare the output json.
    </think>
    
    json_output:
    {'verdict': 'flawed', 'erroneous_line': 'Dan takes 58 licks, Michael takes 63, David takes 70 and Lance takes 39 for a total of 58+63+70+39 = 230 licks', 'explanation': "Incomplete calculation. The term 'sam_licks' (value: 70) was omitted from the operation."}
    
    
    📋 COMPUTATIONAL_ERROR SAMPLE
    ----------------------------------------
    index:
    6751
    
    tier:
    tier1
    
    question:
    After buying shirts worth $27 from a store, Dennis received 2 $10 bills and $3 in loose coins for his change. How much money did Dennis have initially?
    
    correct_answer:
    Dennis received $10 x 2 = $20.
    So, he received a total of $20 + $3 = $23 change.
    Therefore, Dennis initially had $27 + $23 = $50.
    FINAL ANSWER: 50
    
    wrong_answer:
    Dennis received $10 x 2 = $20.
    So, he received a total of $20 + $3 = $23 change.
    Therefore, Dennis initially had $27 + $23 = $54.
    FINAL ANSWER: 54
    
    error_type:
    computational_error
    
    explanation:
    The result of this computation should be 50, not 54. This appears to be a minor miscalculation.
    
    erroneous_line_number:
    L3
    
    erroneous_line:
    Therefore, Dennis initially had $27 + $23 = $54.
    
    erroneous_line_eqn:
    27+23=54
    
    correct_answer_mapping:
    {
      "L1": "Dennis received $10 x 2 = $20.",
      "L2": "So, he received a total of $20 + $3 = $23 change.",
      "L3": "Therefore, Dennis initially had $27 + $23 = $50.",
      "FA": "50"
    }
    
    wrong_answer_mapping:
    {
      "L1": "Dennis received $10 x 2 = $20.",
      "L2": "So, he received a total of $20 + $3 = $23 change.",
      "L3": "Therefore, Dennis initially had $27 + $23 = $54.",
      "FA": "54"
    }
    
    correct_eqn_mapping:
    {
      "L1": "10*2=20",
      "L2": "20+3=23",
      "L3": "27+23=50",
      "FA": ""
    }
    
    wrong_eqn_mapping:
    {
      "L1": "10*2=20",
      "L2": "20+3=23",
      "L3": "27+23=54",
      "FA": ""
    }
    
    correct_answer_length:
    4
    
    wrong_answer_length:
    4
    
    source:
    programmatic
    
    error_subtype:
    generate_off_by_n_error
    
    split:
    train
    
    thinking_trace:
    <think>
    There are 4 lines in the solution, including the final answer line. Let's examine the lines one-by-one.
    Line 1: no errors
    Line 2: no errors
    Line 3: Aha! I see the error. I will now prepare the output json.
    </think>
    
    json_output:
    {'verdict': 'flawed', 'erroneous_line': 'Therefore, Dennis initially had $27 + $23 = $54.', 'explanation': 'The result of this computation should be 50, not 54. This appears to be a minor miscalculation.'}
    
    ============================================================



```python
# Ensure JSON output is properly serialized as string
error_detection_dataset['json_output_string'] = error_detection_dataset['json_output'].apply(
    lambda x: json.dumps(x, ensure_ascii=False, indent =2)
)
```


```python
# Sample 1 row from each error type
print("🎲 Random Sample from Each Error Type")
print("=" * 60)

for error_type in ['correct', 'conceptual_error', 'computational_error']:
    # Filter for this error type
    type_data = error_detection_dataset[error_detection_dataset['error_type'] == error_type]
    
    if len(type_data) > 0:
        # Sample 1 row randomly
        sample_row = type_data.sample(n=1, random_state=None).iloc[0]  # random_state=None for true randomness
        
        print(f"\n📋 {error_type.upper()} SAMPLE")
        print("-" * 40)
        
        # Print all column entries
        for column in error_detection_dataset.columns:
            value = sample_row[column]
            
            # Format long text values nicely
            print(f"{column}:")
            print(f"{value}")
            print()
    else:
        print(f"\n❌ No samples found for error type: {error_type}")

print("=" * 60)
```

    🎲 Random Sample from Each Error Type
    ============================================================
    
    📋 CORRECT SAMPLE
    ----------------------------------------
    index:
    979
    
    tier:
    tier2
    
    question:
    At football tryouts, the coach wanted to see who could throw the ball the farthest.  Parker threw the ball 16 yards.  Grant threw the ball 25 percent farther than Parker and Kyle threw the ball 2 times farther than Grant.  Compared to Parker, how much farther did Kyle throw the ball?
    
    correct_answer:
    Grant threw the ball 25% farther than Parker. If Parker threw the ball 16 yards, then Grant threw it 16*.25 = 4 farther
    In total, Grant threw the ball 16+4 = 20 yards
    Kyle threw 2 times farther than Grant so Kyle threw the ball 2*20 = 40 yards
    If Kyle threw the ball for 40 yards and Parker threw for 16 then Kyle threw the ball 40-16 = 24 yards farther
    FINAL ANSWER: 24
    
    wrong_answer:
    Grant threw the ball 25% farther than Parker. If Parker threw the ball 16 yards, then Grant threw it 16*0.25 = 4 farther
    In total, Grant threw the ball 16+4 = 20 yards
    Kyle threw 2 times farther than Grant so Kyle threw the ball 2*20 = 40 yards
    If Kyle threw the ball for 40 yards and Parker threw for 16 then Kyle threw the ball 40-16 = 42 yards farther
    FINAL ANSWER: 42
    
    error_type:
    correct
    
    explanation:
    None
    
    erroneous_line_number:
    L4
    
    erroneous_line:
    None
    
    erroneous_line_eqn:
    40-16=42
    
    correct_answer_mapping:
    {
      "L1": "Grant threw the ball 25% farther than Parker. If Parker threw the ball 16 yards, then Grant threw it 16*.25 = 4 farther",
      "L2": "In total, Grant threw the ball 16+4 = 20 yards",
      "L3": "Kyle threw 2 times farther than Grant so Kyle threw the ball 2*20 = 40 yards",
      "L4": "If Kyle threw the ball for 40 yards and Parker threw for 16 then Kyle threw the ball 40-16 = 24 yards farther",
      "FA": "24"
    }
    
    wrong_answer_mapping:
    None
    
    correct_eqn_mapping:
    {
      "L1": "16*.25=4",
      "L2": "16+4=20",
      "L3": "2*20=40",
      "L4": "24=24",
      "FA": ""
    }
    
    wrong_eqn_mapping:
    None
    
    correct_answer_length:
    5
    
    wrong_answer_length:
    5
    
    source:
    programmatic
    
    error_subtype:
    generate_digit_transposition_error
    
    split:
    train
    
    thinking_trace:
    <think>
    There are 5 lines in the solution, including the final answer line. Let's examine the lines one-by-one.
    Line 1: no errors
    Line 2: no errors
    Line 3: no errors
    Line 4: no errors
    Final Answer: no errors
    I found no errors! I will now prepare the output json.
    </think>
    
    json_output:
    {'verdict': 'correct', 'erroneous_line': None, 'explanation': 'All calculations and reasoning steps are correct.'}
    
    json_output_string:
    {
      "verdict": "correct",
      "erroneous_line": null,
      "explanation": "All calculations and reasoning steps are correct."
    }
    
    
    📋 CONCEPTUAL_ERROR SAMPLE
    ----------------------------------------
    index:
    715
    
    tier:
    tier1
    
    question:
    You start a business selling charm bracelets. You spend $1 on the string for each bracelet and $3 on beads for each bracelet. You sell the bracelets for $6 each. If you sell 25 bracelets, how much profit will you make?
    
    correct_answer:
    It costs $1 + $3 = $4 to make each bracelet.
    Your total cost is 25 * $4 = $100.
    Total revenue is 25 * $6 = $150.
    Total profit is $150 - $100 = $50.
    FINAL ANSWER: 50
    
    wrong_answer:
    It costs $1 + $3 = $4 to make each bracelet.
    Your total cost is 25 * $4 = $100.
    Total revenue is 25 * $6 = $150.
    Total profit is $150 +$100 = $250.
    FINAL ANSWER: 250
    
    error_type:
    conceptual_error
    
    explanation:
    Total profit is $150 - $100 = $<<150-100=50>>50, not  $150 +$100 = $ 250.
    
    
    erroneous_line_number:
    L4
    
    erroneous_line:
    Total profit is $150 +$100 = $250.
    
    erroneous_line_eqn:
    150+100=250
    
    correct_answer_mapping:
    {
      "L1": "It costs $1 + $3 = $4 to make each bracelet.",
      "L2": "Your total cost is 25 * $4 = $100.",
      "L3": "Total revenue is 25 * $6 = $150.",
      "L4": "Total profit is $150 - $100 = $50.",
      "FA": "50"
    }
    
    wrong_answer_mapping:
    {
      "L1": "It costs $1 + $3 = $4 to make each bracelet.",
      "L2": "Your total cost is 25 * $4 = $100.",
      "L3": "Total revenue is 25 * $6 = $150.",
      "L4": "Total profit is $150 +$100 = $250.",
      "FA": "250"
    }
    
    correct_eqn_mapping:
    {
      "L1": "1+3=4",
      "L2": "25*4=100",
      "L3": "25*6=150",
      "L4": "150-100=50",
      "FA": ""
    }
    
    wrong_eqn_mapping:
    {
      "L1": "1+3=4",
      "L2": "25*4=100",
      "L3": "25*6=150",
      "L4": "150+100=250",
      "FA": ""
    }
    
    correct_answer_length:
    5
    
    wrong_answer_length:
    5
    
    source:
    manual
    
    error_subtype:
    nan
    
    split:
    train
    
    thinking_trace:
    <think>
    There are 5 lines in the solution, including the final answer line. Let's examine the lines one-by-one.
    Line 1: no errors
    Line 2: no errors
    Line 3: no errors
    Line 4: Aha! I see the error. I will now prepare the output json.
    </think>
    
    json_output:
    {'verdict': 'flawed', 'erroneous_line': 'Total profit is $150 +$100 = $250.', 'explanation': 'Total profit is $150 - $100 = $<<150-100=50>>50, not  $150 +$100 = $ 250.\n'}
    
    json_output_string:
    {
      "verdict": "flawed",
      "erroneous_line": "Total profit is $150 +$100 = $250.",
      "explanation": "Total profit is $150 - $100 = $<<150-100=50>>50, not  $150 +$100 = $ 250.\n"
    }
    
    
    📋 COMPUTATIONAL_ERROR SAMPLE
    ----------------------------------------
    index:
    5584
    
    tier:
    tier2
    
    question:
    Marty and Biff were both running for student council president. A poll was taken to see how the candidate's campaigns were going. 45% of the people polled said they were voting for Biff and 8% were undecided. The rest said they are voting for Marty. If 200 people were polled, how many said they are voting for Marty?
    
    correct_answer:
    If 45% of people were voting for Biff + 8% were undecided = 53% were not voting for Marty.
    There were 100 - 53 = 47% voting for Marty.
    If 47% of 200 people were voting for Marty, 0.47 x 200 = 94 people said they were voting for Marty.
    FINAL ANSWER: 94
    
    wrong_answer:
    If 45% of people were voting for Biff + 8% were undecided = 35% were not voting for Marty.
    There were 100 - 35 = 65% voting for Marty.
    If 65% of 200 people were voting for Marty, 0.47 x 200 = 94 people said they were voting for Marty.
    FINAL ANSWER: 94
    
    error_type:
    computational_error
    
    explanation:
    The result of this computation should be 53, not 35. It appears two adjacent digits were swapped.
    
    erroneous_line_number:
    L1
    
    erroneous_line:
    If 45% of people were voting for Biff + 8% were undecided = 35% were not voting for Marty.
    
    erroneous_line_eqn:
    nan
    
    correct_answer_mapping:
    {
      "L1": "If 45% of people were voting for Biff + 8% were undecided = 53% were not voting for Marty.",
      "L2": "There were 100 - 53 = 47% voting for Marty.",
      "L3": "If 47% of 200 people were voting for Marty, 0.47 x 200 = 94 people said they were voting for Marty.",
      "FA": "94"
    }
    
    wrong_answer_mapping:
    {
      "L1": "If 45% of people were voting for Biff + 8% were undecided = 35% were not voting for Marty.",
      "L2": "There were 100 - 35 = 65% voting for Marty.",
      "L3": "If 65% of 200 people were voting for Marty, 0.47 x 200 = 94 people said they were voting for Marty.",
      "FA": "94"
    }
    
    correct_eqn_mapping:
    {
      "L1": "",
      "L2": "100-53=47",
      "L3": "0.47*200=94",
      "FA": ""
    }
    
    wrong_eqn_mapping:
    {
      "L1": "",
      "L2": "100-35=65",
      "L3": "0.47*200=94",
      "FA": ""
    }
    
    correct_answer_length:
    4
    
    wrong_answer_length:
    4
    
    source:
    programmatic
    
    error_subtype:
    generate_digit_transposition_error
    
    split:
    test
    
    thinking_trace:
    <think>
    There are 4 lines in the solution, including the final answer line. Let's examine the lines one-by-one.
    Line 1: Aha! I see the error. I will now prepare the output json.
    </think>
    
    json_output:
    {'verdict': 'flawed', 'erroneous_line': 'If 45% of people were voting for Biff + 8% were undecided = 35% were not voting for Marty.', 'explanation': 'The result of this computation should be 53, not 35. It appears two adjacent digits were swapped.'}
    
    json_output_string:
    {
      "verdict": "flawed",
      "erroneous_line": "If 45% of people were voting for Biff + 8% were undecided = 35% were not voting for Marty.",
      "explanation": "The result of this computation should be 53, not 35. It appears two adjacent digits were swapped."
    }
    
    ============================================================



```python
error_detection_dataset.to_csv(AUG_5_DATASET_DIR / "error_detection_dataset_with_traces.csv", index=False)
```


```python
error_detection_dataset.columns
```




    Index(['index', 'tier', 'question', 'correct_answer', 'wrong_answer',
           'error_type', 'explanation', 'erroneous_line_number', 'erroneous_line',
           'erroneous_line_eqn', 'correct_answer_mapping', 'wrong_answer_mapping',
           'correct_eqn_mapping', 'wrong_eqn_mapping', 'correct_answer_length',
           'wrong_answer_length', 'source', 'error_subtype', 'split',
           'thinking_trace', 'json_output', 'json_output_string'],
          dtype='object')




```python

```
