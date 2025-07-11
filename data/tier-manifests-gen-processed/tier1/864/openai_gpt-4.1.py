def solve():
    """Index: 864.
    Returns: the total number of coffee cups brewed in 1 week.
    """
    # L1
    cups_per_hour_weekday = 10 # 10 coffee cups per hour on a weekday
    hours_per_day = 5 # open 5 hours a day every single day
    cups_per_weekday = cups_per_hour_weekday * hours_per_day

    # L2
    weekdays_per_week = 5 # 5 weekdays in a week
    total_weekday_cups = cups_per_weekday * weekdays_per_week

    # L3
    weekend_cups = 120 # 120 coffee cups in total over the weekend
    total_week_cups = total_weekday_cups + weekend_cups

    # FA
    answer = total_week_cups
    return answer