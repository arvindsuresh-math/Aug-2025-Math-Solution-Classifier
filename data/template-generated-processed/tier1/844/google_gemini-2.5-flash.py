def solve():
    """Index: 844.
    Returns: how much older Andy is than Rahim, right now, in years.
    """
    # L1
    multiplier_twice = 2 # twice as old
    rahim_age_now = 6 # Rahim is 6 now
    andy_age_in_5_years = multiplier_twice * rahim_age_now

    # L2
    years_in_future = 5 # In 5 years
    andy_age_now = andy_age_in_5_years - years_in_future

    # L3
    age_difference = andy_age_now - rahim_age_now

    # FA
    answer = age_difference
    return answer