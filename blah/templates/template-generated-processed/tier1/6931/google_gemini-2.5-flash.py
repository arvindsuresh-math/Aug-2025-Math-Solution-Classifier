def solve():
    """Index: 6931.
    Returns: the total time it takes Max to both mow and fertilize the lawn.
    """
    # L1
    mow_time = 40 # 40 minutes
    fertilize_multiplier = 2 # twice that long
    fertilize_time = fertilize_multiplier * mow_time

    # L2
    total_time = fertilize_time + mow_time

    # FA
    answer = total_time
    return answer