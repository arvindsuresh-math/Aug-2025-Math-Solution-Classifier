def solve():
    """Index: 1780.
    Returns: the total amount Faith will earn by the end of the week.
    """
    # L1
    hourly_rate = 13.50 # $13.50 per hour
    normal_hours_per_day = 8 # 8 hours a day
    daily_normal_earnings = hourly_rate * normal_hours_per_day

    # L2
    normal_work_days_per_week = 5 # 5 days a week
    weekly_normal_earnings = normal_work_days_per_week * daily_normal_earnings

    # L3
    overtime_hours_per_day = 2 # 2 hours of overtime per day
    daily_overtime_earnings = overtime_hours_per_day * hourly_rate

    # L4
    weekly_overtime_earnings = daily_overtime_earnings * normal_work_days_per_week

    # L5
    total_weekly_earnings = weekly_normal_earnings + weekly_overtime_earnings

    # FA
    answer = total_weekly_earnings
    return answer