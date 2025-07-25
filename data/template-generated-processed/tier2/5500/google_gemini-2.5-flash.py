def solve():
    """Index: 5500.
    Returns: the final price of the set.
    """
    # L1
    original_price = 2000 # new modern bedroom set for $2000
    initial_discount_percent_num = 15 # 15% off
    initial_discount_percent_decimal = 0.15 # 2000*.15
    initial_discount_amount = original_price * initial_discount_percent_decimal

    # L2
    price_after_initial_discount = original_price - initial_discount_amount

    # L3
    credit_card_discount_percent_num = 10 # additional 10% off
    credit_card_discount_percent_decimal = 0.10 # .10*1700
    percent_factor = 0.01 # WK
    credit_card_discount_amount = credit_card_discount_percent_num * percent_factor * price_after_initial_discount

    # L4
    price_after_credit_card_discount = price_after_initial_discount - credit_card_discount_amount

    # L5
    gift_card_amount = 200.00 # $200.00 in gift cards
    final_price = price_after_credit_card_discount - gift_card_amount

    # FA
    answer = final_price
    return answer