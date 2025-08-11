def solve():
    """Index: 4325.
    Returns: the time in minutes the second bus ride takes.
    """
    # L1
    wait_time_first_bus = 12 # 12 minutes waiting for her first bus
    ride_time_first_bus = 30 # 30 minutes riding on her first bus
    combined_first_bus_time = wait_time_first_bus + ride_time_first_bus

    # L2
    divisor_for_second_bus_time = 2 # half the combined wait and trip time
    second_bus_ride_time = combined_first_bus_time / divisor_for_second_bus_time

    # FA
    answer = second_bus_ride_time
    return answer