def solve():
    """Index: 1071.
    Returns: the combined time in seconds for David to swim all four 100-meter events.
    """
    # L1
    freestyle_time = 48 # swims the 100-meter freestyle in 48 seconds
    backstroke_slower = 4 # backstroke 4 seconds slower than freestyle
    backstroke_time = freestyle_time + backstroke_slower

    # L2
    butterfly_slower = 3 # butterfly 3 seconds slower than backstroke
    butterfly_time = backstroke_time + butterfly_slower

    # L3
    breaststroke_slower = 2 # breaststroke 2 seconds slower than butterfly
    breaststroke_time = butterfly_time + breaststroke_slower

    # L4
    total_time = freestyle_time + backstroke_time + butterfly_time + breaststroke_time

    # FA
    answer = total_time
    return answer