def solve():
    """Index: 674.
    Returns: the total number of full parking spots.
    """
    # L1
    num_stories = 4 # 4 stories tall
    spots_per_level = 100 # 100 spots per level
    total_possible_spots = num_stories * spots_per_level

    # L2
    first_level_open_spots = 58 # 58 open parking spots on the first level
    more_on_second_level = 2 # 2 more open parking spots on the second level
    second_level_open_spots = first_level_open_spots + more_on_second_level

    # L3
    more_on_third_level = 5 # 5 more open parking spots on the third level
    third_level_open_spots = second_level_open_spots + more_on_third_level

    # L4
    fourth_level_open_spots = 31 # 31 open parking spots on the fourth level
    total_open_spots = first_level_open_spots + second_level_open_spots + third_level_open_spots + fourth_level_open_spots

    # L5
    total_full_spots = total_possible_spots - total_open_spots

    # FA
    answer = total_full_spots
    return answer