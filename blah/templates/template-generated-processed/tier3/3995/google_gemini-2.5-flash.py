def solve():
    """Index: 3995.
    Returns: the total number of tiles Kimiko needs to buy.
    """
    # L1
    kitchen_width = 48 # 48 inches
    tile_width = 6 # Each tile is 6 square inches
    tiles_in_one_row = kitchen_width / tile_width

    # L2
    kitchen_height = 72 # 72 inches
    number_of_rows = kitchen_height / tile_width

    # L3
    total_tiles = tiles_in_one_row * number_of_rows

    # FA
    answer = total_tiles
    return answer