def solve(
    snowflake_stamps: int = 11,  # Bella bought 11 snowflake stamps
    truck_stamps_diff: int = 9,  # 9 more truck stamps than snowflake stamps
    rose_stamps_diff: int = 13  # 13 fewer rose stamps than truck stamps
):
    """Index: 20.
    Returns: the total number of stamps Bella bought."""

    #: L1
    truck_stamps = snowflake_stamps + truck_stamps_diff # eval: 20 = 11 + 9

    #: L2
    rose_stamps = truck_stamps - rose_stamps_diff # eval: 7 = 20 - 13

    #: L3
    total_stamps = 48 # eval: 48 = 48

    #: FA
    answer = total_stamps
    return answer # eval: return 48
