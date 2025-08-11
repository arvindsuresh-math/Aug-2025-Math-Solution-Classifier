def solve():
    """Index: 3450.
    Returns: the total minutes Carson will spend gardening.
    """
    # L1
    num_lines_to_mow = 40 # mow 40 lines
    time_per_line = 2 # 2 minutes to mow one line
    mowing_time = num_lines_to_mow * time_per_line

    # L2
    num_rows_flowers = 8 # 8 rows of flowers
    flowers_per_row = 7 # each with 7 flowers
    total_flowers = num_rows_flowers * flowers_per_row

    # L3
    time_per_flower = 0.5 # half a minute to plant each flower
    planting_time = time_per_flower * total_flowers

    # L4
    total_gardening_time = planting_time + mowing_time

    # FA
    answer = total_gardening_time
    return answer