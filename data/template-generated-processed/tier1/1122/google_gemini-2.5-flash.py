def solve():
    """Index: 1122.
    Returns: the total number of hours Tim runs per week now.
    """
    # L1
    initial_run_days_per_week = 3 # run 3 times a week
    extra_run_days_per_week = 2 # add an extra 2 days a week
    new_run_days_per_week = initial_run_days_per_week + extra_run_days_per_week

    # L2
    morning_run_hours = 1 # 1 hour in the morning
    evening_run_hours = 1 # 1 in the evening
    hours_per_run_day = morning_run_hours + evening_run_hours

    # L3
    total_hours_per_week = hours_per_run_day * new_run_days_per_week

    # FA
    answer = total_hours_per_week
    return answer