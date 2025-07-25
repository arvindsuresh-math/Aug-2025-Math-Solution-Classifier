def solve():
    """Index: 6395.
    Returns: the total amount the client has to pay for the ladders.
    """
    # L1
    num_ladders_type1 = 10 # 10 ladders
    rungs_per_ladder_type1 = 50 # 50 rungs
    total_rungs_type1 = num_ladders_type1 * rungs_per_ladder_type1

    # L2
    num_ladders_type2 = 20 # 20 ladders
    rungs_per_ladder_type2 = 60 # 60 rungs
    total_rungs_type2 = num_ladders_type2 * rungs_per_ladder_type2

    # L3
    total_rungs_overall = total_rungs_type2 + total_rungs_type1

    # L4
    cost_per_rung = 2 # $2 for every rung
    total_cost = cost_per_rung * total_rungs_overall

    # FA
    answer = total_cost
    return answer