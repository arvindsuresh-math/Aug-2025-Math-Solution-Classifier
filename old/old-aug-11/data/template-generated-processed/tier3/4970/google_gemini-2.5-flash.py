def solve():
    """Index: 4970.
    Returns: the daughter's age in 3 years.
    """
    # L1
    mother_current_age = 41 # mother is 41 years old now
    years_ago = 5 # 5 years ago
    mother_age_five_years_ago = mother_current_age - years_ago

    # L2
    half_divisor = 2 # half hers
    daughter_age_five_years_ago = mother_age_five_years_ago / half_divisor

    # L3
    daughter_current_age = daughter_age_five_years_ago + years_ago

    # L4
    years_in_future = 3 # in 3 years
    daughter_age_in_three_years = daughter_current_age + years_in_future

    # FA
    answer = daughter_age_in_three_years
    return answer