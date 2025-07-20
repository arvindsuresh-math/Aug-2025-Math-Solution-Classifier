def solve():
    """Index: 3141.
    Returns: the total number of calories John gets in a day.
    """
    # L1
    breakfast_calories = 500 # Breakfast is 500 calories
    lunch_increase_percent = 0.25 # 25% more calories
    lunch_increase_amount = breakfast_calories * lunch_increase_percent

    # L2
    lunch_calories = breakfast_calories + lunch_increase_amount

    # L3
    dinner_multiplier = 2 # twice as many calories as lunch
    dinner_calories = lunch_calories * dinner_multiplier

    # L4
    num_shakes = 3 # 3 shakes
    calories_per_shake = 300 # each 300 calories
    total_shake_calories = num_shakes * calories_per_shake

    # L5
    total_daily_calories = breakfast_calories + lunch_calories + dinner_calories + total_shake_calories

    # FA
    answer = total_daily_calories
    return answer