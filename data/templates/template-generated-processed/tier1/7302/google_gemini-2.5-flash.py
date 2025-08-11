def solve():
    """Index: 7302.
    Returns: the total area of wall space that Linda will have to paint.
    """
    # L1
    wall_height = 8 # 8 feet tall
    wall_width = 20 # 20 feet wide
    solid_wall_area = wall_height * wall_width

    # L2
    doorway_width = 3 # 3-foot by 7-foot doorway
    doorway_height = 7 # 3-foot by 7-foot doorway
    doorway_area = doorway_width * doorway_height

    # L3
    window_width = 6 # 6-foot by 4-foot window
    window_height = 4 # 6-foot by 4-foot window
    window_area = window_width * window_height

    # L4
    closet_door_width = 5 # 5-foot by 7-foot doorway
    closet_door_height = 7 # 5-foot by 7-foot doorway
    closet_door_area = closet_door_width * closet_door_height

    # L5
    total_obstacles_area = doorway_area + window_area + closet_door_area

    # L6
    num_walls = 4 # 4 walls
    total_gross_wall_area = num_walls * solid_wall_area

    # L7
    paintable_area = total_gross_wall_area - total_obstacles_area

    # FA
    answer = paintable_area
    return answer