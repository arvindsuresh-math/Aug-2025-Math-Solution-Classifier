def solve():
    """Index: 3795.
    Returns: the speed limit.
    """
    # L1
    distance_miles = 60 # 60 miles away
    time_hours = 1 # an hour
    natasha_speed = distance_miles / time_hours

    # L2
    speed_over_limit = 10 # 10 mph over the speed limit
    speed_limit = natasha_speed - speed_over_limit

    # FA
    answer = speed_limit
    return answer