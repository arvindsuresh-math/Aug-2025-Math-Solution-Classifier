```python
import re
import json
from pathlib import Path
from tqdm.notebook import tqdm
import pandas as pd 

# --- 1. Define Paths and Models ---
def find_project_root(marker: str = ".git") -> Path:
    current_path = Path.cwd().resolve()
    while current_path != current_path.parent:
        if (current_path / marker).exists():
            return current_path
        current_path = current_path.parent
    raise FileNotFoundError(f"Could not find project root. Marker '{marker}' not found.")

PROJECT_ROOT = find_project_root()
DATA_DIR = PROJECT_ROOT / 'data'

RAW_TEMPLATE_DIR = DATA_DIR / "template-generated-raw"
PROCESSED_TEMPLATE_DIR = DATA_DIR / "template-generated-processed"

MODELS = ['openai_gpt-4.1', 'google_gemini-2.5-flash']

print(f"Input Raw Templates: {RAW_TEMPLATE_DIR}")
print(f"Output for Processed Files: {PROCESSED_TEMPLATE_DIR}")


# --- 2. MODIFIED Helper Function for Processing ---
def process_single_raw_template(
    raw_file_path: Path,
    output_dir: Path,
    model_name: str
) -> tuple[str, str | None]:
    """
    Reads a single raw template .txt file and processes it.

    --- MODIFIED: Returns a tuple (status, reason) ---
    - ('success', None) on success.
    - ('failure', 'reason_string') on failure.
    """
    if not raw_file_path.exists():
        return 'failure', 'FileNotFound'

    try:
        content = raw_file_path.read_text(encoding='utf-8').strip()
        if not content:
            return 'failure', 'FileIsEmpty'

        # Extract content from ```json ... ``` block if it exists
        match = re.search(r'```json\s*([\s\S]*?)\s*```', content, re.DOTALL)
        json_string = match.group(1) if match else content

        template_data = json.loads(json_string)

        function_code = template_data.get("function_code")
        logical_steps = template_data.get("logical_steps")

        if not function_code or not logical_steps:
            return 'failure', 'MissingKeys'

        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / f"{model_name}.py").write_text(function_code, encoding='utf-8')
        with open(output_dir / f"{model_name}.json", 'w', encoding='utf-8') as f:
            json.dump(logical_steps, f, indent=2)

        return 'success', None
        
    except json.JSONDecodeError:
        return 'failure', 'JSONDecodeError'
    except Exception as e:
        return 'failure', f'UnexpectedError:{type(e).__name__}'


# --- 3. MODIFIED Main Driver Function ---
def preprocess_all_raw_templates(
    raw_dir: Path,
    processed_dir: Path,
    models: list[str]
):
    """
    Iterates through all raw templates, saves successes, and logs failures.
    """
    print("\n--- Starting Pre-processing of Raw Templates ---")
    if not raw_dir.is_dir():
        print(f"ERROR: Source directory not found: {raw_dir}")
        return

    success_count = 0
    # --- NEW: List to store details of failed files ---
    failures = []
    
    tier_dirs = sorted([d for d in raw_dir.iterdir() if d.is_dir() and d.name.startswith('tier')])

    for tier_dir in tqdm(tier_dirs, desc="Processing Tiers"):
        index_dirs = sorted([d for d in tier_dir.iterdir() if d.is_dir() and d.name.isdigit()], key=lambda p: int(p.name))
        
        for index_dir in index_dirs:
            for model_name in models:
                raw_file = index_dir / f"{model_name}.txt"
                output_dir = processed_dir / tier_dir.name / index_dir.name
                
                status, reason = process_single_raw_template(raw_file, output_dir, model_name)
                
                if status == 'success':
                    success_count += 1
                else:
                    failures.append({
                        'filepath': str(raw_file.relative_to(PROJECT_ROOT)),
                        'reason': reason
                    })
    
    print("\n--- Pre-processing Complete ---")
    print(f"Successfully processed: {success_count} files")
    
    # --- NEW: Save the failure log to a CSV file ---
    if failures:
        print(f"Failed to process:      {len(failures)} files")
        failure_log_path = raw_dir / "failed_templates_log.csv"
        df_failures = pd.DataFrame(failures)
        df_failures.to_csv(failure_log_path, index=False)
        print(f"Failure log saved to: {failure_log_path}")
    else:
        print("Failed to process:      0 files")


# --- 4. Execute the Pipeline ---
preprocess_all_raw_templates(RAW_TEMPLATE_DIR, PROCESSED_TEMPLATE_DIR, MODELS)
```

    Input Raw Templates: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/template-generated-raw
    Output for Processed Files: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/template-generated-processed
    
    --- Starting Pre-processing of Raw Templates ---



    Processing Tiers:   0%|          | 0/5 [00:00<?, ?it/s]


    
    --- Pre-processing Complete ---
    Successfully processed: 4796 files
    Failed to process:      1056 files
    Failure log saved to: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/template-generated-raw/failed_templates_log.csv

