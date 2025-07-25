def solve(
    snowflake_stamps: int = 11,  # Bella bought 11 snowflake stamps
    truck_stamps_diff: int = 9,  # 9 more truck stamps than snowflake stamps
    rose_stamps_diff: int = 13  # 13 fewer rose stamps than truck stamps
):
    """Index: 20.
    Returns: the total number of stamps Bella bought."""

    #: L1

    #: L2
    rose_stamps = truck_stamps_diff - rose_stamps_diff

    #: L3
    total_stamps = snowflake_stamps + truck_stamps_diff + rose_stamps

    #: FA
    answer = total_stamps
    return answer