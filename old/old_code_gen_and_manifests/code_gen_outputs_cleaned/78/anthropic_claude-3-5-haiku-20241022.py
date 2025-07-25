def solve(
    num_cookie_pies: int = 3,  # Manny had 3 birthday cookie pies
    slices_per_pie: int = 10,  # each of the cookie pies were cut into 10 slices
    num_classmates: int = 24,  # 24 classmates
    num_teachers: int = 1  # Mr. Keith
):
    """Index: 78.
    Returns: the number of cookie slices left after everyone has one piece."""
    #: L1
    total_slices = num_cookie_pies * slices_per_pie

    #: L2
    total_people_eating = num_classmates + num_teachers + 1  # +1 for Manny himself

    #: L3
    slices_left = total_slices - total_people_eating

    answer = slices_left  # FINAL ANSWER
    return answer