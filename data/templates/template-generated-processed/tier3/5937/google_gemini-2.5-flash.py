def solve():
    """Index: 5937.
    Returns: the total number of marbles Beth has left.
    """
    # L1
    total_marbles = 72 # 72 marbles
    num_colors = 3 # three colors
    marbles_per_color = total_marbles / num_colors

    # L2
    lost_red_marbles = 5 # loses 5 red
    remaining_red_marbles = marbles_per_color - lost_red_marbles

    # L3
    blue_loss_multiplier = 2 # twice as many blue
    lost_blue_marbles = lost_red_marbles * blue_loss_multiplier

    # L4
    remaining_blue_marbles = marbles_per_color - lost_blue_marbles

    # L5
    yellow_loss_multiplier = 3 # three times as many yellow ones than red ones
    lost_yellow_marbles = lost_red_marbles * yellow_loss_multiplier

    # L6
    remaining_yellow_marbles = marbles_per_color - lost_yellow_marbles

    # L7
    total_marbles_left = remaining_red_marbles + remaining_blue_marbles + remaining_yellow_marbles

    # FA
    answer = total_marbles_left
    return answer