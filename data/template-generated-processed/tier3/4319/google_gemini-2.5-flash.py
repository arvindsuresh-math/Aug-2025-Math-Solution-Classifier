def solve():
    """Index: 4319.
    Returns: the total money Tammy will have earned.
    """
    # L1
    num_trees = 10 # 10 orange trees
    oranges_per_tree_per_day = 12 # pick 12 oranges each day
    oranges_per_day = num_trees * oranges_per_tree_per_day

    # L2
    oranges_per_pack = 6 # sells 6-packs of oranges
    packs_per_day = oranges_per_day / oranges_per_pack

    # L3
    days_per_week = 7 # WK
    packs_per_week = packs_per_day * days_per_week

    # L4
    num_weeks = 3 # after 3 weeks
    total_packs_sold = packs_per_week * num_weeks

    # L5
    price_per_pack = 2 # for $2
    total_money_earned = total_packs_sold * price_per_pack

    # FA
    answer = total_money_earned
    return answer