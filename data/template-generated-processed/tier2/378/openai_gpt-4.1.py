def solve():
    """Index: 378.
    Returns: Uki's total earnings for five days.
    """
    # L1
    cupcakes_per_day = 20 # she can bake an average of twenty cupcakes
    cupcake_price = 1.5 # cupcakes at $1.50 each
    cupcake_earnings = cupcakes_per_day * cupcake_price

    # L2
    cookies_per_day = 10 # ten packets of cookies
    cookie_price = 2 # cookies at $2 per packet
    cookie_earnings = cookies_per_day * cookie_price

    # L3
    biscuits_per_day = 20 # twenty packets of biscuits
    biscuit_price = 1 # biscuits at $1 per packet
    biscuit_earnings = biscuits_per_day * biscuit_price

    # L4
    daily_earnings = cupcake_earnings + cookie_earnings + biscuit_earnings
    days = 5 # for five days
    total_earnings = days * daily_earnings

    # FA
    answer = total_earnings
    return answer