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
        df = pd.read_csv(catalog_path)
        # Ensure proper data types
        df['decision_date_utc'] = df['decision_date_utc'].astype('string')
        df['decision_time_utc'] = df['decision_time_utc'].astype('string')
        df['manual_edits'] = df['manual_edits'].astype('string')
        df['filepath'] = df['filepath'].astype('string')
        return df
    else:
        # Create DataFrame with proper dtypes
        dtypes = {
            'index': 'int64',
            'tier': 'string',
            'model': 'string',
            'mutation_type': 'string',
            'target_variable': 'string',
            'correct_value': 'string',
            'flawed_value': 'string',
            'repro_seed': 'string',
            'decision_date_utc': 'string',
            'decision_time_utc': 'string',
            'status': 'string',
            'manual_edits': 'string',
            'filepath': 'string',
            'validator': 'string'
        }
        return pd.DataFrame(columns=catalog_columns).astype(dtypes)

def get_candidate_file_path(candidates_dir: Path, tier: str, index: int, model: str, mutation_type: str):
    """
    Constructs the path to the candidate JSON file based on the catalog entry.
    """
    # Search for the file in the candidates directory structure
    # The structure should be: candidates_dir / tier / index / *.json
    tier_dir = candidates_dir / tier
    if not tier_dir.exists():
        return None
    
    index_dir = tier_dir / str(index)
    if not index_dir.exists():
        return None
    
    # Look for JSON files that match the pattern
    json_files = list(index_dir.glob("*.json"))
    
    # Filter by model and mutation_type if possible
    for json_file in json_files:
        try:
            data = load_json(json_file)
            if (data.get('model_name') == model and 
                data.get('mutation_details', {}).get('type') == mutation_type):
                return json_file
        except:
            continue
    
    # If no exact match, return the first JSON file found
    return json_files[0] if json_files else None

def get_ordered_todo_items(catalog_df):
    """
    Returns catalog entries ordered by priority:
    1. Todo items first
    2. Within todo items, descending order of tier
    3. Non-todo items last, also by descending tier
    """
    if catalog_df.empty:
        return catalog_df
    
    # Create a tier ordering for sorting (higher tiers first)
    tier_order = {'tier4': 4, 'tier3': 3, 'tier2': 2, 'tier1': 1}
    catalog_df['tier_numeric'] = catalog_df['tier'].map(tier_order).fillna(0)
    
    # Create priority ordering: todo=0 (highest priority), others=1
    catalog_df['priority'] = catalog_df['status'].apply(lambda x: 0 if x == 'todo' else 1)
    
    # Sort by priority first, then by tier (descending)
    ordered_df = catalog_df.sort_values(
        ['priority', 'tier_numeric'], 
        ascending=[True, False]
    ).reset_index(drop=True)
    
    # Remove helper columns
    ordered_df = ordered_df.drop(['tier_numeric', 'priority'], axis=1)
    
    return ordered_df

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
    /* Style for erroneous line marker */
    div[data-testid="stTextInput"] input[value*="● L1"],
    div[data-testid="stTextInput"] input[value*="● L2"],
    div[data-testid="stTextInput"] input[value*="● L3"],
    div[data-testid="stTextInput"] input[value*="● L4"],
    div[data-testid="stTextInput"] input[value*="● FA"] {
        color: #d32f2f !important;
        font-weight: bold !important;
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
    /* Progress indicator styling */
    .progress-info {
        padding: 0.5rem;
        background-color: #E3F2FD;
        border: 1px solid #BBDEFB;
        border-radius: 5px;
        color: #0D47A1;
        margin-bottom: 1rem;
    }
    /* Enhanced button styling */
    .stButton > button {
        height: 3.5em !important;
        font-size: 1.3em !important;
        font-weight: bold !important;
        width: 100% !important;
        border-radius: 10px !important;
        margin-bottom: 0.5em !important;
        border: 2px solid transparent !important;
        transition: all 0.3s ease !important;
    }
    /* Accept button - Green */
    .stButton:nth-of-type(1) > button {
        background-color: #4CAF50 !important;
        color: white !important;
        border-color: #45a049 !important;
    }
    .stButton:nth-of-type(1) > button:hover {
        background-color: #45a049 !important;
        border-color: #3d8b40 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 8px rgba(76, 175, 80, 0.3) !important;
    }
    /* Skip button - Yellow */
    .stButton:nth-of-type(2) > button {
        background-color: #FFD600 !important;
        color: #333 !important;
        border-color: #FFC107 !important;
    }
    .stButton:nth-of-type(2) > button:hover {
        background-color: #FFC107 !important;
        border-color: #FFB300 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 8px rgba(255, 214, 0, 0.3) !important;
    }
    /* Reject button - Red */
    .stButton:nth-of-type(3) > button {
        background-color: #F44336 !important;
        color: white !important;
        border-color: #e53935 !important;
    }
    .stButton:nth-of-type(3) > button:hover {
        background-color: #e53935 !important;
        border-color: #d32f2f !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 8px rgba(244, 67, 54, 0.3) !important;
    }
    /* Keyboard shortcut hints */
    .shortcut-hint {
        font-size: 0.8em;
        opacity: 0.7;
        margin-top: 0.25em;
    }
    /* Status badge styling */
    .status-badge {
        display: inline-block;
        padding: 0.2em 0.6em;
        border-radius: 15px;
        font-size: 0.9em;
        font-weight: bold;
        margin-left: 0.5em;
    }
    .status-todo {
        background-color: #fff3cd;
        color: #856404;
        border: 1px solid #ffeaa7;
    }
    .status-accepted {
        background-color: #d1f2eb;
        color: #0c5460;
        border: 1px solid #7dcea0;
    }
    .status-rejected {
        background-color: #f8d7da;
        color: #721c24;
        border: 1px solid #f5c6cb;
    }
    .status-skipped {
        background-color: #e2e3e5;
        color: #383d41;
        border: 1px solid #d6d8db;
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

    # Get ordered items based on priority (todo first, then by tier descending)
    ordered_catalog = get_ordered_todo_items(catalog_df)
    st.session_state.ordered_catalog = ordered_catalog
    st.session_state.current_index = 0
    st.session_state.initialised = True

catalog_df = st.session_state.catalog_df
ordered_catalog = st.session_state.ordered_catalog
current_index = st.session_state.current_index
PROJECT_ROOT = st.session_state.PROJECT_ROOT
person_name = st.session_state.person_name

# ──────────────────────────────────────────────────────────────────────────
# Main Application UI
# ──────────────────────────────────────────────────────────────────────────

if current_index >= len(ordered_catalog):
    st.success("🎉 All candidates have been processed!")
    st.info(f"The validation catalog is saved at: {st.session_state.CATALOG_PATH}")
    st.dataframe(catalog_df)
    st.stop()

# Get current catalog entry
current_entry = ordered_catalog.iloc[current_index]

# Find the corresponding JSON file
candidate_path = get_candidate_file_path(
    st.session_state.CANDIDATES_DIR,
    current_entry['tier'],
    current_entry['index'],
    current_entry['model'],
    current_entry['mutation_type']
)

if candidate_path is None or not candidate_path.exists():
    st.error(f"Could not find candidate file for index {current_entry['index']}, tier {current_entry['tier']}")
    st.write("Skipping to next item...")
    st.session_state.current_index += 1
    st.rerun()

filename = candidate_path.name
candidate_data = load_json(candidate_path)

index = current_entry['index']
mutation_details = candidate_data.get("mutation_details", {})
mutation_type = mutation_details.get("type", "N/A")
original_solution = candidate_data.get("original_solution_mapping", {})
initial_flawed_reconstruction = candidate_data.get("flawed_nl_reconstruction", {})

# Count remaining items by status
todo_count = len(ordered_catalog[ordered_catalog['status'] == 'todo'])
remaining_count = len(ordered_catalog) - current_index

# --- Header and Metadata Section (Revised Layout) ---
st.markdown(f"""
<div class="title-container">
    <h3>Conceptual Error Validation - {person_name.title()}</h3>
    <h3>Remaining: {remaining_count} (Todo: {todo_count})</h3>
</div>
""", unsafe_allow_html=True)

# Show progress info with enhanced status badge
current_status = current_entry['status']
status_class = f"status-{current_status.replace('ed', '')}" if current_status != 'todo' else "status-todo"
status_badge = f'<span class="status-badge {status_class}">{current_status.title()}</span>'

st.markdown(f"""
<div class="progress-info">
    📊 <strong>Progress:</strong> {current_index + 1}/{len(ordered_catalog)} | 
    <strong>Index:</strong> {index} |
    <strong>Current Status:</strong> {status_badge} | 
    <strong>Tier:</strong> {current_entry['tier']} | 
    <strong>Mutation:</strong> {mutation_type} |
    <strong>Filename:</strong> {filename}
</div>
""", unsafe_allow_html=True)

# Get the erroneous line number for highlighting
erroneous_line_number = candidate_data.get("erroneous_line_number", "")

col1_meta, col2_meta = st.columns([1, 5])
with col1_meta:
    st.markdown('<p class="metadata-label">Erroneous Line</p>', unsafe_allow_html=True)
    st.text_input("Erroneous Line", value=erroneous_line_number, key="erroneous_line_number_edit", label_visibility="collapsed")
with col2_meta:
    st.markdown('<p class="metadata-label">Explanation</p>', unsafe_allow_html=True)
    st.text_input("Explanation", value=candidate_data.get("explanation"), key="explanation_edit", label_visibility="collapsed")

st.markdown("---")

# --- Main Comparison View ---
col1, col2, col3 = st.columns([8, 1, 8], gap="small")
col1.markdown("##### ✅ Correct Solution")
col2.markdown("##### Line")
col3.markdown("##### ✏️ Flawed Solution (Editable)")

line_keys = sorted(original_solution.keys(), key=lambda k: (k != 'FA', int(k[1:]) if k.startswith('L') else float('inf')))

for line_num in line_keys:
    is_erroneous_line = line_num == erroneous_line_number
    
    with col1:
        st.text_input(
            label=f"display_{line_num}", value=original_solution.get(line_num, ''),
            key=f"display_{line_num}", disabled=True, label_visibility="collapsed"
        )
    with col2:
        # Add visual marker for erroneous line
        line_display = f"● {line_num}" if is_erroneous_line else line_num
        st.text_input(
            label=f"line_num_display_{line_num}", value=line_display,
            key=f"line_num_display_{line_num}", disabled=True, label_visibility="collapsed"
        )
    with col3:
        st.text_input(
            label=f"edit_{line_num}", value=initial_flawed_reconstruction.get(line_num, ""),
            key=f"edit_{line_num}", label_visibility="collapsed"
        )

# --- Decision Buttons ---
st.markdown("---")

# Show keyboard shortcuts hint
st.markdown("""
<div style="text-align: center; margin-bottom: 1rem; opacity: 0.7;">
    💡 <strong>Keyboard shortcuts:</strong> Press A for Accept, S for Skip, R for Reject
</div>
""", unsafe_allow_html=True)

# Enhanced Decision Buttons with better spacing and tooltips
btn_col1, btn_col2, btn_col3 = st.columns(3, gap="large")

decision = None

with btn_col1:
    accept = st.button("✅ Accept", key="accept_btn", use_container_width=True, help="Accept this error candidate (Shortcut: A)")
    st.markdown('<div class="shortcut-hint">Press A</div>', unsafe_allow_html=True)
with btn_col2:
    skip = st.button("⏭️ Skip", key="skip_btn", use_container_width=True, help="Skip this candidate for now (Shortcut: S)")
    st.markdown('<div class="shortcut-hint">Press S</div>', unsafe_allow_html=True)
with btn_col3:
    reject = st.button("❌ Reject", key="reject_btn", use_container_width=True, help="Reject this error candidate (Shortcut: R)")
    st.markdown('<div class="shortcut-hint">Press R</div>', unsafe_allow_html=True)

# Add keyboard shortcut functionality
st.markdown("""
<script>
document.addEventListener('keydown', function(event) {
    if (event.target.tagName === 'INPUT' || event.target.tagName === 'TEXTAREA') {
        return; // Don't trigger shortcuts when typing in input fields
    }
    
    switch(event.key.toLowerCase()) {
        case 'a':
            event.preventDefault();
            const acceptBtn = window.parent.document.querySelector('button[kind="primary"]');
            if (acceptBtn && acceptBtn.innerText.includes('Accept')) acceptBtn.click();
            break;
        case 's':
            event.preventDefault();
            const skipBtn = window.parent.document.querySelector('button[kind="primary"]');
            if (skipBtn && skipBtn.innerText.includes('Skip')) skipBtn.click();
            break;
        case 'r':
            event.preventDefault();
            const rejectBtn = window.parent.document.querySelector('button[kind="primary"]');
            if (rejectBtn && rejectBtn.innerText.includes('Reject')) rejectBtn.click();
            break;
    }
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
    
    # Convert manual_edits list to string for storage
    manual_edits_str = ','.join(manual_edits) if manual_edits else ''
    
    # Update the existing row in the catalog
    mask = (
        (catalog_df['index'] == index) & 
        (catalog_df['tier'] == current_entry['tier']) & 
        (catalog_df['mutation_type'] == mutation_type)
    )
    catalog_df.loc[mask, 'decision_date_utc'] = now_utc.strftime('%Y-%m-%d')
    catalog_df.loc[mask, 'decision_time_utc'] = now_utc.strftime('%H:%M:%S')
    catalog_df.loc[mask, 'status'] = decision
    catalog_df.loc[mask, 'manual_edits'] = manual_edits_str
    catalog_df.loc[mask, 'filepath'] = final_filepath_str

    # Save updated catalog
    st.session_state.catalog_df = catalog_df
    catalog_df.to_csv(st.session_state.CATALOG_PATH, index=False)
    
    # Show success message with action taken
    decision_emoji = {"accepted": "✅", "skipped": "⏭️", "rejected": "❌"}
    st.success(f"{decision_emoji[decision]} {decision.title()} item {index}! Moving to next candidate...")
    
    # Refresh the ordered catalog for the next iteration
    st.session_state.ordered_catalog = get_ordered_todo_items(catalog_df)
    st.session_state.current_index += 1
    st.rerun()