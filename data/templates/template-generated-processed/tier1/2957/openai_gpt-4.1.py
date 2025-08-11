def solve():
    """Index: 2957.
    Returns: the total number of hours Tim sleeps in a week.
    """
    # L1
    hours_per_day_weekdays = 6 # sleeps 6 hours per day for 5 days a week
    num_weekdays = 5 # 5 days a week
    sleep_weekdays = hours_per_day_weekdays * num_weekdays

    # L2
    hours_per_day_weekend = 10 # 10 hours a day for the other 2
    num_weekend_days = 2 # the other 2
    sleep_weekend = hours_per_day_weekend * num_weekend_days

    # L3
    total_sleep = sleep_weekdays + sleep_weekend

    # FA
    answer = total_sleep
    return answer