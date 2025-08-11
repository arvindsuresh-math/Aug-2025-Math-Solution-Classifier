def solve():
    """Index: 3192.
    Returns: the total number of levels in the tower.
    """
    # L1
    total_blocks = 96 # 96 blocks of stone
    blocks_per_step = 3 # three massive blocks of stone
    total_steps = total_blocks / blocks_per_step

    # L2
    steps_per_level = 8 # Each level has eight huge steps
    total_levels = total_steps / steps_per_level

    # FA
    answer = total_levels
    return answer