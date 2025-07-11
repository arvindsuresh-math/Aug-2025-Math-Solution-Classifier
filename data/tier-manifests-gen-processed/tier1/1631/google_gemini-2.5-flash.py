def solve():
    """Index: 1631.
    Returns: the sister's age when John is 50 years old.
    """
    # L1
    john_current_age = 10 # John is 10 years old
    multiplier_twice = 2 # twice his age
    sister_current_age = john_current_age * multiplier_twice

    # L2
    age_difference = sister_current_age - john_current_age

    # L3
    john_future_age = 50 # When he is 50 years old
    sister_future_age = john_future_age + age_difference

    # FA
    answer = sister_future_age
    return answer