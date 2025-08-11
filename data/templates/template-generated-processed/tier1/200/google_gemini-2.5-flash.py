def solve():
    """Index: 200.
    Returns: the total amount Sansa earns every 3 days.
    """
    # L1
    price_8_inch = 5 # sells an 8-inch portrait for $5
    num_8_inch_sold_per_day = 3 # sells three 8-inch portraits
    earnings_8_inch_portraits_per_day = price_8_inch * num_8_inch_sold_per_day

    # L2
    multiplier_16_inch_price = 2 # twice the price of the 8-inch portrait
    price_16_inch = price_8_inch * multiplier_16_inch_price

    # L3
    num_16_inch_sold_per_day = 5 # sells five 16-inch portraits
    earnings_16_inch_portraits_per_day = price_16_inch * num_16_inch_sold_per_day

    # L4
    total_earnings_per_day = earnings_16_inch_portraits_per_day + earnings_8_inch_portraits_per_day

    # L5
    num_days = 3 # every 3 days
    total_earnings_3_days = total_earnings_per_day * num_days

    # FA
    answer = total_earnings_3_days
    return answer