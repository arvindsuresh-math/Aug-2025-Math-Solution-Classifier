"""
Module: linear_system_templates.py

Synthetic‑dataset scaffolding (Step 1)
====================================
This single file provides every building‑block needed to **generate and verify
2 × 2 linear‑system problems** for a grading‑model fine‑tuning corpus.

Key design contracts
--------------------
1. *Ground truth is deterministic* – the canonical solver (`solve_linear_2x2`) is
   frozen; downstream hashes will break if it changes.
2. *Each error template returns a unique tuple* – for **any** coefficient set we
   admit into the dataset, **no two templates produce the same answer** and
   none equal the truth.
3. *Never singular* – neither the original nor any template‑transformed system
   is allowed to be singular; templates raise `ValueError` early if that would
   happen so the sampler can redraw.
4. *Low collision probability on blind draws* – because we outright reject
   collisions during sampling, the empirical collision rate when you call
   `collision_rate()` should be ≈ 0 %.

Run `python linear_system_templates.py` and you should see:

```
✓ All smoke tests passed — templates diverge from truth, never singular,
  and collision rate ≈ 0 %.
```
"""

from __future__ import annotations

import random
from typing import Tuple

from sympy import Matrix
from sympy.matrices.common import NonInvertibleMatrixError

# -----------------------------------------------------------------------------
# 1. Canonical ground‑truth solver
# -----------------------------------------------------------------------------

def solve_linear_2x2(a: int, b: int, c: int, d: int, e: int, f: int) -> Tuple:
    """Return the exact solution `(x, y)` of the system:

        a·x + b·y = e
        c·x + d·y = f

    The implementation is *frozen* once the dataset is versioned.
    """
    M = Matrix([[a, b], [c, d]])
    rhs = Matrix([e, f])
    sol = M.LUsolve(rhs)
    return sol[0], sol[1]


# -----------------------------------------------------------------------------
# 2. Helpers
# -----------------------------------------------------------------------------

def determinant(a: int, b: int, c: int, d: int) -> int:  # small utility
    return a * d - b * c


def _safe_solve(a, b, c, d, e, f):
    """Wrapper catching SymPy's `NonInvertibleMatrixError` and re‑raising `ValueError`."""
    try:
        return solve_linear_2x2(a, b, c, d, e, f)
    except NonInvertibleMatrixError as exc:
        raise ValueError("Singular matrix after template transformation") from exc


# -----------------------------------------------------------------------------
# 3. Error templates (deterministic functions)
# -----------------------------------------------------------------------------


def swap_rhs(a: int, b: int, c: int, d: int, e: int, f: int):
    """Mistake: **swap right‑hand‑side constants**."""
    return _safe_solve(a, b, c, d, f, e)


def sign_error_eq1(a: int, b: int, c: int, d: int, e: int, f: int):
    """Mistake: **flip the sign of coefficient `b` in equation 1**."""
    return _safe_solve(a, -b, c, d, e, f)


def flip_sign_consts(a: int, b: int, c: int, d: int, e: int, f: int):
    """Mistake: **multiply both constants by −1**."""
    return _safe_solve(a, b, c, d, -e, -f)


ERROR_TEMPLATES = {
    "SWAP_RHS": swap_rhs,
    "SIGN_ERROR_EQ1": sign_error_eq1,
    "FLIP_SIGN": flip_sign_consts,
}

# -----------------------------------------------------------------------------
# 4. Smart coefficient sampler – *guarantees* uniqueness & non‑singularity
# -----------------------------------------------------------------------------


def _templates_unique(coeffs) -> bool:
    """Return `True` iff every template output is distinct and != truth."""
    a, b, c, d, e, f = coeffs
    truth = solve_linear_2x2(a, b, c, d, e, f)
    seen = {truth}
    for tmpl in ERROR_TEMPLATES.values():
        try:
            wrong = tmpl(a, b, c, d, e, f)
        except ValueError:
            return False  # singular after transformation
        if wrong in seen:
            return False
        seen.add(wrong)
    return True


def random_coefficients(low: int = -5, high: int = 5):
    """Draw coefficients until they satisfy *all* step‑1 contracts."""
    while True:
        # Coefficients a–d first so we can early‑reject determinant zero
        a, b, c, d = (random.randint(low, high) for _ in range(4))
        if determinant(a, b, c, d) == 0:
            continue  # base matrix singular ⇒ redraw all six
        e, f = (random.randint(low, high) for _ in range(2))
        coeffs = (a, b, c, d, e, f)
        if _templates_unique(coeffs):
            return coeffs


# -----------------------------------------------------------------------------
# 5. Collision‑rate estimator (should be ~0 after sampler upgrade)
# -----------------------------------------------------------------------------


def collision_rate(t1: str, t2: str, draws: int = 5_000) -> float:
    f1, f2 = ERROR_TEMPLATES[t1], ERROR_TEMPLATES[t2]
    hits = 0
    for _ in range(draws):
        coeffs = random_coefficients()
        if f1(*coeffs) == f2(*coeffs):
            hits += 1
    return hits / draws


# -----------------------------------------------------------------------------
# 6. Smoke tests
# -----------------------------------------------------------------------------


def _test_each_template_diverges_from_truth():
    a, b, c, d, e, f = 2, 1, 3, 4, 5, 6
    truth = solve_linear_2x2(a, b, c, d, e, f)
    for name, tmpl in ERROR_TEMPLATES.items():
        assert tmpl(a, b, c, d, e, f) != truth, f"{name} matched truth unexpectedly"


def _test_sign_error_definition():
    a, b, c, d, e, f = 3, 2, 7, -1, -4, 5
    expected = solve_linear_2x2(a, -b, c, d, e, f)
    assert sign_error_eq1(a, b, c, d, e, f) == expected


def _test_sampler_uniqueness(draws: int = 2_000):
    for _ in range(draws):
        coeffs = random_coefficients()
        assert _templates_unique(coeffs), f"Sampler returned non‑unique coeffs {coeffs}"


def _test_collision_rates():
    rate = collision_rate("SWAP_RHS", "SIGN_ERROR_EQ1", draws=1_000)
    assert rate < 0.01, f"Collision rate still too high: {rate:.3f}"


# -----------------------------------------------------------------------------
# 7. CLI entry‑point
# -----------------------------------------------------------------------------


if __name__ == "__main__":
    _test_each_template_diverges_from_truth()
    _test_sign_error_definition()
    _test_sampler_uniqueness()
    _test_collision_rates()

    print(
        "✓ All smoke tests passed — templates diverge from truth, never singular, and "
        "collision rate ≈ 0 %."
    )
