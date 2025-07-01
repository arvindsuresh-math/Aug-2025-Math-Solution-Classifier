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
    time_first_part = size_first_part_mb / rate_first_part_mbps # eval: 12.0 = 60 / 5

    #: L2
    remaining_size_mb = total_size_mb + size_first_part_mb # eval: 150 = 90 + 60

    #: L3
    time_second_part = remaining_size_mb / rate_second_part_mbps # eval: 15.0 = 150 / 10

    #: L4
    total_time = time_first_part + time_second_part # eval: 27.0 = 12.0 + 15.0

    #: FA
    answer = total_time
    return answer # eval: return 27.0
