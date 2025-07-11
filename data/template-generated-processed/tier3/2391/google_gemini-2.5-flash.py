def solve():
    """Index: 2391.
    Returns: the number of pieces of chocolate candy Lucas will make.
    """
    # L1
    pieces_per_student = 4 # 4 pieces of chocolate candy for each of his students
    total_pieces_last_monday = 40 # He made 40 pieces of chocolate candy last Monday
    num_students_last_monday = total_pieces_last_monday / pieces_per_student

    # L2
    students_not_coming = 3 # 3 of Lucas' students will not be coming to class
    num_students_this_monday = num_students_last_monday - students_not_coming

    # L3
    chocolate_candy_this_monday = pieces_per_student * num_students_this_monday

    # FA
    answer = chocolate_candy_this_monday
    return answer