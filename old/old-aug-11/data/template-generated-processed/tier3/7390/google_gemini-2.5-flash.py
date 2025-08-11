def solve():
    """Index: 7390.
    Returns: the current age.
    """
    # L2
    age_multiplier = 3 # three times older
    years_ago = 6 # six years ago
    years_ago_times_multiplier = years_ago * age_multiplier

    # L4
    # The solution implicitly performs the rearrangement from X = 3X - 18 to -2X = -18
    # before the final division. The values -2 and -18 are derived from these steps.
    coefficient_of_X = 1 - age_multiplier
    constant_term_after_rearrangement = -years_ago_times_multiplier
    current_age = constant_term_after_rearrangement / coefficient_of_X

    # FA
    answer = current_age
    return answer