# annotate_jsonl_streamlit.py
"""
Streamlit app to step through a JSONL math‑problem dataset and build a
parallel *annotated* JSONL file with intentionally wrong answers and error
metadata.

### ✨ Key features
* `--start N` lets you begin at any row (0‑indexed)
* **Jump to item #** box in the sidebar for random access
* **Skip →** button to move past a problem without saving
* **Incremental, append‑only output** – refresh the page or even close the
  tab and continue later without losing work (`--out` file is appended to
  line‑by‑line)

### Usage (typical Windows example)
```powershell
pip install --upgrade streamlit
streamlit run annotate_jsonl_streamlit.py \ \
         -- --src C:\path\math.jsonl \ \
         --out C:\path\math_annotated.jsonl
```
If you omit `--out`, the script uses `<src stem>_annotated.jsonl` next to the
source file; or `annotated.jsonl` in the working directory if no `--src`.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import streamlit as st

# ──────────────────────────────────────────────────────────────────────────
# Streamlit ≥1.33 switched from st.experimental_rerun → st.rerun
# ──────────────────────────────────────────────────────────────────────────
_rerun = st.rerun if hasattr(st, "rerun") else st.experimental_rerun

# ════════════════════════════════════════════════════════════════════════
# Helper utilities
# ════════════════════════════════════════════════════════════════════════

def load_jsonl(path: Path) -> list[dict]:
    """Return list of dicts from a JSONL file."""
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def dump_line(obj: dict) -> str:
    """Serialize a single object to one JSONL line (no newline)."""
    return json.dumps(obj, ensure_ascii=False)

# ════════════════════════════════════════════════════════════════════════
# CLI arg parsing
# ════════════════════════════════════════════════════════════════════════

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("--src", type=Path, help="Path to the source JSONL file")
parser.add_argument("--out", type=Path, help="Path to *output* annotated JSONL (appended)")
parser.add_argument("--start", type=int, default=None, help="0‑based row index to start from (overrides resume position)")
cli_args, _ = parser.parse_known_args()

# Determine output file path
if cli_args.out:
    out_path = cli_args.out
elif cli_args.src:
    out_path = cli_args.src.with_name(f"{cli_args.src.stem}_annotated.jsonl")
else:
    out_path = Path("annotated.jsonl")

# ════════════════════════════════════════════════════════════════════════
# Streamlit setup & session‑state initialisation
# ════════════════════════════════════════════════════════════════════════

st.set_page_config(page_title="Math Dataset Annotator", page_icon="📚", layout="wide")

if "initialised" not in st.session_state:
    # --------------------------------------------------------------
    # Load source questions
    # --------------------------------------------------------------
    if cli_args.src and cli_args.src.exists():
        st.session_state.raw = load_jsonl(cli_args.src)
    else:
        st.session_state.raw = []

    # --------------------------------------------------------------
    # Load existing annotations (resume capability)
    # --------------------------------------------------------------
    st.session_state.annotated = load_jsonl(out_path)

    # --------------------------------------------------------------
    # Set starting index: CLI --start overrides, else resume length
    # --------------------------------------------------------------
    if cli_args.start is not None:
        st.session_state.i = max(cli_args.start, 0)
    else:
        st.session_state.i = len(st.session_state.annotated)

    st.session_state.initialised = True

# ════════════════════════════════════════════════════════════════════════
# Ensure source data present (upload fallback)
# ════════════════════════════════════════════════════════════════════════

if not st.session_state.raw:
    st.warning("Pass --src <file.jsonl> when launching, or upload below →")
    uploaded = st.file_uploader("Upload source JSONL", type="jsonl")
    if uploaded is not None:
        content = uploaded.getvalue().decode("utf-8")
        st.session_state.raw = [json.loads(l) for l in content.splitlines() if l.strip()]
        _rerun()
    st.stop()

raw = st.session_state.raw
n_total = len(raw)

# ════════════════════════════════════════════════════════════════════════
# Sidebar – navigation & info
# ════════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("### Navigation")
    jump = st.number_input(
        "Jump to item # (1‑based)", min_value=1, max_value=n_total,
        value=min(st.session_state.i + 1, n_total), step=1,
        help="Type a number and press Enter to jump")
    if jump - 1 != st.session_state.i:
        st.session_state.i = int(jump - 1)
        _rerun()
    st.markdown("---")
    st.write("Total questions:", n_total)
    st.write("Annotations saved:", len(st.session_state.annotated))
    st.write("Output file:", out_path.name)

# ════════════════════════════════════════════════════════════════════════
# Main UI – current item
# ════════════════════════════════════════════════════════════════════════
idx = st.session_state.i

if idx >= n_total:
    st.success("🎉 All questions processed!")
    st.info(f"Your annotations live in `{out_path}` – open it anytime.")
    st.download_button(
        "⬇️ Download copy of annotated file",
        out_path.read_text(encoding="utf-8"),
        file_name=out_path.name,
        mime="application/json",
    )
    st.stop()

entry = raw[idx]

st.markdown(f"### ➡️ Item {idx + 1} of {n_total}")

st.markdown("#### Question 📝")
st.write(entry["question"])

st.markdown("#### Reference Answer ✅")
st.code(entry["answer"], language="text")

# -----------------------------
# Annotation form
# -----------------------------
with st.form(key="annotate"):
    wrong_answer = st.text_area("✏️ Wrong answer", value=entry["answer"], height=160)
    col1, col2 = st.columns(2)
    with col1:
        error_type = st.text_input("Error type (e.g. computational, concept, units)")
    with col2:
        explanation = st.text_area("Short explanation", height=100)

    submitted = st.form_submit_button("💾 Save & Next →")

# Skip button (doesn’t write anything)
if st.button("⏭️ Skip →", help="Go to the next item without saving"):
    st.session_state.i += 1
    _rerun()

if submitted:
    new_annotation = {
        "question": entry["question"],
        "answer": entry["answer"],
        "wrong_answer": wrong_answer,
        "error_type": error_type,
        "explanation": explanation,
    }

    # In‑memory list (for stats + download copy)
    st.session_state.annotated.append(new_annotation)

    # Append directly to output file for persistence
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("a", encoding="utf-8") as fh:
        fh.write(dump_line(new_annotation) + "\n")

    st.session_state.i += 1
    _rerun()
