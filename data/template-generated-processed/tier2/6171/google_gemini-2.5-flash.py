def solve():
    """Index: 6171.
    Returns: the total money Ted needs to purchase the produce.
    """
    # L1
    num_bananas = 5 # 5 bananas
    cost_per_banana = 2 # $2 each
    cost_bananas = num_bananas * cost_per_banana

    # L2
    num_oranges = 10 # 10 oranges
    cost_per_orange = 1.50 # $1.50 each
    cost_oranges = num_oranges * cost_per_orange

    # L3
    total_cost = cost_bananas + cost_oranges

    # FA
    answer = total_cost
    return answer