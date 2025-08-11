def solve():
    """Index: 5532.
    Returns: the total amount Emma paid for her shopping.
    """
    # L1
    cheese_quantity = 8 # 8 kg of cheese
    cost_per_kg_cheese = 4 # One kilogram of cheese costs $4
    cost_cheese = cheese_quantity * cost_per_kg_cheese

    # L2
    extra_cost_vegetable = 2 # $2 more expensive
    cost_per_kg_vegetable = cost_per_kg_cheese + extra_cost_vegetable

    # L3
    vegetable_quantity = 7 # 7 kg of vegetables
    cost_vegetables = vegetable_quantity * cost_per_kg_vegetable

    # L4
    total_cost = cost_cheese + cost_vegetables

    # FA
    answer = total_cost
    return answer