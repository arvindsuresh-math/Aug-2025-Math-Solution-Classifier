def solve():
    """Index: 6673.
    Returns: the total hours Sherman drives a week.
    """
    # L1
    commute_time_one_way = 30 # 30-minute commute
    daily_commute_minutes = commute_time_one_way + commute_time_one_way

    # L2
    work_days_per_week = 5 # 5 days a week
    weekly_commute_minutes = work_days_per_week * daily_commute_minutes

    # L3
    minutes_per_hour = 60 # WK
    weekly_commute_hours = weekly_commute_minutes / minutes_per_hour

    # L4
    weekend_hours_per_day = 2 # 2 hours, each day
    weekend_days = 2 # both Saturday and Sunday
    weekly_weekend_hours = weekend_hours_per_day * weekend_days

    # L5
    total_weekly_driving_hours = weekly_commute_hours + weekly_weekend_hours

    # FA
    answer = total_weekly_driving_hours
    return answer