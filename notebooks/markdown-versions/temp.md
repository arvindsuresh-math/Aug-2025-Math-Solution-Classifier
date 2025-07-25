```python
import json
import re
import ast
import inspect
import importlib.util
from pathlib import Path
from types import ModuleType
from typing import Callable, Any, Dict, List
from fractions import Fraction as BuiltinFraction
import datetime
import functools
import random
import copy

import pandas as pd
from tqdm.notebook import tqdm
# from datasets import load_dataset, Dataset

# --- Path and Directory Definitions ---
def find_project_root(marker: str = ".git") -> Path:
    current_path = Path.cwd().resolve()
    while current_path != current_path.parent:
        if (current_path / marker).exists():
            return current_path
        current_path = current_path.parent
    raise FileNotFoundError(f"Could not find project root. Marker '{marker}' not found.")

PROJECT_ROOT = find_project_root()
DATA_DIR = PROJECT_ROOT / 'data'

PROCESSED_TEMPLATE_DIR = DATA_DIR / "template-generated-processed"
GENERATED_ERRORS_DIR = DATA_DIR / "computational-errors-generated"

MODELS = ['openai_gpt-4.1', 'google_gemini-2.5-flash']

print(f"Project root: {PROJECT_ROOT}")
print(f"Input (Processed Templates): {PROCESSED_TEMPLATE_DIR}")
print(f"Output (Generated Errors): {GENERATED_ERRORS_DIR}")

# --- Ensure Directories Exist ---
PROCESSED_TEMPLATE_DIR.mkdir(parents=True, exist_ok=True)
GENERATED_ERRORS_DIR.mkdir(parents=True, exist_ok=True)
```

    Project root: /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math
    Input (Processed Templates): /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/template-generated-processed
    Output (Generated Errors): /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/computational-errors-generated



```python
df = pd.read_csv(DATA_DIR / 'sft-datasets' / 'level-1-binary' / 'sft_level1_catalog.csv')

sample = df.head()
sample.to_csv(DATA_DIR / 'sft-datasets' / 'level-1-binary' / 'sft_level1_catalog_sample.csv', index=False)
```


```python
# --- Load GSM8K Dataset ---
from datasets import load_dataset, Dataset
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

def get_tier(index: int, tier_lists: dict[str, list[int]]) -> str:
    found = None
    for tier, indices in tier_lists.items():
        if index in indices:
            found = tier
            break
    if found:
        return found
    else:
        raise ValueError(f"Index {index} not found in any tier lists.")
```

    Tier definitions loaded.



```python
df = pd.read_csv('../data/manually_generated_errors_final.csv')

# create a df with 3 conceptual error samples and 3 computational error samples
def create_error_samples(df: pd.DataFrame, num_samples: int = 3) -> pd.DataFrame:
    conceptual_errors = df[df['error_type'] == 'conceptual'].sample(n=num_samples, random_state=42)
    computational_errors = df[df['error_type'] == 'computational'].sample(n=num_samples, random_state=42)
    return pd.concat([conceptual_errors, computational_errors]).reset_index(drop=True)

sample_df = create_error_samples(df)
# Save the sample DataFrame to a CSV file
sample_df.to_csv('../data/sampled_errors.csv', index=False)

```


```python

```


```python
# load the error samples json file
with open(DATA_DIR / 'conceptual_error_samples.json', 'r') as json_file:
    conceptual_error_samples = json.load(json_file)

# add a "tier" field to each error sample
for error_type, details in conceptual_error_samples.items():
    for sample in details['samples']:
        sample['tier'] = get_tier(sample['index'], TIER_LISTS)
```


```python
# for each sample in the error samples, add the raw template from DATA_DIR / 'template-generated-raw'

for error_type, details in conceptual_error_samples.items():
    for sample in details['samples']:
        tier = sample['tier']
        if tier == 'tier5':
            continue  # Skip symbolic tier as it doesn't have raw templates

        idx = str(sample['index'])
        template_folder = DATA_DIR / 'template-generated-raw' / tier / idx

        # Choose a random template file from the folder
        template_files = list(template_folder.glob('*.txt'))
        if not template_files:
            raise FileNotFoundError(f"No template files found in {template_folder}")
        file = template_files[0]  # For simplicity, just take the first file
        with open(file, 'r') as f:
            sample['formalization_template'] = json.loads(f.read())

# Save the updated error samples with tiers back to the JSON file
with open(DATA_DIR / 'conceptual_error_samples_with_tiers.json', 'w') as json_file:
    json.dump(conceptual_error_samples, json_file, indent=2)
```


```python
conceptual_error_samples_small = copy.deepcopy(conceptual_error_samples)

# Keep only 3 samples per error type
for error_type, details in conceptual_error_samples_small.items():
    details['samples'] = details['samples'][:3]

# Save the small error samples to a new JSON file
with open(DATA_DIR / 'conceptual_error_samples_small.json', 'w') as json_file:
    json.dump(conceptual_error_samples_small, json_file, indent=2)
```


```python

```
