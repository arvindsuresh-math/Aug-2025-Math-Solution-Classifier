def solve():
    """Index: 3224.
    Returns: the total distance Stephen rides his bicycle to church in miles.
    """
    # L1
    minutes_per_third_trip = 15 # If each third of his trip takes 15 minutes
    minutes_per_hour = 60 # WK
    time_per_third_trip_hours = minutes_per_third_trip / minutes_per_hour

    # L2
    speed_first_third = 16 # 16 miles per hour
    distance_first_third = speed_first_third * time_per_third_trip_hours

    # L3
    speed_second_third = 12 # 12 miles per hour
    distance_second_third = speed_second_third * time_per_third_trip_hours

    # L4
    speed_third_third = 20 # 20 miles per hour
    distance_third_third = speed_third_third * time_per_third_trip_hours

    # L5
    total_distance = distance_first_third + distance_second_third + distance_third_third

    # FA
    answer = total_distance
    return answer