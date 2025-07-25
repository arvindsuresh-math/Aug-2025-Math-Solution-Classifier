def solve():
    """Index: 3456.
    Returns: the number of students in the fourth group.
    """
    # L1
    group1_students = 5 # One group had 5 students
    group2_students = 8 # another 8 students
    group3_students = 7 # and the third 7 students
    students_in_first_three_groups = group1_students + group2_students + group3_students

    # L2
    total_students = 24 # 24 total students
    students_in_fourth_group = total_students - students_in_first_three_groups

    # FA
    answer = students_in_fourth_group
    return answer