def solve():
    """Index: 346.
    Returns: the number of paint cans Lucille needs.
    """
    # L1
    wall_1_width = 3 # Two of her walls are 3 meters wide
    wall_height = 2 # 2 meters tall
    area_wall_1 = wall_1_width * wall_height

    # L2
    num_wall_1 = 2 # Two of her walls
    total_area_wall_1_set = area_wall_1 * num_wall_1

    # L3
    wall_3_width = 5 # The third wall is 5 meters wide
    area_wall_3 = wall_3_width * wall_height

    # L4
    wall_4_width = 4 # The final wall is 4 meters wide
    area_wall_4 = wall_4_width * wall_height

    # L5
    total_area_to_cover = total_area_wall_1_set + area_wall_3 + area_wall_4

    # L6
    coverage_per_can = 2 # each can of paint covers 2 square meters
    cans_needed = total_area_to_cover / coverage_per_can

    # FA
    answer = cans_needed
    return answer