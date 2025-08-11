def solve():
    """Index: 2235.
    Returns: the total grams of fat Robbie gets in a week.
    """
    # L1
    rice_morning = 3 # 3 cups of rice in the morning
    fat_per_cup = 10 # a cup of rice has 10 grams of fat
    fat_morning = rice_morning * fat_per_cup

    # L2
    rice_afternoon = 2 # 2 cups of rice in the afternoon
    fat_afternoon = fat_per_cup * rice_afternoon

    # L3
    rice_evening = 5 # 5 cups of rice in the evening
    fat_evening = rice_evening * fat_per_cup

    # L4
    fat_per_day = fat_evening + fat_morning + fat_afternoon

    # L5
    days_per_week = 7 # WK
    fat_per_week = fat_per_day * days_per_week

    # FA
    answer = fat_per_week
    return answer