def solve():
    """Index: 7099.
    Returns: the total number of skips Matt got.
    """
    # L1
    jump_duration_minutes = 10 # 10 minutes
    seconds_per_minute = 60 # WK
    total_seconds = jump_duration_minutes * seconds_per_minute

    # L2
    skips_per_second = 3 # 3 times per second
    total_skips = total_seconds * skips_per_second

    # FA
    answer = total_skips
    return answer