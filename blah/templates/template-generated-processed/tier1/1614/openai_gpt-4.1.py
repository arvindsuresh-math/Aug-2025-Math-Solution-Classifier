def solve():
    """Index: 1614.
    Returns: the number of hours Joseph saves by taking route B both ways instead of route A.
    """
    # L1
    route_a_one_way = 5 # it will take him 5 hours to arrive
    round_trip_multiplier = 2 # both ways (to Boston and back)
    route_a_total = route_a_one_way * round_trip_multiplier

    # L2
    route_b_one_way = 2 # it will only take him 2 hours to arrive
    route_b_total = route_b_one_way * round_trip_multiplier

    # L3
    time_saved = route_a_total - route_b_total

    # FA
    answer = time_saved
    return answer