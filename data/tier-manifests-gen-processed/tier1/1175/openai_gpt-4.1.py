def solve():
    """Index: 1175.
    Returns: the price Henry needs to pay for the pair of jeans.
    """
    # L1
    socks_price = 5 # The socks cost $5
    tshirt_more_than_socks = 10 # t-shirt is $10 more expensive than the socks
    tshirt_price = socks_price + tshirt_more_than_socks

    # L2
    jeans_multiplier = 2 # jeans are twice the price of the t-shirt
    jeans_price = jeans_multiplier * tshirt_price

    # FA
    answer = jeans_price
    return answer