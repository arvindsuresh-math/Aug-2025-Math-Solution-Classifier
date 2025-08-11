def solve():
    """Index: 4373.
    Returns: the number of cents Lucille has left.
    """
    # L1
    grass_weeds = 32 # thirty-two in the grass around the fruit trees
    half_divisor = 2 # half the grass
    weeds_pulled_from_grass = grass_weeds / half_divisor

    # L2
    flower_bed_weeds = 11 # eleven weeds in the flower bed
    vegetable_patch_weeds = 14 # fourteen in the vegetable patch
    total_weeds_pulled = flower_bed_weeds + vegetable_patch_weeds + weeds_pulled_from_grass

    # L3
    cents_per_weed = 6 # six cents for every weed
    total_earnings = total_weeds_pulled * cents_per_weed

    # L4
    soda_cost = 99 # bought a soda for 99 cents
    cents_left = total_earnings - soda_cost

    # FA
    answer = cents_left
    return answer