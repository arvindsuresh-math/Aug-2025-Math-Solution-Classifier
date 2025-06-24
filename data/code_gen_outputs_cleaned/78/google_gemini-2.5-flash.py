def solve(
        num_cookie_pies: int = 3, # Manny had 3 birthday cookie pies
        num_classmates: int = 24, # to share with his 24 classmates
        num_teacher: int = 1, # and his teacher, Mr. Keith
        num_slices_per_pie: int = 10, # each of the cookie pies were cut into 10 slices
        manny_pieces: int = 1, # Manny ... all had 1 piece
        classmate_pieces: int = 1, # his classmates ... all had 1 piece
        teacher_pieces: int = 1 # Mr. Keith all had 1 piece
    ):
    """Index: 78.
    Returns: the number of cookie slices left after everyone has had one piece.
    """
    #: L1
    total_cookie_slices = num_cookie_pies * num_slices_per_pie

    #: L2
    total_people_who_ate = num_classmates + num_teacher + manny_pieces

    #: L3
    slices_left = total_cookie_slices - total_people_who_ate

    answer = slices_left # FINAL ANSWER
    return answer