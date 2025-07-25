def solve():
    """Index: 5605.
    Returns: Jared's current age.
    """
    # L1
    tom_age_in_five_years = 30 # Tom will be 30 in five years
    years_until_tom_is_30 = 5 # in five years
    tom_current_age = tom_age_in_five_years - years_until_tom_is_30

    # L2
    years_ago = 2 # Two years ago
    tom_age_two_years_ago = tom_current_age - years_ago

    # L3
    multiplier_twice = 2 # twice as old
    jared_age_two_years_ago = tom_age_two_years_ago * multiplier_twice

    # L4
    jared_current_age = jared_age_two_years_ago + years_ago

    # FA
    answer = jared_current_age
    return answer