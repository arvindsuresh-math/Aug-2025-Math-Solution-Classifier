def solve():
    """Index: 1164.
    Returns: the amount of water left in the tank at the end of the fourth hour.
    """
    # L1
    water_lost_per_hour = 2 # loses 2 gallons of water per hour
    total_hours = 4 # over the four hours
    total_water_lost = water_lost_per_hour * total_hours

    # L2
    water_added_hour3 = 1 # adds 1 gallon of water to the tank in hour three
    water_added_hour4 = 3 # adds three gallons of water to the tank in the fourth hour
    total_water_added = water_added_hour3 + water_added_hour4

    # L3
    initial_water = 40 # tank starts with 40 gallons of water
    water_left = initial_water - total_water_lost + total_water_added

    # FA
    answer = water_left
    return answer