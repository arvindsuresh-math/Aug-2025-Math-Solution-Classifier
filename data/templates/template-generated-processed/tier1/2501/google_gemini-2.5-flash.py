def solve():
    """Index: 2501.
    Returns: the sum of Ann's and Tom's ages 10 years later.
    """
    # L1
    ann_current_age = 6 # Ann is 6 years old
    tom_age_multiplier = 2 # two times older
    tom_current_age = ann_current_age * tom_age_multiplier

    # L2
    years_later = 10 # 10 years later
    ann_age_future = ann_current_age + years_later

    # L3
    tom_age_future = tom_current_age + years_later

    # L4
    sum_of_ages_future = ann_age_future + tom_age_future

    # FA
    answer = sum_of_ages_future
    return answer