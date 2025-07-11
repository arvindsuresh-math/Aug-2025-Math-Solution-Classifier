def solve():
    """Index: 1982.
    Returns: the total meters of masking tape Elijah needs to order.
    """
    # L1
    num_walls_6m = 2 # 2 of his walls are 6 meters wide
    width_6m = 6 # 6 meters wide
    tape_for_6m_walls = num_walls_6m * width_6m

    # L2
    num_walls_4m = 2 # other 2 walls are 4 meters wide
    width_4m = 4 # 4 meters wide
    tape_for_4m_walls = num_walls_4m * width_4m

    # L3
    total_tape = tape_for_6m_walls + tape_for_4m_walls

    # FA
    answer = total_tape
    return answer