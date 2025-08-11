def solve():
    """Index: 2485.
    Returns: the total time Carly spends practicing swimming in a month.
    """
    # L1
    butterfly_hours_per_day = 3 # 3 hours a day
    butterfly_days_per_week = 4 # 4 days a week
    butterfly_hours_per_week = butterfly_hours_per_day * butterfly_days_per_week

    # L2
    backstroke_hours_per_day = 2 # 2 hours a day
    backstroke_days_per_week = 6 # six days a week
    backstroke_hours_per_week = backstroke_hours_per_day * backstroke_days_per_week

    # L3
    total_hours_per_week = butterfly_hours_per_week + backstroke_hours_per_week

    # L4
    weeks_in_month = 4 # month with 4 weeks
    total_hours_per_month = total_hours_per_week * weeks_in_month

    # FA
    answer = total_hours_per_month
    return answer