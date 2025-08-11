def solve():
    """Index: 4230.
    Returns: the number of 4-ounce glasses that can be filled with the remaining water.
    """
    # L1
    num_eight_ounce_glasses = 4 # four 8 ounce glasses
    capacity_eight_ounce_glass = 8 # 8-ounce glasses
    ounces_used_eight_ounce_glasses = num_eight_ounce_glasses * capacity_eight_ounce_glass

    # L2
    num_five_ounce_glasses = 6 # six 5 ounce glasses
    capacity_five_ounce_glass = 5 # 5-ounce glasses
    ounces_used_five_ounce_glasses = num_five_ounce_glasses * capacity_five_ounce_glass

    # L3
    total_ounces_used = ounces_used_eight_ounce_glasses + ounces_used_five_ounce_glasses

    # L4
    initial_water_ounces = 122 # 122 ounces of water
    ounces_remaining = initial_water_ounces - total_ounces_used

    # L5
    capacity_four_ounce_glass = 4 # 4-ounce glasses
    num_four_ounce_glasses = ounces_remaining / capacity_four_ounce_glass

    # FA
    answer = num_four_ounce_glasses
    return answer