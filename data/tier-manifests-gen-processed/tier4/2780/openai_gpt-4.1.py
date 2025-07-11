def solve():
    """Index: 2780.
    Returns: the total money Crystal made from selling the last cupcakes and cookies.
    """
    # L1
    cupcake_price_orig = 3.00 # $3.00 cupcakes
    price_reduction_divisor = 2 # reduced by half
    cupcake_price_reduced = cupcake_price_orig / price_reduction_divisor

    # L2
    cookie_price_orig = 2.00 # $2.00 cookies
    cookie_price_reduced = cookie_price_orig / price_reduction_divisor

    # L3
    cupcakes_sold = 16 # last 16 cupcakes
    cupcake_revenue = cupcakes_sold * cupcake_price_reduced

    # L4
    cookies_sold = 8 # 8 cookies
    cookie_revenue = cookies_sold * cookie_price_reduced

    # L5
    total_revenue = cupcake_revenue + cookie_revenue

    # FA
    answer = total_revenue
    return answer