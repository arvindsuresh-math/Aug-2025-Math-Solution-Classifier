def solve():
    """Index: 1806.
    Returns: the total duration of Tim's trip in hours.
    """
    # L1
    driving_hours = 5 # He drove 5 hours
    traffic_multiplier = 2 # twice as long as he was driving
    traffic_hours = driving_hours * traffic_multiplier

    # L2
    total_trip_hours = traffic_hours + driving_hours

    # FA
    answer = total_trip_hours
    return answer