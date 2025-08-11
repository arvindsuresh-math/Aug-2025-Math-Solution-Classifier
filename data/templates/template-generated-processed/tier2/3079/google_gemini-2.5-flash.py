def solve():
    """Index: 3079.
    Returns: the original cost for the jeans before all the discounts.
    """
    # L1
    final_cost_after_all_discounts = 14.50 # the cost of a pair of jeans is $14.50
    wednesday_discount_amount = 10.00 # additional $10.00 off
    cost_before_wednesday_discount = final_cost_after_all_discounts + wednesday_discount_amount

    # L2
    summer_discount_percent = 0.50 # 50% discount
    multiplier_for_original_cost = 1 / summer_discount_percent
    original_cost = cost_before_wednesday_discount * multiplier_for_original_cost

    # FA
    answer = original_cost
    return answer