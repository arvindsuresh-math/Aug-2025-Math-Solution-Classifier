def solve():
    """Index: 7407.
    Returns: the total number of pencils sold.
    """
    # L1
    num_first_students = 2 # The first two students
    pencils_per_first_student = 2 # bought 2 pencils each
    pencils_first_group = num_first_students * pencils_per_first_student

    # L2
    num_next_students = 6 # The next six students
    pencils_per_next_student = 3 # bought three pencils each
    pencils_next_group = num_next_students * pencils_per_next_student

    # L3
    pencils_last_student_1 = 1 # only bought one pencil each
    pencils_last_student_2 = 1 # only bought one pencil each
    pencils_last_group = pencils_last_student_1 + pencils_last_student_2

    # L4
    total_pencils_sold = pencils_first_group + pencils_next_group + pencils_last_group

    # FA
    answer = total_pencils_sold
    return answer