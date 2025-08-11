def solve():
    """Index: 3123.
    Returns: how much more water Madeline needs to drink.
    """
    # L1
    bottle_capacity = 12 # Her water bottle can hold 12 ounces of water
    refills = 7 # She refills her water bottle 7 times
    water_drank = bottle_capacity * refills

    # L2
    target_water = 100 # Madeline wants to drink 100 ounces of water in a day
    water_needed = target_water - water_drank

    # FA
    answer = water_needed
    return answer