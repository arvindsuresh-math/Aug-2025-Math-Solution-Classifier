"""
gsm8k_validator_v2.py
======================

Performs a flexible, score-based validation of multiple LLM-generated `solve()`
functions for a given GSM8K problem. Instead of a rigid pass/fail filter, this
script analyzes all pairs of models to find the most robust and comprehensive
consensus.

The final output is a confidence score (0.0-1.0+) that reflects:
1.  **Completeness:** The proportion of arguments that were successfully aligned
    between models (the Alignment Ratio).
2.  **Clarity:** The semantic similarity of the aligned argument names and
    comments (the Semantic Strength).
3.  **Consensus:** The number of models that are all mutually, functionally
    equivalent, with a bonus applied for larger consensus groups ("cliques").

Core Logic:
-----------
1.  **Parse & Pre-filter (UT-1):** All generated Python files for a problem are
    parsed using a robust, regex-based approach. The list is then filtered,
    keeping only files that produce the correct answer for the default values.

2.  **Pairwise Alignment (UT-2):** For every pair of surviving models, the script
    finds the best possible argument alignment. It uses an efficient "bucket and
    match" strategy, first grouping arguments by type and default value (these groups are the "buckets"), then
    performing a semantic comparison on the combined text of the argument name
    and its comment.

3.  **Pairwise Fuzzing (UT-3):** Each successfully aligned pair is fuzz-tested
    for functional equivalence using the "Fuzz Aligned, Freeze Unaligned"
    strategy. That is, the aligned args are fuzzed (with 50 different values) and the unaligned args are frozen. 
    This robustly verifies that the underlying mathematical logic is
    identical, even when function signatures do not perfectly match.

4.  **Scoring & Consensus:**
    - Each functionally equivalent pair receives a `PairwiseQualityScore` based
      on its Alignment Ratio and Semantic Strength.
    - The script identifies the largest "clique" of models that are all
      mutually validated against each other.
    - A final `ConfidenceScore` is computed from the clique's average quality,
      boosted by a bonus for the size of the consensus.

Dependencies
------------
black                – whitespace-stable formatting
hypothesis           – property-based fuzzing
sentence-transformers (mpnet-base) – SBERT cosine for comment semantics
numpy                - for fast vector operations
"""

from __future__ import annotations

# --- (inside gsm8k_validator.py) ---

import importlib.util
import inspect
import itertools
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Any, Tuple, Dict

import black
import hypothesis.strategies as st
import libcst as cst  # <--- ADD THIS LINE
import numpy as np
from hypothesis import given, settings, HealthCheck
from sentence_transformers import SentenceTransformer

import pprint

from collections import defaultdict


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
print(f"Project root identified: {PROJECT_ROOT}")
BASE_OUTPUT_DIR = PROJECT_ROOT / 'data' / 'code_gen_outputs_cleaned'

_MODEL = SentenceTransformer("all-mpnet-base-v2")
_COS_THRESHOLD = 0.70  # SBERT cosine ≥ 0.7 ⇒ semantic match
_FUZZ_EXAMPLES = 50  # Hypothesis draws
_MIN_ALIGNMENT_FOR_FUZZ = 1 # A pair must align on at least one arg to be fuzzed

# --- Scoring Weights --- #
W_ALIGNMENT = 0.7
W_SEMANTIC = 0.3

# --- Consensus Bonus Multipliers --- #
CONSENSUS_BONUS = {
    2: 1.0,  # Baseline for a pair
    3: 1.1,  # 10% bonus for a 3-way consensus
    4: 1.2,  # 20% bonus for a 4-way consensus
    5: 1.3,
}

_TRACE_RE = re.compile(r"^#: L(\d+)\b")
_DOC_INDEX_RE = re.compile(r"^Index:\s*(\d+)")


# ---------------------------------------------------------------------- #
#  Dataclasses for Structured Data
# ---------------------------------------------------------------------- #

@dataclass(frozen=True)
class Argument:
    """Represents a single argument from a function signature."""
    name: str
    arg_type: str  # <--- ADD THIS LINE
    default: Any
    comment: str


@dataclass(frozen=True)
class ParsedFile:
    """Normalised representation of a generated code file."""
    path: Path
    module_code: str
    func: Any
    args: List[Argument] = field(default_factory=list)


@dataclass(frozen=True)
class AlignmentResult:
    """Stores the result of aligning two ParsedFiles."""
    aligned_pairs: List[Tuple[Argument, Argument]]
    unaligned_A: List[Argument]
    unaligned_B: List[Argument]
    semantic_scores: List[float]


@dataclass
class PairwiseValidation:
    """Stores the full result of a successful pairwise validation."""
    file_A: ParsedFile
    file_B: ParsedFile
    alignment: AlignmentResult
    quality_score: float


# ---------------------------------------------------------------------- #
#  Core Logic Implementation
# ---------------------------------------------------------------------- #

# In your validator script, find and replace the parse_file function

def parse_file(path: Path) -> ParsedFile | None:
    """
    Parse one generated .py file into a structured ParsedFile object using
    a direct, regex-based approach.
    """
    try:
        src_raw = path.read_text(encoding="utf-8")
        src_fmt = black.format_str(src_raw, mode=black.FileMode())

        signature_match = re.search(r"def solve\s*\((.*?)\):", src_fmt, re.DOTALL)
        if not signature_match:
            raise ValueError("Could not find a 'def solve(...):' signature.")
        
        signature_content = signature_match.group(1)

        args = []
        # --- MODIFIED REGEX: Now captures the type hint in group(2) ---
        arg_pattern = re.compile(
            r"^\s*([a-zA-Z_]\w*)\s*:\s*(\w+)\s*=\s*(.*?)\s*,?\s*(?:#\s*(.*))?$"
        )

        for line in signature_content.splitlines():
            if not line.strip(): continue
            match = arg_pattern.match(line)
            if match:
                name = match.group(1)
                arg_type = match.group(2) # <--- CAPTURE TYPE
                default_str = match.group(3).strip()
                default_val = eval(default_str)
                comment = match.group(4).strip() if match.group(4) else ""
                
                args.append(Argument(
                    name=name,
                    arg_type=arg_type, # <--- STORE TYPE
                    default=default_val,
                    comment=comment
                ))

        spec = importlib.util.spec_from_loader(f"gsm8k_{path.stem}_{hash(path)}", loader=None)
        mod_dyn = importlib.util.module_from_spec(spec)
        exec(src_fmt, mod_dyn.__dict__)

        return ParsedFile(
            path=path,
            module_code=src_fmt,
            func=mod_dyn.solve,
            args=args
        )
    except (FileNotFoundError, StopIteration, SyntaxError, Exception) as e:
        print(f"[Parser Error] Skipping {path.name}: {e!r}", file=sys.stderr)
        return None


def ut1_answer_match(files: List[ParsedFile], gold: float) -> List[ParsedFile]:
    """Keep only files whose solve() returns the official answer with default args."""
    ok_files = []
    for pf in files:
        try:
            if np.isclose(pf.func(), gold):
                ok_files.append(pf)
        except Exception as e:
            print(f"[UT-1 Fail] {pf.path.name} raised {e!r}", file=sys.stderr)
    return ok_files

def find_best_alignment(file_A: ParsedFile, file_B: ParsedFile) -> AlignmentResult:
    """
    Finds the best argument alignment using a 'bucket and match' strategy.
    1. Groups args from each file into buckets by (type, default_value).
    2. Only performs semantic comparison on args within matching buckets.
    """
    # --- 1. Create buckets for each file's arguments ---
    buckets_A = defaultdict(list)
    for arg in file_A.args:
        buckets_A[(arg.arg_type, arg.default)].append(arg)
        
    buckets_B = defaultdict(list)
    for arg in file_B.args:
        buckets_B[(arg.arg_type, arg.default)].append(arg)

    aligned_pairs = []
    semantic_scores = []
    
    # --- 2. Iterate through buckets that exist in BOTH files ---
    common_keys = set(buckets_A.keys()) & set(buckets_B.keys())
    
    for key in common_keys:
        args_in_bucket_A = buckets_A[key]
        args_in_bucket_B = buckets_B[key]
        
        # --- 3. Perform semantic alignment ONLY within the current bucket ---
        texts_A = [arg.name.replace("_", " ") + " | " + arg.comment for arg in args_in_bucket_A]
        texts_B = [arg.name.replace("_", " ") + " | " + arg.comment for arg in args_in_bucket_B]
        
        embeddings_A = _MODEL.encode(texts_A, normalize_embeddings=True)
        embeddings_B = _MODEL.encode(texts_B, normalize_embeddings=True)
        similarity_matrix = embeddings_A @ embeddings_B.T

        # Use a greedy matching strategy within the bucket
        sorted_indices = np.argsort(similarity_matrix, axis=None)[::-1]
        flat_indices = np.atleast_1d(sorted_indices)
        rows, cols = np.unravel_index(flat_indices, similarity_matrix.shape)

        used_in_bucket_A = set()
        used_in_bucket_B = set()

        for i, j in zip(rows, cols):
            if i in used_in_bucket_A or j in used_in_bucket_B:
                continue

            similarity_score = similarity_matrix[i, j]
            if similarity_score >= _COS_THRESHOLD:
                aligned_pairs.append((args_in_bucket_A[i], args_in_bucket_B[j]))
                semantic_scores.append(similarity_score)
                used_in_bucket_A.add(i)
                used_in_bucket_B.add(j)

    # --- 4. Calculate the final unaligned sets ---
    final_aligned_A = {p[0] for p in aligned_pairs}
    final_aligned_B = {p[1] for p in aligned_pairs}
    unaligned_A = [arg for arg in file_A.args if arg not in final_aligned_A]
    unaligned_B = [arg for arg in file_B.args if arg not in final_aligned_B]

    return AlignmentResult(aligned_pairs, unaligned_A, unaligned_B, semantic_scores)


def fuzz_aligned_pair(alignment: AlignmentResult, func_A: callable, func_B: callable) -> bool:
    """Fuzz-test an aligned pair using the 'Fuzz Aligned, Freeze Unaligned' strategy."""
    if len(alignment.aligned_pairs) < _MIN_ALIGNMENT_FOR_FUZZ:
        return False

    strat_map = {}
    for i, (arg_A, _) in enumerate(alignment.aligned_pairs):
        literal = arg_A.default
        strat = st.floats if isinstance(literal, float) else st.integers
        strat_map[f"pair_{i}"] = strat(min_value=1, max_value=50)

    # Freeze unaligned args to their defaults
    frozen_kwargs_A = {arg.name: arg.default for arg in alignment.unaligned_A}
    frozen_kwargs_B = {arg.name: arg.default for arg in alignment.unaligned_B}

    @settings(max_examples=_FUZZ_EXAMPLES, deadline=None, suppress_health_check=[HealthCheck.too_slow])
    @given(st.fixed_dictionaries(strat_map))
    def _check(fuzzed_values):
        kwargs_A = frozen_kwargs_A.copy()
        kwargs_B = frozen_kwargs_B.copy()

        for i, (arg_A, arg_B) in enumerate(alignment.aligned_pairs):
            fuzzed_val = fuzzed_values[f"pair_{i}"]
            kwargs_A[arg_A.name] = fuzzed_val
            kwargs_B[arg_B.name] = fuzzed_val

        assert np.isclose(func_A(**kwargs_A), func_B(**kwargs_B))

    try:
        _check()
        return True
    except Exception:
        return False


def calculate_pairwise_score(alignment: AlignmentResult, file_A: ParsedFile, file_B: ParsedFile) -> float:
    """Calculate the quality score for a single validated pair."""
    num_aligned = len(alignment.aligned_pairs)
    
    # --- MODIFIED: A more robust Alignment Ratio calculation ---
    total_unique_args = num_aligned + len(alignment.unaligned_A) + len(alignment.unaligned_B)
    alignment_ratio = num_aligned / total_unique_args if total_unique_args > 0 else 1.0

    # Semantic Strength (no change needed here)
    semantic_strength = np.mean(alignment.semantic_scores) if alignment.semantic_scores else 1.0

    return (W_ALIGNMENT * alignment_ratio) + (W_SEMANTIC * semantic_strength)


# ---------------------------------------------------------------------- #
#  Orchestration and Reporting
# ---------------------------------------------------------------------- #

def analyze_problem_outputs(problem_dir: Path, gold_answer: float):
    """Main orchestrator to analyze all model outputs for a single problem."""
    print(f"\n{'='*20} Analyzing Problem: {problem_dir.name} {'='*20}")
    
    all_files = list(problem_dir.glob("*.py"))
    if not all_files:
        print("No Python files found in this directory.")
        return

    parsed_files = [pf for pf in [parse_file(p) for p in all_files] if pf is not None]
    print(f"Found and parsed {len(parsed_files)} files.")

    survivors_ut1 = ut1_answer_match(parsed_files, gold_answer)
    print(f"{len(survivors_ut1)} files passed UT-1 (correct default answer).")
    if len(survivors_ut1) < 2:
        print("Not enough models passed UT-1 to find a pair. Aborting.")
        return

    # --- Pairwise Validation ---
    validated_pairs: List[PairwiseValidation] = []
    for file_A, file_B in itertools.combinations(survivors_ut1, 2):
        alignment = find_best_alignment(file_A, file_B)
        
        if fuzz_aligned_pair(alignment, file_A.func, file_B.func):
            score = calculate_pairwise_score(alignment, file_A, file_B)
            validated_pairs.append(PairwiseValidation(file_A, file_B, alignment, score))
            print(f"  ✓ Validated Pair: ({file_A.path.name}, {file_B.path.name}), Score: {score:.3f}")

    if not validated_pairs:
        print("\nNo functionally equivalent pairs found after fuzzing.")
        return

    # --- Find Best Consensus Clique ---
    nodes = survivors_ut1
    adj = {pf.path.name: set() for pf in nodes}
    for vp in validated_pairs:
        adj[vp.file_A.path.name].add(vp.file_B.path.name)
        adj[vp.file_B.path.name].add(vp.file_A.path.name)

    best_clique_names = []
    # Check for cliques of decreasing size
    for size in range(len(nodes), 1, -1):
        # Use a list of names for combinations, not the ParsedFile objects
        node_names = [pf.path.name for pf in nodes]
        for combo_names in itertools.combinations(node_names, size):
            is_clique = all(
                combo_names[j] in adj[combo_names[i]] for i in range(size) for j in range(i + 1, size)
            )
            if is_clique:
                best_clique_names = list(combo_names)
                break
        if best_clique_names:
            break
    
    # --- Calculate Final Score and Report ---
    # This block now correctly handles the case where no clique is found
    if not best_clique_names and validated_pairs:
        # If no clique > 2 found, find the single best pair
        print("\nNo consensus clique found. Reporting score for the single best pair.")
        best_pair = max(validated_pairs, key=lambda vp: vp.quality_score)
        final_score = best_pair.quality_score
        clique_size = 2
        best_clique_names = sorted([best_pair.file_A.path.name, best_pair.file_B.path.name])
        avg_quality = final_score
        bonus = CONSENSUS_BONUS.get(clique_size, 1.0)
    elif best_clique_names:
        # A clique was found
        clique_size = len(best_clique_names)
        clique_pairs_scores = [
            vp.quality_score for vp in validated_pairs 
            if vp.file_A.path.name in best_clique_names and vp.file_B.path.name in best_clique_names
        ]
        avg_quality = np.mean(clique_pairs_scores) if clique_pairs_scores else 0
        bonus = CONSENSUS_BONUS.get(clique_size, max(CONSENSUS_BONUS.values()))
        final_score = avg_quality * bonus
    else:
        # This case handles when there are no validated pairs at all
        clique_size = 0
        avg_quality = 0
        bonus = 0
        final_score = 0

    print("\n" + "-"*50)
    print("                 VALIDATION SUMMARY")
    print("-"*50)
    print(f"Best Consensus Found: {clique_size}-way agreement")
    if best_clique_names:
        print(f"Models in Best Clique:")
        for name in sorted(best_clique_names):
            print(f"  - {name}")
    else:
        print("Models in Best Clique: None")

    print(f"\nAverage Pairwise Quality in Clique: {avg_quality:.4f}")
    print(f"Consensus Bonus Multiplier: x{bonus}")
    print(f"FINAL CONFIDENCE SCORE: {final_score:.4f}")
    print("-"*50)


###########################

from datasets import load_dataset

# Load the GSM8K dataset (train split)
gsm8k_train = load_dataset("gsm8k", "main", split="train")

def extract_gsm8k_answer(gsm8k_data, index):
    """
    Extracts the final numerical answer from a GSM8K sample.
    Args:
        gsm8k_data: The loaded GSM8K dataset (e.g., gsm8k_train).
        index: The integer index of the sample.
    Returns:
        The answer as a float if possible, else as a string.
    """
    answer_text = gsm8k_data[index]['answer']
    # The answer is after the last '####'
    if '####' in answer_text:
        answer = answer_text.split('####')[-1].strip()
    else:
        answer = answer_text.strip()
    # Try to convert to float or int
    try:
        return float(answer.replace(',', ''))
    except ValueError:
        return answer
    

# --- Execute the Full Pipeline for samples 0-99 ---

for PROBLEM_INDEX in range(100):
    GOLD_ANSWER = extract_gsm8k_answer(gsm8k_train, PROBLEM_INDEX)
    print(f"\nProcessing Problem Index: {PROBLEM_INDEX}, Gold Answer: {GOLD_ANSWER}")

    problem_dir = BASE_OUTPUT_DIR / str(PROBLEM_INDEX)
    if not problem_dir.is_dir():
        print(f"Error: Directory not found at {problem_dir}")
    else:
        # This single function call runs the entire validation and scoring process
        analyze_problem_outputs(problem_dir, GOLD_ANSWER)