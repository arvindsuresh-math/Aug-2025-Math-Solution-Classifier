def solve():
    """Index: 2047.
    Returns: the total amount John spent after applying the coupon.
    """
    # L1
    vacuum_price = 250 # vacuum cleaner for $250
    dishwasher_price = 450 # dishwasher for $450
    combined_price = vacuum_price + dishwasher_price

    # L2
    coupon = 75 # $75 off coupon
    total_paid = combined_price - coupon

    # FA
    answer = total_paid
    return answer