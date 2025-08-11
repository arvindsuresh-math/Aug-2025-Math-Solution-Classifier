def solve():
    """Index: 3753.
    Returns: the number of students who didn't pass their exams.
    """
    # L1
    total_students = 804 # 804 senior high school students
    passed_percentage = 75 # 75% passed
    percent_to_decimal_factor = 0.01 # WK
    students_passed = total_students * passed_percentage * percent_to_decimal_factor

    # L2
    students_failed = total_students - students_passed

    # FA
    answer = students_failed
    return answer