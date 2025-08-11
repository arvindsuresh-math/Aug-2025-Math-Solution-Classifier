def solve():
    """Index: 2445.
    Returns: how many fewer eyes the lizard has than the combined number of spots and wrinkles.
    """
    # L1
    num_eyes = 3 # three-eyed lizard
    wrinkles_per_eye = 3 # 3 times more wrinkles than eyes
    num_wrinkles = wrinkles_per_eye * num_eyes

    # L2
    spots_per_wrinkle = 7 # seven times more spots than wrinkles
    num_spots = spots_per_wrinkle * num_wrinkles

    # L3
    combined_spots_wrinkles = num_spots + num_wrinkles

    # L4
    fewer_eyes_than_combined = combined_spots_wrinkles - num_eyes

    # FA
    answer = fewer_eyes_than_combined
    return answer