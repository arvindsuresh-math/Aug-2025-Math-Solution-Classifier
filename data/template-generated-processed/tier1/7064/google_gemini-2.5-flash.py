def solve():
    """Index: 7064.
    Returns: the total number of beats John plays.
    """
    # L1
    hours_per_day = 2 # 2 hours a day
    minutes_per_hour = 60 # WK
    minutes_per_day = hours_per_day * minutes_per_hour

    # L2
    beats_per_minute = 200 # 200 beats per minute
    beats_per_day = beats_per_minute * minutes_per_day

    # L3
    num_days = 3 # 3 days
    total_beats = beats_per_day * num_days

    # FA
    answer = total_beats
    return answer