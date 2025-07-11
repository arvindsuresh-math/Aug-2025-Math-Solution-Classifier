def solve():
    """Index: 2843.
    Returns: the number of additional wheel rotations Greg needs to reach his goal.
    """
    # L1
    goal_blocks = 8 # ride at least 8 blocks
    rotations_per_block = 200 # each block he rides, his wheels rotate 200 times
    total_rotations_needed = goal_blocks * rotations_per_block

    # L2
    already_rotated = 600 # wheels have already rotated 600 times
    rotations_remaining = total_rotations_needed - already_rotated

    # FA
    answer = rotations_remaining
    return answer