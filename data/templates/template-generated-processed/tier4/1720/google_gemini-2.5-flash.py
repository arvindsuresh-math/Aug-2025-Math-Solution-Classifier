def solve():
    """Index: 1720.
    Returns: the original price of the pair of shoes.
    """
    # L1
    paid_percentage_total = 100 # WK
    discount_percentage = 20 # 20% discount
    paid_percentage = paid_percentage_total - discount_percentage
    paid_amount = 480 # paid $480
    paid_percentage_decimal = paid_percentage / paid_percentage_total

    # L4
    original_price = paid_amount / paid_percentage_decimal

    # FA
    answer = original_price
    return answer