def solve():
    """Index: 3551.
    Returns: the time in minutes it takes each group to go through the museum.
    """
    # L1
    total_students = 18 # 18 students in total
    num_groups = 3 # 3 groups
    students_per_group = total_students / num_groups

    # L2
    minutes_per_student = 4 # each student takes 4 minutes
    time_per_group = students_per_group * minutes_per_student

    # FA
    answer = time_per_group
    return answer