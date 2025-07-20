def solve():
    """Index: 4454.
    Returns: the total square feet of glass needed.
    """
    # L1
    long_wall_length = 30 # 30 feet by 12 feet
    wall_height = 12 # 30 feet by 12 feet and 20 feet by 12 feet
    area_one_long_wall = long_wall_length * wall_height

    # L2
    num_long_walls = 2 # two of those walls
    total_area_long_walls = area_one_long_wall * num_long_walls

    # L3
    short_wall_length = 20 # 20 feet by 12 feet
    area_short_wall = short_wall_length * wall_height

    # L4
    total_glass_needed = total_area_long_walls + area_short_wall

    # FA
    answer = total_glass_needed
    return answer