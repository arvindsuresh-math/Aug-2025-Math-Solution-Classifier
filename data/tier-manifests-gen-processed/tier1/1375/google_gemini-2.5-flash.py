def solve():
    """Index: 1375.
    Returns: the total profit earned by the farmer after deducting the cost of food.
    """
    # L1
    months_group1 = 12 # 12 months
    cost_per_month_per_pig = 10 # $10 per month to feed each animal
    num_pigs_group1 = 3 # 3 pigs
    food_cost_group1 = months_group1 * cost_per_month_per_pig * num_pigs_group1

    # L2
    months_group2 = 16 # 16 months
    num_pigs_group2 = 3 # remaining 3 pigs
    food_cost_group2 = months_group2 * cost_per_month_per_pig * num_pigs_group2

    # L3
    total_food_cost = food_cost_group1 + food_cost_group2

    # L4
    total_pigs_sold = 6 # 6 piglets
    price_per_pig = 300 # $300
    total_revenue = total_pigs_sold * price_per_pig

    # L5
    profit = total_revenue - total_food_cost

    # FA
    answer = profit
    return answer