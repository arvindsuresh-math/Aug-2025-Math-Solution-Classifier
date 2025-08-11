def solve():
    """Index: 697.
    Returns: the total time Joey will spend studying.
    """
    # L1
    hours_per_night_weekday = 2 # 2 hours per night
    nights_per_week_weekday = 5 # 5 nights a week
    weekday_study_hours = hours_per_night_weekday * nights_per_week_weekday

    # L2
    hours_per_day_weekend = 3 # 3 hours a day on the weekends
    days_in_weekend = 2 # WK
    weekend_study_hours = hours_per_day_weekend * days_in_weekend

    # L3
    total_hours_per_week = weekday_study_hours + weekend_study_hours

    # L4
    weeks_until_exam = 6 # 6 weeks away
    total_study_time = weeks_until_exam * total_hours_per_week

    # FA
    answer = total_study_time
    return answer