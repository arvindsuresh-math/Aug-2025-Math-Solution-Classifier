def solve():
    """Index: 2088.
    Returns: the cost per serving of the meal.
    """
    # L1
    pasta_cost = 1.00 # The pasta costs $1.00 per box
    sauce_cost = 2.00 # a jar of sauce is $2.00
    meat_cost = 5.00 # 1 pound of meatballs is $5.00
    total_cost = pasta_cost + sauce_cost + meat_cost

    # L2
    num_servings = 8 # He wants to stretch this meal into 8 servings
    cost_per_serving = total_cost / num_servings

    # FA
    answer = cost_per_serving
    return answer