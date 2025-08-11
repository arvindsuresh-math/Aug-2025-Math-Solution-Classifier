def solve():
    """Index: 6286.
    Returns: the total number of bees in the hive including the queen at the end of 7 days.
    """
    # L1
    bees_born_per_day = 3000 # 3000 bees hatch from the queen's eggs every day
    num_days = 7 # at the end of 7 days
    total_new_bees = bees_born_per_day * num_days

    # L2
    bees_lost_per_day = 900 # loses 900 bees every day
    total_lost_bees = bees_lost_per_day * num_days

    # L3
    initial_bees = 12500 # at the beginning the queen had 12500 bees
    bees_after_7_days = initial_bees + total_new_bees - total_lost_bees

    # L4
    queen_count = 1 # WK
    final_total_bees = bees_after_7_days + queen_count

    # FA
    answer = final_total_bees
    return answer