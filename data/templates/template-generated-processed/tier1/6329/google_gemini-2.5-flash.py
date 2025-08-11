def solve():
    """Index: 6329.
    Returns: the number of students remaining.
    """
    # L1
    num_groups = 3 # 3 groups
    students_per_group = 8 # 8
    initial_students = num_groups * students_per_group

    # L2
    students_left_early = 2 # 2 students left early
    remaining_students = initial_students - students_left_early

    # FA
    answer = remaining_students
    return answer