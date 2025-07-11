def solve():
    """Index: 225.
    Returns: the total number of gallons of water needed for all the washes.
    """
    # L1
    heavy_gallons_per_load = 20 # uses 20 gallons of water for a heavy wash
    num_heavy_washes = 2 # two heavy washes
    heavy_total = heavy_gallons_per_load * num_heavy_washes

    # L2
    regular_gallons_per_load = 10 # 10 gallons of water for a regular wash
    num_regular_washes = 3 # three regular washes
    regular_total = regular_gallons_per_load * num_regular_washes

    # L3
    light_gallons_per_load = 2 # 2 gallons of water for a light wash
    num_light_washes = 1 # one light wash to do
    light_total = light_gallons_per_load * num_light_washes

    # L4
    num_bleached_loads = 2 # Two of the loads need to be bleached
    extra_light_per_bleach = 2 # an extra light wash cycle (2 gallons) per bleached load
    bleach_extra_total = extra_light_per_bleach * num_bleached_loads

    # L5
    total_gallons = heavy_total + regular_total + light_total + bleach_extra_total

    # FA
    answer = total_gallons
    return answer