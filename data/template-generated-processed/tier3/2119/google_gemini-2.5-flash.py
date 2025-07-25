def solve():
    """Index: 2119.
    Returns: the number of oranges less each student will get.
    """
    # L1
    initial_total_oranges = 108 # 108 oranges
    num_students = 12 # 12 students
    oranges_per_student_initial = initial_total_oranges / num_students

    # L2
    bad_oranges = 36 # 36 of the oranges were bad
    remaining_oranges = initial_total_oranges - bad_oranges

    # L3
    oranges_per_student_after_removal = remaining_oranges / num_students

    # L4
    oranges_less_per_student = oranges_per_student_initial - oranges_per_student_after_removal

    # FA
    answer = oranges_less_per_student
    return answer