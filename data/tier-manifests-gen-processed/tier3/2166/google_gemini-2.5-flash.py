def solve():
    """Index: 2166.
    Returns: the total number of turns the wheel makes in two hours.
    """
    # L1
    seconds_per_minute = 60 # WK
    time_interval_seconds = 30 # 30 seconds
    sets_of_30_seconds_per_minute = seconds_per_minute / time_interval_seconds

    # L2
    turns_per_30_seconds = 6 # 6 turns
    turns_per_minute = turns_per_30_seconds * sets_of_30_seconds_per_minute

    # L3
    minutes_per_hour = 60 # WK
    turns_per_hour = turns_per_minute * minutes_per_hour

    # L4
    target_hours = 2 # two hours
    total_turns = turns_per_hour * target_hours

    # FA
    answer = total_turns
    return answer