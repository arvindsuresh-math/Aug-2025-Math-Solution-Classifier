def solve():
    """Index: 4872.
    Returns: the total time in minutes to braid all the dancers' hair.
    """
    # L1
    num_dancers = 8 # 8 dancers'
    braids_per_dancer = 5 # five braids
    total_braids = num_dancers * braids_per_dancer

    # L2
    seconds_per_braid = 30 # each braid takes 30 seconds
    total_time_seconds = total_braids * seconds_per_braid

    # L3
    seconds_per_minute = 60 # WK
    total_time_minutes = total_time_seconds / seconds_per_minute

    # FA
    answer = total_time_minutes
    return answer