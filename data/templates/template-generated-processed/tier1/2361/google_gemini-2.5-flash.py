def solve():
    """Index: 2361.
    Returns: Martha's current age.
    """
    # L1
    ellen_current_age = 10 # Ellen is 10 years old now
    years_in_future = 6 # in six years
    ellen_age_in_six_years = ellen_current_age + years_in_future

    # L2
    multiplier_for_twice = 2 # twice as old as Ellen
    martha_age = multiplier_for_twice * ellen_age_in_six_years

    # FA
    answer = martha_age
    return answer