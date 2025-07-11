def solve():
    """Index: 2088.
    Returns: the cost of each serving.
    """
    # L1
    pasta_cost = 1.00 # $1.00 per box
    sauce_cost = 2.00 # $2.00
    meatballs_cost = 5.00 # $5.00
    total_meal_cost = pasta_cost + sauce_cost + meatballs_cost

    # L2
    num_servings = 8 # 8 servings
    cost_per_serving = total_meal_cost / num_servings

    # FA
    answer = cost_per_serving
    return answer