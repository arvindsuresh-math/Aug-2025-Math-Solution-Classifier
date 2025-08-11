def solve():
    """Index: 4671.
    Returns: the average minutes per stop the delivery person needs.
    """
    # L1
    initial_potential_stops = 12 # 12 pizzas to deliver
    stops_consolidated = 2 # two of the stops are for orders of two pizzas
    total_stops = initial_potential_stops - stops_consolidated

    # L2
    total_delivery_time = 40 # deliver all of the pizzas in 40 minutes
    minutes_per_stop_average = total_delivery_time / total_stops

    # FA
    answer = minutes_per_stop_average
    return answer