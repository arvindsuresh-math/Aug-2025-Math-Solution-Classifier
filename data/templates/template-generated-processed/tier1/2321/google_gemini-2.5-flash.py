def solve():
    """Index: 2321.
    Returns: the total number of blocks Pete traveled.
    """
    # L1
    blocks_to_garage = 5 # walked 5 blocks from his house to the bus garage
    blocks_by_bus = 20 # rode the bus 20 blocks to the post office
    blocks_to_post_office = blocks_to_garage + blocks_by_bus

    # L2
    round_trip_multiplier = 2 # came home the same way
    total_blocks_traveled = blocks_to_post_office * round_trip_multiplier

    # FA
    answer = total_blocks_traveled
    return answer