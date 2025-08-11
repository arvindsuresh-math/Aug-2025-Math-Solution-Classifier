def solve():
    """Index: 1853.
    Returns: the total number of shirts Shenny should pack for her vacation.
    """
    # L1
    total_days = 7 # Between Monday and Sunday there are 7 days
    days_with_same_shirt = 2 # using the same shirt for 2 days (Monday and Sunday)
    days_with_different_shirts = total_days - days_with_same_shirt

    # L2
    shirts_per_day = 2 # 2 different shirts each of those 5 days
    shirts_for_different_days = shirts_per_day * days_with_different_shirts

    # L3
    shirts_for_same_days = 1 # 1 shirt for Monday and Sunday (same shirt)
    total_shirts = shirts_for_different_days + shirts_for_same_days

    # FA
    answer = total_shirts
    return answer