def solve():
    """Index: 1256.
    Returns: the total number of vegetables Conor can chop per week.
    """
    # L1
    eggplants_per_day = 12 # 12 eggplants
    work_days_per_week = 4 # works 4 times a week
    eggplants_per_week = eggplants_per_day * work_days_per_week

    # L2
    carrots_per_day = 9 # 9 carrots
    carrots_per_week = carrots_per_day * work_days_per_week

    # L3
    potatoes_per_day = 8 # 8 potatoes
    potatoes_per_week = potatoes_per_day * work_days_per_week

    # L4
    total_vegetables_per_week = eggplants_per_week + carrots_per_week + potatoes_per_week

    # FA
    answer = total_vegetables_per_week
    return answer