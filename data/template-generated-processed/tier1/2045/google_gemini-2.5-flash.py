def solve():
    """Index: 2045.
    Returns: the total time Andrew takes to reach the Bronx from Manhattan.
    """
    # L1
    subway_time = 10 # rides the subway for 10 hours
    multiplier_train_subway = 2 # twice as much time as the subway ride
    train_time = multiplier_train_subway * subway_time

    # L2
    subway_train_total_time = subway_time + train_time

    # L3
    bike_time = 8 # bikes the remaining distance for 8 hours
    total_travel_time = subway_train_total_time + bike_time

    # FA
    answer = total_travel_time
    return answer