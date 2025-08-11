def solve():
    """Index: 3655.
    Returns: the total cost Martha needs to pay for the ingredients.
    """
    # L1
    meat_quantity_kg = 0.5 # 500 grams of meat
    meat_cost_per_kg = 8 # meat $8 per kilogram
    meat_cost = meat_quantity_kg * meat_cost_per_kg

    # L2
    cheese_quantity_kg = 1.5 # 1.5kg of cheese
    cheese_cost_per_kg = 6 # cheese costs $6 per kilogram
    cheese_cost = cheese_quantity_kg * cheese_cost_per_kg

    # L3
    total_cost = meat_cost + cheese_cost

    # FA
    answer = total_cost
    return answer