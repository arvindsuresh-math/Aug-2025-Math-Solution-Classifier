def solve():
    """Index: 1982.
    Returns: the total meters of masking tape Elijah needs to order.
    """
    # L1
    num_walls_type2 = 2 # 2 of his walls
    width_wall_type2 = 6 # 6 meters wide
    tape_for_type2_walls = num_walls_type2 * width_wall_type2

    # L2
    num_walls_type1 = 2 # the other 2 walls
    width_wall_type1 = 4 # 4 meters wide
    tape_for_type1_walls = num_walls_type1 * width_wall_type1

    # L3
    total_tape_needed = tape_for_type2_walls + tape_for_type1_walls

    # FA
    answer = total_tape_needed
    return answer