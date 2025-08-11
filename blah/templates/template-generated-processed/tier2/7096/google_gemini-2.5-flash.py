def solve():
    """Index: 7096.
    Returns: the total cost of 3 bottles of gummy vitamins.
    """
    # L1
    bottle_price = 15.00 # $15.00 per bottle
    discount_percent_text = 20 # 20% off
    discount_percent_decimal = 0.20 # 20% off
    discount_amount_per_bottle = bottle_price * discount_percent_decimal

    # L2
    price_per_bottle_after_discount = bottle_price - discount_amount_per_bottle

    # L3
    num_coupons = 3 # 3 $2.00 coupons
    coupon_value = 2.00 # $2.00 coupons
    total_coupon_value = num_coupons * coupon_value

    # L4
    num_bottles_bought = 3 # 3 bottles
    cost_before_coupons = num_bottles_bought * price_per_bottle_after_discount

    # L5
    final_cost = cost_before_coupons - total_coupon_value

    # FA
    answer = final_cost
    return answer