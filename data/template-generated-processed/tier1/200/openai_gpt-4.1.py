def solve():
    """Index: 200.
    Returns: the total amount Sansa earns in 3 days from selling portraits.
    """
    # L1
    price_8in = 5 # sells an 8-inch portrait for $5
    num_8in_per_day = 3 # sells three 8-inch portraits per day
    earnings_8in_per_day = price_8in * num_8in_per_day

    # L2
    multiplier_16in = 2 # 16-inch portrait for twice the price of the 8-inch portrait
    price_16in = price_8in * multiplier_16in

    # L3
    num_16in_per_day = 5 # sells five 16-inch portraits per day
    earnings_16in_per_day = price_16in * num_16in_per_day

    # L4
    total_earnings_per_day = earnings_16in_per_day + earnings_8in_per_day

    # L5
    num_days = 3 # every 3 days
    total_earnings = total_earnings_per_day * num_days

    # FA
    answer = total_earnings
    return answer