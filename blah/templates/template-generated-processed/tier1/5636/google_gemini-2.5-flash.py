def solve():
    """Index: 5636.
    Returns: the amount of change they should get from the payment.
    """
    # L1
    eggs_cost = 3 # eggs for $3
    pancakes_cost_initial = 2 # pancakes for $2
    cocoa_mug_cost = 2 # 2 mugs of cocoa for $2 each
    initial_food_cost = eggs_cost + pancakes_cost_initial + cocoa_mug_cost + cocoa_mug_cost

    # L2
    tax_amount = 1 # The tax is $1
    total_cost_with_tax_initial = initial_food_cost + tax_amount

    # L3
    additional_pancakes_cost = 2 # 1 more batch of pancakes
    additional_cocoa_cost = 2 # 1 more mug of cocoa
    final_total_cost = total_cost_with_tax_initial + additional_pancakes_cost + additional_cocoa_cost

    # L4
    amount_paid = 15 # from $15
    change_amount = amount_paid - final_total_cost

    # FA
    answer = change_amount
    return answer