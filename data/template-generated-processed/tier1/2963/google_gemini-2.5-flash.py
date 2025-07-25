def solve():
    """Index: 2963.
    Returns: Tully's age a year ago.
    """
    # L1
    kate_current_age = 29 # Kate is now 29 years old
    years_from_now = 3 # Three years from now
    kate_future_age = kate_current_age + years_from_now

    # L2
    tully_age_multiplier = 2 # twice as old
    tully_future_age = kate_future_age * tully_age_multiplier

    # L3
    tully_current_age = tully_future_age - years_from_now

    # L4
    years_ago = 1 # a year ago
    tully_age_last_year = tully_current_age - years_ago

    # FA
    answer = tully_age_last_year
    return answer