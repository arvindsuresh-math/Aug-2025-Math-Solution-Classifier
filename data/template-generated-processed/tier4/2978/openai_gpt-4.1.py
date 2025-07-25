def solve():
    """Index: 2978.
    Returns: the price James paid per shirt after the discount.
    """
    # L1
    total_price = 60 # $60 for 3 shirts
    discount_percent = 0.4 # 40% off sale
    discount_amount = total_price * discount_percent

    # L2
    paid_after_discount = total_price - discount_amount

    # L3
    num_shirts = 3 # 3 shirts
    price_per_shirt = paid_after_discount / num_shirts

    # FA
    answer = price_per_shirt
    return answer