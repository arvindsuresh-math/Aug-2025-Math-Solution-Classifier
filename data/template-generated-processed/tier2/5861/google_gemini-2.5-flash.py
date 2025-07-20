def solve():
    """Index: 5861.
    Returns: the total cost of Ralph's items.
    """
    # L1
    discount_percent_decimal_L1 = 0.20 # 20% discount on an item
    item_price = 20.00 # This item is $20.00 to start
    discount_percent_num_L1 = 20 # 20% discount
    percent_factor = 0.01 # WK
    item_discount_amount = discount_percent_num_L1 * percent_factor * item_price

    # L2
    initial_cart_total = 54.00 # $54.00 worth of products in his cart
    total_after_item_discount = initial_cart_total - item_discount_amount

    # L3
    coupon_percent_decimal = 0.10 # 10% coupon
    coupon_percent_num = 10 # 10% coupon
    coupon_discount_amount = coupon_percent_num * percent_factor * total_after_item_discount

    # L4
    final_cost = total_after_item_discount - coupon_discount_amount

    # FA
    answer = final_cost
    return answer