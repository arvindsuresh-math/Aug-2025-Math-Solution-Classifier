def solve():
    """Index: 4681.
    Returns: the total number of hours Coby took to arrive at the destination.
    """
    # L1
    distance_washington_idaho = 640 # 640 miles away from Washington
    speed_washington_idaho = 80 # traveling at a speed of 80 miles per hour going to Idaho
    time_washington_idaho = distance_washington_idaho / speed_washington_idaho

    # L2
    distance_idaho_nevada = 550 # 550 miles away from Nevada
    speed_idaho_nevada = 50 # at a speed of 50 miles per hour from Idaho to Nevada
    time_idaho_nevada = distance_idaho_nevada / speed_idaho_nevada

    # L3
    total_travel_time = time_idaho_nevada + time_washington_idaho

    # FA
    answer = total_travel_time
    return answer