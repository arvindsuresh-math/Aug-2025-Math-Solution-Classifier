def solve():
    """Index: 1294.
    Returns: the total number of hours Tom is able to get to the "Virgo" island.
    """
    # L1
    plane_multiplier = 4 # four times longer
    boat_trip_duration = 2 # 2 hours
    plane_trip_duration = plane_multiplier * boat_trip_duration

    # L2
    total_journey_duration = plane_trip_duration + boat_trip_duration

    # FA
    answer = total_journey_duration
    return answer