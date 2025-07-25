def solve():
    """Index: 3574.
    Returns: the total number of nuts needed.
    """
    # L1
    total_percent = 100 # WK
    nuts_fraction_percent = 25 # 1/4 of her cookies to have nuts in them (1/4 = 25%)
    chocolate_chips_percent = 40 # 40% to have chocolate chips in them
    nuts_and_chocolate_chips_percent = total_percent - nuts_fraction_percent - chocolate_chips_percent

    # L2
    total_nuts_percent = nuts_fraction_percent + nuts_and_chocolate_chips_percent

    # L3
    total_cookies = 60 # If she makes 60 cookies
    total_nuts_decimal = 0.6 # WK
    cookies_with_nuts = total_cookies * total_nuts_decimal

    # L4
    nuts_per_cookie = 2 # uses 2 nuts per cookie
    total_nuts_needed = cookies_with_nuts * nuts_per_cookie

    # FA
    answer = total_nuts_needed
    return answer