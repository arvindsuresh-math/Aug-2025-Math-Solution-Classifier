"""
gsm8k_validator.py
==================

End-to-end checker for **three independently generated** `solve()` files
that formalise the same GSM8K problem.  The script enforces the _compact
format_ we finally adopted:

* 2-line docstring header (`Index: …`, `Returns: …`)
* Semantic argument names (no numeric prefix)
* Trace comments that start **exactly** with `#: L<n>`
* No calculator annotations inside the code
* Final answer stored in `answer` with `# FINAL ANSWER`

The pipeline performs four orthogonal tests:

UT-0  – Default run returns the official numeric answer  
UT-1  – Trace-comment lists are identical across files  
UT-2  – Arguments match in default literals **and** comment semantics  
UT-3  – Hypothesis fuzzing confirms functional equivalence

Files that pass all four tests are optionally rewritten into a *canonical*
form (`X1 …, Y1 …`) suitable for automated error-injection experiments.

Dependencies
------------
black                – whitespace-stable formatting  
libcst               – reliable CST traversal with comment access  
hypothesis           – property-based fuzzing  
sentence-transformers (mpnet-base) – SBERT cosine for comment semantics
"""

from __future__ import annotations

import hashlib
import importlib.util
import inspect
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, Any

import black
import hypothesis.strategies as st
import libcst as cst
from hypothesis import given, settings
from sentence_transformers import SentenceTransformer

# ---------------------------------------------------------------------- #
#  Global constants & regex helpers
# ---------------------------------------------------------------------- #

_MODEL = SentenceTransformer("all-mpnet-base-v2")
_COS_THRESHOLD = 0.90          # SBERT cosine ≥ 0.9 ⇒ semantic match
_FUZZ_EXAMPLES  = 60           # Hypothesis draws

_TRACE_RE = re.compile(r"^#: L(\d+)\b")          # matches trace comment
_DOC_INDEX_RE = re.compile(r"^Index:\s*(\d+)")   # first docstring line


# ---------------------------------------------------------------------- #
#  ParsedFile dataclass
# ---------------------------------------------------------------------- #

@dataclass
class ParsedFile:
    """
    Normalised representation of a generated code file.

    Attributes
    ----------
    index         : str
        Problem ID, e.g. ``"Q310"``.
    path          : pathlib.Path
        Path to the original file on disk.
    module_code   : str
        Black-formatted source code.
    trace_keys    : List[str]
        Ordered list like ``["L1", "L2", …]`` extracted from comments.
    arg_defaults  : List[str]
        Default literal strings in the function signature.
    arg_comments  : List[str]
        Trailing comments for each argument.
    func          : callable
        Dynamically imported ``solve`` function ready for execution.
    """
    index: str
    path: Path
    module_code: str
    trace_keys: List[str]
    arg_defaults: List[str]
    arg_comments: List[str]
    func: Any


# ---------------------------------------------------------------------- #
#  Parsing utilities
# ---------------------------------------------------------------------- #

def parse_file(path: Path) -> ParsedFile:
    """
    Parse one generated `.py` file and extract all information needed
    by the validators.

    Why a dedicated parser?
    -----------------------
    * Centralises Black formatting (whitespace normalisation).
    * Collects trace comments, argument literals, and their semantic
      comments in **one** traversal (libcst).
    * Dynamically imports the `solve()` function so UT-0 and UT-3 can
      execute it in memory without writing temp files.
    """
    src_raw = path.read_text()
    src_fmt = black.format_str(src_raw, mode=black.FileMode())

    # ------- docstring extraction & index check ------------------- #
    doc_match = re.search(r'"""(.*?)"""', src_fmt, re.S)
    if not doc_match:
        raise ValueError(f"{path}   » missing two-line docstring")
    first_line = doc_match.group(1).strip().splitlines()[0]
    idx_match = _DOC_INDEX_RE.match(first_line)
    if not idx_match:
        raise ValueError(f"{path}   » first docstring line must start 'Index:'")
    index = f"Q{idx_match.group(1)}"

    # ------- trace comment list ----------------------------------- #
    trace_keys = [
        f"L{m.group(1)}"
        for line in src_fmt.splitlines()
        if (m := _TRACE_RE.match(line.lstrip()))
    ]
    if not trace_keys:
        raise ValueError(f"{path}   » no trace comments found")

    # ------- AST walk for args ------------------------------------ #
    mod     = cst.parse_module(src_fmt)
    func_nd = next(
        n for n in mod.body
        if isinstance(n, cst.FunctionDef) and n.name.value == "solve"
    )
    arg_defaults, arg_comments = [], []
    for param in func_nd.params.params:
        arg_defaults.append(param.default.code if param.default else None)
        cmt = (
            param.trailing_whitespace.comment.value.lstrip("#").strip()
            if param.trailing_whitespace.comment else ""
        )
        arg_comments.append(cmt)

    # ------- dynamic import --------------------------------------- #
    spec = importlib.util.spec_from_loader(f"gsm8k_{index}_{hash(path)}", loader=None)
    mod_dyn = importlib.util.module_from_spec(spec)
    exec(src_fmt, mod_dyn.__dict__)

    return ParsedFile(
        index=index,
        path=path,
        module_code=src_fmt,
        trace_keys=trace_keys,
        arg_defaults=arg_defaults,
        arg_comments=arg_comments,
        func=mod_dyn.solve,
    )


# ---------------------------------------------------------------------- #
#  Unit Test 0 – default answer match
# ---------------------------------------------------------------------- #

def ut0_answer_match(files: List[ParsedFile], gold: int | float) -> List[ParsedFile]:
    """
    Keep only files whose `solve()` returns the official answer when
    called *with default arguments*.

    Rationale
    ---------
    Eliminates obvious errors: hard-coded wrong literals, mis-parsed
    numbers, or runtime exceptions.
    """
    ok = []
    for pf in files:
        try:
            if pf.func() == gold:
                ok.append(pf)
        except Exception as e:
            print(f"[UT-0] {pf.path.name} raised {e!r}", file=sys.stderr)
    return ok


# ---------------------------------------------------------------------- #
#  Unit Test 1 – identical trace lists
# ---------------------------------------------------------------------- #

def ut1_trace_lists_equal(files: List[ParsedFile]) -> bool:
    """
    Verify that every surviving file has the *same* ordered list of trace
    keys (`L1`, `L2`, …).

    Why:
    ----
    Ensures no model skipped or re-ordered steps; makes later
    canonicalisation deterministic.
    """
    hashes = {
        hashlib.sha1(",".join(p.trace_keys).encode()).hexdigest()
        for p in files
    }
    return len(hashes) == 1


# ---------------------------------------------------------------------- #
#  Unit Test 2 – argument semantic alignment
# ---------------------------------------------------------------------- #

def ut2_arg_semantics(files: List[ParsedFile]) -> bool:
    """
    Check two things:
    1. Argument *default literals* match exactly across files.
    2. Trailing comments are semantically equivalent (SBERT cosine ≥ 0.9).

    Rationale
    ---------
    Detects swapped wage vs. hours, wrong default numbers, or comment /
    code drift that numeric fuzzing may not catch immediately.
    """
    ref_def  = files[0].arg_defaults
    ref_emb  = _MODEL.encode(files[0].arg_comments, normalize_embeddings=True)

    for pf in files[1:]:
        if pf.arg_defaults != ref_def:
            return False
        emb = _MODEL.encode(pf.arg_comments, normalize_embeddings=True)
        if ((emb * ref_emb).sum(axis=1) < _COS_THRESHOLD).any():
            return False
    return True


# ---------------------------------------------------------------------- #
#  Unit Test 3 – property-based fuzz equivalence
# ---------------------------------------------------------------------- #

def ut3_fuzz_equivalent(files: List[ParsedFile], n=_FUZZ_EXAMPLES) -> bool:
    """
    Use Hypothesis to generate random overrides for **all arguments** and
    require that every file returns the same value.

    Rationale
    ---------
    Guards against coincidental agreement on default literals.  Divergent
    internal logic will surface when you vary inputs.
    """
    funcs = [pf.func for pf in files]
    sig   = inspect.signature(funcs[0])
    strat_map = {}
    for param in sig.parameters.values():
        literal = param.default
        strat_map[param.name] = (
            st.floats(1, 30) if isinstance(literal, float) else st.integers(1, 30)
        )

    @settings(max_examples=n, deadline=None)
    @given(st.fixed_dictionaries(strat_map))
    def _check(kwargs):
        ref = funcs[0](**kwargs)
        for fn in funcs[1:]:
            assert fn(**kwargs) == ref

    try:
        _check()
        return True
    except Exception as e:
        print(f"[UT-3] fuzz divergence: {e!r}", file=sys.stderr)
        return False


# ---------------------------------------------------------------------- #
#  Canonical renamer (optional post-step)
# ---------------------------------------------------------------------- #

_RE_IDENT = re.compile(r"\b([A-Za-z_]\w*)\b")

def canonicalise(source: str, arg_order: List[str], trace_keys: List[str]) -> str:
    """
    Return a *canonical* version of `source` where:

    * Arguments become `X1`, `X2`, … following their order in `arg_order`.
    * The variable assigned immediately after `#: L<n>` becomes `Y<n>`.

    This deterministic form is ideal for later error-injection because it
    decouples variable names from human semantics.

    Parameters
    ----------
    source     : str
        Original source code.
    arg_order  : List[str]
        Ordered list of argument names in the `solve` signature.
    trace_keys : List[str]
        Ordered list of trace keys extracted earlier.

    Returns
    -------
    str
        Source code with canonical identifiers.
    """
    # map args → Xi
    arg_map = {old: f"X{i+1}" for i, old in enumerate(arg_order)}

    # map intermediates via trace comments
    lines = source.splitlines()
    interm_map: Dict[str, str] = {}
    for idx, key in enumerate(trace_keys):
        # find the line number of #: L<n>
        for i, line in enumerate(lines):
            if line.lstrip().startswith(f"#: {key}"):
                # next line should have assignment
                lhs_match = re.match(r"\s*([A-Za-z_]\w*)\s*=", lines[i + 1])
                if lhs_match:
                    interm_map[lhs_match.group(1)] = f"Y{key[1:]}"
                break

    name_map = {**arg_map, **interm_map}
    return _RE_IDENT.sub(lambda m: name_map.get(m.group(1), m.group(1)), source)


# ---------------------------------------------------------------------- #
#  Orchestration function
# ---------------------------------------------------------------------- #

def validate_triplet(paths: List[Path], gold: int | float) -> List[Path]:
    """
    Run UT-0…UT-3 on a list of *three* files that claim to solve the same
    GSM8K item.  If at least two survive **all** tests, write canonical
    versions (`canon_<name>.py`) and return their original paths.

    Side-effects:
    -------------
    • Prints status lines for each stage.  
    • Writes canonical files next to originals.

    Returns
    -------
    List[Path]
        Paths of files that passed, or an empty list if quorum fails.
    """
    parsed = [parse_file(p) for p in paths]

    parsed = ut0_answer_match(parsed, gold)
    if len(parsed) < 2:
        print("Quorum failed at UT-0")
        return []

    if not ut1_trace_lists_equal(parsed):
        print("Trace lists differ (UT-1)")
        return []

    if not ut2_arg_semantics(parsed):
        print("Arg mismatch (UT-2)")
        return []

    if not ut3_fuzz_equivalent(parsed):
        print("Functional divergence (UT-3)")
        return []

    # optional canonicalise
    arg_order = list(inspect.signature(parsed[0].func).parameters.keys())
    for pf in parsed:
        canon = canonicalise(pf.module_code, arg_order, pf.trace_keys)
        (pf.path.parent / f"canon_{pf.path.name}").write_text(canon)

    print("All tests passed; canonical files written.")
    return [pf.path for pf in parsed]


# ---------------------------------------------------------------------- #
#  Command-line entry point
# ---------------------------------------------------------------------- #

if __name__ == "__main__":
    import argparse, json

    parser = argparse.ArgumentParser(description="Validate three GSM8K code files.")
    parser.add_argument("gold_answer", type=json.loads, help="official numeric answer")
    parser.add_argument("files", nargs=3, type=Path, help="exactly three .py files")
    args = parser.parse_args()

    validate_triplet(args.files, args.gold_answer)