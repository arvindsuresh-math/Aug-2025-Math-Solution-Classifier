def solve():
    """Index: 3844.
    Returns: the cost of each single steak knife.
    """
    # L1
    knives_per_set = 4 # each set contains 4 steak knives
    num_sets_bought = 2 # Elizabeth buys both sets
    total_knives = knives_per_set * num_sets_bought

    # L2
    cost_per_set = 80.00 # $80.00 per set
    total_cost = cost_per_set * num_sets_bought

    # L3
    cost_per_knife = total_cost / total_knives

    # FA
    answer = cost_per_knife
    return answer