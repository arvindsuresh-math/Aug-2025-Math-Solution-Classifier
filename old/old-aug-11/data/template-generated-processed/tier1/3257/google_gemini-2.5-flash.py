def solve():
    """Index: 3257.
    Returns: the total number of passengers on the bus at the last station.
    """
    # L1
    initial_passengers = 50 # 50 passengers on a bus
    first_stop_get_on = 16 # 16 more passengers get on the bus
    passengers_after_first_stop = initial_passengers + first_stop_get_on

    # L2
    other_stops_get_off = 22 # 22 passengers get off the bus
    passengers_after_get_off = passengers_after_first_stop - other_stops_get_off

    # L3
    other_stops_get_on = 5 # 5 passengers more get on the bus
    final_passengers = passengers_after_get_off + other_stops_get_on

    # FA
    answer = final_passengers
    return answer