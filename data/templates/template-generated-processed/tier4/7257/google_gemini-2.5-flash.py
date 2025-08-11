def solve():
    """Index: 7257.
    Returns: the total money James made.
    """
    # L1
    beef_pounds = 20 # 20 pounds of beef
    pork_fraction_divisor = 2 # half that much pork
    pork_pounds = beef_pounds / pork_fraction_divisor

    # L2
    total_meat_pounds = beef_pounds + pork_pounds

    # L3
    meat_per_meal = 1.5 # 1.5 pounds of meat to make meals
    num_meals = total_meat_pounds / meat_per_meal

    # L4
    price_per_meal = 20 # Each meal sells for $20
    total_money_made = num_meals * price_per_meal

    # FA
    answer = total_money_made
    return answer