def solve():
    """Index: 2041.
    Returns: the amount of change Tony will have after buying water.
    """
    # L1
    sandbox_depth = 2 # two feet deep
    sandbox_width = 4 # four feet wide
    sandbox_length = 5 # 5 feet long
    sandbox_volume = sandbox_depth * sandbox_width * sandbox_length

    # L2
    weight_per_cubic_foot = 3 # A cubic foot of sand weighs 3 pounds
    total_sand_needed_pounds = sandbox_volume * weight_per_cubic_foot

    # L3
    bucket_capacity = 2 # a bucket that holds 2 pounds of sand
    total_trips = total_sand_needed_pounds / bucket_capacity

    # L4
    trips_per_drink = 4 # every 4 trips he takes he drinks
    number_of_drink_occasions = total_trips / trips_per_drink

    # L5
    ounces_per_drink = 3 # drinks 3 ounces of bottled water
    total_ounces_water_needed = number_of_drink_occasions * ounces_per_drink

    # L6
    bottle_size_ounces = 15 # A 15 ounce bottle of water
    bottles_needed = total_ounces_water_needed / bottle_size_ounces

    # L7
    bottle_cost = 2 # A 15 ounce bottle of water costs $2
    total_water_cost = bottles_needed * bottle_cost

    # L8
    money_on_hand = 10 # He has $10 with him
    change_amount = money_on_hand - total_water_cost

    # FA
    answer = change_amount
    return answer