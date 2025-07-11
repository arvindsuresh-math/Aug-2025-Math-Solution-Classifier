def solve():
    """Index: 412.
    Returns: the number of cookies Uncle Jude put in the fridge.
    """
    # L1
    tim_cookies = 15 # 15 cookies to Tim
    multiplier_anna = 2 # twice as many cookies as he gave Tim to Anna
    anna_cookies = multiplier_anna * tim_cookies

    # L2
    mike_cookies = 23 # 23 cookies to Mike
    total_given = tim_cookies + mike_cookies + anna_cookies

    # L3
    total_baked = 256 # Uncle Jude baked 256 cookies
    fridge_cookies = total_baked - total_given

    # FA
    answer = fridge_cookies
    return answer