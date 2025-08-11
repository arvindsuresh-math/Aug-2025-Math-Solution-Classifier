def solve():
    """Index: 6261.
    Returns: the cost of one pair of pants.
    """
    # L1
    total_cost_jessica = 20 # Jessica bought 2 shirts for $20 total
    num_shirts_jessica = 2 # 2 shirts
    cost_per_shirt = total_cost_jessica / num_shirts_jessica

    # L2
    num_pants_peter = 2 # 2 pairs of pants
    num_shirts_peter = 5 # and 5 shirts
    total_cost_peter = 62 # for $62 total
    cost_of_shirts_for_peter = num_shirts_peter * cost_per_shirt

    # L3
    cost_of_pants_for_peter = total_cost_peter - cost_of_shirts_for_peter

    # L4
    cost_per_pair_of_pants = cost_of_pants_for_peter / num_pants_peter

    # FA
    answer = cost_per_pair_of_pants
    return answer