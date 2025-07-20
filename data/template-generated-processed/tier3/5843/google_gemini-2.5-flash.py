def solve():
    """Index: 5843.
    Returns: the total number of fries Sally had for lunch.
    """
    # L1
    mark_fries = 36 # his 36 fries
    fraction_denominator = 3 # one-third of his 36 fries
    fries_from_mark = mark_fries / fraction_denominator

    # L2
    sally_initial_fries = 14 # Sally had 14 fries
    total_sally_fries = sally_initial_fries + fries_from_mark

    # FA
    answer = total_sally_fries
    return answer