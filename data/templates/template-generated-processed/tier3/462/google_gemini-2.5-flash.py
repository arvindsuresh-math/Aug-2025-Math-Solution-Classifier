def solve():
    """Index: 462.
    Returns: the total number of skips by Roberto and Valerie.
    """
    # L1
    roberto_skips_per_hour = 4200 # Roberto can skip 4,200 times an hour
    minutes_per_hour = 60 # WK
    roberto_skips_per_minute = roberto_skips_per_hour / minutes_per_hour

    # L2
    valerie_skips_per_minute = 80 # Valerie can skip 80 times a minute
    total_skips_per_minute = roberto_skips_per_minute + valerie_skips_per_minute

    # L3
    jump_duration_minutes = 15 # jump rope for fifteen minutes straight
    total_skips = total_skips_per_minute * jump_duration_minutes

    # FA
    answer = total_skips
    return answer