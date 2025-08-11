def solve():
    """Index: 1177.
    Returns: the total amount James makes a week.
    """
    # L1
    hours_per_day = 8 # 8 hours a day
    days_per_week = 4 # 4 days a week
    total_hours_per_week = hours_per_day * days_per_week

    # L2
    hourly_rate = 20 # $20 an hour
    weekly_earnings = total_hours_per_week * hourly_rate

    # FA
    answer = weekly_earnings
    return answer