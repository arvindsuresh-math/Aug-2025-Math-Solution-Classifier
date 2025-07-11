def solve():
    """Index: 380.
    Returns: Patrick's current age.
    """
    # L1
    robert_future_age = 30 # Robert will turn 30
    years_until_future_age = 2 # after 2 years
    robert_current_age = robert_future_age - years_until_future_age

    # L2
    patrick_age_divisor = 2 # Patrick is half the age
    patrick_current_age = robert_current_age / patrick_age_divisor

    # FA
    answer = patrick_current_age
    return answer