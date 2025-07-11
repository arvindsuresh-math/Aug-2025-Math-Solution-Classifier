def solve():
    """Index: 2412.
    Returns: Barbara's age when Mike is 24.
    """
    # L1
    mike_current_age = 16 # Mike is 16 years old
    half_divisor = 2 # half as old as he is
    barbara_current_age = mike_current_age / half_divisor

    # L2
    mike_future_age = 24 # Mike is 24 years old
    years_passed = mike_future_age - mike_current_age

    # L3
    barbara_future_age = barbara_current_age + years_passed

    # FA
    answer = barbara_future_age
    return answer