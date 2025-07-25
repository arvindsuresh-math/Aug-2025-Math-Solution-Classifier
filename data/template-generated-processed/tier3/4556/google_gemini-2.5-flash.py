def solve():
    """Index: 4556.
    Returns: the average hours each student in 5th grade needs to read per day.
    """
    # L1
    sixth_grade_hours = 299 # The 6th grade already finished and read a total of 299 hours
    beat_by_hours = 1 # beat them by 1
    target_total_hours = sixth_grade_hours + beat_by_hours

    # L2
    days_in_week_for_calculation = 5 # WK
    target_daily_hours_class = target_total_hours / days_in_week_for_calculation

    # L3
    fifth_grade_students = 20 # The fifth grade has 20 students
    hours_per_student_per_day = target_daily_hours_class / fifth_grade_students

    # FA
    answer = hours_per_student_per_day
    return answer