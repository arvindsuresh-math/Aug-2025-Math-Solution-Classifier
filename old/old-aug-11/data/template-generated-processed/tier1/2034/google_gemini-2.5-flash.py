def solve():
    """Index: 2034.
    Returns: the duration of Luke's bus ride in minutes.
    """
    # L1
    total_trip_hours = 8 # 8 hours
    train_ride_hours = 6 # 6-hour train ride
    time_before_train_hours = total_trip_hours - train_ride_hours

    # L2
    minutes_per_hour = 60 # WK
    time_before_train_minutes = time_before_train_hours * minutes_per_hour

    # L3
    walk_time_minutes = 15 # walk for 15 minutes
    twice_multiplier = 2 # twice this long
    wait_time_minutes = walk_time_minutes * twice_multiplier

    # L4
    bus_ride_minutes = time_before_train_minutes - wait_time_minutes - walk_time_minutes

    # FA
    answer = bus_ride_minutes
    return answer