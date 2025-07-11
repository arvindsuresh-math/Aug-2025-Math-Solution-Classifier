def solve():
    """Index: 1161.
    Returns: the number of cookies Meena has left after the bake sale.
    """
    # L1
    meena_dozen = 5 # 5 dozen cookies
    dozen = 12 # WK
    total_baked = meena_dozen * dozen

    # L2
    mr_stone_dozen = 2 # 2 dozen cookies
    mr_stone_buys = mr_stone_dozen * dozen

    # L3
    brock_buys = 7 # Brock buys 7 cookies
    katy_multiplier = 2 # twice as many as Brock
    katy_buys = katy_multiplier * brock_buys

    # L4
    total_sold = mr_stone_buys + brock_buys + katy_buys

    # L5
    answer = total_baked - total_sold
    return answer