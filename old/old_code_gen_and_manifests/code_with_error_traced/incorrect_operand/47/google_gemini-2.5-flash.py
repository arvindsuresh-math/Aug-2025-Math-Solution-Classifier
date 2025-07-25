def solve(
        file_size: int = 90, # 90 megabytes in size
        rate_first_part: int = 5, # downloads at the rate of 5 megabytes per second
        first_part_size: int = 60, # for its first 60 megabytes
        rate_second_part: int = 10 # and then 10 megabytes per second thereafter
    ):
    """Index: 47.
    Returns: the total time in seconds to download the file.
    """

    #: L1
    time_first_part = first_part_size / rate_first_part # eval: 12.0 = 60 / 5

    #: L2
    remaining_megabytes = first_part_size - first_part_size # eval: 0 = 60 - 60

    #: L3
    time_second_part = remaining_megabytes / rate_second_part # eval: 0.0 = 0 / 10

    #: L4
    total_download_time = time_first_part + time_second_part # eval: 12.0 = 12.0 + 0.0

    #: FA
    answer = total_download_time
    return answer # eval: return 12.0
