def solve():
    """Index: 1720.
    Returns: the original price of the pair of shoes.
    """
    # L1
    paid_amount = 480 # she paid $480
    discount_percent = 20 # 20% discount
    full_percent = 100 # WK
    paid_percent = full_percent - discount_percent
    paid_fraction = paid_percent / full_percent

    # L3
    # 0.8x = $480
    # paid_fraction * x = paid_amount
    # L4
    original_price = paid_amount / paid_fraction

    # FA
    answer = original_price
    return answer