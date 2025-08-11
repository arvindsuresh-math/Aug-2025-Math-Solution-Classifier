def solve():
    """Index: 529.
    Returns: the minimum number of rides needed so the 30-day pass is strictly cheaper per ride.
    """
    # L2
    pass_cost = 50 # 30-day pass costs $50
    one_way_cost = 2 # one-way ticket costs $2
    rides_equal_cost = pass_cost / one_way_cost

    # L3
    minimum_rides = int(rides_equal_cost) + 1

    # FA
    answer = minimum_rides
    return answer