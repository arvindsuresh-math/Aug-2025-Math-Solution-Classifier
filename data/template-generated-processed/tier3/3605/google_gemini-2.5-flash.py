def solve():
    """Index: 3605.
    Returns: the number of hours it will take you to get to the destination.
    """
    # L1
    mr_harris_walk_time = 2 # Mr. Harris took 2 hours to walk to the store
    distance_multiplier = 3 # 3 times further away
    mr_harris_time_to_your_destination = mr_harris_walk_time * distance_multiplier

    # L2
    speed_multiplier = 2 # twice as fast
    your_walk_time = mr_harris_time_to_your_destination / speed_multiplier

    # FA
    answer = your_walk_time
    return answer