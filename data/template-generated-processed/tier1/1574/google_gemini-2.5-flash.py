def solve():
    """Index: 1574.
    Returns: the total number of bricks used to make both walls.
    """
    # L1
    bricks_per_row = 30 # 30 bricks in a single row
    rows_per_wall = 50 # 50 rows in each wall
    bricks_per_wall = bricks_per_row * rows_per_wall

    # L2
    num_walls = 2 # Two brick walls
    total_bricks = bricks_per_wall * num_walls

    # FA
    answer = total_bricks
    return answer