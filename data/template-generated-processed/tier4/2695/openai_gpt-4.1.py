def solve():
    """Index: 2695.
    Returns: the total time Marcus spends with his dog in minutes.
    """
    # L1
    bath_minutes = 20 # Marcus spends 20 minutes giving his dog a bath
    blowdry_divisor = 2 # half as long blow-drying her
    blowdry_minutes = bath_minutes / blowdry_divisor

    # L2
    walk_distance_miles = 3 # 3-mile trail
    walk_speed_mph = 6 # Marcus walks at 6 miles per hour
    walk_time_hours = walk_distance_miles / walk_speed_mph

    # L3
    minutes_per_hour = 60 # WK
    walk_time_minutes = walk_time_hours * minutes_per_hour

    # L4
    total_time_minutes = blowdry_minutes + bath_minutes + walk_time_minutes

    # FA
    answer = total_time_minutes
    return answer