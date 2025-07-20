def solve():
    """Index: 4076.
    Returns: the total cost to feed the special food fish.
    """
    # L1
    total_goldfish = 50 # 50 goldfish
    special_food_percentage = 0.2 # 20% of the goldfish
    num_special_food_fish = total_goldfish * special_food_percentage

    # L2
    food_per_goldfish_oz = 1.5 # eats 1.5 ounces of food per day
    total_special_food_oz_per_day = num_special_food_fish * food_per_goldfish_oz

    # L3
    cost_special_food_per_oz = 3 # costs $3 an ounce
    total_cost_special_food = total_special_food_oz_per_day * cost_special_food_per_oz

    # FA
    answer = total_cost_special_food
    return answer