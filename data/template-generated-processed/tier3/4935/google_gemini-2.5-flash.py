def solve():
    """Index: 4935.
    Returns: the number of days it will take for Jamie's father to burn off 5 pounds.
    """
    # L1
    pounds_to_lose = 5 # 5 pounds
    calories_per_pound = 3500 # 3,500 calories in a pound of body fat
    total_calories_to_burn = pounds_to_lose * calories_per_pound

    # L2
    calories_burned_daily = 2500 # burns 2,500 calories of fat a day
    calories_eaten_daily = 2000 # eating 2000 calories a day
    net_calories_burned_per_day = calories_burned_daily - calories_eaten_daily

    # L3
    days_to_burn_off_fat = total_calories_to_burn / net_calories_burned_per_day

    # FA
    answer = days_to_burn_off_fat
    return answer