def solve():
    """Index: 1976.
    Returns: the number of boats left.
    """
    # L1
    total_boats = 30 # Madison makes 30 paper boats
    eaten_percent = 20 # 20% are eaten by fish
    percent_factor = 0.01 # WK
    boats_eaten_by_fish = total_boats * eaten_percent * percent_factor

    # L2
    shot_boats = 2 # shoots two of the others
    boats_left = total_boats - boats_eaten_by_fish - shot_boats

    # FA
    answer = boats_left
    return answer