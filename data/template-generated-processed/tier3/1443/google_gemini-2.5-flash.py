def solve():
    """Index: 1443.
    Returns: the total dollars saved on the original price of the jeans.
    """
    # L1
    full_price = 125 # cost $125 at full price
    sale_percent_val = 20 # on sale for 20% off
    percent_divisor = 100 # WK
    sale_fraction_denominator = 5 # 1 /5 off
    sale_discount = full_price / sale_fraction_denominator

    # L2
    price_after_sale = full_price - sale_discount

    # L3
    coupon_amount = 10 # took off $10
    price_after_coupon = price_after_sale - coupon_amount

    # L4
    card_percent_val = 10 # another 10% off
    card_fraction_denominator = 10 # 1 / 10 off
    card_discount = price_after_coupon / card_fraction_denominator

    # L5
    final_price = price_after_coupon - card_discount

    # L6
    total_savings = full_price - final_price

    # FA
    answer = total_savings
    return answer