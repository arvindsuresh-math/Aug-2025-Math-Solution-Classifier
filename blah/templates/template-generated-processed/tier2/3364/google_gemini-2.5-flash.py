def solve():
    """Index: 3364.
    Returns: the amount Zane paid for the shirts.
    """
    # L1
    num_shirts = 2 # 2 polo shirts
    regular_price_per_shirt = 50 # $50 each at the regular price
    total_regular_price = num_shirts * regular_price_per_shirt

    # L2
    discount_percent_num = 40 # 40% off
    percent_factor = 0.01 # WK
    discount_amount = total_regular_price * discount_percent_num * percent_factor

    # L3
    final_cost = total_regular_price - discount_amount

    # FA
    answer = final_cost
    return answer