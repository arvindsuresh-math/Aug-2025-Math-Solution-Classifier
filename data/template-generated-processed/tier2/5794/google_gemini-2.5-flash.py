def solve():
    """Index: 5794.
    Returns: the amount of money Todd has after paying back his brother.
    """
    # L1
    borrowed_amount = 100 # borrowed $100
    ingredient_cost = 75 # spent $75 on ingredients
    money_after_ingredients = borrowed_amount - ingredient_cost

    # L2
    num_snow_cones_sold = 200 # sells 200 of them
    price_per_snow_cone = 0.75 # for $.75 each
    money_from_sales = num_snow_cones_sold * price_per_snow_cone

    # L3
    total_money_before_repayment = money_after_ingredients + money_from_sales

    # L4
    repayment_amount = 110 # repay him $110
    final_money = total_money_before_repayment - repayment_amount

    # FA
    answer = final_money
    return answer