def solve():
    """Index: 4977.
    Returns: the number of days it takes the sprinkler system to use the specified amount of water.
    """
    # L1
    morning_water = 4 # four liters of water in the morning
    evening_water = 6 # six liters in the evening
    daily_water_usage = morning_water + evening_water

    # L2
    total_water_needed = 50 # use 50 liters of water
    days_to_use_water = total_water_needed / daily_water_usage

    # FA
    answer = days_to_use_water
    return answer