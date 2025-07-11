def solve():
    """Index: 407.
    Returns: Milford's age in 3 years.
    """
    # L1
    eustace_future_age = 39 # he will be 39
    years_in_future = 3 # in 3 years
    eustace_current_age = eustace_future_age - years_in_future

    # L2
    age_ratio = 2 # Eustace is twice as old as Milford
    milford_current_age = eustace_current_age / age_ratio

    # L3
    milford_future_age = milford_current_age + years_in_future

    # FA
    answer = milford_future_age
    return answer