def solve():
    """Index: 4944.
    Returns: the cost per trip to the park.
    """
    # L1
    num_sons = 2 # each of his sons
    pass_cost_each = 100.00 # $100.00 each
    total_pass_cost = num_sons * pass_cost_each

    # L2
    oldest_son_trips = 35 # oldest son went to the park 35 times
    youngest_son_trips = 15 # youngest went 15 times
    total_trips = oldest_son_trips + youngest_son_trips

    # L3
    cost_per_trip = total_pass_cost / total_trips

    # FA
    answer = cost_per_trip
    return answer