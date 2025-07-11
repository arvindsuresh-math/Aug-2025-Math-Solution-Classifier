def solve():
    """Index: 2423.
    Returns: the total amount of water in the tank at the end of the heavy rain.
    """
    # L1
    inflow_rate = 2 # water flows into the tank at a rate of 2 L/min
    rain_duration = 90 # for 90 minutes
    rainwater_collected = inflow_rate * rain_duration

    # L2
    initial_water = 100 # He has 100 L of rainwater in his tank
    total_water = initial_water + rainwater_collected

    # FA
    answer = total_water
    return answer