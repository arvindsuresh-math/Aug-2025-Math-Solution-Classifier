def solve():
    """Index: 6912.
    Returns: the cost of a can of tuna in cents.
    """
    # L1
    paid_amount = 20.0 # paid $20
    change_received = 5.50 # got $5.50 in change
    total_without_coupons = paid_amount - change_received

    # L2
    num_coupons = 5 # 5 coupons
    coupon_value_dollars = 0.25 # 25 cents off
    full_price_all_tuna = total_without_coupons + num_coupons * coupon_value_dollars

    # L3
    num_cans = 9 # 9 cans
    cost_per_can_dollars = full_price_all_tuna / num_cans

    # L4
    dollars_to_cents_factor = 100 # WK
    cost_per_can_cents = cost_per_can_dollars * dollars_to_cents_factor

    # FA
    answer = cost_per_can_cents
    return answer