def solve():
    """Index: 2862.
    Returns: the total cost of Emily's entire order.
    """
    # L1
    num_curtain_pairs = 2 # 2 pairs of curtains
    cost_per_curtain_pair = 30.00 # $30.00 each
    curtains_total_cost = num_curtain_pairs * cost_per_curtain_pair

    # L2
    num_wall_prints = 9 # 9 wall prints
    cost_per_wall_print = 15.00 # $15.00 each
    prints_total_cost = num_wall_prints * cost_per_wall_print

    # L3
    installation_service_cost = 50.00 # For $50.00 they will come to your house
    total_order_cost = curtains_total_cost + prints_total_cost + installation_service_cost

    # FA
    answer = total_order_cost
    return answer