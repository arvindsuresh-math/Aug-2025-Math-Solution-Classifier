def solve():
    """Index: 407.
    Returns: Milford's age in 3 years.
    """
    # L1
    eustace_future_age = 39 # In 3 years, he will be 39
    years_in_future = 3 # In 3 years
    eustace_current_age = eustace_future_age - years_in_future

    # L2
    age_multiplier = 2 # twice as old
    milford_current_age = eustace_current_age / age_multiplier

    # L3
    milford_future_age = milford_current_age + years_in_future

    # FA
    answer = milford_future_age
    return answer