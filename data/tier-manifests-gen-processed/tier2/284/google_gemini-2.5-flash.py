def solve():
    """Index: 284.
    Returns: the total number of vibrations experienced by Matt.
    """
    # L1
    lowest_setting_vibrations = 1600 # vibrates at 1600 vibrations per second
    faster_percent_decimal = 0.6 # vibrates 60% faster
    faster_vibrations = lowest_setting_vibrations * faster_percent_decimal

    # L2
    highest_setting_vibrations = lowest_setting_vibrations + faster_vibrations

    # L3
    usage_minutes = 5 # for 5 minutes
    seconds_per_minute = 60 # WK
    usage_seconds = usage_minutes * seconds_per_minute

    # L4
    total_vibrations = highest_setting_vibrations * usage_seconds

    # FA
    answer = total_vibrations
    return answer