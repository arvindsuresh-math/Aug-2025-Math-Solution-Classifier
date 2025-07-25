def solve():
    """Index: 3961.
    Returns: the time it will take Janet to get home.
    """
    # L1
    blocks_south_initial = 8 # walks 8 blocks south
    blocks_north_initial = 3 # walks 3 blocks north
    net_south_blocks = blocks_south_initial - blocks_north_initial

    # L2
    west_multiplier = 7 # seven times as many blocks west
    blocks_west = blocks_north_initial * west_multiplier

    # L3
    east_multiplier = 2 # twice as many blocks east
    blocks_east = blocks_south_initial * east_multiplier

    # L4
    net_west_blocks = blocks_west - blocks_east

    # L5
    total_distance_to_home = net_south_blocks + net_west_blocks

    # L6
    speed_blocks_per_minute = 2 # 2 blocks/minute
    time_to_home_minutes = total_distance_to_home / speed_blocks_per_minute

    # FA
    answer = time_to_home_minutes
    return answer