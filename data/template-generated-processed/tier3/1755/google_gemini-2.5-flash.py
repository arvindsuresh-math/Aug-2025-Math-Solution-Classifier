def solve():
    """Index: 1755.
    Returns: the total time the trip took.
    """
    # L1
    normal_distance = 150 # His normal trip is 150 miles
    normal_time = 3 # would take him 3 hours
    speed = normal_distance / normal_time

    # L2
    out_of_way_distance = 50 # driving 50 miles out of the way
    detour_multiplier = 2 # WK
    detour_distance = out_of_way_distance * detour_multiplier

    # L3
    detour_time = detour_distance / speed

    # L4
    total_trip_time = normal_time + detour_time

    # FA
    answer = total_trip_time
    return answer