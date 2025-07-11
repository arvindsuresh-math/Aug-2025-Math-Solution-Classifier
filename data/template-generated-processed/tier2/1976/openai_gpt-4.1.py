def solve():
    """Index: 1976.
    Returns: the number of boats left after some are eaten and some are destroyed.
    """
    # L1
    total_boats = 30 # Madison makes 30 paper boats
    percent_eaten_num = 20 # 20% are eaten by fish
    percent_factor = 0.01 # WK
    boats_eaten = total_boats * percent_eaten_num * percent_factor

    # L2
    boats_destroyed_by_arrows = 2 # Madison shoots two of the others
    boats_left = total_boats - boats_eaten - boats_destroyed_by_arrows

    # FA
    answer = boats_left
    return answer