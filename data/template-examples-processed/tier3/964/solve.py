def solve():
    """Index: 964.
    Returns: the number of additional wings Alan must eat per minute.
    """
    # L1
    kevin_wings = 64 # 64 wings
    kevin_minutes = 8 # in 8 minutes
    kevin_rate = kevin_wings / kevin_minutes

    # L2
    alan_current_rate = 5 # eat 5 hot wings per minute
    rate_to_equal = kevin_rate - alan_current_rate

    # L3
    increment_to_beat = 1 # WK
    rate_to_beat = rate_to_equal + increment_to_beat

    # FA
    answer = rate_to_beat
    return answer