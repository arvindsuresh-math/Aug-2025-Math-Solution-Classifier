def solve():
    """Index: 6509.
    Returns: the total cost to feed the turtles.
    """
    # L1
    total_turtle_weight = 30 # 30 pounds of turtles
    food_per_body_weight_unit = 0.5 # 1/2 pound of body weight
    total_ounces_needed = total_turtle_weight / food_per_body_weight_unit

    # L2
    ounces_per_jar = 15 # Each jar of food contains 15 ounces
    num_jars_needed = total_ounces_needed / ounces_per_jar

    # L3
    cost_per_jar = 2 # costs $2
    total_cost = num_jars_needed * cost_per_jar

    # FA
    answer = total_cost
    return answer