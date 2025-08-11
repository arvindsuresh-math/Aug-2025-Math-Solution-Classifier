def solve():
    """Index: 6659.
    Returns: Maxwell's current age.
    """
    # L1
    sister_current_age = 2 # his sister is now 2
    years_in_future = 2 # In 2 years
    sister_future_age = sister_current_age + years_in_future

    # L2
    multiplier_twice = 2 # twice his sister's age
    maxwell_future_age = sister_future_age * multiplier_twice

    # L3
    maxwell_current_age = maxwell_future_age - years_in_future

    # FA
    answer = maxwell_current_age
    return answer