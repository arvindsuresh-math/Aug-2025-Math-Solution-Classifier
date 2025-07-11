def solve():
    """Index: 2023.
    Returns: the number of years until Beth is twice her sister's age.
    """
    # L1
    beth_current_age = 18 # Beth is 18 years old
    sister_current_age = 5 # her little sister is 5
    age_difference = beth_current_age - sister_current_age

    # L2
    multiplier_for_twice = 2 # twice her sister's age
    beth_target_age = age_difference * multiplier_for_twice

    # L3
    years_until_target_age = beth_target_age - beth_current_age

    # FA
    answer = years_until_target_age
    return answer