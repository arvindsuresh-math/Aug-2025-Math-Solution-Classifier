def solve():
    """Index: 3238.
    Returns: the total time it takes Jill to run up and down the hill.
    """
    # L1
    hill_distance = 900 # 900 foot hill
    speed_up_hill = 9 # 9 feet/second
    time_up_hill = hill_distance / speed_up_hill

    # L2
    speed_down_hill = 12 # 12 feet/second
    time_down_hill = hill_distance / speed_down_hill

    # L3
    total_time = time_up_hill + time_down_hill

    # FA
    answer = total_time
    return answer