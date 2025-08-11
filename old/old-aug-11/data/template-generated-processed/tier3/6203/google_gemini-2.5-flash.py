def solve():
    """Index: 6203.
    Returns: the cost of 5 spoons sold separately.
    """
    # L1
    total_cost_7_spoons = 21 # A set of 7 spoons costs $21
    num_spoons_in_set = 7 # A set of 7 spoons
    cost_per_spoon = total_cost_7_spoons / num_spoons_in_set

    # L2
    num_spoons_to_buy = 5 # how much would 5 spoons cost
    cost_of_5_spoons = num_spoons_to_buy * cost_per_spoon

    # FA
    answer = cost_of_5_spoons
    return answer