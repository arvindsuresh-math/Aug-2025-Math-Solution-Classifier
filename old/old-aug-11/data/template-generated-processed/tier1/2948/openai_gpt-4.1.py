def solve():
    """Index: 2948.
    Returns: the total number of legos needed to build the 3-level pyramid.
    """
    # L1
    bottom_legos_per_side = 7 # bottom level has 7 legos per side
    bottom_legos = bottom_legos_per_side * bottom_legos_per_side

    # L2
    second_legos_per_side = bottom_legos_per_side - 1

    # L3
    second_legos = second_legos_per_side * second_legos_per_side

    # L4
    top_legos_per_side = second_legos_per_side - 1

    # L5
    top_legos = top_legos_per_side * top_legos_per_side

    # L6
    total_legos = bottom_legos + second_legos + top_legos

    # FA
    answer = total_legos
    return answer