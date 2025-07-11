def solve():
    """Index: 892.
    Returns: the amount of the discount Clark received.
    """
    # L1
    part_price = 80 # $80
    quantity_bought = 7 # buys 7 of them
    original_total_cost = part_price * quantity_bought

    # L2
    actual_paid_cost = 439 # pay $439
    discount_amount = original_total_cost - actual_paid_cost

    # FA
    answer = discount_amount
    return answer