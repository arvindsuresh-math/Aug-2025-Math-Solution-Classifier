def solve():
    """Index: 5288.
    Returns: the total cost of the backpacks.
    """
    # L1
    num_backpacks = 5 # 5 personalized backpacks
    backpack_unit_price = 20.00 # $20.00
    initial_total_cost = num_backpacks * backpack_unit_price

    # L2
    discount_percent_text = 20 # 20% off
    discount_rate_decimal = 0.20 # 20% off of $20.00
    discount_amount = initial_total_cost * discount_rate_decimal

    # L3
    cost_after_discount = initial_total_cost - discount_amount

    # L4
    monogram_cost_per_backpack = 12.00 # $12.00 each
    total_monogram_cost = num_backpacks * monogram_cost_per_backpack

    # L5
    final_total_cost = cost_after_discount + total_monogram_cost

    # FA
    answer = final_total_cost
    return answer