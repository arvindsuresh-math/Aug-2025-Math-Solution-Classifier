def solve():
    """Index: 6609.
    Returns: the total amount John paid for the toys.
    """
    # L1
    num_toys = 5 # 5 toys
    cost_per_toy = 3 # each cost $3
    total_cost_before_discount = num_toys * cost_per_toy

    # L2
    discount_percent_decimal = 0.2 # 20% discount
    discount_amount = total_cost_before_discount * discount_percent_decimal

    # L3
    final_cost = total_cost_before_discount - discount_amount

    # FA
    answer = final_cost
    return answer