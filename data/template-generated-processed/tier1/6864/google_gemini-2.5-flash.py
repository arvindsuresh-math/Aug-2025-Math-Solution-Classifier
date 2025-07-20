def solve():
    """Index: 6864.
    Returns: the number of paper cups used.
    """
    # L1
    num_dozens_per_set = 2 # 2-dozen paper cups
    dozen = 12 # WK
    cups_per_set = num_dozens_per_set * dozen

    # L2
    num_sets = 4 # four sets
    total_prepared_cups = cups_per_set * num_sets

    # L3
    damaged_cups = 5 # 5 cups were damaged
    unused_cups = 30 # 30 were not used
    total_not_used = damaged_cups + unused_cups

    # L4
    cups_used = total_prepared_cups - total_not_used

    # FA
    answer = cups_used
    return answer