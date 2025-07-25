def solve():
    """Index: 4438.
    Returns: the total time Paris studies during the semester.
    """
    # L1
    weekday_hours_per_day = 3 # studies 3 hours a day
    weekdays_per_week = 5 # WK
    weekday_hours_per_week = weekdays_per_week * weekday_hours_per_day

    # L2
    saturday_hours = 4 # 4 hours studying on Saturday
    sunday_hours = 5 # 5 hours studying on Sunday
    weekend_hours_per_week = saturday_hours + sunday_hours

    # L3
    total_hours_per_week = weekday_hours_per_week + weekend_hours_per_week

    # L4
    semester_weeks = 15 # The fall semester lasts 15 weeks
    total_study_time_semester = semester_weeks * total_hours_per_week

    # FA
    answer = total_study_time_semester
    return answer