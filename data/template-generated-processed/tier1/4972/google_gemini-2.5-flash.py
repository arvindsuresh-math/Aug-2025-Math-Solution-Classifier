def solve():
    """Index: 4972.
    Returns: the total number of candy bars Amanda kept for herself.
    """
    # L1
    initial_candy_bars = 7 # Amanda had 7 candy bars
    gave_sister_first_time = 3 # She gave 3 to her sister
    remaining_after_first_giveaway = initial_candy_bars - gave_sister_first_time

    # L2
    multiplier_second_giveaway = 4 # 4 times as many candy bars
    gave_sister_second_time = multiplier_second_giveaway * gave_sister_first_time

    # L3
    bought_new_candy_bars = 30 # bought another 30 candy bars
    remaining_after_second_giveaway = bought_new_candy_bars - gave_sister_second_time

    # L4
    total_kept = remaining_after_second_giveaway + remaining_after_first_giveaway

    # FA
    answer = total_kept
    return answer