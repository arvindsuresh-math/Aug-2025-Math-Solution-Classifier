def solve():
    """Index: 1915.
    Returns: the cost in dollars to build 4 birdhouses.
    """
    # L1
    planks_per_birdhouse = 7 # Building one birdhouse requires 7 planks
    plank_cost = 3 # one plank costs $3
    plank_total_cost = planks_per_birdhouse * plank_cost

    # L2
    nails_per_birdhouse = 20 # 20 nails
    nail_cost = 0.05 # 1 nail costs $0.05
    nail_total_cost = nails_per_birdhouse * nail_cost

    # L3
    single_birdhouse_cost = plank_total_cost + nail_total_cost

    # L4
    num_birdhouses = 4 # to build 4 birdhouses
    total_cost = num_birdhouses * single_birdhouse_cost

    # FA
    answer = total_cost
    return answer