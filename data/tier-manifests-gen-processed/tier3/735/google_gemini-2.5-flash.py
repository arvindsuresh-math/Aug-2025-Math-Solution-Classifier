def solve():
    """Index: 735.
    Returns: the required speed in miles per hour.
    """
    # L1
    time_minutes = 10 # 10 minutes
    distance_miles = 5 # 5 mile lake
    minutes_per_mile = time_minutes / distance_miles

    # L2
    minutes_per_hour = 60 # WK
    speed_mph = minutes_per_hour / minutes_per_mile

    # FA
    answer = speed_mph
    return answer