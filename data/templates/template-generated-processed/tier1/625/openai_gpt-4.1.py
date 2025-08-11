def solve():
    """Index: 625.
    Returns: the total number of trash cans the town has paid for.
    """
    # L1
    street_trash_cans = 14 # adding 14 trash cans to the streets
    multiplier_back_of_stores = 2 # twice as many trash cans to the back of stores
    back_store_trash_cans = street_trash_cans * multiplier_back_of_stores

    # L2
    total_trash_cans = street_trash_cans + back_store_trash_cans

    # FA
    answer = total_trash_cans
    return answer