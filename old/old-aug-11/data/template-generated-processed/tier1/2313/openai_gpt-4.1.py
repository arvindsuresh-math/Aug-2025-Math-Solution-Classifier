def solve():
    """Index: 2313.
    Returns: Christian's age in eight years.
    """
    # L1
    brian_future_age = 40 # Brian will be 40 years old (in 8 years)
    years_until_future = 8 # in eight more years
    brian_current_age = brian_future_age - years_until_future

    # L2
    christian_multiplier = 2 # Christian is twice as old as Brian
    christian_current_age = christian_multiplier * brian_current_age

    # L3
    christian_age_in_8_years = christian_current_age + years_until_future

    # FA
    answer = christian_age_in_8_years
    return answer