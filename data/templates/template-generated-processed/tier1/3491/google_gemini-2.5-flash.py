def solve():
    """Index: 3491.
    Returns: the total tablespoons of coffee needed.
    """
    # L1
    weak_coffee_tbsp_per_cup = 1 # 1 tablespoon of coffee per cup of water to make it weak
    strong_coffee_multiplier = 2 # doubles that amount
    strong_coffee_tbsp_per_cup = weak_coffee_tbsp_per_cup * strong_coffee_multiplier

    # L2
    cups_of_weak_coffee = 12 # 12 cups of both weak and strong coffee
    total_weak_coffee_tbsp = weak_coffee_tbsp_per_cup * cups_of_weak_coffee

    # L3
    cups_of_strong_coffee = 12 # 12 cups of both weak and strong coffee
    total_strong_coffee_tbsp = strong_coffee_tbsp_per_cup * cups_of_strong_coffee

    # L4
    total_coffee_tbsp = total_weak_coffee_tbsp + total_strong_coffee_tbsp

    # FA
    answer = total_coffee_tbsp
    return answer