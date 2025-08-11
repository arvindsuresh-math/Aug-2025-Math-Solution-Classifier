def solve():
    """Index: 2513.
    Returns: the total number of chefs and waiters left.
    """
    # L1
    initial_chefs = 16 # 16 chefs
    chefs_drop_out = 6 # 6 chefs drop out
    chefs_left = initial_chefs - chefs_drop_out

    # L2
    initial_waiters = 16 # 16 waiters
    waiters_drop_out = 3 # 3 waiters drop out
    waiters_left = initial_waiters - waiters_drop_out

    # L3
    total_left = chefs_left + waiters_left

    # FA
    answer = total_left
    return answer