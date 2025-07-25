def solve():
    """Index: 2915.
    Returns: the number of years until their combined age is 44.
    """
    # L1
    adam_age = 8 # Adam is 8 years old
    tom_age = 12 # Tom is 12 years old
    current_combined_age = adam_age + tom_age

    # L2
    years_passed_unit = 1 # 1 year
    number_of_brothers = 2 # 1 * 2
    age_increase_per_year = years_passed_unit * number_of_brothers

    # L3
    target_combined_age = 44 # combined age be 44 years old
    age_needed_increase = target_combined_age - current_combined_age

    # L4
    years_until_target_age = age_needed_increase / age_increase_per_year

    # FA
    answer = years_until_target_age
    return answer