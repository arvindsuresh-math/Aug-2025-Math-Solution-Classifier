def solve():
    """Index: 2695.
    Returns: the total time Marcus spends with his dog in minutes.
    """
    # L1
    bath_time_minutes = 20 # 20 minutes giving his dog a bath
    blow_dry_divisor = 2 # half as long blow-drying her
    blow_dry_time_minutes = bath_time_minutes / blow_dry_divisor

    # L2
    trail_distance_miles = 3 # 3-mile trail
    walking_speed_mph = 6 # walks at 6 miles per hour
    walk_time_hours = trail_distance_miles / walking_speed_mph

    # L3
    minutes_per_hour = 60 # WK
    walk_time_minutes = walk_time_hours * minutes_per_hour

    # L4
    total_time_minutes = blow_dry_time_minutes + bath_time_minutes + walk_time_minutes

    # FA
    answer = total_time_minutes
    return answer