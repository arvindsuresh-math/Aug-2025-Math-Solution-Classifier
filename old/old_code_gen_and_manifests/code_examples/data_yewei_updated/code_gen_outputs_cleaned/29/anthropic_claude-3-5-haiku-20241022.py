def solve(
    previous_rent_percentage: float = 0.4,  # Mrs. Snyder used to spend 40% of her monthly income on rent and utilities
    new_rent_percentage: float = 0.25,  # now her rent and utilities only amount to 25% of her monthly income
    salary_increase: int = 600  # Her salary was recently increased by $600
):
    """Index: 29.
    Returns: Mrs. Snyder's previous monthly income.
    """
    #: L1
    # Let previous monthly income be p (this is handled implicitly in the solution)

    #: L2
    # Previous rent and utilities calculation is 40% of p

    #: L3
    # New income is p + $600

    #: L4
    # New rent and utilities is 25% of (p + $600)

    #: L5
    # Equation: 2p/5 = (p+$600)/4

    #: L6
    # Multiply both sides by 20
    # 8p = 5p + $3000

    #: L7
    # Subtract 5p from both sides
    # 3p = $3000

    #: L8
    # Divide both sides by 3
    answer = 3000 / 3  # FINAL ANSWER
    return answer