def solve():
    """Index: 2423.
    Returns: the total amount of water in the tank at the end of the heavy rain.
    """
    # L1
    rate_L_per_min = 2 # rate of 2 L/min
    duration_minutes = 90 # for 90 minutes
    collected_water = rate_L_per_min * duration_minutes

    # L2
    initial_water = 100 # 100 L of rainwater
    total_water = initial_water + collected_water

    # FA
    answer = total_water
    return answer