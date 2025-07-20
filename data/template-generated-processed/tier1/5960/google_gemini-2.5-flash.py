def solve():
    """Index: 5960.
    Returns: the sum of the ages of Josiah and Hans in three years.
    """
    # L1
    hans_current_age = 15 # Hans is 15 years old now
    josiah_age_multiplier = 3 # three times as old as Hans
    josiah_current_age = hans_current_age * josiah_age_multiplier

    # L2
    years_in_future = 3 # In three years
    josiah_future_age = josiah_current_age + years_in_future

    # L3
    hans_future_age = hans_current_age + years_in_future

    # L4
    sum_of_ages_future = josiah_future_age + hans_future_age

    # FA
    answer = sum_of_ages_future
    return answer