def solve():
    """Index: 1618.
    Returns: the total amount of money James paid for the shoes.
    """
    # L1
    original_price_cheaper_pair = 40 # first pair of shoes for $40
    half_off_divisor = 2 # half off the original price
    discounted_cheaper_price = original_price_cheaper_pair / half_off_divisor

    # L2
    original_price_expensive_pair = 60 # second one for $60
    total_price_before_extra_discount = discounted_cheaper_price + original_price_expensive_pair

    # L3
    extra_discount_divisor = 4 # a fourth off the total amount
    final_discount_amount = total_price_before_extra_discount / extra_discount_divisor

    # L4
    final_price_paid = total_price_before_extra_discount - final_discount_amount

    # FA
    answer = final_price_paid
    return answer