def solve():
    """Index: 6777.
    Returns: the total kilometers traveled during the journey.
    """
    # L1
    total_trip_duration = 8 # an eight-hour business trip
    half_factor = 0.5 # first half of the trip
    half_trip_duration = total_trip_duration * half_factor

    # L2
    speed_first_half = 70 # speed of 70 kilometers per hour
    distance_first_half = half_trip_duration * speed_first_half

    # L3
    speed_second_half = 85 # speed of 85 kilometers per hour
    distance_second_half = half_trip_duration * speed_second_half

    # L4
    total_distance = distance_first_half + distance_second_half

    # FA
    answer = total_distance
    return answer