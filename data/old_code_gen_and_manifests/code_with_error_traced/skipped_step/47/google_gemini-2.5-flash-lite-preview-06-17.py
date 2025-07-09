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

    #: L2
    remaining_size = total_file_size - first_part_size # eval: 30 = 90 - 60

    #: L3
    time_second_part = remaining_size / second_part_rate # eval: 3.0 = 30 / 10

    #: L4
    total_time = second_part_rate + time_second_part # eval: 13.0 = 10 + 3.0

    #: FA
    answer = total_time
    return answer # eval: return 13.0
