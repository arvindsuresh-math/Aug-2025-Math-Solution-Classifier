def solve():
    """Index: 2993.
    Returns: the total order cost after the discount.
    """
    # L1
    num_items = 7 # John buys 7 items
    item_cost = 200 # each cost $200
    total_cost = num_items * item_cost

    # L2
    discount_threshold = 1000 # over $1000
    discount_eligible_amount = total_cost - discount_threshold

    # L3
    discount_rate = 0.1 # 10% discount
    discount_amount = discount_eligible_amount * discount_rate

    # L4
    final_cost = total_cost - discount_amount

    # FA
    answer = final_cost
    return answer