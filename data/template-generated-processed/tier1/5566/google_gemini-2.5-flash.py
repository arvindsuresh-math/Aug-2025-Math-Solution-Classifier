def solve():
    """Index: 5566.
    Returns: the total blocks Annie traveled.
    """
    # L1
    blocks_to_bus_stop = 5 # walked 5 blocks from her house to the bus stop
    blocks_bus_to_coffee_shop = 7 # rode the bus 7 blocks to the coffee shop
    blocks_to_coffee_shop = blocks_to_bus_stop + blocks_bus_to_coffee_shop

    # L2
    multiplier_round_trip = 2 # came home the same way
    total_blocks_round_trip = blocks_to_coffee_shop * multiplier_round_trip

    # FA
    answer = total_blocks_round_trip
    return answer