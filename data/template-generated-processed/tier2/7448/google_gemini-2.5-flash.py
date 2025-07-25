def solve():
    """Index: 7448.
    Returns: the new price of the bedside lamp after the discount.
    """
    # L1
    original_price = 120 # was worth $120
    discount_rate = 0.2 # 20% discount
    discount_amount = original_price * discount_rate

    # L2
    new_price = original_price - discount_amount

    # FA
    answer = new_price
    return answer