def solve():
    """Index: 5765.
    Returns: the total amount of food the puppy will eat over the next 4 weeks.
    """
    # L1
    days_per_week = 7 # WK
    first_period_weeks = 2 # two weeks starting tomorrow
    days_in_first_period = first_period_weeks * days_per_week

    # L2
    food_per_feeding_first_period = 0.25 # 1/4 cup of food
    feedings_per_day_first_period = 3 # three times a day
    cups_per_day_first_period = food_per_feeding_first_period * feedings_per_day_first_period

    # L3
    total_food_first_period = cups_per_day_first_period * days_in_first_period

    # L4
    food_per_feeding_second_period = 0.5 # 1/2 cup of food
    feedings_per_day_second_period = 2 # twice a day
    cups_per_day_second_period = food_per_feeding_second_period * feedings_per_day_second_period

    # L5
    second_period_weeks = 2 # For the following 2 weeks
    days_in_second_period = second_period_weeks * days_per_week
    total_food_second_period = cups_per_day_second_period * days_in_second_period

    # L6
    food_fed_today = 0.5 # fed him 1/2 cup of food today
    total_food_over_4_weeks = food_fed_today + total_food_first_period + total_food_second_period

    # FA
    answer = total_food_over_4_weeks
    return answer