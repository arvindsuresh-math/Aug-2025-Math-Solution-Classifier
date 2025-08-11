def solve():
    """Index: 6952.
    Returns: the amount of change Lauren would get back.
    """
    # L1
    meat_pounds = 2 # 2 pounds of hamburger meat
    meat_price_per_pound = 3.50 # $3.50 a pound
    meat_cost = meat_pounds * meat_price_per_pound

    # L2
    tomato_weight = 1.5 # 1.5-pound tomato
    tomato_price_per_pound = 2.00 # $2.00 per pound
    tomato_cost = tomato_weight * tomato_price_per_pound

    # L3
    buns_cost = 1.50 # 1 pack of hamburger buns for $1.50
    lettuce_cost = 1.00 # A head of lettuce for $1.00
    pickles_cost_initial = 2.50 # a jar of pickles that cost $2.50
    total_cost_before_coupon = meat_cost + buns_cost + lettuce_cost + tomato_cost + pickles_cost_initial

    # L4
    coupon_amount = 1.00 # $1.00 off coupon
    total_cost_after_coupon = total_cost_before_coupon - coupon_amount

    # L5
    payment_amount = 20.00 # paid with a $20 bill
    change_amount = payment_amount - total_cost_after_coupon

    # FA
    answer = change_amount
    return answer