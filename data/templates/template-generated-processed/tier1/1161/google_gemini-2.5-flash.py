def solve():
    """Index: 1161.
    Returns: the number of cookies Meena has left.
    """
    # L1
    num_dozen_baked = 5 # 5 dozen cookies
    dozen = 12 # WK
    total_baked_cookies = num_dozen_baked * dozen

    # L2
    num_dozen_stone_buys = 2 # 2 dozen cookies
    stone_buys_cookies = num_dozen_stone_buys * dozen

    # L3
    brock_buys = 7 # Brock buys 7 cookies
    katy_multiplier = 2 # twice as many as Brock
    katy_buys_cookies = katy_multiplier * brock_buys

    # L4
    total_sold_cookies = stone_buys_cookies + brock_buys + katy_buys_cookies

    # L5
    cookies_left = total_baked_cookies - total_sold_cookies

    # FA
    answer = cookies_left
    return answer