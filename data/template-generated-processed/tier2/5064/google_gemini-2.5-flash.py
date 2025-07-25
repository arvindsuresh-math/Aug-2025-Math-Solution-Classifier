def solve():
    """Index: 5064.
    Returns: the total cost for tile.
    """
    # L1
    courtyard_length = 10 # 10 feet
    courtyard_width = 25 # 25 feet
    courtyard_area = courtyard_length * courtyard_width

    # L2
    tiles_per_sq_foot = 4 # 4 tiles per square foot
    total_tiles_needed = courtyard_area * tiles_per_sq_foot

    # L3
    green_tile_percentage_text = 40 # 40%
    percent_to_decimal_factor = 0.01 # WK
    num_green_tiles = total_tiles_needed * green_tile_percentage_text * percent_to_decimal_factor

    # L4
    num_red_tiles = total_tiles_needed - num_green_tiles

    # L5
    cost_per_red_tile = 1.50 # $1.50/tile
    cost_red_tiles = num_red_tiles * cost_per_red_tile

    # L6
    cost_per_green_tile = 3.00 # $3/tile
    cost_green_tiles = num_green_tiles * cost_per_green_tile

    # L7
    total_cost = cost_red_tiles + cost_green_tiles

    # FA
    answer = total_cost
    return answer