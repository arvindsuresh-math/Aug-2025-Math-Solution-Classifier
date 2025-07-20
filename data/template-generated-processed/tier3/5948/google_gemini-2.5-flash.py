def solve():
    """Index: 5948.
    Returns: the total construction costs required for the project.
    """
    # L1
    land_cost_per_sq_m = 50 # land costs $50 per square meter
    required_sq_meters = 2000 # requires 2000 square meters
    cost_for_land = land_cost_per_sq_m * required_sq_meters

    # L2
    brick_cost_per_1000 = 100 # bricks cost $100 per 1000 bricks
    bricks_unit = 1000 # bricks cost $100 per 1000 bricks
    required_bricks = 10000 # 10000 bricks
    cost_for_bricks = (brick_cost_per_1000 / bricks_unit) * required_bricks

    # L3
    tile_cost_per_tile = 10 # roof tiles cost $10 per roof tile
    required_tiles = 500 # 500 roof tiles
    cost_for_tiles = tile_cost_per_tile * required_tiles

    # L4
    total_construction_cost = cost_for_land + cost_for_bricks + cost_for_tiles

    # FA
    answer = total_construction_cost
    return answer