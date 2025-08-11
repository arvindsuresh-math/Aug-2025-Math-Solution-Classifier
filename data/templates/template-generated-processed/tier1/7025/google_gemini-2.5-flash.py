def solve():
    """Index: 7025.
    Returns: the number of calories Voldemort can still take.
    """
    # L1
    cake_calories = 110 # a piece of cake that has 110 calories
    chips_calories = 310 # 1 pack of chips that contained 310 calories
    coke_calories = 215 # a 500 ml bottle of coke that has 215 calories
    night_intake = cake_calories + chips_calories + coke_calories

    # L2
    breakfast_calories = 560 # 560 calories
    lunch_calories = 780 # 780 calories
    day_intake_breakfast_lunch = breakfast_calories + lunch_calories

    # L3
    total_daily_intake = day_intake_breakfast_lunch + night_intake

    # L4
    daily_limit = 2500 # 2500 calorie intake limit per day
    remaining_calories = daily_limit - total_daily_intake

    # FA
    answer = remaining_calories
    return answer