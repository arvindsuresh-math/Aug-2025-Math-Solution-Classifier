def solve():
    """Index: 5877.
    Returns: the profit Alexa and Emily made after paying off expenses.
    """
    # L1
    cost_lemons = 10 # $10 for lemons
    cost_sugar = 5 # $5 for sugar
    cost_cups = 3 # $3 for cups
    total_expenses = cost_lemons + cost_sugar + cost_cups

    # L2
    price_per_cup = 4 # $4 a cup
    cups_sold = 21 # 21 cups
    total_revenue = price_per_cup * cups_sold

    # L3
    profit = total_revenue - total_expenses

    # FA
    answer = profit
    return answer