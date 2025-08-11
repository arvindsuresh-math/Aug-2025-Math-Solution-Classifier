def solve():
    """Index: 4445.
    Returns: the total square feet of wall Matt needs to paint.
    """
    # L1
    living_room_length = 40 # square 40 feet by 40 feet
    wall_height = 10 # All the walls in Matt's house are 10 feet tall
    living_room_wall_area = living_room_length * wall_height

    # L2
    num_living_room_walls = 3 # three walls in his living room
    total_living_room_area = living_room_wall_area * num_living_room_walls

    # L3
    bedroom_long_side = 12 # rectangle 10 feet by 12 feet
    bedroom_long_wall_area = bedroom_long_side * wall_height

    # L4
    num_long_bedroom_walls = 2 # all four walls in his bedroom, which is a rectangle 10 feet by 12 feet
    total_long_bedroom_area = bedroom_long_wall_area * num_long_bedroom_walls

    # L5
    bedroom_short_side = 10 # rectangle 10 feet by 12 feet
    bedroom_short_wall_area = bedroom_short_side * wall_height

    # L6
    num_short_bedroom_walls = 2 # all four walls in his bedroom, which is a rectangle 10 feet by 12 feet
    total_short_bedroom_area = bedroom_short_wall_area * num_short_bedroom_walls

    # L7
    total_paint_area = total_living_room_area + total_long_bedroom_area + total_short_bedroom_area

    # FA
    answer = total_paint_area
    return answer