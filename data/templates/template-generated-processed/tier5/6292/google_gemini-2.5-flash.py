def solve():
    """Index: 6292.
    Returns: the present age of Allen's mother.
    """
    # L1
    years_later = 3 # In 3 years
    total_age_increase = years_later + years_later

    # L2
    sum_ages_in_future = 41 # sum of their ages will be 41
    sum_present_ages = sum_ages_in_future - total_age_increase

    # L5
    age_difference = 25 # 25 years younger
    sixty = sum_present_ages + age_difference

    # L6
    coefficient_of_x = 2 # WK
    mother_present_age = sixty / coefficient_of_x

    # FA
    answer = mother_present_age
    return answer