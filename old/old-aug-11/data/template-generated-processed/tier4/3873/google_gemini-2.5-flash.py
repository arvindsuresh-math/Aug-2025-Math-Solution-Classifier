def solve():
    """Index: 3873.
    Returns: the speed of the runner with the higher average speed.
    """
    # L1
    tiffany_blocks = 6 # 6 blocks
    tiffany_minutes = 3 # 3 minutes
    tiffany_speed = tiffany_blocks / tiffany_minutes

    # L2
    moses_blocks = 12 # 12 blocks
    moses_minutes = 8 # 8 minutes
    moses_speed = moses_blocks / moses_minutes

    # L3
    highest_speed = tiffany_speed # 2 > 1.5

    # FA
    answer = highest_speed
    return answer