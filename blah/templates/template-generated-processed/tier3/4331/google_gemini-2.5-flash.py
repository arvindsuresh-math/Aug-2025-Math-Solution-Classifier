def solve():
    """Index: 4331.
    Returns: the total number of data instances recorded by the device.
    """
    # L1
    minutes_per_hour = 60 # WK
    seconds_per_minute = 60 # WK
    seconds_in_hour = minutes_per_hour * seconds_per_minute

    # L2
    recording_interval_seconds = 5 # every 5 seconds
    total_data_instances = seconds_in_hour / recording_interval_seconds

    # FA
    answer = total_data_instances
    return answer