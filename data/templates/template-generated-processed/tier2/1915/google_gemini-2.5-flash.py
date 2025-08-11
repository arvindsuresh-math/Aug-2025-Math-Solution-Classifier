def solve():
    """Index: 1915.
    Returns: the total cost to build 4 birdhouses.
    """
    # L1
    planks_per_birdhouse = 7 # 7 planks
    cost_per_plank = 3 # one plank costs $3
    cost_planks_one_birdhouse = planks_per_birdhouse * cost_per_plank

    # L2
    nails_per_birdhouse = 20 # 20 nails
    cost_per_nail = 0.05 # 1 nail costs $0.05
    cost_nails_one_birdhouse = nails_per_birdhouse * cost_per_nail

    # L3
    total_cost_one_birdhouse = cost_planks_one_birdhouse + cost_nails_one_birdhouse

    # L4
    num_birdhouses = 4 # build 4 birdhouses
    total_cost_four_birdhouses = num_birdhouses * total_cost_one_birdhouse

    # FA
    answer = total_cost_four_birdhouses
    return answer