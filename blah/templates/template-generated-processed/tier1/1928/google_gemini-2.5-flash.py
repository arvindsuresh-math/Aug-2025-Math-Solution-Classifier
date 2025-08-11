def solve():
    """Index: 1928.
    Returns: the total number of passengers transported between both stations.
    """
    # L1
    passengers_oneway = 100 # 100 passengers from one station to the other one way
    passengers_return = 60 # on the return trip carried 60 passengers
    first_trip_total_passengers = passengers_oneway + passengers_return

    # L2
    additional_round_trips = 3 # three more round trips
    additional_trips_total_passengers = additional_round_trips * first_trip_total_passengers

    # L3
    total_passengers_transported = first_trip_total_passengers + additional_trips_total_passengers

    # FA
    answer = total_passengers_transported
    return answer