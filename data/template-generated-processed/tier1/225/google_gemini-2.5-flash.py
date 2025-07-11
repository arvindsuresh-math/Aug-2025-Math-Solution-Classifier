def solve():
    """Index: 225.
    Returns: the total number of gallons of water needed.
    """
    # L1
    gallons_heavy_wash = 20 # 20 gallons of water for a heavy wash
    num_heavy_washes = 2 # two heavy washes
    water_heavy_washes = gallons_heavy_wash * num_heavy_washes

    # L2
    gallons_regular_wash = 10 # 10 gallons of water for a regular wash
    num_regular_washes = 3 # three regular washes
    water_regular_washes = gallons_regular_wash * num_regular_washes

    # L3
    gallons_light_wash = 2 # 2 gallons of water for a light wash
    num_light_washes = 1 # one light wash
    water_light_washes = gallons_light_wash * num_light_washes

    # L4
    num_bleached_loads = 2 # Two of the loads need to be bleached
    water_bleached_loads = gallons_light_wash * num_bleached_loads

    # L5
    total_water_needed = water_heavy_washes + water_regular_washes + water_light_washes + water_bleached_loads

    # FA
    answer = total_water_needed
    return answer