def solve():
    """Index: 1113.
    Returns: the sum of Viggo's and his brother's current ages.
    """
    # L1
    brother_age_past = 2 # when his brother was 2
    multiplier_twice = 2 # Twice Viggo's younger brother's age
    twice_brother_age_past = multiplier_twice * brother_age_past

    # L2
    viggo_more_than_twice = 10 # 10 years more than twice
    viggo_age_past = viggo_more_than_twice + twice_brother_age_past

    # L3
    viggo_age_difference = viggo_age_past - brother_age_past

    # L4
    brother_age_current = 10 # his younger brother is currently 10 years old
    viggo_age_current = brother_age_current + viggo_age_difference

    # L5
    sum_of_ages = viggo_age_current + brother_age_current

    # FA
    answer = sum_of_ages
    return answer