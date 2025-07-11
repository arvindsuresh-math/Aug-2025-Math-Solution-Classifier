def solve():
    """Index: 2047.
    Returns: the total amount John spent after applying the coupon.
    """
    # L1
    vacuum_cleaner_price = 250 # vacuum cleaner for $250
    dishwasher_price = 450 # dishwasher for $450
    combined_price = vacuum_cleaner_price + dishwasher_price

    # L2
    coupon_discount = 75 # a $75 off coupon
    final_price = combined_price - coupon_discount

    # FA
    answer = final_price
    return answer