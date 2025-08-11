def solve():
    """Index: 6704.
    Returns: the horizontal distance moved in feet.
    """
    # L1
    final_elevation = 1450 # His elevation increases to 1450 feet
    initial_elevation = 100 # His elevation increases from 100 feet
    vertical_distance_climbed = final_elevation - initial_elevation

    # L2
    horizontal_ratio_multiplier = 2 # for every two feet horizontally
    horizontal_distance_moved = vertical_distance_climbed * horizontal_ratio_multiplier

    # FA
    answer = horizontal_distance_moved
    return answer