def solve():
    """Index: 1175.
    Returns: the amount Henry needs to pay for the pair of jeans.
    """
    # L1
    socks_cost = 5 # The socks cost $5
    tshirt_more_than_socks = 10 # the t-shirt is $10 more expensive than the socks
    tshirt_cost = socks_cost + tshirt_more_than_socks

    # L2
    multiplier_for_jeans = 2 # The jeans are twice the price of the t-shirt
    jeans_cost = multiplier_for_jeans * tshirt_cost

    # FA
    answer = jeans_cost
    return answer