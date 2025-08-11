def solve():
    """Index: 7212.
    Returns: the height Ravi can jump in inches.
    """
    # L1
    jump1 = 23 # 23 inches
    jump2 = 27 # 27 inches
    jump3 = 28 # 28 inches
    total_height_three_jumpers = jump1 + jump2 + jump3

    # L2
    num_jumpers = 3 # three next highest jumpers
    average_height_three_jumpers = total_height_three_jumpers / num_jumpers

    # L3
    ravi_jump_factor = 1.5 # 1.5 times higher
    ravi_jump_height = average_height_three_jumpers * ravi_jump_factor

    # FA
    answer = ravi_jump_height
    return answer