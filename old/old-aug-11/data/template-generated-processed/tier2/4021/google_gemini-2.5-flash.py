def solve():
    """Index: 4021.
    Returns: the total time the trip takes.
    """
    # L1
    drive_time_each_way = 2 # 2-hour drive each way
    num_ways = 2 # each way
    total_driving_time = drive_time_each_way * num_ways

    # L2
    beach_time_multiplier = 2.5 # 2.5 times at long at the beach
    beach_time = total_driving_time * beach_time_multiplier

    # L3
    total_trip_time = beach_time + total_driving_time

    # FA
    answer = total_trip_time
    return answer