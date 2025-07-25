def solve():
    """Index: 5993.
    Returns: the number of days it will take to lose the target weight.
    """
    # L1
    calories_burned_daily = 2300 # burns 2300 a day
    calories_eaten_daily = 1800 # eats 1800 calories a day
    net_calories_burned_daily = calories_burned_daily - calories_eaten_daily

    # L2
    calories_per_pound = 4000 # burn 4000 calories to lose 1 pound
    pounds_to_lose = 10 # lose 10 pounds
    total_calories_needed = calories_per_pound * pounds_to_lose

    # L3
    days_to_lose_weight = total_calories_needed / net_calories_burned_daily

    # FA
    answer = days_to_lose_weight
    return answer