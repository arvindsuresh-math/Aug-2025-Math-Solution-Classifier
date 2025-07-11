def solve():
    """Index: 152.
    Returns: the cost of the discounted newspaper subscription.
    """
    # L1
    normal_price = 80 # subscription normally costs $80
    discount_percentage = 45 # 45% discount
    percent_divisor = 100 # WK
    discount_amount = normal_price * discount_percentage / percent_divisor

    # L2
    discounted_price = normal_price - discount_amount

    # FA
    answer = discounted_price
    return answer