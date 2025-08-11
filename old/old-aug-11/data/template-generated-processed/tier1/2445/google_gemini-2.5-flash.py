def solve():
    """Index: 2445.
    Returns: the number of fewer eyes the lizard has than the combined number of spots and wrinkles.
    """
    # L1
    wrinkles_multiplier = 3 # 3 times more wrinkles than eyes
    lizard_eyes = 3 # three-eyed lizard
    num_wrinkles = wrinkles_multiplier * lizard_eyes

    # L2
    spots_multiplier = 7 # seven times more spots than wrinkles
    num_spots = spots_multiplier * num_wrinkles

    # L3
    combined_spots_wrinkles = num_spots + num_wrinkles

    # L4
    fewer_eyes = combined_spots_wrinkles - lizard_eyes

    # FA
    answer = fewer_eyes
    return answer