def solve():
    """Index: 4724.
    Returns: the number of exams Mrs. Watson needs to grade on Wednesday.
    """
    # L1
    total_exams = 120 # 120 final exams
    monday_grade_percent_num = 60 # 60% of the exams
    percent_factor = 0.01 # WK
    monday_graded_exams = total_exams * monday_grade_percent_num * percent_factor

    # L2
    remaining_exams_after_monday = total_exams - monday_graded_exams

    # L3
    tuesday_grade_percent_num = 75 # 75% of the remaining exams
    tuesday_graded_exams = remaining_exams_after_monday * tuesday_grade_percent_num * percent_factor

    # L4
    wednesday_remaining_exams = remaining_exams_after_monday - tuesday_graded_exams

    # FA
    answer = wednesday_remaining_exams
    return answer