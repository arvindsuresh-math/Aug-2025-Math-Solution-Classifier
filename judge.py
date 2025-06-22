# judge.py
"""
Judge functions for the synthetic 2×2-system dataset.

Responsibilities
----------------
1.  Parse the student’s final line `Answer: (x, y) = (...)`.
2.  Verify that tuple against:
      • the canonical truth             (solve_linear_2x2)
      • the deterministic wrong answer  (ERROR_TEMPLATES[template])
3.  Return a structured verdict so the data-gen script can decide
   whether to keep or reject the sample.

Future-proofing
---------------
If you later want a “reasoning-style” check (e.g. second LLM that reviews the
explanation text) just add another field in the Verdict dataclass — the
surface API won’t change.
"""
from __future__ import annotations

import re
import json
from dataclasses import dataclass
from typing import Tuple, Dict, Any, Optional

import sympy as sp

import linear_system_templates as lst  # <— the Step-1 module


# ---------------------------------------------------------------------
# 1.  Regex to grab (x, y)
# ---------------------------------------------------------------------
_ANSWER_RE = re.compile(
    r"Answer:\s*\(\s*([^\s,()]+)\s*,\s*([^\s,()]+)\s*\)",
    flags=re.I,
)


def _parse_final_xy(text: str) -> Optional[Tuple[sp.Rational, sp.Rational]]:
    """
    Return (x, y) as SymPy Rationals or None if the pattern isn't found / unparsable.
    """
    m = _ANSWER_RE.search(text)
    if not m:
        return None
    x_str, y_str = m.groups()
    try:
        return sp.Rational(x_str), sp.Rational(y_str)
    except (ValueError, sp.SympifyError):
        return None


# ---------------------------------------------------------------------
# 2.  Verdict object
# ---------------------------------------------------------------------
@dataclass
class Verdict:
    ok: bool
    reason: str  # "ok", "parse_fail", "truth_mismatch", "wrong_mismatch", "collides_truth"

    @property
    def is_reject(self) -> bool:
        return not self.ok

    def to_json(self) -> str:
        return json.dumps(self.__dict__)


# ---------------------------------------------------------------------
# 3.  Public judging API
# ---------------------------------------------------------------------
def judge_sample(record: Dict[str, Any]) -> Verdict:
    """
    Parameters
    ----------
    record
        A single JSONL row produced by the Writer.  Must contain:
        • coefficients  – list[int] length-6
        • template      – str  (key into ERROR_TEMPLATES)
        • answer_steps  – str  (raw model text)
        • final_xy      – list[str]  (optional; not used here)

    Returns
    -------
    Verdict
        ok = True   ➜ keep the sample
        ok = False  ➜ throw away + log reason
    """
    coeffs = tuple(record["coefficients"])
    template = record["template"]
    assistant_text = record["answer_steps"]

    parsed = _parse_final_xy(assistant_text)
    if parsed is None:
        return Verdict(False, "parse_fail")

    # Ground-truth tuples
    truth_x, truth_y = lst.solve_linear_2x2(*coeffs)
    expected_wrong_x, expected_wrong_y = lst.ERROR_TEMPLATES[template](*coeffs)

    if template.upper() == "CORRECT":
        return Verdict(parsed == (truth_x, truth_y), "truth_mismatch" if parsed != (truth_x, truth_y) else "ok")

    # Any template other than CORRECT
    if parsed == (truth_x, truth_y):
        return Verdict(False, "collides_truth")
    if parsed != (expected_wrong_x, expected_wrong_y):
        return Verdict(False, "wrong_mismatch")

    return Verdict(True, "ok")
