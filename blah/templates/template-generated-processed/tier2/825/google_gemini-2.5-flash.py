def solve():
    """Index: 825.
    Returns: the total amount paid for the bed and bed frame after discount.
    """
    # L1
    bed_frame_cost = 75 # The bed frame is $75
    bed_price_multiplier = 10 # the bed is 10 times that price
    bed_cost = bed_frame_cost * bed_price_multiplier

    # L2
    total_initial_cost = bed_cost + bed_frame_cost

    # L3
    discount_percent = 0.2 # 20% off
    discount_amount = total_initial_cost * discount_percent

    # L4
    final_cost = total_initial_cost - discount_amount

    # FA
    answer = final_cost
    return answer