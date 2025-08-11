def solve():
    """Index: 20.
    Returns: the total number of stamps Bella bought in all.
    """
    # L1
    snowflake_stamps = 11 # Bella bought 11 snowflake stamps
    truck_more_than_snowflake = 9 # 9 more truck stamps than snowflake stamps
    truck_stamps = snowflake_stamps + truck_more_than_snowflake

    # L2
    rose_fewer_than_truck = 13 # 13 fewer rose stamps than truck stamps
    rose_stamps = truck_stamps - rose_fewer_than_truck

    # L3
    total_stamps = snowflake_stamps + truck_stamps + rose_stamps

    # FA
    answer = total_stamps
    return answer