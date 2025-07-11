def solve():
    """Index: 2501.
    Returns: the sum of Ann's and Tom's ages 10 years later.
    """
    # L1
    ann_age = 6 # Ann is 6 years old
    tom_multiplier = 2 # Tom is now two times older
    tom_age = ann_age * tom_multiplier

    # L2
    years_later = 10 # 10 years later
    ann_future_age = ann_age + years_later

    # L3
    tom_future_age = tom_age + years_later

    # L4
    sum_ages = ann_future_age + tom_future_age

    # FA
    answer = sum_ages
    return answer