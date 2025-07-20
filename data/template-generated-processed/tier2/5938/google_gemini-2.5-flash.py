def solve():
    """Index: 5938.
    Returns: the final price the man must pay for the sneakers.
    """
    # L1
    sneakers_original_price = 120 # a $120 pair of sneakers
    coupon_discount_amount = 10 # a coupon for $10 off
    price_after_coupon = sneakers_original_price - coupon_discount_amount

    # L2
    membership_discount_decimal = 0.1 # membership discount of 10% off (used as 0.1 in calculation)
    membership_discount_percent_text = 10 # membership discount of 10% off (used as 10% in text)
    membership_discount_amount = price_after_coupon * membership_discount_decimal

    # L3
    final_price = price_after_coupon - membership_discount_amount

    # FA
    answer = final_price
    return answer