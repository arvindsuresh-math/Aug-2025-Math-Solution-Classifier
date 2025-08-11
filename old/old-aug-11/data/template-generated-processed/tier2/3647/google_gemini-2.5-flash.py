def solve():
    """Index: 3647.
    Returns: the total amount Carla pays for her order.
    """
    # L1
    initial_cost = 7.50 # Carla's order at Mcdonald's costs $7.50
    coupon_amount = 2.50 # coupon for $2.50
    cost_after_coupon = initial_cost - coupon_amount

    # L2
    total_percent = 100 # WK
    senior_discount_percent = 20 # 20% discount
    percentage_paid_value = total_percent - senior_discount_percent

    # L3
    percentage_paid_decimal = percentage_paid_value / 100
    final_price = cost_after_coupon * percentage_paid_decimal

    # FA
    answer = final_price
    return answer