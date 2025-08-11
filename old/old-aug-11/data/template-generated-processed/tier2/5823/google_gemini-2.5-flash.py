def solve():
    """Index: 5823.
    Returns: the amount of water wasted during one hour.
    """
    # L1
    drips_per_minute = 10 # drips about 10 times
    volume_per_drop = 0.05 # each drop contains 0.05 mL
    wasted_per_minute = drips_per_minute * volume_per_drop

    # L2
    minutes_per_hour = 60 # WK
    wasted_per_hour = wasted_per_minute * minutes_per_hour

    # FA
    answer = wasted_per_hour
    return answer