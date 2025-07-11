def solve():
    """Index: 1206.
    Returns: the total number of jumps Spencer will do in 5 days.
    """
    # L1
    jumps_per_minute = 4 # jumps 4 times per minute
    minutes_per_session = 10 # 10 minutes each session
    jumps_per_session = jumps_per_minute * minutes_per_session

    # L2
    sessions_per_day = 2 # 2 sessions each day
    num_days = 5 # in 5 days
    total_sessions = sessions_per_day * num_days

    # L3
    total_jumps_in_5_days = total_sessions * jumps_per_session

    # FA
    answer = total_jumps_in_5_days
    return answer