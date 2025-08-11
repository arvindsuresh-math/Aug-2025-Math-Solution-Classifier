def solve():
    """Index: 462.
    Returns: the total number of skips Roberto and Valerie make in fifteen minutes.
    """
    # L1
    roberto_hourly_skips = 4200 # Roberto can skip 4,200 times an hour
    minutes_per_hour = 60 # WK
    roberto_minute_skips = roberto_hourly_skips / minutes_per_hour

    # L2
    valerie_minute_skips = 80 # Valerie can skip 80 times a minute
    total_minute_skips = roberto_minute_skips + valerie_minute_skips

    # L3
    total_minutes = 15 # jump rope for fifteen minutes straight
    total_skips = total_minute_skips * total_minutes

    # FA
    answer = total_skips
    return answer