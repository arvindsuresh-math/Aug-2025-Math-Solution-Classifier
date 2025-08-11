def solve():
    """Index: 4558.
    Returns: the number of slices of pizza left.
    """
    # L1
    total_slices = 16 # cut into 16 slices
    dinner_eaten_denominator = 4 # one-fourth of it
    dinner_eaten_slices = total_slices / dinner_eaten_denominator

    # L2
    slices_left_after_dinner = total_slices - dinner_eaten_slices

    # L3
    yves_eaten_denominator = 4 # one-fourth of the remaining pizza
    yves_eaten_slices = slices_left_after_dinner / yves_eaten_denominator

    # L4
    slices_left_after_yves = slices_left_after_dinner - yves_eaten_slices

    # L5
    num_siblings = 2 # his two siblings
    slices_per_sibling = 2 # ate 2 slices each
    siblings_eaten_slices = slices_per_sibling * num_siblings

    # L6
    final_slices_left = slices_left_after_yves - siblings_eaten_slices

    # FA
    answer = final_slices_left
    return answer