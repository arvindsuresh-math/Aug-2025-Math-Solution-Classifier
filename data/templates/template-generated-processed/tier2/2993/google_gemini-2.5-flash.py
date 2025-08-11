def solve():
    """Index: 2993.
    Returns: the final cost of John's order after the discount.
    """
    # L1
    num_items = 7 # 7 items
    cost_per_item = 200 # each cost $200
    total_initial_cost = num_items * cost_per_item

    # L2
    discount_threshold = 1000 # over $1000
    discount_eligible_amount = total_initial_cost - discount_threshold

    # L3
    discount_rate_decimal = 0.1 # 10% discount
    discount_amount = discount_eligible_amount * discount_rate_decimal

    # L4
    final_cost = total_initial_cost - discount_amount

    # FA
    answer = final_cost
    return answer