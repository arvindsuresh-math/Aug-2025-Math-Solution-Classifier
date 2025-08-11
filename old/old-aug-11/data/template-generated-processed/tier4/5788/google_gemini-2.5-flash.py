def solve():
    """Index: 5788.
    Returns: the time in minutes it would take Birgit to go 8 kilometers.
    """
    # L1
    hiking_hours = 3.5 # 3.5 hours
    minutes_per_hour = 60 # WK
    minutes_hiking = hiking_hours * minutes_per_hour

    # L2
    distance_km = 21 # 21 kilometers in that time
    average_speed_min_per_km = minutes_hiking / distance_km

    # L3
    birgit_speed_difference = 4 # 4 minutes/km faster
    birgit_speed_min_per_km = average_speed_min_per_km - birgit_speed_difference

    # L4
    target_distance_km = 8 # to go 8 kilometers
    birgit_time_for_target_distance = birgit_speed_min_per_km * target_distance_km

    # FA
    answer = birgit_time_for_target_distance
    return answer