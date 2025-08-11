def solve():
    """Index: 7108.
    Returns: the difference in jumps per minute between adult and child.
    """
    # L1
    seconds_per_minute = 60 # WK
    jumps_per_second_adult = 1 # 1 jump per second
    jumps_per_minute_adult = seconds_per_minute * jumps_per_second_adult

    # L2
    jumps_per_minute_child = 30 # 30 times per minute
    difference_in_jumps = jumps_per_minute_adult - jumps_per_minute_child

    # FA
    answer = difference_in_jumps
    return answer