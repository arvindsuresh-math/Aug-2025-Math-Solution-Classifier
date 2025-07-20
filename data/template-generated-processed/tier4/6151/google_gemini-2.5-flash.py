def solve():
    """Index: 6151.
    Returns: the time in minutes Justin can run home.
    """
    # L1
    total_blocks_to_home = 8 # 8 blocks from home
    blocks_per_run_segment = 2 # 2 blocks in 1.5 minutes
    num_segments = total_blocks_to_home / blocks_per_run_segment

    # L2
    minutes_per_run_segment = 1.5 # 1.5 minutes
    total_minutes_to_home = num_segments * minutes_per_run_segment

    # FA
    answer = total_minutes_to_home
    return answer