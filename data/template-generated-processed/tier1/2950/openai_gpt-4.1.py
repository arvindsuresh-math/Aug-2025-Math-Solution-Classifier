def solve():
    """Index: 2950.
    Returns: the total number of open parking spots in all levels.
    """
    # L1
    first_level_spots = 4 # 4 open parking spots on the first level
    second_level_more = 7 # 7 more open parking spots on the second level than on the first level
    second_level_spots = first_level_spots + second_level_more

    # L2
    third_level_more = 6 # 6 more open parking spots on the third level than on the second level
    third_level_spots = second_level_spots + third_level_more

    # L3
    fourth_level_spots = 14 # 14 open parking spots on the fourth level
    total_spots = first_level_spots + second_level_spots + third_level_spots + fourth_level_spots

    # FA
    answer = total_spots
    return answer