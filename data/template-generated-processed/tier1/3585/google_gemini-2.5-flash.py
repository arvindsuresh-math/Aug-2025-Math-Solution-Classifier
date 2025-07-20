def solve():
    """Index: 3585.
    Returns: the number of meals left to be distributed.
    """
    # L1
    meals_prepared_initial = 113 # Colt and Curt prepared 113 meals
    meals_from_sole_mart = 50 # Sole Mart provided 50 more meals
    total_meals = meals_prepared_initial + meals_from_sole_mart

    # L2
    meals_given_away = 85 # given 85 meals already
    meals_left = total_meals - meals_given_away

    # FA
    answer = meals_left
    return answer