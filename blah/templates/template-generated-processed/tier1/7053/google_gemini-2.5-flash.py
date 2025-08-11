def solve():
    """Index: 7053.
    Returns: the total number of marbles the magician has left.
    """
    # L1
    initial_red_marbles = 20 # 20 red marbles
    taken_red_marbles = 3 # takes away 3 red marbles
    remaining_red_marbles = initial_red_marbles - taken_red_marbles

    # L2
    multiplier_blue_marbles = 4 # four times as many blue marbles as red marbles
    taken_blue_marbles = multiplier_blue_marbles * taken_red_marbles

    # L3
    initial_blue_marbles = 30 # 30 blue marbles
    remaining_blue_marbles = initial_blue_marbles - taken_blue_marbles

    # L4
    total_marbles_left = remaining_red_marbles + remaining_blue_marbles

    # FA
    answer = total_marbles_left
    return answer