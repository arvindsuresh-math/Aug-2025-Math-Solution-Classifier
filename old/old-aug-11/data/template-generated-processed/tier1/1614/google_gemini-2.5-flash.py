def solve():
    """Index: 1614.
    Returns: the time saved if Joseph takes route B to Boston and back home.
    """
    # L1
    route_a_one_way_time = 5 # 5 hours to arrive
    round_trip_multiplier = 2 # to Boston and back to his home
    route_a_round_trip_time = route_a_one_way_time * round_trip_multiplier

    # L2
    route_b_one_way_time = 2 # 2 hours to arrive
    route_b_round_trip_time = route_b_one_way_time * round_trip_multiplier

    # L3
    time_saved = route_a_round_trip_time - route_b_round_trip_time

    # FA
    answer = time_saved
    return answer