def solve(
    num_cookie_pies: int = 3, # Manny had 3 birthday cookie pies
    num_classmates: int = 24, # share with his 24 classmates
    num_teachers: int = 1, # and his teacher, Mr. Keith
    slices_per_pie: int = 10, # each of the cookie pies were cut into 10 slices
    slices_per_person: int = 1 # Manny, his classmates, and Mr. Keith all had 1 piece
):
    """Index: 78.
    Returns: the number of cookie slices left.
    """

    #: L1
    total_slices = num_cookie_pies * slices_per_pie # eval: 30 = 3 * 10

    #: L2

    #: L3
    slices_left = total_slices - num_cookie_pies # eval: 27 = 30 - 3

    #: FA
    answer = slices_left
    return answer # eval: return 27
