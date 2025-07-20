def solve():
    """Index: 3396.
    Returns: how much more they earned in the evening than in the morning.
    """
    # L1
    remy_soda_morning_sales = 55 # Remy sold 55 bottles of soda
    nick_soda_fewer_than_remy = 6 # six fewer bottles of soda than Remy
    nick_soda_morning_sales = remy_soda_morning_sales - nick_soda_fewer_than_remy

    # L2
    total_morning_bottles_sold = remy_soda_morning_sales + nick_soda_morning_sales

    # L3
    price_per_bottle = 0.50 # The price per bottle is $.50
    total_morning_earnings = total_morning_bottles_sold * price_per_bottle

    # L4
    total_evening_sales = 55 # total evening sales are $55
    earnings_difference = total_evening_sales - total_morning_earnings

    # FA
    answer = earnings_difference
    return answer