def solve():
    """Index: 4240.
    Returns: the sum of the ages of Alex and Allison now.
    """
    # L1
    diane_future_age = 30 # When Diane turns 30
    alex_age_multiplier = 2 # half the age of Alex
    alex_future_age = diane_future_age * alex_age_multiplier

    # L2
    allison_age_divisor = 2 # twice as old as Allison
    allison_future_age = diane_future_age / allison_age_divisor

    # L3
    diane_current_age = 16 # Diane is 16 years old now
    years_until_future = diane_future_age - diane_current_age

    # L4
    alex_current_age = alex_future_age - years_until_future

    # L5
    allison_current_age = allison_future_age - years_until_future

    # L6
    sum_current_ages = alex_current_age + allison_current_age

    # FA
    answer = sum_current_ages
    return answer