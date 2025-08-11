def solve():
    """Index: 1301.
    Returns: the total number of tiles in the shower.
    """
    # L1
    tiles_width = 8 # 8 tiles running the width of the wall
    tiles_height = 20 # 20 tiles running the height of the wall
    tiles_per_wall = tiles_width * tiles_height

    # L2
    num_walls = 3 # 3 sided shower
    total_tiles = tiles_per_wall * num_walls

    # FA
    answer = total_tiles
    return answer