def solve():
    """Index: 2364.
    Returns: the lowest grade the absent student can get for the class to still get a pizza party.
    """
    # L1
    total_students = 25 # 25 students in the class
    target_average_score_percent = 75 # higher than 75%
    target_average_score_decimal = target_average_score_percent / 100 # WK
    required_total_score_sum = total_students * target_average_score_decimal

    # L2
    absent_student_count = 1 # One student is absent
    students_who_took_test = total_students - absent_student_count
    average_score_taken_test_percent = 77 # average score of the students who took the test was 77%
    average_score_taken_test_decimal = average_score_taken_test_percent / 100 # WK
    current_total_score_sum = students_who_took_test * average_score_taken_test_decimal

    # L3
    percent_conversion_factor = 100 # WK
    score_needed_decimal = required_total_score_sum - current_total_score_sum
    lowest_grade_absent_student_percent = score_needed_decimal * percent_conversion_factor

    # FA
    answer = lowest_grade_absent_student_percent
    return answer