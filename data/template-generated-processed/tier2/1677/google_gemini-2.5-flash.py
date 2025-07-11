def solve():
    """Index: 1677.
    Returns: the additional worth of food needed for free delivery.
    """
    # L1
    burger_cost_per_item = 3.20 # 2 quarter-pounder burgers for $3.20 each
    num_burgers = 2 # 2 quarter-pounder burgers
    total_burger_cost = burger_cost_per_item * num_burgers

    # L2
    fries_cost_per_item = 1.90 # 2 large fries that cost $1.90 each
    num_fries = 2 # 2 large fries
    total_fries_cost = num_fries * fries_cost_per_item

    # L3
    milkshake_cost_per_item = 2.40 # 2 milkshakes that cost $2.40 each
    num_milkshakes = 2 # 2 milkshakes
    total_milkshake_cost = num_milkshakes * milkshake_cost_per_item

    # L4
    total_current_cost = total_burger_cost + total_fries_cost + total_milkshake_cost

    # L5
    min_purchase_for_delivery = 18 # minimum purchase of $18
    additional_food_needed = min_purchase_for_delivery - total_current_cost

    # FA
    answer = additional_food_needed
    return answer