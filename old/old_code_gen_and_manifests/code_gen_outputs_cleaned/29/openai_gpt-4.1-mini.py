def solve(
    increase_amount: int = 600,  # salary was recently increased by $600
    old_rent_fraction: float = 0.40,  # used to spend 40% of income on rent and utilities
    new_rent_fraction: float = 0.25  # now rent and utilities amount to 25% of income
):
    """Index: 29.
    Returns: the previous monthly income before the salary increase.
    """
    #: L1
    # Let previous monthly income be p (unknown)

    #: L2
    # Cost of rent and utilities was 40% of p = 2p/5
    old_rent_cost_expr = (2/5)  # coefficient for p

    #: L3
    # New income is p + 600
    # p is unknown, increase_amount is 600

    #: L4
    # New rent cost is 25% of (p + 600) = (p + 600)/4
    new_rent_cost_expr = (1/4)  # coefficient for (p + 600)

    #: L5
    # Equate old rent cost and new rent cost:
    # (2/5)*p = (1/4)*(p + 600)

    #: L6
    # Multiply both sides by 20:
    # 8p = 5p + 3000
    # Rearranged to solve for p

    #: L7
    # 3p = 3000

    #: L8
    previous_income = 3000 / 3

    answer = previous_income  # FINAL ANSWER
    return answer