def solve():
    """Index: 3871.
    Returns: the number of markers each student in the last group receives.
    """
    # L1
    students_group1 = 10 # The first group has 10 students
    markers_per_student_group1 = 2 # who will have 2 markers each
    markers_used_group1 = students_group1 * markers_per_student_group1

    # L2
    students_group2 = 15 # the second group has 15 students
    markers_per_student_group2 = 4 # who will have 4 markers each
    markers_used_group2 = students_group2 * markers_per_student_group2

    # L3
    total_markers_used_groups1_2 = markers_used_group1 + markers_used_group2

    # L4
    markers_per_box = 5 # If each box of markers contains 5 markers
    num_boxes = 22 # from the 22 boxes of markers
    total_markers_available = markers_per_box * num_boxes

    # L5
    remaining_markers_for_last_group = total_markers_available - total_markers_used_groups1_2

    # L6
    total_students = 30 # Each of the 30 students
    students_in_last_group = total_students - students_group1 - students_group2

    # L7
    markers_per_student_last_group = remaining_markers_for_last_group / students_in_last_group

    # FA
    answer = markers_per_student_last_group
    return answer