def solve():
    """Index: 1806.
    Returns: the total duration of the trip in hours.
    """
    # L1
    hours_driven = 5 # He drove 5 hours
    multiplier_traffic = 2 # twice as long
    traffic_hours = hours_driven * multiplier_traffic

    # L2
    total_trip_hours = traffic_hours + hours_driven

    # FA
    answer = total_trip_hours
    return answer