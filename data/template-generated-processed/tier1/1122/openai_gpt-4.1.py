def solve():
    """Index: 1122.
    Returns: the total number of hours Tim runs per week now.
    """
    # L1
    times_per_week_before = 3 # run 3 times a week
    extra_days = 2 # add an extra 2 days a week
    times_per_week_now = times_per_week_before + extra_days

    # L2
    hours_morning = 1 # 1 hour in the morning
    hours_evening = 1 # 1 in the evening
    hours_per_day = hours_morning + hours_evening

    # L3
    total_hours_per_week = hours_per_day * times_per_week_now

    # FA
    answer = total_hours_per_week
    return answer