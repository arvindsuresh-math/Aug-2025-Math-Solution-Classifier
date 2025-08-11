def solve():
    """Index: 1631.
    Returns: John's sister's age when John is 50 years old.
    """
    # L1
    john_age = 10 # John is 10 years old
    sister_multiplier = 2 # His sister is twice his age
    sister_age = john_age * sister_multiplier

    # L2
    age_difference = sister_age - john_age

    # L3
    john_future_age = 50 # when he is 50 years old
    sister_future_age = john_future_age + age_difference

    # FA
    answer = sister_future_age
    return answer