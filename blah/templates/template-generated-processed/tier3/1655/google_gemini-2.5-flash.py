def solve():
    """Index: 1655.
    Returns: the amount Abe spends on wages.
    """
    # L1
    budget = 3000 # If his budget is $3000
    food_divisor = 3 # a third of his budget on food
    food_cost = budget / food_divisor

    # L2
    supplies_divisor = 4 # a quarter of his budget on restaurant supplies
    supplies_cost = budget / supplies_divisor

    # L3
    wages_cost = budget - food_cost - supplies_cost

    # FA
    answer = wages_cost
    return answer