def solve():
    """Index: 2313.
    Returns: Christian's age in eight years.
    """
    # L1
    brian_future_age = 40 # Brian will be 40 years old
    years_in_future = 8 # In eight more years
    brian_current_age = brian_future_age - years_in_future

    # L2
    christian_age_multiplier = 2 # Christian is twice as old as Brian
    christian_current_age = christian_age_multiplier * brian_current_age

    # L3
    christian_future_age = christian_current_age + years_in_future

    # FA
    answer = christian_future_age
    return answer