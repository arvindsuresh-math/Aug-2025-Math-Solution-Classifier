def solve():
    """Index: 1375.
    Returns: the total profit the farmer earned after deducting the cost of food.
    """
    # L1
    pigs_sold_12 = 3 # sells 3 pigs after 12 months
    months_12 = 12 # after 12 months
    feed_cost_per_month = 10 # $10 per month to feed each animal
    food_cost_12 = months_12 * feed_cost_per_month * pigs_sold_12

    # L2
    pigs_sold_16 = 3 # remaining 3 pigs after 16 months
    months_16 = 16 # after 16 months
    food_cost_16 = months_16 * feed_cost_per_month * pigs_sold_16

    # L3
    total_food_cost = food_cost_12 + food_cost_16

    # L4
    total_pigs = 6 # 6 piglets
    sale_price_per_pig = 300 # $300 per pig
    total_revenue = total_pigs * sale_price_per_pig

    # L5
    profit = total_revenue - total_food_cost

    # FA
    answer = profit
    return answer