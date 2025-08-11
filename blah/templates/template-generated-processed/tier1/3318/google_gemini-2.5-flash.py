def solve():
    """Index: 3318.
    Returns: the total number of fruits Kannon would have eaten in the two meals.
    """
    # L1
    apples_last_night = 3 # 3 apples
    banana_last_night = 1 # a banana
    oranges_last_night = 4 # 4 oranges
    fruits_last_night = apples_last_night + banana_last_night + oranges_last_night

    # L2
    more_apples_today = 4 # 4 more apples than last night
    apples_today = apples_last_night + more_apples_today

    # L3
    banana_multiplier_today = 10 # 10 times as many bananas
    bananas_today = banana_last_night * banana_multiplier_today

    # L4
    orange_multiplier_today = 2 # twice as many oranges
    oranges_today = apples_today * orange_multiplier_today

    # L5
    fruits_tonight = oranges_today + bananas_today + apples_today

    # L6
    total_fruits_two_meals = fruits_tonight + fruits_last_night

    # FA
    answer = total_fruits_two_meals
    return answer