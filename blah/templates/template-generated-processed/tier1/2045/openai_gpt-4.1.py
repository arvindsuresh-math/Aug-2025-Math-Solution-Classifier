def solve():
    """Index: 2045.
    Returns: the total time Andrew takes to reach the Bronx from Manhattan.
    """
    # L1
    subway_hours = 10 # rides the subway for 10 hours
    train_multiplier = 2 # twice as much time as the subway ride
    train_hours = train_multiplier * subway_hours

    # L2
    subway_and_train_hours = subway_hours + train_hours

    # L3
    bike_hours = 8 # bikes the remaining distance for 8 hours
    total_time = subway_and_train_hours + bike_hours

    # FA
    answer = total_time
    return answer