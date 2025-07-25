def solve():
    """Index: 706.
    Returns: the number of tiles needed to complete the pool.
    """
    # L1
    blue_tiles = 48 # 48 blue tiles
    red_tiles = 32 # 32 red tiles
    current_tiles = blue_tiles + red_tiles

    # L2
    total_needed = 100 # pool needs 100 tiles to be completed
    tiles_needed = total_needed - current_tiles

    # FA
    answer = tiles_needed
    return answer