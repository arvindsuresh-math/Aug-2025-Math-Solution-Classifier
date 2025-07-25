def solve():
    """Index: 2780.
    Returns: the total money made from selling cupcakes and cookies.
    """
    # L1
    cupcake_original_price = 3.00 # $3.00 cupcakes
    half_reduction_divisor = 2 # reduced her ... by half
    cupcake_reduced_price = cupcake_original_price / half_reduction_divisor

    # L2
    cookie_original_price = 2.00 # $2.00 cookies
    cookie_reduced_price = cookie_original_price / half_reduction_divisor

    # L3
    num_cupcakes_sold = 16 # sold the last 16 cupcakes
    money_from_cupcakes = num_cupcakes_sold * cupcake_reduced_price

    # L4
    num_cookies_sold = 8 # and 8 cookies
    money_from_cookies = num_cookies_sold * cookie_reduced_price

    # L5
    total_money_made = money_from_cupcakes + money_from_cookies

    # FA
    answer = total_money_made
    return answer