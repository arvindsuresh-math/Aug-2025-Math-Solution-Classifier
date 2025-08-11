def solve():
    """Index: 4442.
    Returns: the total cost to get the weight needed.
    """
    # L1
    initial_weight = 60 # It weighed 60 pounds
    weight_increase_percent = 0.6 # increase the weight by 60%
    additional_weight_needed = initial_weight * weight_increase_percent

    # L2
    weight_per_ingot = 2 # 2-pound steel ingots
    num_ingots_needed = additional_weight_needed / weight_per_ingot

    # L3
    cost_per_ingot = 5 # Each ingot cost $5
    initial_cost = num_ingots_needed * cost_per_ingot

    # L4
    discount_percent = 0.2 # 20% discount
    discount_amount = initial_cost * discount_percent

    # L5
    final_cost = initial_cost - discount_amount

    # FA
    answer = final_cost
    return answer