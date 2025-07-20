def solve():
    """Index: 4803.
    Returns: the cost per serving of pie.
    """
    # L1
    pounds_of_apples = 2 # 2 pounds of apples
    cost_per_pound_apples = 2.00 # $2.00 per pound
    cost_apples = pounds_of_apples * cost_per_pound_apples

    # L2
    cost_pie_crust = 2.00 # The pre-made pie crust cost $2.00
    cost_lemon = 0.50 # The lemon cost $.50
    cost_butter = 1.50 # the butter cost $1.50
    total_cost = cost_apples + cost_pie_crust + cost_lemon + cost_butter

    # L3
    num_servings = 8 # serve 8 people
    cost_per_serving = total_cost / num_servings

    # FA
    answer = cost_per_serving
    return answer