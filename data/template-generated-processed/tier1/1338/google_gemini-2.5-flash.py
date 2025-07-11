def solve():
    """Index: 1338.
    Returns: the total number of bulbs needed for the house.
    """
    # L1
    medium_lights = 12 # 12 medium ceiling lights
    multiplier_large_lights = 2 # twice as many large ceiling lights as medium ceiling lights
    num_large_lights = multiplier_large_lights * medium_lights

    # L2
    small_lights_more_than_medium = 10 # ten more small lights than medium ones
    num_small_lights = small_lights_more_than_medium + medium_lights

    # L3
    bulbs_per_small_light = 1 # The small ones require 1 bulb
    bulbs_for_small_lights = bulbs_per_small_light * num_small_lights

    # L4
    bulbs_per_medium_light = 2 # the medium ones require 2
    bulbs_for_medium_lights = bulbs_per_medium_light * medium_lights

    # L5
    bulbs_per_large_light = 3 # the large ones need 3 bulbs
    bulbs_for_large_lights = bulbs_per_large_light * num_large_lights

    # L6
    total_bulbs = bulbs_for_small_lights + bulbs_for_medium_lights + bulbs_for_large_lights

    # FA
    answer = total_bulbs
    return answer