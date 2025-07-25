def solve():
    """Index: 6819.
    Returns: the total number of hours Vicky has to wait.
    """
    # L1
    program_size_gb = 360 # The program’s size is 360GB
    mb_per_gb = 1000 # There are 1000 MB per GB
    program_size_mb = program_size_gb * mb_per_gb

    # L2
    download_speed_mbps = 50 # 50 MB/second
    total_seconds_downloading = program_size_mb / download_speed_mbps

    # L3
    seconds_per_hour = 3600 # WK
    total_hours_waiting = total_seconds_downloading / seconds_per_hour

    # FA
    answer = total_hours_waiting
    return answer