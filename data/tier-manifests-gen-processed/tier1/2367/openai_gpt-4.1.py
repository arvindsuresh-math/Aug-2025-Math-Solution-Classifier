def solve():
    """Index: 2367.
    Returns: the number of meals the chef has for dinner.
    """
    # L1
    lunch_prepared = 17 # chef prepared 17 meals to sell for lunch
    lunch_sold = 12 # he sold 12 meals
    lunch_left = lunch_prepared - lunch_sold

    # L2
    dinner_prepared = 5 # chef prepared another 5 meals for dinner
    dinner_total = lunch_left + dinner_prepared

    # FA
    answer = dinner_total
    return answer