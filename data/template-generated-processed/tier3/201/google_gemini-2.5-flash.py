def solve():
    """Index: 201.
    Returns: the average number of apples Archibald eats per week.
    """
    # L1
    weeks_first_period = 2 # two weeks
    apples_per_day_first_period = 1 # 1 apple a day
    days_per_week = 7 # WK
    days_in_first_period = weeks_first_period * days_per_week
    apples_first_period = days_in_first_period * apples_per_day_first_period

    # L2
    weeks_second_period = 3 # Over the next three weeks
    apples_second_period = apples_first_period

    # L3
    weeks_third_period = 2 # Over the next two weeks
    apples_per_day_third_period = 3 # eats 3 apples a day
    days_in_third_period = weeks_third_period * days_per_week
    apples_third_period = days_in_third_period * apples_per_day_third_period

    # L4
    total_apples = apples_first_period + apples_second_period + apples_third_period

    # L5
    total_weeks = 7 # Over these 7 weeks
    average_apples_per_week = total_apples / total_weeks

    # FA
    answer = average_apples_per_week
    return answer