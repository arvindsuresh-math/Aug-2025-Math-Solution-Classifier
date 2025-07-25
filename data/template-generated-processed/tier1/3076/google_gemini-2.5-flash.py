def solve():
    """Index: 3076.
    Returns: Rachel's age when Emily is half her age.
    """
    # L1
    rachel_age_initial = 24 # Rachel, is 24 years old
    emily_age_initial = 20 # Emily is 20 years old
    age_difference = rachel_age_initial - emily_age_initial

    # L2
    multiplier_for_twice = 2 # half her age
    rachel_age_when_emily_half = age_difference * multiplier_for_twice

    # FA
    answer = rachel_age_when_emily_half
    return answer