def solve():
    """Index: 1300.
    Returns: the total time Martin wastes.
    """
    # L1
    traffic_wait_hours = 2 # 2 hours waiting in traffic
    multiplier_freeway = 4 # four times that long
    freeway_exit_time = traffic_wait_hours * multiplier_freeway

    # L2
    total_waste_time = freeway_exit_time + traffic_wait_hours

    # FA
    answer = total_waste_time
    return answer