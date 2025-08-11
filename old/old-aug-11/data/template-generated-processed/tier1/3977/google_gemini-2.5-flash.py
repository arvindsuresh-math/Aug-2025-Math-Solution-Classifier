def solve():
    """Index: 3977.
    Returns: the total number of sequins Jane adds to her costume.
    """
    # L1
    blue_rows = 6 # 6 rows of 8 blue sequins
    blue_sequins_per_row = 8 # 8 blue sequins each
    total_blue_sequins = blue_rows * blue_sequins_per_row

    # L2
    purple_rows = 5 # 5 rows of 12 purple sequins
    purple_sequins_per_row = 12 # 12 purple sequins each
    total_purple_sequins = purple_rows * purple_sequins_per_row

    # L3
    green_rows = 9 # 9 rows of 6 green sequins
    green_sequins_per_row = 6 # 6 green sequins each
    total_green_sequins = green_rows * green_sequins_per_row

    # L4
    total_sequins = total_blue_sequins + total_purple_sequins + total_green_sequins

    # FA
    answer = total_sequins
    return answer