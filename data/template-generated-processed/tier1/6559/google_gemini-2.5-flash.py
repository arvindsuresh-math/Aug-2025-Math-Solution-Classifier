def solve():
    """Index: 6559.
    Returns: the number of white tiles.
    """
    # L1
    yellow_tiles = 3 # Three tiles are yellow
    blue_tiles_more_than_yellow = 1 # one more than the number of yellow tiles
    blue_tiles = yellow_tiles + blue_tiles_more_than_yellow

    # L2
    purple_tiles = 6 # Six tiles are purple
    colored_tiles_total = yellow_tiles + blue_tiles + purple_tiles

    # L3
    total_tiles = 20 # 20 equal tiles
    white_tiles = total_tiles - colored_tiles_total

    # FA
    answer = white_tiles
    return answer