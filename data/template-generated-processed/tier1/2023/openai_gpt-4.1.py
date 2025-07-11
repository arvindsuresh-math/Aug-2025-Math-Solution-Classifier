def solve():
    """Index: 2023.
    Returns: the number of years until Beth is twice her sister's age.
    """
    # L1
    beth_age = 18 # Beth is 18 years old
    sister_age = 5 # her little sister is 5
    age_difference = beth_age - sister_age

    # L2
    multiplier = 2 # twice her sister's age
    beth_twice_age = age_difference * multiplier

    # L3
    years_until_twice = beth_twice_age - beth_age

    # FA
    answer = years_until_twice
    return answer