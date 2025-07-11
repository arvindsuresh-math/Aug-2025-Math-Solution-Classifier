def solve():
    """Index: 1090.
    Returns: the number of students Beth had in her class at the end of her final year.
    """
    # L1
    initial_students = 150 # 150 students in her 10th-grade class
    students_joined = 30 # 30 more students join
    students_after_joining = initial_students + students_joined

    # L2
    students_left = 15 # 15 students left
    final_students = students_after_joining - students_left

    # FA
    answer = final_students
    return answer