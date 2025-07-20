def solve():
    """Index: 3332.
    Returns: the number of times Jason steps on his partner's feet.
    """
    # L1 and L2 are descriptive and set up the algebraic relationships.
    # The numerical inputs are defined here for use in subsequent computational steps.
    nancy_factor = 3 # Nancy steps on her partner's feet 3 times as often as Jason
    total_steps = 32 # together they step on each other's feet 32 times

    # L3
    jason_coefficient_implicit = 1 # WK
    combined_coefficient = nancy_factor + jason_coefficient_implicit

    # L4
    jason_steps = total_steps / combined_coefficient

    # FA
    answer = jason_steps
    return answer