def solve(
    num_cookie_pies: int = 3,  # Manny had 3 birthday cookie pies
    slices_per_pie: int = 10,  # each of the cookie pies were cut into 10 slices
    num_classmates: int = 24,  # Manny had 24 classmates
    num_teachers: int = 1,     # his teacher, Mr. Keith
    num_manny: int = 1         # Manny himself
):
    """Index: 78.
    Returns: the number of cookie slices left after everyone has one slice.
    """

    #: L1
    total_slices = 31 # eval: 31 = 31

    #: L2
    total_people = num_classmates + num_teachers + num_manny # eval: 26 = 24 + 1 + 1

    #: L3
    slices_left = total_slices - total_people # eval: 5 = 31 - 26

    #: FA
    answer = slices_left
    return answer # eval: return 5
