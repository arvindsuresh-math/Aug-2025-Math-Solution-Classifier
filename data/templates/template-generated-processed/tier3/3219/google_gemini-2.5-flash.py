def solve():
    """Index: 3219.
    Returns: the cost of each chair.
    """
    # L1
    total_cost = 135 # for $135
    table_cost = 55 # The patio table cost $55
    cost_of_chairs = total_cost - table_cost

    # L2
    num_chairs = 4 # and 4 chairs
    cost_per_chair = cost_of_chairs / num_chairs

    # FA
    answer = cost_per_chair
    return answer