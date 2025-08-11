def solve():
    """Index: 6618.
    Returns: the total number of clothes Martha will take home.
    """
    # L1
    bought_jackets = 4 # buy 4 jackets
    jackets_for_free_divisor = 2 # For every 2 jackets she buys, she gets 1 free jacket
    free_jackets = bought_jackets / jackets_for_free_divisor

    # L2
    bought_tshirts = 9 # buy 9 t-shirts
    tshirts_for_free_divisor = 3 # For every 3 t-shirts she buys, she gets 1 free t-shirt
    free_tshirts = bought_tshirts / tshirts_for_free_divisor

    # L3
    total_jackets = bought_jackets + free_jackets

    # L4
    total_tshirts = bought_tshirts + free_tshirts

    # L5
    total_clothes = total_jackets + total_tshirts

    # FA
    answer = total_clothes
    return answer