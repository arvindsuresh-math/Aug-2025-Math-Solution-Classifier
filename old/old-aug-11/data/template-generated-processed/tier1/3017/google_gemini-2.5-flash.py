def solve():
    """Index: 3017.
    Returns: the age difference between Mandy and her sister.
    """
    # L1
    mandy_age = 3 # Mandy is 3 years old
    brother_age_multiplier = 4 # Her brother is 4 times as old as she is
    brother_age = mandy_age * brother_age_multiplier

    # L2
    sister_age_difference = 5 # Her sister is 5 years younger than her brother
    sister_age = brother_age - sister_age_difference

    # L3
    age_difference_mandy_sister = sister_age - mandy_age

    # FA
    answer = age_difference_mandy_sister
    return answer