def solve():
    """Index: 1778.
    Returns: Dorothy's profit.
    """
    # L1
    num_doughnuts_made = 25 # made 25 doughnuts
    selling_price_per_doughnut = 3 # sells each for $3
    total_earnings = num_doughnuts_made * selling_price_per_doughnut

    # L2
    ingredient_cost = 53 # spent $53 to buy doughnut ingredients
    profit = total_earnings - ingredient_cost

    # FA
    answer = profit
    return answer