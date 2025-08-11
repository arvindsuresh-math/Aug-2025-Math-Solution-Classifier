def solve():
    """Index: 1778.
    Returns: Dorothy's profit from selling the doughnuts.
    """
    # L1
    num_doughnuts = 25 # she made 25 doughnuts
    price_per_doughnut = 3 # sells each for $3
    total_earnings = num_doughnuts * price_per_doughnut

    # L2
    ingredient_cost = 53 # spent $53 to buy doughnut ingredients
    profit = total_earnings - ingredient_cost

    # FA
    answer = profit
    return answer