def solve():
    """Index: 1233.
    Returns: the total number of miles Kevin ran.
    """
    # L1
    speed1 = 10 # ran at 10 miles per hour
    time1 = 0.5 # for half an hour
    distance1 = speed1 * time1

    # L2
    speed2 = 20 # ran at 20 miles per hour
    time2 = 0.5 # for half an hour
    distance2 = speed2 * time2

    # L3
    speed3 = 8 # ran at 8 miles per hour
    time3 = 0.25 # 15 minutes is a quarter of an hour
    distance3 = speed3 * time3

    # L4
    total_distance = distance1 + distance2 + distance3

    # FA
    answer = total_distance
    return answer