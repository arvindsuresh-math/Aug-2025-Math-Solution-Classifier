def solve(
    num_cookie_pies: int = 3,  # Manny had 3 birthday cookie pies
    slices_per_pie: int = 10,  # each of the cookie pies were cut into 10 slices
    num_classmates: int = 24,  # Manny's 24 classmates
    num_teachers: int = 1      # his teacher, Mr. Keith
):
    """Index: 78.
    Returns: the number of cookie slices left after Manny, his classmates, and his teacher each have one slice.
    """
    #: L1
    total_slices = num_cookie_pies * slices_per_pie

    #: L2
    total_people = num_classmates + 1 + num_teachers  # Manny + classmates + teacher

    #: L3
    slices_left = total_slices - total_people

    answer = slices_left  # FINAL ANSWER
    return answer