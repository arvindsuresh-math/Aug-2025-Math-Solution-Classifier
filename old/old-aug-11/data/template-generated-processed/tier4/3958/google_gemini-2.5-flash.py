def solve():
    """Index: 3958.
    Returns: the final price Mrs. Brown will pay for the shoes.
    """
    # L1
    original_price = 125 # a pair of shoes that costs $125
    initial_discount_percent_num = 10 # 10% discount
    percent_divisor = 100 # WK
    initial_discount_amount = original_price * initial_discount_percent_num / percent_divisor

    # L2
    price_after_initial_discount = original_price - initial_discount_amount

    # L3
    additional_discount_percent_num = 4 # additional 4% off
    additional_discount_amount = price_after_initial_discount * additional_discount_percent_num / percent_divisor

    # L4
    final_price = price_after_initial_discount - additional_discount_amount

    # FA
    answer = final_price
    return answer