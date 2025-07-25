def solve():
    """Index: 2361.
    Returns: Martha's current age.
    """
    # L1
    ellen_now = 10 # Ellen is 10 years old now
    years_in_future = 6 # in six years
    ellen_in_six_years = ellen_now + years_in_future

    # L2
    martha_multiplier = 2 # twice as old
    martha_now = martha_multiplier * ellen_in_six_years

    # FA
    answer = martha_now
    return answer