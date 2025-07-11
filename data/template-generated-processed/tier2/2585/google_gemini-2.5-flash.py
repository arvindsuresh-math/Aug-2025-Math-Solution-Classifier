def solve():
    """Index: 2585.
    Returns: the amount an officer who has served at least three years has to pay for shoes.
    """
    # L1
    full_price = 85 # full price of $85
    first_discount_rate = 0.2 # 20% discount
    first_discount_amount = full_price * first_discount_rate

    # L2
    price_after_first_discount = full_price - first_discount_amount

    # L3
    additional_discount_rate = 0.25 # additional 25% off
    additional_discount_amount = price_after_first_discount * additional_discount_rate

    # L4
    final_price = price_after_first_discount - additional_discount_amount

    # FA
    answer = final_price
    return answer