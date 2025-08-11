def solve():
    """Index: 674.
    Returns: the total number of full parking spots in all levels.
    """
    # L1
    num_levels = 4 # 4 stories tall
    spots_per_level = 100 # 100 spots per level
    total_spots = num_levels * spots_per_level

    # L2
    open_first = 58 # 58 open parking spots on the first level
    open_second_more = 2 # 2 more open parking spots on the second level than on the first level
    open_second = open_first + open_second_more

    # L3
    open_third_more = 5 # 5 more open parking spots on the third level than on the second level
    open_third = open_second + open_third_more

    # L4
    open_fourth = 31 # 31 open parking spots on the fourth level
    total_open = open_first + open_second + open_third + open_fourth

    # L5
    full_spots = total_spots - total_open

    # FA
    answer = full_spots
    return answer