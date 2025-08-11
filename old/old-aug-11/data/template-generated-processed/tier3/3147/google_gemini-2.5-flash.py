def solve():
    """Index: 3147.
    Returns: the total grams of birdseed Peter needs to buy for a week.
    """
    # L1
    num_parakeets = 3 # 3 parakeets
    parakeet_daily_food = 2 # each parakeet eats 2 grams a day
    total_parakeet_daily_food = num_parakeets * parakeet_daily_food

    # L2
    num_parrots = 2 # 2 parrots
    parrot_daily_food = 14 # His parrots eat 14 grams a day
    total_parrot_daily_food = num_parrots * parrot_daily_food

    # L3
    finch_food_numerator = 1 # WK
    finch_food_denominator = 2 # WK
    finch_daily_food = (finch_food_numerator / finch_food_denominator) * parakeet_daily_food

    # L4
    num_finches = 4 # 4 finches
    total_finch_daily_food = num_finches * finch_daily_food

    # L5
    total_daily_food = total_parakeet_daily_food + total_parrot_daily_food + total_finch_daily_food

    # L6
    days_per_week = 7 # WK

    # L7
    total_weekly_food = days_per_week * total_daily_food

    # FA
    answer = total_weekly_food
    return answer