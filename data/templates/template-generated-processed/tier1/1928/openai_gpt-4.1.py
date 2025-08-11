def solve():
    """Index: 1928.
    Returns: the total number of passengers transported between both stations that day.
    """
    # L1
    passengers_one_way = 100 # carried 100 passengers from one station to the other one way
    passengers_return = 60 # and on the return trip carried 60 passengers
    first_round_trip_total = passengers_one_way + passengers_return

    # L2
    additional_round_trips = 3 # train made three more round trips
    additional_trips_total = additional_round_trips * first_round_trip_total

    # L3
    total_passengers = first_round_trip_total + additional_trips_total

    # FA
    answer = total_passengers
    return answer