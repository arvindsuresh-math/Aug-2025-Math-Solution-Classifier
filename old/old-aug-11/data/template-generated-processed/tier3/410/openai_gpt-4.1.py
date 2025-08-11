def solve():
    """Index: 410.
    Returns: the number of hours Mark would need to jump rope to break the record.
    """
    # L1
    jumps_per_second = 3 # He can jump 3 times a second
    seconds_per_minute = 60 # WK
    jumps_per_minute = jumps_per_second * seconds_per_minute

    # L2
    minutes_per_hour = 60 # WK
    jumps_per_hour = jumps_per_minute * minutes_per_hour

    # L3
    record_jumps = 54000 # The record is 54,000
    hours_needed = record_jumps / jumps_per_hour

    # FA
    answer = hours_needed
    return answer