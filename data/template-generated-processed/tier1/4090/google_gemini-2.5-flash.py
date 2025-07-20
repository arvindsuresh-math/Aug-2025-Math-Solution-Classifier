def solve():
    """Index: 4090.
    Returns: the total money earned from selling cookies.
    """
    # L1
    chocolate_cookies_sold = 220 # 220 chocolate cookies
    price_per_chocolate_cookie = 1 # $1 per cookie
    chocolate_earnings = chocolate_cookies_sold * price_per_chocolate_cookie

    # L2
    vanilla_cookies_sold = 70 # 70 vanilla cookies
    price_per_vanilla_cookie = 2 # $2 per cookie
    vanilla_earnings = vanilla_cookies_sold * price_per_vanilla_cookie

    # L3
    total_earned = chocolate_earnings + vanilla_earnings

    # FA
    answer = total_earned
    return answer