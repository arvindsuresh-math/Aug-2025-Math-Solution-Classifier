def solve():
    """Index: 47.
    Returns: the total time in seconds to download the file entirely.
    """
    # L1
    first_part_size = 60 # first 60 megabytes
    download_rate_first_part = 5 # 5 megabytes per second for its first 60 megabytes
    time_first_part = first_part_size / download_rate_first_part

    # L2
    total_file_size = 90 # 90 megabytes in size
    remaining_megabytes = total_file_size - first_part_size

    # L3
    download_rate_remaining_part = 10 # 10 megabytes per second thereafter
    time_remaining_part = remaining_megabytes / download_rate_remaining_part

    # L4
    total_time = time_first_part + time_remaining_part

    # FA
    answer = total_time
    return answer