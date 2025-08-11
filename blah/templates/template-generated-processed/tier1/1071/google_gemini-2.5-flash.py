def solve():
    """Index: 1071.
    Returns: the combined length of time, in seconds, to swim all four 100-meter events.
    """
    # L1
    freestyle_time = 48 # 48 seconds
    backstroke_slower_than_freestyle = 4 # 4 seconds slower than he swims the 100-meter freestyle
    backstroke_time = freestyle_time + backstroke_slower_than_freestyle

    # L2
    butterfly_slower_than_backstroke = 3 # 3 seconds slower than he swims the 100-meter backstroke
    butterfly_time = backstroke_time + butterfly_slower_than_backstroke

    # L3
    breaststroke_slower_than_butterfly = 2 # 2 seconds slower than he swims the 100-meter butterfly
    breaststroke_time = butterfly_time + breaststroke_slower_than_butterfly

    # L4
    total_time = freestyle_time + backstroke_time + butterfly_time + breaststroke_time

    # FA
    answer = total_time
    return answer