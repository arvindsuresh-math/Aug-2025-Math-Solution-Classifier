def solve():
    """Index: 3518.
    Returns: the total number of hours it will take Martha to paint the kitchen.
    """
    # L1
    wall_length_1 = 12 # 12 foot
    wall_height = 10 # 10 foot high ceilings
    area_wall_1 = wall_length_1 * wall_height

    # L2
    num_walls_1 = 2 # two walls that are 12' X 10'
    total_area_walls_1 = area_wall_1 * num_walls_1

    # L3
    wall_length_2 = 16 # 16 foot
    area_wall_2 = wall_length_2 * wall_height

    # L4
    num_walls_2 = 2 # two walls that are 16' by 10'
    total_area_walls_2 = area_wall_2 * num_walls_2

    # L5
    total_square_footage_walls = total_area_walls_1 + total_area_walls_2

    # L6
    num_coats = 3 # one coat of primer and two coats of paint
    total_square_footage_to_paint = total_square_footage_walls * num_coats

    # L7
    painting_rate = 40 # paint 40 square feet per hour
    total_hours = total_square_footage_to_paint / painting_rate

    # FA
    answer = total_hours
    return answer