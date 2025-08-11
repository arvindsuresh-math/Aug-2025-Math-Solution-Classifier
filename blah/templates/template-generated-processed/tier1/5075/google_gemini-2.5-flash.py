def solve():
    """Index: 5075.
    Returns: the amount paid after discounts.
    """
    # L1
    spend_for_discount = 100 # $100 that you spend
    discount_per_increment = 10 # $10 for every $100
    initial_purchase_amount = 250 # $250 before discounts
    num_increments = initial_purchase_amount // spend_for_discount
    total_discount = discount_per_increment * num_increments

    # L2
    final_payment = initial_purchase_amount - total_discount

    # FA
    answer = final_payment
    return answer