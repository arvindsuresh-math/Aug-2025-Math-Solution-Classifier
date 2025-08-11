def solve():
    """Index: 3716.
    Returns: John's current elevation.
    """
    # L1
    rate_downward = 10 # 10 feet down per minute
    time_traveled = 5 # for 5 minutes
    distance_traveled_down = rate_downward * time_traveled

    # L2
    initial_elevation = 400 # an elevation of 400 feet
    current_elevation = initial_elevation - distance_traveled_down

    # FA
    answer = current_elevation
    return answer