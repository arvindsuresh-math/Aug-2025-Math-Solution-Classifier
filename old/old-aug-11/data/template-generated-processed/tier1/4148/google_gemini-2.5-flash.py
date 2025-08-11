def solve():
    """Index: 4148.
    Returns: Diana's age today.
    """
    # L1
    grace_age_last_year = 3 # Grace turned 3 a year ago
    years_ago = 1 # a year ago
    grace_age_today = grace_age_last_year + years_ago

    # L2
    diana_age_multiplier = 2 # twice as old
    diana_age_today = grace_age_today * diana_age_multiplier

    # FA
    answer = diana_age_today
    return answer