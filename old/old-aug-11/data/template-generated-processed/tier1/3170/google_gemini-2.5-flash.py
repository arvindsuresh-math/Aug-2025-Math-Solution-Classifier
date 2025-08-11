def solve():
    """Index: 3170.
    Returns: the total time the raccoons were stalled by both locks.
    """
    # L1
    first_lock_stall_time = 5 # stalls them for 5 minutes
    multiplier_three_times = 3 # three times as long as the first lock
    less_than_three_times = 3 # 3 minutes less than three times as long
    second_lock_stall_time = first_lock_stall_time * multiplier_three_times - less_than_three_times

    # L2
    multiplier_five_times = 5 # five times as long as the second lock alone
    total_stall_time = second_lock_stall_time * multiplier_five_times

    # FA
    answer = total_stall_time
    return answer