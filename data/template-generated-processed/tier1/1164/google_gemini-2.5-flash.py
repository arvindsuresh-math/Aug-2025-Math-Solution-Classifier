def solve():
    """Index: 1164.
    Returns: the amount of water left in the tank at the end of the fourth hour.
    """
    # L1
    loss_rate_per_hour = 2 # loses 2 gallons of water per hour
    total_hours = 4 # at the end of the fourth hour
    total_loss = loss_rate_per_hour * total_hours

    # L2
    added_hour_3 = 1 # adds 1 gallon of water to the tank in hour three
    added_hour_4 = 3 # adds three gallons of water to the tank in the fourth hour
    total_added = added_hour_3 + added_hour_4

    # L3
    initial_water = 40 # tank starts with 40 gallons of water
    water_left = initial_water - total_loss + total_added

    # FA
    answer = water_left
    return answer