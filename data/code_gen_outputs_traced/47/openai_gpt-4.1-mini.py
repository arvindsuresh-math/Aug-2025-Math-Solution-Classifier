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
    time_first_part = first_part_mb / first_rate_mb_per_sec # eval: 12.0 = 60 / 5
    #: L2
    remaining_mb = file_size_mb - first_part_mb # eval: 30 = 90 - 60
    #: L3
    time_remaining = remaining_mb / second_rate_mb_per_sec # eval: 3.0 = 30 / 10
    #: L4
    total_time = time_first_part + time_remaining # eval: 15.0 = 12.0 + 3.0
    answer = total_time  # FINAL ANSWER # eval: 15.0 = 15.0  # FINAL ANSWER
    return answer # eval: return 15.0