def solve():
    """Index: 6558.
    Returns: the time it would take to go to the bathroom 6 times.
    """
    # L1
    total_time_8_times = 20 # 20 minutes for John to go to the bathroom 8 times
    num_times_initial = 8 # 8 times
    time_per_visit = total_time_8_times / num_times_initial

    # L2
    num_times_target = 6 # to go 6 times
    total_time_6_times = time_per_visit * num_times_target

    # FA
    answer = total_time_6_times
    return answer