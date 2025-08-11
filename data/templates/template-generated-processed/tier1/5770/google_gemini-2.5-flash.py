def solve():
    """Index: 5770.
    Returns: the total number of eggs supplied to two stores in a week.
    """
    # L1
    eggs_per_dozen_store_1 = 5 # 5 dozen eggs
    dozen = 12 # WK
    eggs_store_1_per_day = eggs_per_dozen_store_1 * dozen

    # L2
    eggs_store_2_per_day = 30 # another store with 30 eggs each day
    total_eggs_per_day = eggs_store_1_per_day + eggs_store_2_per_day

    # L3
    days_in_week = 7 # WK
    total_eggs_per_week = total_eggs_per_day * days_in_week

    # FA
    answer = total_eggs_per_week
    return answer