def solve():
    """Index: 5979.
    Returns: the average GPA for the school.
    """
    # L1
    sixth_grade_gpa = 93 # The average GPA for 6th graders is 93
    gpa_increase_7th_grade = 2 # 2 more than the 6th graders
    seventh_grade_gpa = sixth_grade_gpa + gpa_increase_7th_grade

    # L2
    eighth_grade_gpa = 91 # the 8th graders average GPA is 91
    total_gpa_sum = sixth_grade_gpa + seventh_grade_gpa + eighth_grade_gpa

    # L3
    number_of_grades = 3 # WK
    average_school_gpa = total_gpa_sum / number_of_grades

    # FA
    answer = average_school_gpa
    return answer