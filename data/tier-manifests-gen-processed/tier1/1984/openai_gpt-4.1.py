def solve():
    """Index: 1984.
    Returns: how many more calories Jacob ate than he planned.
    """
    # L1
    lunch_calories = 900 # 900 calories for lunch
    breakfast_calories = 400 # 400 calories for breakfast
    dinner_calories = 1100 # 1100 calories for dinner
    total_calories = lunch_calories + breakfast_calories + dinner_calories

    # L2
    calorie_goal = 1800 # less than 1800 calories a day
    over_calories = total_calories - calorie_goal

    # FA
    answer = over_calories
    return answer