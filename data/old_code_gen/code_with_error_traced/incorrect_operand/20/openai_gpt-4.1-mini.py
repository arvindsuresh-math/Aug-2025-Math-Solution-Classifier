def solve(
    snowflake_stamps: int = 11,  # Bella bought 11 snowflake stamps
    truck_more_than_snowflake: int = 9,  # She bought 9 more truck stamps than snowflake stamps
    rose_less_than_truck: int = 13  # and 13 fewer rose stamps than truck stamps
):
    """Index: 20.
    Returns: the total number of stamps Bella bought.
    """

    #: L1
    truck_stamps = snowflake_stamps + snowflake_stamps # eval: 22 = 11 + 11

    #: L2
    rose_stamps = truck_stamps - rose_less_than_truck # eval: 9 = 22 - 13

    #: L3
    total_stamps = snowflake_stamps + truck_stamps + rose_stamps # eval: 42 = 11 + 22 + 9

    #: FA
    answer = total_stamps
    return answer # eval: return 42
