def solve():
    """Index: 580.
    Returns: the total number of bricks of snow Libby used for her igloo.
    """
    # L1
    total_rows = 10 # total of 10 rows of bricks of snow
    half_divisor = 2 # bottom half / top half
    rows_per_half = total_rows / half_divisor

    # L2
    bottom_bricks_per_row = 12 # 12 bricks of snow in each row (bottom half)
    bottom_half_bricks = rows_per_half * bottom_bricks_per_row

    # L3
    top_bricks_per_row = 8 # 8 bricks of snow in each row (top half)
    top_half_bricks = rows_per_half * top_bricks_per_row

    # L4
    total_bricks = bottom_half_bricks + top_half_bricks

    # FA
    answer = total_bricks
    return answer