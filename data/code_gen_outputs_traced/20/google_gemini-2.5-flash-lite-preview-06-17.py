def solve(
    num_snowflake_stamps: int = 11, # Bella bought 11 snowflake stamps
    more_truck_than_snowflake: int = 9, # She bought 9 more truck stamps than snowflake stamps
    fewer_rose_than_truck: int = 13 # and 13 fewer rose stamps than truck stamps
):
    """Index: 20.
    Returns: the total number of stamps Bella bought.
    """
    #: L1
    num_truck_stamps = num_snowflake_stamps + more_truck_than_snowflake # eval: 20 = 11 + 9
    #: L2
    num_rose_stamps = num_truck_stamps - fewer_rose_than_truck # eval: 7 = 20 - 13
    #: L3
    total_stamps = num_snowflake_stamps + num_truck_stamps + num_rose_stamps # eval: 38 = 11 + 20 + 7
    answer = total_stamps # FINAL ANSWER # eval: 38 = 38 # FINAL ANSWER
    return answer # eval: return 38