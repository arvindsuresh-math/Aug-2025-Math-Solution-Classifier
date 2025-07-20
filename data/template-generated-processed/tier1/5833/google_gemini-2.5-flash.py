def solve():
    """Index: 5833.
    Returns: the total cost for the clothes.
    """
    # L1
    num_shirts = 3 # three shirts
    cost_per_shirt = 5 # Every shirt costs $5
    cost_shirts = num_shirts * cost_per_shirt

    # L2
    num_jeans = 2 # two pairs of jeans
    cost_per_jeans = 10 # a pair of jeans $10
    cost_jeans = num_jeans * cost_per_jeans

    # L3
    num_hats = 4 # four hats
    cost_per_hat = 4 # every hat $4
    cost_hats = num_hats * cost_per_hat

    # L4
    total_cost = cost_shirts + cost_jeans + cost_hats

    # FA
    answer = total_cost
    return answer