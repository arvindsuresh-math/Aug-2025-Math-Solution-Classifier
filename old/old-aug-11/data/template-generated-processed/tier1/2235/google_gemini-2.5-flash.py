def solve():
    """Index: 2235.
    Returns: the total grams of fat Robbie gets in a week.
    """
    # L1
    morning_cups_rice = 3 # 3 cups of rice in the morning
    grams_fat_per_cup = 10 # 10 grams of fat
    morning_fat = morning_cups_rice * grams_fat_per_cup

    # L2
    afternoon_cups_rice = 2 # 2 cups of rice in the afternoon
    afternoon_fat = grams_fat_per_cup * afternoon_cups_rice

    # L3
    evening_cups_rice = 5 # 5 cups of rice in the evening
    evening_fat = evening_cups_rice * grams_fat_per_cup

    # L4
    daily_fat_total = evening_fat + morning_fat + afternoon_fat

    # L5
    days_in_week = 7 # WK
    weekly_fat_total = daily_fat_total * days_in_week

    # FA
    answer = weekly_fat_total
    return answer