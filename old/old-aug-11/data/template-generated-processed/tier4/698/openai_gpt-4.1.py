def solve():
    """Index: 698.
    Returns: the number of gigabytes still available on the USB drive.
    """
    # L2
    total_gb = 16 # 16 GB capacity USB drive
    busy_percent_num = 50 # 50% is already busy
    percent_divisor = 100 # WK
    busy_fraction = busy_percent_num / percent_divisor
    busy_gb = busy_fraction * total_gb

    # L3
    available_gb = total_gb - busy_gb

    # FA
    answer = available_gb
    return answer