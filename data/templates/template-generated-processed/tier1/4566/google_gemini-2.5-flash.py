def solve():
    """Index: 4566.
    Returns: how many years older Zion's dad is than him in 10 years.
    """
    # L1
    zion_age = 8 # Zion is 8 years old
    multiplier_four_times = 4 # 4 times his age
    four_times_zion_age = zion_age * multiplier_four_times

    # L2
    dad_more_than_four_times = 3 # 3 more than 4 times his age
    dad_age_current = four_times_zion_age + dad_more_than_four_times

    # L3
    years_in_future = 10 # In 10 years
    zion_age_future = zion_age + years_in_future

    # L4
    dad_age_future = dad_age_current + years_in_future

    # L5
    age_difference_future = dad_age_future - zion_age_future

    # FA
    answer = age_difference_future
    return answer