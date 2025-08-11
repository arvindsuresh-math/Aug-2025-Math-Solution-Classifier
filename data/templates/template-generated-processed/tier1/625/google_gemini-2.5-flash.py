def solve():
    """Index: 625.
    Returns: the total number of trash cans the town has paid for.
    """
    # L1
    street_trash_cans = 14 # 14 trash cans to the streets
    multiplier_twice = 2 # twice as many trash cans
    store_trash_cans = street_trash_cans * multiplier_twice

    # L2
    total_trash_cans = street_trash_cans + store_trash_cans

    # FA
    answer = total_trash_cans
    return answer