def solve():
    """Index: 4990.
    Returns: the number of shirts missing.
    """
    # L1
    num_trousers = 10 # 10 pairs of trousers
    cost_per_trousers = 9 # $9 for each pair of trousers
    cost_trousers = num_trousers * cost_per_trousers

    # L2
    total_bill = 140 # a bill of $140
    cost_shirts = total_bill - cost_trousers

    # L3
    cost_per_shirt = 5 # $5 per shirt
    total_shirts_laundered = cost_shirts / cost_per_shirt

    # L4
    shirts_found = 2 # only dropped off 2 shirts
    missing_shirts = total_shirts_laundered - shirts_found

    # FA
    answer = missing_shirts
    return answer