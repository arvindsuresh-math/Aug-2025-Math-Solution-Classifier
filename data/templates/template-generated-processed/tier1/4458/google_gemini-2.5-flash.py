def solve():
    """Index: 4458.
    Returns: the total number of hours the business is open in a week.
    """
    # L1
    weekday_end_hour = 10 # 10p every day Monday through Friday
    weekday_start_hour = 4 # 4 pm to 10p every day Monday through Friday
    hours_per_weekday = weekday_end_hour - weekday_start_hour

    # L2
    num_weekdays = 5 # WK
    total_weekday_hours = hours_per_weekday * num_weekdays

    # L3
    weekend_end_hour = 10 # 10 pm on weekends
    weekend_start_hour = 6 # 6 pm to 10 pm on weekends
    hours_per_weekend_day = weekend_end_hour - weekend_start_hour

    # L4
    num_weekend_days = 2 # WK
    total_weekend_hours = hours_per_weekend_day * num_weekend_days

    # L5
    total_hours_per_week = total_weekday_hours + total_weekend_hours

    # FA
    answer = total_hours_per_week
    return answer