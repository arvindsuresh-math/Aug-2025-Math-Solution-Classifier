def solve():
    """Index: 580.
    Returns: the total number of bricks of snow Libby used for her igloo.
    """
    # L1
    total_rows = 10 # total of 10 rows of bricks of snow
    half_divisor = 2 # bottom half of the igloo
    bottom_half_rows = total_rows / half_divisor

    # L2
    bricks_per_row_bottom = 12 # 12 bricks of snow in each row
    total_bricks_bottom_half = bottom_half_rows * bricks_per_row_bottom

    # L3
    bricks_per_row_top = 8 # 8 bricks of snow in each row
    total_bricks_top_half = bottom_half_rows * bricks_per_row_top

    # L4
    total_bricks_igloo = total_bricks_bottom_half + total_bricks_top_half

    # FA
    answer = total_bricks_igloo
    return answer