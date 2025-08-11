def solve():
    """Index: 6764.
    Returns: the total number of pieces of bread needed.
    """
    # L1
    other_students_in_group = 5 # travel in a group with 5 other students
    student_self = 1 # WK
    students_per_group = other_students_in_group + student_self

    # L2
    total_groups = 5 # a total of 5 groups
    total_students = total_groups * students_per_group

    # L3
    sandwiches_per_student = 2 # Each student needs 2 sandwiches
    total_sandwiches = total_students * sandwiches_per_student

    # L4
    pieces_of_bread_per_sandwich = 2 # WK
    total_bread_pieces = total_sandwiches * pieces_of_bread_per_sandwich

    # FA
    answer = total_bread_pieces
    return answer