def solve():
    """Index: 825.
    Returns: the total amount James pays for everything after the discount.
    """
    # L1
    bed_frame_price = 75 # bed frame is $75
    bed_multiplier = 10 # bed is 10 times that price
    bed_price = bed_frame_price * bed_multiplier

    # L2
    total_price_before_discount = bed_price + bed_frame_price

    # L3
    discount_percent = 0.2 # 20% off
    discount_amount = total_price_before_discount * discount_percent

    # L4
    final_price = total_price_before_discount - discount_amount

    # FA
    answer = final_price
    return answer