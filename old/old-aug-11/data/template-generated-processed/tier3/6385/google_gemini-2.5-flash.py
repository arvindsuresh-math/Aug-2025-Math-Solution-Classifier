def solve():
    """Index: 6385.
    Returns: the number of "Victors" worth of food a bear would eat.
    """
    # L1
    num_weeks = 3 # in 3 weeks
    days_per_week = 7 # WK
    total_days = num_weeks * days_per_week

    # L2
    food_per_day = 90 # 90 pounds of food per day
    total_food_eaten = food_per_day * total_days

    # L3
    victor_weight = 126 # Victor weighs 126 pounds
    victors_worth_of_food = total_food_eaten / victor_weight

    # FA
    answer = victors_worth_of_food
    return answer