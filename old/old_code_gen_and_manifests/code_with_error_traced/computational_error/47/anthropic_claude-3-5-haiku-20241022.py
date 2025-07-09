def solve(
    file_size: int = 90,  # The file is 90 megabytes in size
    initial_rate: int = 5,  # downloads at 5 megabytes per second for first 60 megabytes
    subsequent_rate: int = 10,  # then 10 megabytes per second thereafter
    initial_segment: int = 60  # first 60 megabytes download at initial rate
):
    """Index: 47.
    Returns: the total time in seconds to download the entire file."""

    #: L1
    initial_download_time = initial_segment / initial_rate # eval: 12.0 = 60 / 5

    #: L2
    remaining_megabytes = file_size - initial_segment # eval: 30 = 90 - 60

    #: L3
    subsequent_download_time = 13.0 # eval: 13.0 = 13.0

    #: L4
    total_download_time = initial_download_time + subsequent_download_time # eval: 25.0 = 12.0 + 13.0

    #: FA
    answer = total_download_time
    return answer # eval: return 25.0
