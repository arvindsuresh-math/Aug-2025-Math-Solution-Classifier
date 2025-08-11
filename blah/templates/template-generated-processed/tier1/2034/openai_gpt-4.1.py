def solve():
    """Index: 2034.
    Returns: the number of minutes Luke's bus ride takes.
    """
    # L1
    total_trip_hours = 8 # entire trip takes him 8 hours
    train_ride_hours = 6 # 6-hour train ride
    pre_train_hours = total_trip_hours - train_ride_hours

    # L2
    minutes_per_hour = 60 # WK
    pre_train_minutes = pre_train_hours * minutes_per_hour

    # L3
    walk_minutes = 15 # walk for 15 minutes
    wait_multiplier = 2 # wait twice this long
    wait_minutes = walk_minutes * wait_multiplier

    # L4
    bus_minutes = pre_train_minutes - wait_minutes - walk_minutes

    # FA
    answer = bus_minutes
    return answer