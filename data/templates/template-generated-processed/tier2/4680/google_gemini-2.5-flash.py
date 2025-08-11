def solve():
    """Index: 4680.
    Returns: the total cost of Adam's purchases.
    """
    # L1
    nuts_kilograms = 3 # 3 kilograms of nuts
    cost_per_kg_nuts = 12 # One kilogram of nuts costs $12
    cost_nuts = nuts_kilograms * cost_per_kg_nuts

    # L2
    dried_fruits_kilograms = 2.5 # 2.5 kilograms of dried fruits
    cost_per_kg_dried_fruit = 8 # one kilogram of dried fruit costs $8
    cost_dried_fruits = dried_fruits_kilograms * cost_per_kg_dried_fruit

    # L3
    total_cost = cost_nuts + cost_dried_fruits

    # FA
    answer = total_cost
    return answer