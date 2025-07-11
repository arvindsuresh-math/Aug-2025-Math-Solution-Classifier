def solve():
    """Index: 378.
    Returns: Uki's total earnings for five days.
    """
    # L1
    num_cupcakes_per_day = 20 # twenty cupcakes
    cupcake_price = 1.50 # $1.50 each
    daily_cupcake_earnings = num_cupcakes_per_day * cupcake_price

    # L2
    num_cookie_packets_per_day = 10 # ten packets of cookies
    cookie_packet_price = 2 # $2 per packet
    daily_cookie_earnings = num_cookie_packets_per_day * cookie_packet_price

    # L3
    num_biscuit_packets_per_day = 20 # twenty packets of biscuits
    biscuit_packet_price = 1 # $1 per packet
    daily_biscuit_earnings = num_biscuit_packets_per_day * biscuit_packet_price

    # L4
    daily_total_earnings = daily_cupcake_earnings + daily_cookie_earnings + daily_biscuit_earnings
    num_days = 5 # five days
    total_earnings_five_days = num_days * daily_total_earnings

    # FA
    answer = total_earnings_five_days
    return answer