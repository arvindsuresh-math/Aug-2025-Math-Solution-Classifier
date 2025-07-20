def solve():
    """Index: 5684.
    Returns: the total number of tissues the kindergartner groups bring together.
    """
    # L1
    group1_students = 9 # 9 students
    group2_students = 10 # 10 students
    group3_students = 11 # 11 students
    total_kindergartners = group1_students + group2_students + group3_students

    # L2
    tissues_per_box = 40 # 40 tissues
    total_tissues = total_kindergartners * tissues_per_box

    # FA
    answer = total_tissues
    return answer