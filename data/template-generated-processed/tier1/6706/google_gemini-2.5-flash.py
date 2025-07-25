def solve():
    """Index: 6706.
    Returns: the number of students in Grade 6.
    """
    # L1
    grade_4_students = 30 # 30 students in Grade 4
    grade_5_students = 35 # 35 students in Grade 5
    students_grade_4_and_5 = grade_4_students + grade_5_students

    # L2
    total_students = 100 # 100 students in Grades 4, 5, and 6
    students_grade_6 = total_students - students_grade_4_and_5

    # FA
    answer = students_grade_6
    return answer