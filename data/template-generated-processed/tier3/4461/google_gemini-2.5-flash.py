def solve():
    """Index: 4461.
    Returns: the total number of students Ms. Hatcher taught for the day.
    """
    # L1
    third_graders = 20 # 20 third-graders
    fourth_grade_multiplier = 2 # twice the number of third-graders
    fourth_graders = third_graders * fourth_grade_multiplier

    # L2
    fifth_grade_divisor = 2 # half as many students
    fifth_graders = third_graders / fifth_grade_divisor

    # L3
    total_students_taught = third_graders + fourth_graders + fifth_graders

    # FA
    answer = total_students_taught
    return answer