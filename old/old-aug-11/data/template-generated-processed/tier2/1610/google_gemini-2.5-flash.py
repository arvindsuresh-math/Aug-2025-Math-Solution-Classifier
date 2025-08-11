def solve():
    """Index: 1610.
    Returns: the total liters of water Micah drank.
    """
    # L1
    morning_water_liters = 1.5 # drank 1.5 liters of water in the morning
    afternoon_multiplier = 3 # three times that much water
    afternoon_water_liters = morning_water_liters * afternoon_multiplier

    # L2
    total_water_liters = morning_water_liters + afternoon_water_liters

    # FA
    answer = total_water_liters
    return answer