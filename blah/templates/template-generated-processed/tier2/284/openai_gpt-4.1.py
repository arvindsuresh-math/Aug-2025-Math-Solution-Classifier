def solve():
    """Index: 284.
    Returns: the total number of vibrations Matt experiences at the highest setting for 5 minutes.
    """
    # L1
    lowest_setting_vps = 1600 # vibrates at 1600 vibrations per second
    percent_faster = 0.6 # 60% faster
    vps_increase = lowest_setting_vps * percent_faster

    # L2
    highest_setting_vps = lowest_setting_vps + vps_increase

    # L3
    minutes_used = 5 # uses it for 5 minutes
    seconds_per_minute = 60 # WK
    total_seconds = minutes_used * seconds_per_minute

    # L4
    total_vibrations = highest_setting_vps * total_seconds

    # FA
    answer = total_vibrations
    return answer