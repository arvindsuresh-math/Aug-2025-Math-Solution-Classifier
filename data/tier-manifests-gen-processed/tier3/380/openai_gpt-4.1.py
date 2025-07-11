def solve():
    """Index: 380.
    Returns: Patrick's current age.
    """
    # L1
    robert_future_age = 30 # Robert will turn 30 after 2 years
    years_until_30 = 2 # after 2 years
    robert_current_age = robert_future_age - years_until_30

    # L2
    patrick_divisor = 2 # Patrick is half the age
    patrick_current_age = robert_current_age / patrick_divisor

    # FA
    answer = patrick_current_age
    return answer