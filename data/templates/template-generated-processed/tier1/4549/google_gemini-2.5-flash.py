def solve():
    """Index: 4549.
    Returns: the total time for the car's round trip.
    """
    # L1
    bus_trip_time = 40 # bus takes 40 minutes
    car_time_fewer_minutes = 5 # five fewer minutes
    car_one_way_time = bus_trip_time - car_time_fewer_minutes

    # L2
    car_round_trip_time = car_one_way_time + car_one_way_time

    # FA
    answer = car_round_trip_time
    return answer