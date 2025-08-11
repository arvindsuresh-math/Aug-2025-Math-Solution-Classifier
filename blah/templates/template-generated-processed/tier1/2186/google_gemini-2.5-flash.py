def solve():
    """Index: 2186.
    Returns: the total number of miles Jeff traveled.
    """
    # L1
    speed_first_stretch = 80 # driving at 80 miles/hour
    time_first_stretch = 6 # for about 6 hours
    distance_first_stretch = speed_first_stretch * time_first_stretch

    # L2
    speed_second_stretch = 60 # slow down to 60 miles/hour
    time_second_stretch = 4 # drove at this speed for 4 hours
    distance_second_stretch = speed_second_stretch * time_second_stretch

    # L3
    speed_third_stretch = 40 # drove at 40 miles/hour
    time_third_stretch = 2 # for 2 hours
    distance_third_stretch = speed_third_stretch * time_third_stretch

    # L4
    total_distance = distance_first_stretch + distance_second_stretch + distance_third_stretch

    # FA
    answer = total_distance
    return answer