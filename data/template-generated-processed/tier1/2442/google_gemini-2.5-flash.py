def solve():
    """Index: 2442.
    Returns: how long Morgan can hula hoop.
    """
    # L1
    nancy_time = 10 # 10 minutes
    casey_less_than_nancy = 3 # 3 minutes less than Nancy
    casey_time = nancy_time - casey_less_than_nancy

    # L2
    morgan_multiplier = 3 # three times as long as Casey
    morgan_time = morgan_multiplier * casey_time

    # FA
    answer = morgan_time
    return answer