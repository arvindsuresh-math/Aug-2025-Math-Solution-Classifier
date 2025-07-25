def solve():
    """Index: 1256.
    Returns: the total number of vegetables Conor can chop in a week.
    """
    # L1
    eggplants_per_day = 12 # Conor can chop 12 eggplants ... in a day
    days_per_week = 4 # he works 4 times a week
    eggplants_per_week = eggplants_per_day * days_per_week

    # L2
    carrots_per_day = 9 # 9 carrots ... in a day
    carrots_per_week = carrots_per_day * days_per_week

    # L3
    potatoes_per_day = 8 # 8 potatoes ... in a day
    potatoes_per_week = potatoes_per_day * days_per_week

    # L4
    total_vegetables = eggplants_per_week + carrots_per_week + potatoes_per_week

    # FA
    answer = total_vegetables
    return answer