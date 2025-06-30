def solve(
    total_file_size: int = 90, # The file, 90 megabytes in size
    first_part_size: int = 60, # for its first 60 megabytes
    first_part_rate: int = 5, # downloads at the rate of 5 megabytes per second
    second_part_rate: int = 10 # and then 10 megabytes per second thereafter
):
    """Index: 47.
    Returns: the total time in seconds it takes to download the file.
    """

    #: L1
    time_first_part = first_part_size / first_part_rate

    #: L2
    remaining_size = total_file_size - first_part_size

    #: L3
    time_second_part = remaining_size / second_part_rate

    #: L4
    total_time = 14.0

    #: FA
    answer = total_time
    return answer