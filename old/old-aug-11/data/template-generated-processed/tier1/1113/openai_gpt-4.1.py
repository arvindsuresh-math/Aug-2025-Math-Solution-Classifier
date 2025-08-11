def solve():
    """Index: 1113.
    Returns: the sum of Viggo's and his brother's current ages.
    """
    # L1
    brother_age_when_2 = 2 # when his brother was 2
    twice_brother_age = 2 # twice his younger brother's age
    twice_brother_when_2 = twice_brother_age * brother_age_when_2

    # L2
    viggo_more_than_twice = 10 # 10 more than twice his younger brother's age
    viggo_age_when_brother_2 = viggo_more_than_twice + twice_brother_when_2

    # L3
    viggo_age_difference = viggo_age_when_brother_2 - brother_age_when_2

    # L4
    brother_current_age = 10 # his younger brother is currently 10 years old
    viggo_current_age = brother_current_age + viggo_age_difference

    # L5
    combined_age = viggo_current_age + brother_current_age

    # FA
    answer = combined_age
    return answer