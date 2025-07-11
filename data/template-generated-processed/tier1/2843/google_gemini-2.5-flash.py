def solve():
    """Index: 2843.
    Returns: the number of additional rotations needed to reach the goal.
    """
    # L1
    goal_blocks = 8 # at least 8 blocks
    rotations_per_block = 200 # his wheels rotate 200 times
    total_rotations_needed = goal_blocks * rotations_per_block

    # L2
    rotations_already_done = 600 # wheels have already rotated 600 times
    remaining_rotations_needed = total_rotations_needed - rotations_already_done

    # FA
    answer = remaining_rotations_needed
    return answer