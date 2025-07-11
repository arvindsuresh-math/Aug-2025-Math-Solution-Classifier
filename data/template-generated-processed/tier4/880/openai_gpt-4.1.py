def solve():
    """Index: 880.
    Returns: the total time (in hours) Mr. John will have spent jogging after two weeks.
    """
    # L1
    jog_hours = 1 # 1 hour in the morning
    jog_minutes = 30 # 30 minutes in the morning
    minutes_per_hour = 60 # WK
    jog_time_per_day = jog_hours + (jog_minutes / minutes_per_hour)

    # L2
    days_per_week = 7 # 7 days in a week
    jog_time_per_week = jog_time_per_day * days_per_week

    # L3
    num_weeks = 2 # two weeks
    total_jog_time = num_weeks * jog_time_per_week

    # FA
    answer = total_jog_time
    return answer