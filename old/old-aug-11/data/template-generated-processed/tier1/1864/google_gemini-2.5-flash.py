def solve():
    """Index: 1864.
    Returns: Raven's current age.
    """
    # L1
    phoebe_current_age = 10 # Phoebe is currently 10 years old
    years_in_future = 5 # In 5 years
    phoebe_age_future = phoebe_current_age + years_in_future

    # L2
    raven_age_multiplier = 4 # 4 times as old
    raven_age_future = raven_age_multiplier * phoebe_age_future

    # L3
    raven_current_age = raven_age_future - years_in_future

    # FA
    answer = raven_current_age
    return answer