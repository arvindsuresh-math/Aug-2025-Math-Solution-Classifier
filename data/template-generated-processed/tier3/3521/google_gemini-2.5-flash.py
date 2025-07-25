def solve():
    """Index: 3521.
    Returns: Will's net calorie intake after jogging.
    """
    # L1
    minutes_per_hour = 60 # WK
    half_hour_divisor = 2 # half an hour
    jogging_minutes = minutes_per_hour / half_hour_divisor

    # L2
    calories_per_minute = 10 # 10 calories of energy per minute
    calories_used = calories_per_minute * jogging_minutes

    # L3
    initial_calories = 900 # 900 calories of energy
    net_calorie_intake = initial_calories - calories_used

    # FA
    answer = net_calorie_intake
    return answer