def solve():
    """Index: 5511.
    Returns: Nate's age when Ember is 14.
    """
    # L1
    nate_current_age = 14 # Nate who is 14
    half_divisor = 2 # half as old
    ember_current_age = nate_current_age / half_divisor

    # L2
    ember_future_age = 14 # When she is 14 herself
    years_passed = ember_future_age - ember_current_age
    nate_future_age = nate_current_age + years_passed

    # FA
    answer = nate_future_age
    return answer