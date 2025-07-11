def solve():
    """Index: 2373.
    Returns: the number of adults on the bus.
    """
    # L1
    total_passengers = 60 # 60 passengers on a bus
    children_percent_num = 25 # 25% of the bus riders
    percent_factor = 0.01 # WK
    num_children = total_passengers * children_percent_num * percent_factor

    # L2
    num_adults = total_passengers - num_children

    # FA
    answer = num_adults
    return answer