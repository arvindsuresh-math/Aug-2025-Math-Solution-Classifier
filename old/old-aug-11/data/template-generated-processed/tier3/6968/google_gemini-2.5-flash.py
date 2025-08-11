def solve():
    """Index: 6968.
    Returns: the number of periods required for all students to present their projects.
    """
    # L1
    num_students = 32 # 32 students
    time_per_student = 5 # 5 minutes to do so
    total_presentation_minutes = num_students * time_per_student

    # L2
    period_length = 40 # 40 minutes long
    num_periods = total_presentation_minutes / period_length

    # FA
    answer = num_periods
    return answer