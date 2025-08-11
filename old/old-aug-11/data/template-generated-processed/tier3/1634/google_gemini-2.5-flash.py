def solve():
    """Index: 1634.
    Returns: the number of cups of lemonade Alexa needs to sell to make the desired profit.
    """
    # L1
    desired_profit = 80 # profit of $80
    ingredient_cost = 20 # spent $20 on ingredients
    total_revenue_needed = desired_profit + ingredient_cost

    # L2
    price_per_cup = 2 # sells lemonade for $2 for one cup
    cups_to_sell = total_revenue_needed / price_per_cup

    # FA
    answer = cups_to_sell
    return answer