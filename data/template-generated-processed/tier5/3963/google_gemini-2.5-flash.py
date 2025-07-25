def solve():
    """Index: 3963.
    Returns: John's current age.
    """
    # L3
    years_from_now = 9 # 9 years from now
    multiplier = 3 # 3 times as old
    years_ago = 11 # 11 years ago
    distributed_constant_right = multiplier * years_ago

    # L4
    j_coefficient_after_subtraction = multiplier - 1

    # L5
    constant_after_addition = years_from_now + distributed_constant_right

    # L6
    johns_age = constant_after_addition / j_coefficient_after_subtraction

    # FA
    answer = johns_age
    return answer