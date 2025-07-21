# validate_candidates.py
"""
Streamlit GUI for validating and refining programmatically generated conceptual
error candidates for a math problem dataset.

This tool presents a side-by-side comparison of a correct solution and a
programmatically generated flawed version. The user can then edit the flawed
solution on a line-by-line basis, refine the error metadata, and accept or
reject the candidate.

All decisions are logged in a persistent CSV catalog, enabling the session
to be stopped and resumed at any time.

Usage:
    streamlit run validate_candidates.py --theme.base "light" -- --candidates-dir <path_to_candidates> --person-name <validator_name>
"""

from __future__ import annotations

import argparse
import json
import datetime
from pathlib import Path
import streamlit as st
import pandas as pd

# ──────────────────────────────────────────────────────────────────────────
# Utility Functions
# ──────────────────────────────────────────────────────────────────────────

def find_project_root(marker: str = ".git"):
    """
    Traverses the directory structure upwards to locate the project root,
    identified by a marker (e.g., '.git' directory).
    """
    current_path = Path.cwd().resolve()
    while current_path != current_path.parent:
        if (current_path / marker).exists():
            return current_path
        current_path = current_path.parent
    raise FileNotFoundError(f"Could not find project root. Marker '{marker}' not found.")

def load_json(path: Path):
    """Loads a single JSON file and returns its content as a dictionary."""
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def dump_json(data: dict, path: Path):
    """Saves a dictionary to a JSON file with indentation."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_or_initialize_catalog(catalog_path: Path):
    """
    Loads the existing annotation catalog if it exists, otherwise initializes
    an empty DataFrame with the required schema.
    """
    catalog_columns = [
        'index', 'tier', 'model', 'mutation_type', 'target_variable',
        'correct_value', 'flawed_value', 'repro_seed', 'decision_date_utc',
        'decision_time_utc', 'status', 'manual_edits', 'filepath', 'validator'
    ]
    if catalog_path.exists():
        return pd.read_csv(catalog_path)
    else:
        return pd.DataFrame(columns=catalog_columns)

# ──────────────────────────────────────────────────────────────────────────
# Streamlit Page and Session State Setup
# ──────────────────────────────────────────────────────────────────────────

st.set_page_config(page_title="Conceptual Error Validation", page_icon="✍️", layout="wide")

# --- Inject Custom CSS for Styling ---
st.markdown("""
<style>
    /* Remove top padding from the main content block */
    div.block-container {
        padding-top: 1.5rem;
    }
    /* Style for the main title and remaining count header */
    .title-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.5rem;
    }
    .title-container h1, .title-container h3 {
        margin-bottom: 0;
    }
    /* Style for the single, compact metadata line */
    .metadata-container {
        font-size: 1.1rem;
        padding: 0.5rem;
        background-color: #F0F2F6;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    .metadata-container code {
        font-size: 1rem;
    }
    /* Style for the labels of editable fields */
    .metadata-label {
        font-size: 1.1rem;
        font-weight: bold;
        margin-bottom: 0.25rem;
    }
    /* Uniform styling for all text input boxes */
    div[data-testid="stTextInput"] input {
        font-size: 1rem;
        border-radius: 5px;
    }
    /* Styling for disabled inputs (used for alignment) */
    div[data-testid="stTextInput"] input[disabled] {
        -webkit-text-fill-color: #000000;
        color: #000000;
        background-color: #F0F2F6;
    }
    /* Center the text in the line number column */
    div[data-testid="stTextInput"] input[id^="line_num_display"] {
        text-align: center;
        font-weight: bold;
    }
    /* Success message styling */
    .validator-success {
        padding: 0.5rem;
        background-color: #D4EDDA;
        border: 1px solid #C3E6CB;
        border-radius: 5px;
        color: #155724;
        margin-bottom: 1rem;
    }
    /* Error message styling */
    .validator-error {
        padding: 0.5rem;
        background-color: #F8D7DA;
        border: 1px solid #F5C6CB;
        border-radius: 5px;
        color: #721C24;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)


if "initialised" not in st.session_state:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--candidates-dir", type=Path, required=True, help="Directory containing candidate JSON files.")
    parser.add_argument("--person-name", type=str, required=True, help="Name of the person doing validation (used for catalog naming)")
    cli_args, _ = parser.parse_known_args()
    
    # Define valid team member names (update this list with your actual team names)
    VALID_VALIDATORS = ['ali', 'arvind', 'ling', 'mauro', 'yewei']  # Replace with actual names
    
    # Validate person name
    person_name = cli_args.person_name.lower().strip()
    if person_name not in VALID_VALIDATORS:
        st.markdown(f"""
        <div class="validator-error">
            ⚠️ <strong>Invalid validator name:</strong> "{cli_args.person_name}"<br>
            <strong>Valid names are:</strong> {', '.join(VALID_VALIDATORS)}<br>
            <strong>Usage:</strong> <code>streamlit run validate_candidates.py --theme.base "light" -- --candidates-dir &lt;path&gt; --person-name &lt;name&gt;</code>
        </div>
        """, unsafe_allow_html=True)
        st.stop()
    
    # Show success message for valid validator
    st.markdown(f"""
    <div class="validator-success">
        ✅ <strong>Validation session for:</strong> {person_name.title()}<br>
        <strong>Personal catalog:</strong> validation_catalog_{person_name}.csv
    </div>
    """, unsafe_allow_html=True)
    
    PROJECT_ROOT = find_project_root()
    st.session_state.PROJECT_ROOT = PROJECT_ROOT
    st.session_state.CANDIDATES_DIR = cli_args.candidates_dir.resolve()
    st.session_state.ACCEPTED_DIR = PROJECT_ROOT / 'data' / 'conceptual-errors-accepted'
    st.session_state.person_name = person_name
    
    # Updated catalog path to include person name
    st.session_state.CATALOG_PATH = st.session_state.CANDIDATES_DIR / f"validation_catalog_{person_name}.csv"

    catalog_df = load_or_initialize_catalog(st.session_state.CATALOG_PATH)
    st.session_state.catalog_df = catalog_df

    processed_filepaths = set()
    if 'filepath' in catalog_df.columns and not catalog_df['filepath'].empty:
        processed_filepaths = set(catalog_df['filepath'].apply(lambda x: (PROJECT_ROOT / x).resolve() if pd.notna(x) else None))
        
    all_candidate_paths = {p.resolve() for p in st.session_state.CANDIDATES_DIR.rglob("*.json")}
    
    unprocessed_paths = sorted(list(all_candidate_paths - processed_filepaths))
    st.session_state.candidate_paths = unprocessed_paths
    st.session_state.current_index = 0
    st.session_state.initialised = True

catalog_df = st.session_state.catalog_df
candidate_paths = st.session_state.candidate_paths
current_index = st.session_state.current_index
PROJECT_ROOT = st.session_state.PROJECT_ROOT
person_name = st.session_state.person_name

# ──────────────────────────────────────────────────────────────────────────
# Main Application UI
# ──────────────────────────────────────────────────────────────────────────

if current_index >= len(candidate_paths):
    st.success("🎉 All candidates have been processed!")
    st.info(f"The validation catalog is saved at: {st.session_state.CATALOG_PATH}")
    st.dataframe(catalog_df)
    st.stop()

candidate_path = candidate_paths[current_index]
filename = candidate_path.name
candidate_data = load_json(candidate_path)

index, mutation_details = candidate_data.get("index"), candidate_data.get("mutation_details", {})
mutation_type = mutation_details.get("type", "N/A")
original_solution = candidate_data.get("original_solution_mapping", {})
initial_flawed_reconstruction = candidate_data.get("flawed_nl_reconstruction", {})

# --- Header and Metadata Section (Revised Layout) ---
st.markdown(f"""
<div class="title-container">
    <h3>Conceptual Error Validation - {person_name.title()}</h3>
    <h3>Remaining: {len(candidate_paths) - current_index}</h3>
</div>
""", unsafe_allow_html=True)

# ...existing code...
meta_col1, meta_col2, meta_col3 = st.columns([1, 3, 7])
with meta_col1:
    st.markdown('<p class="metadata-label">Index</p>', unsafe_allow_html=True)
    st.text_input("Index", value=str(index), key="index_display", disabled=True, label_visibility="collapsed")
with meta_col2:
    st.markdown('<p class="metadata-label">Mutation type</p>', unsafe_allow_html=True)
    st.text_input("Mutation type", value=str(mutation_type), key="mutation_type_display", disabled=True, label_visibility="collapsed")
with meta_col3:
    st.markdown('<p class="metadata-label">Filename</p>', unsafe_allow_html=True)
    st.text_input("Filename", value=str(filename), key="filename_display", disabled=True, label_visibility="collapsed")

col1_meta, col2_meta = st.columns([1, 5])
with col1_meta:
    st.markdown('<p class="metadata-label">Erroneous Line</p>', unsafe_allow_html=True)
    st.text_input("Erroneous Line", value=candidate_data.get("erroneous_line_number"), key="erroneous_line_number_edit", label_visibility="collapsed")
with col2_meta:
    st.markdown('<p class="metadata-label">Explanation</p>', unsafe_allow_html=True)
    st.text_input("Explanation", value=candidate_data.get("explanation"), key="explanation_edit", label_visibility="collapsed")

st.markdown("---")

# --- Main Comparison View ---
# st.subheader("Solution Comparison and Editing")
col1, col2, col3 = st.columns([8, 1, 8], gap="small")
col1.markdown("##### ✅ Correct Solution")
col2.markdown("##### Line")
col3.markdown("##### ✏️ Flawed Solution (Editable)")

line_keys = sorted(original_solution.keys(), key=lambda k: (k != 'FA', int(k[1:]) if k.startswith('L') else float('inf')))

for line_num in line_keys:
    with col1:
        st.text_input(
            label=f"display_{line_num}", value=original_solution.get(line_num, ''),
            key=f"display_{line_num}", disabled=True, label_visibility="collapsed"
        )
    with col2:
        st.text_input(
            label=f"line_num_display_{line_num}", value=line_num,
            key=f"line_num_display_{line_num}", disabled=True, label_visibility="collapsed"
        )
    with col3:
        st.text_input(
            label=f"edit_{line_num}", value=initial_flawed_reconstruction.get(line_num, ""),
            key=f"edit_{line_num}", label_visibility="collapsed"
        )

# --- Decision Buttons ---
st.markdown("---")

# --- Decision Buttons (large, colored, full-width, ordered Accept, Skip, Reject) ---
btn_col1, btn_col2, btn_col3 = st.columns(3, gap="large")

# Custom CSS for button colors and size
st.markdown("""
<style>
.custom-btn {
    height: 3.5em !important;
    font-size: 1.3em !important;
    font-weight: bold !important;
    width: 100% !important;
    border-radius: 10px !important;
    margin-bottom: 0.5em !important;
    border: none !important;
}
.accept-btn {
    background-color: #4CAF50 !important;
    color: white !important;
}
.skip-btn {
    background-color: #FFD600 !important;
    color: #333 !important;
}
.reject-btn {
    background-color: #F44336 !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

decision = None

with btn_col1:
    accept = st.button("✅ Accept", key="accept_btn", use_container_width=True)
with btn_col2:
    skip = st.button("⏭️ Skip", key="skip_btn", use_container_width=True)
with btn_col3:
    reject = st.button("❌ Reject", key="reject_btn", use_container_width=True)

# JavaScript to apply custom classes to Streamlit buttons
st.markdown("""
<script>
const btns = window.parent.document.querySelectorAll('button');
btns.forEach(btn => {
    if (btn.innerText.includes('Accept')) btn.classList.add('custom-btn', 'accept-btn');
    if (btn.innerText.includes('Skip')) btn.classList.add('custom-btn', 'skip-btn');
    if (btn.innerText.includes('Reject')) btn.classList.add('custom-btn', 'reject-btn');
});
</script>
""", unsafe_allow_html=True)

if accept:
    decision = 'accepted'
elif skip:
    decision = 'skipped'
elif reject:
    decision = 'rejected'

if decision:
    final_explanation = st.session_state.explanation_edit
    final_erroneous_line = st.session_state.erroneous_line_number_edit
    final_flawed_solution_lines = {key: st.session_state[f"edit_{key}"] for key in line_keys if f"edit_{key}" in st.session_state}
    manual_edits = [key for key, value in final_flawed_solution_lines.items() if value != initial_flawed_reconstruction.get(key, "")]
    flawed_solution_text = "\n".join(final_flawed_solution_lines.values())

    if decision == 'accepted':
        final_sft_json = {
            "verdict": "Flawed",
            "error_details": {
                "error_type": mutation_type,
                "erroneous_line_number": final_erroneous_line,
                "explanation": final_explanation
            },
            "context": {
                "question": candidate_data.get('question', 'N/A'),
                "flawed_solution": flawed_solution_text
            }
        }
        tier = candidate_path.parent.parent.name
        index_dir = candidate_path.parent.name
        accepted_path = st.session_state.ACCEPTED_DIR / tier / index_dir / filename
        dump_json(final_sft_json, accepted_path)
        final_filepath_str = str(accepted_path.relative_to(PROJECT_ROOT))
    else:
        final_filepath_str = str(candidate_path.relative_to(PROJECT_ROOT))

    now_utc = datetime.datetime.now(datetime.timezone.utc)
    new_row = {
        'index': index,
        'tier': candidate_path.parent.parent.name,
        'model': candidate_data.get('model_name'),
        'mutation_type': mutation_type,
        'target_variable': mutation_details.get('target_variable'),
        'correct_value': candidate_data.get('correct_value'),
        'flawed_value': candidate_data.get('flawed_value'),
        'repro_seed': candidate_data.get('repro_seed'),
        'decision_date_utc': now_utc.strftime('%Y-%m-%d'),
        'decision_time_utc': now_utc.strftime('%H:%M:%S'),
        'status': decision,
        'manual_edits': manual_edits,
        'filepath': final_filepath_str,
        'validator': person_name  # Add validator name to the record
    }

    st.session_state.catalog_df = pd.concat([catalog_df, pd.DataFrame([new_row])], ignore_index=True)
    st.session_state.catalog_df.to_csv(st.session_state.CATALOG_PATH, index=False)

    st.session_state.current_index += 1
    st.rerun()