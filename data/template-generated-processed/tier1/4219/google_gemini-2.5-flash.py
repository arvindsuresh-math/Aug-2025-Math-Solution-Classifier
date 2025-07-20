def solve():
    """Index: 4219.
    Returns: the total number of beats James hears per week.
    """
    # L1
    hours_per_day = 2 # 2 hours of music a day
    minutes_per_hour = 60 # WK
    minutes_per_day = hours_per_day * minutes_per_hour

    # L2
    beats_per_minute = 200 # 200 beats per minute
    beats_per_day = beats_per_minute * minutes_per_day

    # L3
    days_per_week = 7 # WK
    beats_per_week = beats_per_day * days_per_week

    # FA
    answer = beats_per_week
    return answer