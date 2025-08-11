def solve():
    """Index: 1338.
    Returns: the total number of bulbs needed for all ceiling lights in the house.
    """
    # L1
    num_medium = 12 # 12 medium ceiling lights
    large_to_medium_ratio = 2 # twice as many large ceiling lights as medium
    num_large = large_to_medium_ratio * num_medium

    # L2
    small_more_than_medium = 10 # ten more small lights than medium ones
    num_small = small_more_than_medium + num_medium

    # L3
    bulbs_per_small = 1 # small ones require 1 bulb
    bulbs_small = bulbs_per_small * num_small

    # L4
    bulbs_per_medium = 2 # medium ones require 2 bulbs
    bulbs_medium = bulbs_per_medium * num_medium

    # L5
    bulbs_per_large = 3 # large ones need 3 bulbs
    bulbs_large = bulbs_per_large * num_large

    # L6
    total_bulbs = bulbs_small + bulbs_medium + bulbs_large

    # FA
    answer = total_bulbs
    return answer