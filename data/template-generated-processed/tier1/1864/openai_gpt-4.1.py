def solve():
    """Index: 1864.
    Returns: Raven's current age.
    """
    # L1
    phoebe_current_age = 10 # Phoebe is currently 10 years old
    years_in_future = 5 # In 5 years
    phoebe_future_age = phoebe_current_age + years_in_future

    # L2
    raven_multiplier = 4 # Raven will be 4 times as old as Phoebe
    raven_future_age = raven_multiplier * phoebe_future_age

    # L3
    raven_current_age = raven_future_age - years_in_future

    # FA
    answer = raven_current_age
    return answer