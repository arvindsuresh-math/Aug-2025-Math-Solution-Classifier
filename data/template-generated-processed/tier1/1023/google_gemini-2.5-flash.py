def solve():
    """Index: 1023.
    Returns: the total number of bricks Cooper needs to complete his fence.
    """
    # L1
    rows_per_wall = 5 # 5 bricks high
    bricks_per_row = 20 # 20 bricks long
    bricks_per_layer = rows_per_wall * bricks_per_row

    # L2
    depth_bricks = 2 # 2 bricks deep
    bricks_per_wall = bricks_per_layer * depth_bricks

    # L3
    num_walls = 4 # four walls
    total_bricks = bricks_per_wall * num_walls

    # FA
    answer = total_bricks
    return answer