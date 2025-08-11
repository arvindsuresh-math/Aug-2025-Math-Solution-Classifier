def solve():
    """Index: 2071.
    Returns: the total number of push-ups Jackie can do in one minute with breaks.
    """
    # L1
    total_minutes = 1 # one minute
    seconds_per_minute = 60 # WK
    total_seconds_in_minute = total_minutes * seconds_per_minute

    # L2
    num_breaks = 2 # two 8-second breaks
    break_duration = 8 # 8-second breaks
    total_break_seconds = num_breaks * break_duration

    # L3
    pushup_time = total_seconds_in_minute - total_break_seconds

    # L4
    time_for_pushups = 10 # 5 push-ups in 10 seconds
    num_pushups = 5 # 5 push-ups in 10 seconds
    time_per_pushup = time_for_pushups / num_pushups

    # L5
    total_pushups = pushup_time / time_per_pushup

    # FA
    answer = total_pushups
    return answer