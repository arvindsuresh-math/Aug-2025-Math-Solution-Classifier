def solve():
    """Index: 78.
    Returns: the number of cookie slices left after everyone has one piece.
    """
    # L1
    num_pies = 3 # 3 birthday cookie pies
    slices_per_pie = 10 # each of the cookie pies were cut into 10 slices
    total_slices = num_pies * slices_per_pie

    # L2
    num_classmates = 24 # 24 classmates
    num_teachers = 1 # his teacher, Mr. Keith
    manny = 1 # Manny
    total_people = num_classmates + num_teachers + manny

    # L3
    slices_left = total_slices - total_people

    # FA
    answer = slices_left
    return answer