def solve():
    """Index: 2948.
    Returns: the total number of legos needed to build the pyramid.
    """
    # L1
    bottom_level_side_legos = 7 # bottom level has 7 legos per side
    bottom_layer_total_legos = bottom_level_side_legos * bottom_level_side_legos

    # L2
    lego_reduction_per_level = 1 # each level has one less lego per side
    second_level_side_legos = bottom_level_side_legos - lego_reduction_per_level

    # L3
    second_layer_total_legos = second_level_side_legos * second_level_side_legos

    # L4
    top_level_side_legos = second_level_side_legos - lego_reduction_per_level

    # L5
    top_layer_total_legos = top_level_side_legos * top_level_side_legos

    # L6
    total_legos_needed = bottom_layer_total_legos + second_layer_total_legos + top_layer_total_legos

    # FA
    answer = total_legos_needed
    return answer