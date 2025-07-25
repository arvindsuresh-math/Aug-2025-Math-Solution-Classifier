def solve():
    """Index: 6422.
    Returns: the time it takes Eric to return home.
    """
    # L1
    running_time = 20 # runs for 20 minutes
    jogging_time = 10 # jogs for 10 minutes
    time_to_park = running_time + jogging_time

    # L2
    multiplier_return_trip = 3 # 3 times as long
    return_trip_time = time_to_park * multiplier_return_trip

    # FA
    answer = return_trip_time
    return answer