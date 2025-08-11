def solve():
    """Index: 864.
    Returns: the total number of coffee cups brewed in 1 week.
    """
    # L1
    cups_per_hour_weekday = 10 # 10 coffee cups per hour on a weekday
    hours_open_per_day = 5 # open 5 hours a day
    weekday_cups_per_day = cups_per_hour_weekday * hours_open_per_day

    # L2
    weekdays_in_week = 5 # WK
    total_weekday_cups = weekday_cups_per_day * weekdays_in_week

    # L3
    weekend_cups_total = 120 # 120 coffee cups in total over the weekend
    total_cups_in_week = total_weekday_cups + weekend_cups_total

    # FA
    answer = total_cups_in_week
    return answer