def solve():
    """Index: 5761.
    Returns: the total liters of milk the farmer gets in a week.
    """
    # L1
    milk_per_cow_per_day = 5 # 5 liters of milk a day
    days_per_week = 7 # WK
    milk_per_cow_per_week = milk_per_cow_per_day * days_per_week

    # L2
    num_cows = 52 # 52 cows
    total_milk_per_week = num_cows * milk_per_cow_per_week

    # FA
    answer = total_milk_per_week
    return answer