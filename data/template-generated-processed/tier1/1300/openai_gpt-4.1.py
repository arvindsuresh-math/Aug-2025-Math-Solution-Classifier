def solve():
    """Index: 1300.
    Returns: the total time Martin wastes in hours.
    """
    # L1
    waiting_in_traffic_hours = 2 # spends 2 hours waiting in traffic
    times_longer = 4 # four times that long
    get_off_freeway_hours = waiting_in_traffic_hours * times_longer

    # L2
    total_time_wasted = get_off_freeway_hours + waiting_in_traffic_hours

    # FA
    answer = total_time_wasted
    return answer