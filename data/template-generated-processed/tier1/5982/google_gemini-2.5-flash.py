def solve():
    """Index: 5982.
    Returns: the total hours Ralph spends watching TV in one week.
    """
    # L1
    hours_per_weekday = 4 # 4 hours a day from Monday to Friday
    num_weekdays = 5 # WK
    weekday_hours = hours_per_weekday * num_weekdays

    # L2
    num_weekend_days = 2 # WK
    hours_per_weekend_day = 6 # 6 hours a day on Saturday and Sunday
    weekend_hours = num_weekend_days * hours_per_weekend_day

    # L3
    total_weekly_hours = weekday_hours + weekend_hours

    # FA
    answer = total_weekly_hours
    return answer