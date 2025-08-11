def solve():
    """Index: 4188.
    Returns: the amount Barry is supposed to pay after the discount.
    """
    # L1
    discount_percentage_val = 15 # 15% special discount
    percentage_divisor = 100 # WK
    original_price = 80 # price tag on the shirt says $80
    discount_amount = (discount_percentage_val / percentage_divisor) * original_price

    # L2
    final_price = original_price - discount_amount

    # FA
    answer = final_price
    return answer