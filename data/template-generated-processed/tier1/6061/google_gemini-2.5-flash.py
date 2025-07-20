def solve():
    """Index: 6061.
    Returns: the number of yellow marbles.
    """
    # L1
    red_marbles = 14 # 14 red marbles
    blue_multiplier = 3 # three times as many blue marbles as red
    blue_marbles = red_marbles * blue_multiplier

    # L2
    total_blue_red = blue_marbles + red_marbles

    # L3
    total_marbles = 85 # 85 marbles
    yellow_marbles = total_marbles - total_blue_red

    # FA
    answer = yellow_marbles
    return answer