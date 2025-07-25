def solve():
    """Index: 2284.
    Returns: the number of students in the third studio.
    """
    # L1
    students_studio1 = 110 # 110 students
    students_studio2 = 135 # 135 students
    students_first_two_studios = students_studio1 + students_studio2

    # L2
    total_students = 376 # 376 students
    students_studio3 = total_students - students_first_two_studios

    # FA
    answer = students_studio3
    return answer