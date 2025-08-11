def solve():
    """Index: 4395.
    Returns: the total of Xavier's and Yasmin's current ages.
    """
    # L1
    xavier_future_age = 30 # Xavier will 30 years old
    years_until_future_age = 6 # in six years
    xavier_current_age = xavier_future_age - years_until_future_age

    # L2
    age_multiplier = 2 # twice as old as Yasmin
    yasmin_current_age = xavier_current_age / age_multiplier

    # L3
    total_current_ages = yasmin_current_age + xavier_current_age

    # FA
    answer = total_current_ages
    return answer