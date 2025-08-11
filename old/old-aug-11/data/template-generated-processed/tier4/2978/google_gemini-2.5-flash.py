def solve():
    """Index: 2978.
    Returns: the price paid per shirt after the discount.
    """
    # L1
    original_price = 60 # 3 shirts for $60
    discount_rate = 0.4 # 40% off sale
    discount_amount = original_price * discount_rate

    # L2
    price_after_discount = original_price - discount_amount

    # L3
    num_shirts = 3 # 3 shirts
    cost_per_shirt = price_after_discount / num_shirts

    # FA
    answer = cost_per_shirt
    return answer