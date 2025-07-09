def solve(
        total_file_size: int = 90, # The file, 90 megabytes in size
        download_rate_first_part: int = 5, # downloads at the rate of 5 megabytes per second
        size_first_part: int = 60, # for its first 60 megabytes
        download_rate_second_part: int = 10 # and then 10 megabytes per second thereafter
    ):
    """Index: 47.
    Returns: the total time in seconds it takes to download the file entirely.
    """
    #: L1
    time_first_part = size_first_part / download_rate_first_part

    #: L2
    remaining_megabytes = total_file_size - size_first_part

    #: L3
    time_second_part = remaining_megabytes / download_rate_second_part

    #: L4
    total_download_time = time_first_part + time_second_part

    answer = total_download_time # FINAL ANSWER
    return answer