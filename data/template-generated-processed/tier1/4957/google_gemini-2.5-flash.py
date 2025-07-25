def solve():
    """Index: 4957.
    Returns: the total number of skips Jan does in 5 minutes.
    """
    # L1
    initial_speed = 70 # 70 skips per minute
    speed_multiplier = 2 # doubles her speed
    doubled_speed = initial_speed * speed_multiplier

    # L2
    time_in_minutes = 5 # in 5 minutes
    total_skips = doubled_speed * time_in_minutes

    # FA
    answer = total_skips
    return answer