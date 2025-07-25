def solve():
    """Index: 5799.
    Returns: the total number of blocks Trent traveled.
    """
    # L1
    blocks_to_bus_stop = 4 # walked 4 blocks from his house to the bus stop
    blocks_bus_to_library = 7 # rode the bus 7 blocks to the library
    blocks_to_library = blocks_to_bus_stop + blocks_bus_to_library

    # L2
    total_blocks_traveled = blocks_to_library + blocks_to_library

    # FA
    answer = total_blocks_traveled
    return answer