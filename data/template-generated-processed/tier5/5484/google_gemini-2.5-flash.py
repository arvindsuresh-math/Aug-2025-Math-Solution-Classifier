def solve():
    """Index: 5484.
    Returns: the number of red marbles.
    """
    # L4
    blue_marbles_difference = 24 # 24 more blue marbles
    blue_marbles_multiplier = 5 # 5 times as many blue marbles
    coefficient_of_x = blue_marbles_multiplier - 1
    num_red_marbles = blue_marbles_difference / coefficient_of_x
    final_red_marbles_value = num_red_marbles

    # FA
    answer = num_red_marbles
    return answer