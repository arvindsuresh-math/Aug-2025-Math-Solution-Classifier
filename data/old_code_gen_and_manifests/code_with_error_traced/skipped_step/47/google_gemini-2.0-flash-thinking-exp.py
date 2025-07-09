def solve(
    total_size_mb: int = 90, # 90 megabytes in size
    rate_first_part_mbps: int = 5, # downloads at the rate of 5 megabytes per second
    size_first_part_mb: int = 60, # for its first 60 megabytes
    rate_second_part_mbps: int = 10 # and then 10 megabytes per second thereafter
):
    """Index: 47.
    Returns: the total time in seconds to download the file.
    """

    #: L1

    #: L2
    remaining_size_mb = total_size_mb - size_first_part_mb # eval: 30 = 90 - 60

    #: L3
    time_second_part = remaining_size_mb / rate_second_part_mbps # eval: 3.0 = 30 / 10

    #: L4
    total_time = total_size_mb + time_second_part # eval: 93.0 = 90 + 3.0

    #: FA
    answer = total_time
    return answer # eval: return 93.0
