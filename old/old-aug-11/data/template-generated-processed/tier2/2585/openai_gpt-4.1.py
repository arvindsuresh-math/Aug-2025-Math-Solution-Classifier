def solve():
    """Index: 2585.
    Returns: the amount an officer who has served at least three years has to pay for shoes.
    """
    # L1
    full_price = 85 # full price of $85
    discount1_rate = 0.2 # 20% discount
    discount1_amount = full_price * discount1_rate

    # L2
    price_after_discount1 = full_price - discount1_amount

    # L3
    discount2_rate = 0.25 # 25% off the discounted price
    discount2_amount = price_after_discount1 * discount2_rate

    # L4
    final_price = price_after_discount1 - discount2_amount

    # FA
    answer = final_price
    return answer