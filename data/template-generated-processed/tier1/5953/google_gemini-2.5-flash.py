def solve():
    """Index: 5953.
    Returns: the number of years until Diane is 25 years old.
    """
    # L1
    denise_age_in_two_years = 25 # Denise will be 25 years old
    years_until_denise_25 = 2 # in two years
    denise_current_age = denise_age_in_two_years - years_until_denise_25

    # L2
    diane_age_difference = 4 # 4 years younger
    diane_current_age = denise_current_age - diane_age_difference

    # L3
    diane_target_age = 25 # Diane be 25 years old
    years_until_diane_25 = diane_target_age - diane_current_age

    # FA
    answer = years_until_diane_25
    return answer