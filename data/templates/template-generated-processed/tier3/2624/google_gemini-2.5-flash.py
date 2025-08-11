def solve():
    """Index: 2624.
    Returns: the total amount Maria paid.
    """
    # L1
    total_percentage = 100 # 100 percent represent the original price
    discount_percentage = 25 # 25% discount
    discount_amount = 40 # discount she received is $40
    original_price = total_percentage / discount_percentage * discount_amount

    # L2
    amount_paid = original_price - discount_amount

    # FA
    answer = amount_paid
    return answer