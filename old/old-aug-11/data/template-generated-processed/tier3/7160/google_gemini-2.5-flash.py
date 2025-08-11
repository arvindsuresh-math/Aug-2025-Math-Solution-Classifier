def solve():
    """Index: 7160.
    Returns: the difference in average speed between heavy traffic and no traffic.
    """
    # L1
    distance = 200 # her son's house is 200 miles away
    time_heavy_traffic = 5 # in 5 hours when there is heavy traffic
    speed_heavy_traffic = distance / time_heavy_traffic

    # L2
    time_no_traffic = 4 # takes only 4 hours
    speed_no_traffic = distance / time_no_traffic

    # L3
    speed_difference = speed_no_traffic - speed_heavy_traffic

    # FA
    answer = speed_difference
    return answer