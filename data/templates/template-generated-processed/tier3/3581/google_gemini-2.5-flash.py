def solve():
    """Index: 3581.
    Returns: the number of machines Darryl needs to sell to break even.
    """
    # L1
    cost_parts = 3600 # $3600 for the parts
    cost_patent = 4500 # $4500 for the patent
    total_costs = cost_parts + cost_patent

    # L2
    price_per_machine = 180 # sells for $180
    machines_to_sell = total_costs / price_per_machine

    # FA
    answer = machines_to_sell
    return answer