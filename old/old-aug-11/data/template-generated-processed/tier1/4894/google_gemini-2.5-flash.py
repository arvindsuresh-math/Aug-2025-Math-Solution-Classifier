def solve():
    """Index: 4894.
    Returns: the total number of students in all grades.
    """
    # L1
    students_3rd_grade = 19 # 19 students in the 3rd grade

    # L2
    multiplier_4th_grade = 2 # twice that number
    students_4th_grade = multiplier_4th_grade * students_3rd_grade

    # L3
    boys_2nd_grade = 10 # 10 boys
    girls_2nd_grade = 19 # 19 girls
    students_2nd_grade = boys_2nd_grade + girls_2nd_grade

    # L4
    total_students = students_3rd_grade + students_4th_grade + students_2nd_grade

    # FA
    answer = total_students
    return answer