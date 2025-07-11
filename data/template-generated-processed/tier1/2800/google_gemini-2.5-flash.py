def solve():
    """Index: 2800.
    Returns: the total number of students in grades 2 and 3.
    """
    # L1
    boys_second_grade = 20 # 20 boys
    girls_second_grade = 11 # 11 girls
    students_second_grade = boys_second_grade + girls_second_grade

    # L2
    multiplier_third_grade = 2 # twice that number
    students_third_grade = students_second_grade * multiplier_third_grade

    # L3
    total_students = students_second_grade + students_third_grade

    # FA
    answer = total_students
    return answer