def solve(
    file_size_mb: int = 90,  # The file, 90 megabytes in size
    first_rate_mb_per_sec: int = 5,  # downloads at the rate of 5 megabytes per second for its first 60 megabytes
    first_part_mb: int = 60,  # first 60 megabytes
    second_rate_mb_per_sec: int = 10  # then 10 megabytes per second thereafter
):
    """Index: 47.
    Returns: the total time in seconds to download the entire file.
    """

    #: L1
    time_first_part = first_part_mb / first_rate_mb_per_sec

    #: L2
    remaining_mb = first_rate_mb_per_sec - first_part_mb

    #: L3
    time_remaining = remaining_mb / second_rate_mb_per_sec

    #: L4
    total_time = time_first_part + time_remaining

    #: FA
    answer = total_time
    return answer