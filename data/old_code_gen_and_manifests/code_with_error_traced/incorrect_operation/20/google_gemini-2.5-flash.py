def solve(
        snowflake_stamps: int = 11, # Bella bought 11 snowflake stamps
        more_truck_than_snowflake: int = 9, # She bought 9 more truck stamps than snowflake stamps
        fewer_rose_than_truck: int = 13 # and 13 fewer rose stamps than truck stamps
    ):
    """Index: 20.
    Returns: the total number of stamps Bella bought.
    """

    #: L1
    truck_stamps = snowflake_stamps - more_truck_than_snowflake # eval: 2 = 11 - 9

    #: L2
    rose_stamps = truck_stamps - fewer_rose_than_truck # eval: -11 = 2 - 13

    #: L3
    total_stamps = snowflake_stamps + truck_stamps + rose_stamps # eval: 2 = 11 + 2 + -11

    #: FA
    answer = total_stamps
    return answer # eval: return 2
