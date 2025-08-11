def solve():
    """Index: 3185.
    Returns: the total number of meals served by Gordon's three restaurants per week.
    """
    # L1
    first_restaurant_daily_meals = 20 # first restaurant serves 20 meals
    days_per_week = 7 # WK
    first_restaurant_weekly_meals = first_restaurant_daily_meals * days_per_week

    # L2
    second_restaurant_daily_meals = 40 # second restaurant serves 40 meals
    second_restaurant_weekly_meals = second_restaurant_daily_meals * days_per_week

    # L3
    third_restaurant_daily_meals = 50 # third restaurant serves 50 meals
    third_restaurant_weekly_meals = third_restaurant_daily_meals * days_per_week

    # L4
    total_weekly_meals = first_restaurant_weekly_meals + second_restaurant_weekly_meals + third_restaurant_weekly_meals

    # FA
    answer = total_weekly_meals
    return answer