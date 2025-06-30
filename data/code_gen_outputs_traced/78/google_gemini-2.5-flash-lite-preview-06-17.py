def solve(
    num_pies: int = 3, # Manny had 3 birthday cookie pies
    num_classmates: int = 24, # to share with his 24 classmates
    num_teacher: int = 1, # and his teacher, Mr. Keith.
    slices_per_pie: int = 10, # If each of the cookie pies were cut into 10 slices
    num_pieces_eaten_per_person: int = 1 # Manny, his classmates, and Mr. Keith all had 1 piece
):
    """Index: 78.
    Returns: the number of cookie slices left.
    """
    #: L1
    total_slices = num_pies * slices_per_pie # eval: 30 = 3 * 10
    #: L2
    total_people = num_classmates + num_teacher + num_pieces_eaten_per_person # eval: 26 = 24 + 1 + 1
    #: L3
    slices_left = total_slices - total_people # eval: 4 = 30 - 26
    answer = slices_left # FINAL ANSWER # eval: 4 = 4 # FINAL ANSWER
    return answer # eval: return 4