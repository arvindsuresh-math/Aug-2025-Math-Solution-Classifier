def solve():
    """Index: 20.
    Returns: the total number of stamps Bella bought.
    """
    # L1
    snowflake_stamps = 11 # 11 snowflake stamps
    more_truck_than_snowflake = 9 # 9 more truck stamps than snowflake stamps
    truck_stamps = snowflake_stamps + more_truck_than_snowflake

    # L2
    fewer_rose_than_truck = 13 # 13 fewer rose stamps than truck stamps
    rose_stamps = truck_stamps - fewer_rose_than_truck

    # L3
    total_stamps = snowflake_stamps + truck_stamps + rose_stamps

    # FA
    answer = total_stamps
    return answer