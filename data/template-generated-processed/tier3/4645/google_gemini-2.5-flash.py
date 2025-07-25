def solve():
    """Index: 4645.
    Returns: the number of marbles left in the box.
    """
    # L1
    total_marbles = 50 # 50 marbles in a box
    white_marbles_original = 20 # 20 white marbles
    red_blue_marbles_total = total_marbles - white_marbles_original

    # L2
    divisor_for_equal_colors = 2 # an equal number of red and blue marbles
    marbles_per_color = red_blue_marbles_total / divisor_for_equal_colors

    # L3
    difference_white_blue = white_marbles_original - marbles_per_color

    # L4
    double_factor = 2 # double the difference
    marbles_removed = difference_white_blue * double_factor

    # L5
    marbles_left = total_marbles - marbles_removed

    # FA
    answer = marbles_left
    return answer