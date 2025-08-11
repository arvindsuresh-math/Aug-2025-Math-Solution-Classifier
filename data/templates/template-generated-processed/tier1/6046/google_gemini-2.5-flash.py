def solve():
    """Index: 6046.
    Returns: the number of calories Ellen has left for dinner.
    """
    # L1
    breakfast_calories = 353 # 353 calories
    lunch_calories = 885 # 885
    snack_calories = 130 # 130 calories
    total_calories_eaten = breakfast_calories + lunch_calories + snack_calories

    # L2
    daily_calorie_limit = 2200 # 2,200 calorie a day diet
    calories_left_for_dinner = daily_calorie_limit - total_calories_eaten

    # FA
    answer = calories_left_for_dinner
    return answer