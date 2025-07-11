def solve():
    """Index: 2321.
    Returns: the total number of blocks Pete traveled in all.
    """
    # L1
    blocks_walked = 5 # walked 5 blocks from his house to the bus garage
    blocks_bus = 20 # rode the bus 20 blocks to the post office
    blocks_to_post_office = blocks_walked + blocks_bus

    # L2
    round_trip_multiplier = 2 # came home the same way
    total_blocks = blocks_to_post_office * round_trip_multiplier

    # FA
    answer = total_blocks
    return answer