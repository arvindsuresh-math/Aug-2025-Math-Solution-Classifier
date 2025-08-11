def solve():
    """Index: 697.
    Returns: the total number of hours Joey will spend studying for his SAT exam.
    """
    # L1
    hours_per_night = 2 # 2 hours per night
    nights_per_week = 5 # 5 nights a week
    weekday_hours = hours_per_night * nights_per_week

    # L2
    hours_per_weekend_day = 3 # 3 hours a day on the weekends
    weekend_days = 2 # weekends (Saturday and Sunday)
    weekend_hours = hours_per_weekend_day * weekend_days

    # L3
    weekly_hours = weekday_hours + weekend_hours

    # L4
    weeks_until_exam = 6 # 6 weeks away
    total_hours = weeks_until_exam * weekly_hours

    # FA
    answer = total_hours
    return answer