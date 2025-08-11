def solve():
    """Index: 6164.
    Returns: the total amount Adam paid for shopping.
    """
    # L1
    num_sandwiches = 3 # 3 sandwiches
    price_per_sandwich = 3 # $3 each
    cost_sandwiches = num_sandwiches * price_per_sandwich

    # L2
    cost_water = 2 # a bottle of water for $2
    total_cost = cost_water + cost_sandwiches

    # FA
    answer = total_cost
    return answer