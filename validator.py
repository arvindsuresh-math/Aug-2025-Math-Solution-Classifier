"""
validator.py  –  rigorous cross-validation of GSM8K code formalisations
"""
from __future__ import annotations

import hashlib
import inspect
import io
import json
import re
import tokenize
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

import black
import hypothesis.strategies as st
import libcst as cst
import sympy as sp
from hypothesis import given, settings
from sentence_transformers import SentenceTransformer

# ────────────────────────────────────────────────────────────────────────────────
#  0. global helpers
# ────────────────────────────────────────────────────────────────────────────────
MODEL = SentenceTransformer("all-mpnet-base-v2")
SHA1 = lambda s: hashlib.sha1(s.encode()).hexdigest()[:8]

# ────────────────────────────────────────────────────────────────────────────────
#  1. dataclass to hold the canonical form
# ────────────────────────────────────────────────────────────────────────────────
@dataclass
class CanonicalProgram:
    index: str  # GSM8K question id
    module: cst.Module  # canonical CST
    arg_names: List[str]  # canonicalised parameter names (ordered)
    comments: List[str]  # cleaned English comments (parallel to step_nodes)
    step_nodes: List[cst.CSTNode]  # one node per computation step
    annotations_ok: bool  # all <<…>> annotations numerically correct

    def to_code(self) -> str:
        return self.module.code


# ────────────────────────────────────────────────────────────────────────────────
#  2. stage-wise functions
# ────────────────────────────────────────────────────────────────────────────────
def _extract_index(docstring: str) -> str:
    first_line = docstring.splitlines()[0]
    m = re.match(r"Q(\d+)", first_line.strip())
    if not m:
        raise ValueError("Doc-string must start with something like 'Q1234'")
    return m.group(1)


def _canonical_key(comment: str) -> str:
    txt = re.sub(r"\d+", "", comment.lower())
    return "arg_" + SHA1(txt)


class Canonicaliser(cst.CSTTransformer):
    """
    - Renames parameters & their uses to canonical keys
    - Harvests comments and calculator annotations
    """

    def __init__(self):
        self.param_map: Dict[str, str] = {}
        self.comments: List[str] = []
        self.step_nodes: List[cst.CSTNode] = []
        self.annotations_ok = True

    # argument names in the function signature
    def leave_Param(self, orig: cst.Param, updated: cst.Param) -> cst.Param:
        comment = _trailing_comment(orig)
        key = _canonical_key(comment or orig.name.value)
        self.param_map[orig.name.value] = key
        return updated.with_changes(name=updated.name.with_changes(value=key))

    # rename identifiers throughout body
    def leave_Name(self, orig: cst.Name, updated: cst.Name) -> cst.Name:
        if orig.value in self.param_map:
            return updated.with_changes(value=self.param_map[orig.value])
        return updated

    # harvest preceding inline comment & validate calculator annotation
    def leave_AnnAssign(
        self, orig: cst.AnnAssign, updated: cst.AnnAssign
    ) -> cst.AnnAssign:
        _handle_assignment(self, orig, updated)
        return updated

    def leave_Assign(self, orig: cst.Assign, updated: cst.Assign) -> cst.Assign:
        _handle_assignment(self, orig, updated)
        return updated


def _trailing_comment(node: cst.CSTNode) -> str | None:
    if node.trailing_whitespace.comment:
        return node.trailing_whitespace.comment.value.lstrip("# ").strip()
    return None


def _parse_calc_annotation(text: str) -> Tuple[str, str] | None:
    m = re.search(r"<<([^=]+)=([^>]+)>>", text)
    return m.groups() if m else None


def _handle_assignment(
    canon: Canonicaliser, orig: cst.CSTNode, updated: cst.CSTNode
) -> None:
    cmt = _trailing_comment(orig) or ""
    calc = _parse_calc_annotation(cmt)
    if calc:
        expr_src, value_src = calc
        try:
            value_expr = sp.sympify(expr_src)
            if sp.N(value_expr) != sp.sympify(value_src):
                canon.annotations_ok = False
        except Exception:
            canon.annotations_ok = False
        # strip annotation for embedding
        cmt = re.sub(r"<<.*?>>", "", cmt).strip()

    if cmt:
        canon.comments.append(cmt)
        canon.step_nodes.append(updated)
    # else: we silently allow comment-less assignments (rare)


def canonicalise_file(path: Path) -> CanonicalProgram:
    code = path.read_text()
    # 1. reformat via black for baseline equivalence
    code_fmt = black.format_str(code, mode=black.FileMode())

    # 2. parse
    mod = cst.parse_module(code_fmt)
    docstring = inspect.getdoc(compile(code_fmt, str(path), "exec"))

    # 3. build transformer
    can = Canonicaliser()
    new_mod = mod.visit(can)

    # 4. exact rational literals (fractions) could be added here

    index = _extract_index(docstring or "")
    return CanonicalProgram(
        index=index,
        module=new_mod,
        arg_names=list(can.param_map.values()),
        comments=can.comments,
        step_nodes=can.step_nodes,
        annotations_ok=can.annotations_ok,
    )


# ────────────────────────────────────────────────────────────────────────────────
#  3. comment-based alignment & symbolic equivalence
# ────────────────────────────────────────────────────────────────────────────────
def _embed(sentences: List[str]):
    return MODEL.encode(sentences, normalize_embeddings=True)


def align_steps(prog_a: CanonicalProgram, prog_b: CanonicalProgram) -> List[Tuple[int, int]]:
    """Return list of index pairs (i, j) mapping step i in A to step j in B"""
    emb_a = _embed(prog_a.comments)
    emb_b = _embed(prog_b.comments)
    sim = emb_a @ emb_b.T  # cosine similarity
    mapping: List[Tuple[int, int]] = []
    used_b = set()
    for i, row in enumerate(sim):
        j = int(row.argmax())
        if j not in used_b and row[j] > 0.8:
            mapping.append((i, j))
            used_b.add(j)
    return mapping


def symbolic_equivalent(lhs_src: str, rhs_src: str, arg_names: List[str]) -> bool:
    syms = sp.symbols(arg_names)
    env = {name: sym for name, sym in zip(arg_names, syms)}
    try:
        lhs = sp.sympify(lhs_src, env)
        rhs = sp.sympify(rhs_src, env)
        return sp.simplify(lhs - rhs) == 0
    except Exception:
        return False


def check_symbolic(prog_a: CanonicalProgram, prog_b: CanonicalProgram) -> bool:
    mapping = align_steps(prog_a, prog_b)
    for ia, ib in mapping:
        node_a = prog_a.step_nodes[ia]
        node_b = prog_b.step_nodes[ib]
        if isinstance(node_a, cst.BaseAssign) and isinstance(node_b, cst.BaseAssign):
            # naive: compare entire statement source
            if not symbolic_equivalent(node_a.code, node_b.code, prog_a.arg_names):
                return False
        else:
            return False
    return True


# ────────────────────────────────────────────────────────────────────────────────
#  4. fuzzing equivalence with Hypothesis
# ────────────────────────────────────────────────────────────────────────────────
def _import_module_from_code(code: str, name: str):
    import importlib.util
    spec = importlib.util.spec_from_loader(name, loader=None)
    mod = importlib.util.module_from_spec(spec)
    exec(code, mod.__dict__)
    return mod


def _build_strategy(arg_names: List[str]):
    strat_map = {a: st.integers(min_value=1, max_value=20) for a in arg_names}
    return st.fixed_dictionaries(strat_map)


def run_fuzz_equivalence(prog_a: CanonicalProgram, prog_b: CanonicalProgram, n_examples=50):
    mod_a = _import_module_from_code(prog_a.to_code(), "prog_a")
    mod_b = _import_module_from_code(prog_b.to_code(), "prog_b")

    strat = _build_strategy(prog_a.arg_names)

    @settings(max_examples=n_examples, deadline=None)
    @given(args=strat)
    def _check(args):
        assert prog_a.arg_names == prog_b.arg_names  # same arg ordering
        out_a = mod_a.solve(**args)
        out_b = mod_b.solve(**args)
        assert out_a == out_b

    _check()


# ────────────────────────────────────────────────────────────────────────────────
#  5. high-level orchestration
# ────────────────────────────────────────────────────────────────────────────────
def validate_group(paths: List[Path]) -> None:
    """Run all checks on a *set* of files that claim to solve the SAME GSM8K item"""
    progs = [canonicalise_file(p) for p in paths]
    indices = {p.index for p in progs}
    assert len(indices) == 1, f"Mixed GSM8K indices: {indices}"

    # 1) internal annotation check
    for p in progs:
        if not p.annotations_ok:
            raise ValueError(f"{p} fails calculator-annotation integrity")

    # 2) pairwise symbolic + fuzz tests
    for i in range(len(progs)):
        for j in range(i + 1, len(progs)):
            pa, pb = progs[i], progs[j]
            if not check_symbolic(pa, pb):
                raise ValueError(f"symbolic mismatch between {paths[i]} & {paths[j]}")
            run_fuzz_equivalence(pa, pb)  # raises on failure

    print(f"✓ All {len(progs)} variants for Q{progs[0].index} are consistent")


# ────────────────────────────────────────────────────────────────────────────────
#  6. command-line entry point
# ────────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(description="Validate GSM8K code variants")
    ap.add_argument("files", nargs="+", type=Path, help="paths to .py files of the same item")
    args = ap.parse_args()
    validate_group(args.files)