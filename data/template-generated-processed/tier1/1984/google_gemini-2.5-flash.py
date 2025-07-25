def solve():
    """Index: 1984.
    Returns: the number of calories Jacob ate over his plan.
    """
    # L1
    lunch_calories = 900 # 900 calories for lunch
    breakfast_calories = 400 # 400 calories for breakfast
    dinner_calories = 1100 # 1100 calories for dinner
    total_calories_eaten = lunch_calories + breakfast_calories + dinner_calories

    # L2
    planned_calories_per_day = 1800 # less than 1800 calories a day
    calories_over_planned = total_calories_eaten - planned_calories_per_day

    # FA
    answer = calories_over_planned
    return answer