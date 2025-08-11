def solve():
    """Index: 731.
    Returns: the total amount the clothing store will earn if all shirts and jeans are sold.
    """
    # L1
    shirt_price = 10 # A shirt costs $10 each
    num_shirts = 20 # sells 20 shirts
    shirts_total = shirt_price * num_shirts

    # L2
    jeans_price_multiplier = 2 # jeans costs twice as much
    jeans_price = shirt_price * jeans_price_multiplier

    # L3
    num_jeans = 10 # sells 10 pairs of jeans
    jeans_total = jeans_price * num_jeans

    # L4
    total_earnings = shirts_total + jeans_total

    # FA
    answer = total_earnings
    return answer