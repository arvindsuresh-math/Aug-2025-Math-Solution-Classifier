def solve():
    """Index: 2367.
    Returns: the total number of meals the chef has for dinner.
    """
    # L1
    prepared_lunch_meals = 17 # prepared 17 meals to sell for lunch
    sold_lunch_meals = 12 # sold 12 meals
    remaining_lunch_meals = prepared_lunch_meals - sold_lunch_meals

    # L2
    prepared_dinner_meals = 5 # prepared another 5 meals for dinner
    total_dinner_meals = remaining_lunch_meals + prepared_dinner_meals

    # FA
    answer = total_dinner_meals
    return answer