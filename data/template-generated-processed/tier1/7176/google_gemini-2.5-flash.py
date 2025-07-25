def solve():
    """Index: 7176.
    Returns: the total years Tate spent in high school and college.
    """
    # L1
    normal_high_school_years = 4 # WK
    less_than_normal = 1 # 1 year less than normal
    high_school_years = normal_high_school_years - less_than_normal

    # L2
    multiplier_for_tertiary = 3 # 3 times that long
    tertiary_education_years = multiplier_for_tertiary * high_school_years

    # L3
    total_education_years = high_school_years + tertiary_education_years

    # FA
    answer = total_education_years
    return answer