def solve():
    """Index: 2186.
    Returns: the total number of miles Jeff traveled on his trip.
    """
    # L1
    speed1 = 80 # driving at 80 miles/hour
    time1 = 6 # for about 6 hours
    distance1 = speed1 * time1

    # L2
    speed2 = 60 # slow down to 60 miles/hour
    time2 = 4 # for 4 hours
    distance2 = speed2 * time2

    # L3
    speed3 = 40 # drove at 40 miles/hour
    time3 = 2 # for 2 hours
    distance3 = speed3 * time3

    # L4
    total_distance = distance1 + distance2 + distance3

    # FA
    answer = total_distance
    return answer