def solve():
    """Index: 1797.
    Returns: the total amount John spends.
    """
    # L1
    tshirt_cost_each = 20 # cost $20 each
    num_tshirts = 3 # buys 3 t-shirts
    cost_tshirts = tshirt_cost_each * num_tshirts

    # L2
    cost_pants = 50 # buys $50 in pants
    total_spend = cost_tshirts + cost_pants

    # FA
    answer = total_spend
    return answer