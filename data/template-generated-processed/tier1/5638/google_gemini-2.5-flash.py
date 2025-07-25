def solve():
    """Index: 5638.
    Returns: the total hours Janna sleeps in a week.
    """
    # L1
    weekday_sleep_hours = 7 # 7 hours each day during weekdays
    weekdays_in_week = 5 # WK
    total_weekday_sleep = weekday_sleep_hours * weekdays_in_week

    # L2
    weekend_sleep_hours = 8 # 8 hours each day during weekends
    weekend_days_in_week = 2 # WK
    total_weekend_sleep = weekend_sleep_hours * weekend_days_in_week

    # L3
    total_sleep_in_week = total_weekday_sleep + total_weekend_sleep

    # FA
    answer = total_sleep_in_week
    return answer