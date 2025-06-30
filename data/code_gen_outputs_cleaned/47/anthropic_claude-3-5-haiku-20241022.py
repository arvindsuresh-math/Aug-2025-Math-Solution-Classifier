def solve(
    file_size: int = 90,  # The file is 90 megabytes in size
    initial_rate: int = 5,  # downloads at 5 megabytes per second for first 60 megabytes
    subsequent_rate: int = 10,  # then 10 megabytes per second thereafter
    initial_segment: int = 60  # first 60 megabytes download at initial rate
):
    """Index: 47.
    Returns: the total time in seconds to download the entire file."""
    
    #: L1
    initial_download_time = initial_segment / initial_rate

    #: L2
    remaining_megabytes = file_size - initial_segment

    #: L3
    subsequent_download_time = remaining_megabytes / subsequent_rate

    #: L4
    total_download_time = initial_download_time + subsequent_download_time

    answer = total_download_time  # FINAL ANSWER
    return answer