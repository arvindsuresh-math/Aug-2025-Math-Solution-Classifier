def solve():
    """Index: 5867.
    Returns: the cost of each additional item of clothing.
    """
    # L1
    shirt_cost_each = 18.50 # $18.50 each
    num_shirts = 2 # 2 shirts
    cost_shirts = shirt_cost_each * num_shirts

    # L2
    trousers_cost = 63 # $63
    total_spent_so_far = cost_shirts + trousers_cost

    # L3
    initial_budget = 260 # $260 to spend on clothes
    remaining_budget = initial_budget - total_spent_so_far

    # L4
    num_additional_items = 4 # 4 more articles of clothing
    cost_per_additional_item = remaining_budget / num_additional_items

    # FA
    answer = cost_per_additional_item
    return answer