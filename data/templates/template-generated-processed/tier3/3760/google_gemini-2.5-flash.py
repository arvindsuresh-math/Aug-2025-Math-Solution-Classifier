def solve():
    """Index: 3760.
    Returns: the total money made from selling cookies.
    """
    # L1
    clementine_cookies = 72 # Clementine baked 72 cookies

    # L2
    jake_multiplier = 2 # twice as many cookies as Clementine
    jake_cookies = clementine_cookies * jake_multiplier

    # L3
    combined_clementine_jake_cookies = clementine_cookies + jake_cookies
    tory_divisor = 2 # half as many cookies as Jake and Clementine combined
    tory_cookies = combined_clementine_jake_cookies / tory_divisor

    # L4
    total_cookies = clementine_cookies + jake_cookies + tory_cookies

    # L5
    price_per_cookie = 2 # for $2 each
    total_money_raised = total_cookies * price_per_cookie

    # FA
    answer = total_money_raised
    return answer