def solve():
    """Index: 5458.
    Returns: the total amount of water James can store.
    """
    # L1
    cask_capacity = 20 # a cask stores 20 gallons
    multiplier_for_twice = 2 # twice as much
    barrel_more_than_twice = 3 # 3 gallons more than twice as much
    barrel_capacity = cask_capacity * multiplier_for_twice + barrel_more_than_twice

    # L2
    num_barrels = 4 # he has 4 barrels
    total_water_stored = num_barrels * barrel_capacity

    # FA
    answer = total_water_stored
    return answer