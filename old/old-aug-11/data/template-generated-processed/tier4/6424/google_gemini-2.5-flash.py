def solve():
    """Index: 6424.
    Returns: the number of students who failed.
    """
    # L1
    total_students = 32 # 32 students in a statistics course
    a_grade_percent = 0.25 # 25 percent of the class received an A
    a_grade_students = total_students * a_grade_percent

    # L2
    remaining_students_after_a = total_students - a_grade_students

    # L3
    bc_grade_fraction_denominator = 4 # 1/4 of the remaining students got either a B or C
    bc_grade_students = remaining_students_after_a / bc_grade_fraction_denominator

    # L4
    failed_students = remaining_students_after_a - bc_grade_students

    # FA
    answer = failed_students
    return answer