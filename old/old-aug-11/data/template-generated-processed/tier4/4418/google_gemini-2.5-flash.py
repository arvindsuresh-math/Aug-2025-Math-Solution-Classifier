def solve():
    """Index: 4418.
    Returns: the price of a single appetizer.
    """
    # L1
    total_meal_cost = 50.00 # $50.00 on Chinese take-out
    entree_percentage_as_decimal = 0.80 # 80% of the cost went to 4 entrees
    cost_on_entrees = total_meal_cost * entree_percentage_as_decimal

    # L2
    cost_on_appetizers = total_meal_cost - cost_on_entrees

    # L3
    num_appetizers = 2 # 2 appetizers
    price_per_appetizer = cost_on_appetizers / num_appetizers

    # FA
    answer = price_per_appetizer
    return answer