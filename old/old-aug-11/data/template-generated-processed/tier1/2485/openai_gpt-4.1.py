def solve():
    """Index: 2485.
    Returns: the total hours Carly spends practicing swimming in a 4-week month.
    """
    # L1
    butterfly_hours_per_day = 3 # 3 hours a day (butterfly)
    butterfly_days_per_week = 4 # 4 days a week (butterfly)
    butterfly_weekly = butterfly_hours_per_day * butterfly_days_per_week

    # L2
    backstroke_hours_per_day = 2 # 2 hours a day (backstroke)
    backstroke_days_per_week = 6 # 6 days a week (backstroke)
    backstroke_weekly = backstroke_hours_per_day * backstroke_days_per_week

    # L3
    total_weekly = butterfly_weekly + backstroke_weekly

    # L4
    weeks_per_month = 4 # 4 weeks in a month
    total_monthly = total_weekly * weeks_per_month

    # FA
    answer = total_monthly
    return answer