def solve():
    """Index: 1460.
    Returns: the speed needed for the remainder of the journey.
    """
    # L1
    speed_first_part = 4 # speed of 4km/hr
    time_first_part = 4 # for the first four hours
    distance_first_part = speed_first_part * time_first_part

    # L2
    total_journey_distance = 24 # journey of 24 km
    remaining_distance = total_journey_distance - distance_first_part

    # L3
    total_journey_time = 8 # in 8 hours
    remaining_time = total_journey_time - time_first_part

    # L4
    required_speed = remaining_distance / remaining_time

    # FA
    answer = required_speed
    return answer