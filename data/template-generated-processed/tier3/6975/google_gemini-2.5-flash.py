def solve():
    """Index: 6975.
    Returns: the time in minutes to travel the target distance.
    """
    # L1
    target_distance = 12 # travel 12 km
    initial_distance = 3 # To make 3 km
    distance_multiplier = target_distance / initial_distance

    # L2
    initial_time_hours = 2 # walked for 2 hours
    total_time_hours = initial_time_hours * distance_multiplier

    # L3
    minutes_per_hour = 60 # WK
    total_time_minutes = total_time_hours * minutes_per_hour

    # FA
    answer = total_time_minutes
    return answer