# prepare_annotation_set.py

import pandas as pd
import shutil
from pathlib import Path

# --- Configuration ---

PROJECT_ROOT = Path(__file__).parent
SOURCE_CANDIDATES_DIR = PROJECT_ROOT / "data" / "conceptual-error-candidates"
TARGET_ANNOTATION_DIR = PROJECT_ROOT / "data" / "annotation_set"

# The error types we want to sample for annotation
TARGET_ERROR_TYPES = [
    "operator_swap",
    "incorrect_operand",
    "input_misrepresentation",
    "skipped_step"
]

NUM_PER_TYPE = 100

def prepare_annotation_set(
    source_catalog_path: Path, 
    target_dir: Path, 
    error_types: List[str], 
    num_per_type: int
):
    """
    Reads a master catalog of generated candidates, samples a balanced set,
    and copies the corresponding files into a clean directory for annotation.

    Ensures that each problem index is used only once across all error types.
    """
    if not source_catalog_path.exists():
        print(f"ERROR: Source catalog not found at {source_catalog_path}")
        return

    print("--- Starting Annotation Set Preparation ---")
    
    # 1. Load the master catalog
    try:
        df = pd.read_csv(source_catalog_path)
        print(f"Loaded master catalog with {len(df)} total candidates.")
    except Exception as e:
        print(f"ERROR: Could not read catalog file. {e}")
        return

    # 2. Prepare the target directory
    if target_dir.exists():
        print(f"Target directory {target_dir} already exists. Deleting it to ensure a clean set.")
        shutil.rmtree(target_dir)
    
    pending_dir = target_dir / "pending"
    validated_dir = target_dir / "validated"
    rejected_dir = target_dir / "rejected"
    
    pending_dir.mkdir(parents=True, exist_ok=True)
    validated_dir.mkdir(exist_ok=True)
    rejected_dir.mkdir(exist_ok=True)
    print(f"Created clean target directory structure at {target_dir}")

    # 3. Perform stratified sampling
    used_indices = set()
    all_selected_files = []

    for error_type in error_types:
        print(f"\nSampling for error type: '{error_type}'...")
        
        # Filter for candidates of the current type and that have not been used yet
        available_candidates = df[
            (df['mutation_type'] == error_type) & 
            (~df['index'].isin(used_indices))
        ]
        
        if available_candidates.empty:
            print(f"  > WARNING: No available candidates found for '{error_type}'.")
            continue
        
        # Determine how many to sample
        num_to_sample = min(num_per_type, len(available_candidates))
        
        # Sample the candidates
        sampled = available_candidates.sample(n=num_to_sample, random_state=42)
        print(f"  > Selected {len(sampled)} candidates.")
        
        # Add the selected indices and file paths to our lists
        selected_indices = set(sampled['index'])
        used_indices.update(selected_indices)
        
        selected_files = sampled['filepath'].tolist()
        all_selected_files.extend(selected_files)

    # 4. Copy the selected files to the 'pending' directory
    print(f"\nCopying {len(all_selected_files)} selected files to {pending_dir}...")
    copied_count = 0
    for file_rel_path in all_selected_files:
        source_path = PROJECT_ROOT / file_rel_path
        if source_path.exists():
            target_path = pending_dir / source_path.name
            shutil.copy(source_path, target_path)
            copied_count += 1
        else:
            print(f"  > WARNING: File not found and could not be copied: {source_path}")

    print(f"\n--- Preparation Complete ---")
    print(f"Successfully copied {copied_count} candidate files.")
    print(f"Your annotation set is ready in: {pending_dir}")


if __name__ == "__main__":
    catalog_path = SOURCE_CANDIDATES_DIR / "conceptual_candidate_catalog.csv"
    prepare_annotation_set(
        source_catalog_path=catalog_path,
        target_dir=TARGET_ANNOTATION_DIR,
        error_types=TARGET_ERROR_TYPES,
        num_per_type=NUM_PER_TYPE
    )