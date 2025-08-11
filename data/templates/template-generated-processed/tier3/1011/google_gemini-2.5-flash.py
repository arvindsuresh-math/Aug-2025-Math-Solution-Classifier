def solve():
    """Index: 1011.
    Returns: the number of additional logs the carpenter needs.
    """
    # L1
    initial_logs = 8 # 8 logs
    woodblocks_per_log = 5 # five woodblocks each
    initial_woodblocks = initial_logs * woodblocks_per_log

    # L2
    total_woodblocks_needed = 80 # 80 woodblocks to build it
    remaining_woodblocks_needed = total_woodblocks_needed - initial_woodblocks

    # L3
    logs_still_needed = remaining_woodblocks_needed / woodblocks_per_log

    # FA
    answer = logs_still_needed
    return answer