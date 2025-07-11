def solve():
    """Index: 1023.
    Returns: the total number of bricks Cooper needs to complete his fence.
    """
    # L1
    rows_per_wall = 5 # 5 bricks high
    bricks_per_row = 20 # 20 bricks long
    single_layer_bricks = rows_per_wall * bricks_per_row

    # L2
    wall_thickness = 2 # 2 bricks deep
    bricks_per_wall = single_layer_bricks * wall_thickness

    # L3
    num_walls = 4 # four walls
    total_bricks = bricks_per_wall * num_walls

    # FA
    answer = total_bricks
    return answer