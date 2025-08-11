def solve():
    """Index: 1554.
    Returns: the total time it takes Jerry to throw all cans away.
    """
    # L1
    total_cans = 28 # 28 cans on Jerry's desk
    cans_per_trip = 4 # carry four cans at once
    number_of_trips = total_cans / cans_per_trip

    # L2
    time_per_way = 10 # ten seconds each way
    ways_in_round_trip = 2 # WK
    round_trip_time = time_per_way * ways_in_round_trip

    # L3
    drain_time_per_trip = 30 # 30 seconds to drain those 4 cans
    total_time_per_trip = round_trip_time + drain_time_per_trip

    # L4
    total_time_spent = total_time_per_trip * number_of_trips

    # FA
    answer = total_time_spent
    return answer