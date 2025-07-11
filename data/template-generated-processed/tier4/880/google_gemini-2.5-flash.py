def solve():
    """Index: 880.
    Returns: the total time spent jogging in hours after two weeks.
    """
    # L1
    hours_initial = 1 # 1 hour 30 minutes
    minutes_initial = 30 # 1 hour 30 minutes
    minutes_per_hour = 60 # WK
    jogging_time_per_day_hours = hours_initial + (minutes_initial / minutes_per_hour)

    # L2
    days_per_week = 7 # WK
    jogging_time_per_week_hours = jogging_time_per_day_hours * days_per_week

    # L3
    num_weeks = 2 # two weeks
    total_jogging_time_hours = num_weeks * jogging_time_per_week_hours

    # FA
    answer = total_jogging_time_hours
    return answer