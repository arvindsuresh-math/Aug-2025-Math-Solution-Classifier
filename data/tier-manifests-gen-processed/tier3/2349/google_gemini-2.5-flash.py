def solve():
    """Index: 2349.
    Returns: the total combined cost of their orders.
    """
    # L2
    burger_meal_cost = 6 # burger meal that costs $6
    soda_cost_divisor = 3 # 1/3 as much as the burger meal
    soda_cost = burger_meal_cost / soda_cost_divisor

    # L3
    soda_count = 3 # They are to order a total of 3 sodas for Paulo and Jeremy (1 for Paulo + 2 for Jeremy)
    total_soda_cost = soda_cost * soda_count

    # L4
    burger_meal_count = 3 # They are to order a total of 3 burger meals for Paulo and Jeremy (1 for Paulo + 2 for Jeremy)
    total_burger_meal_cost = burger_meal_cost * burger_meal_count

    # L5
    total_combined_cost = total_soda_cost + total_burger_meal_cost

    # FA
    answer = total_combined_cost
    return answer