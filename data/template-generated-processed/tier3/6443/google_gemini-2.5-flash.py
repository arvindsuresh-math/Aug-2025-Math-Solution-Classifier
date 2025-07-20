def solve():
    """Index: 6443.
    Returns: the time in minutes it will take Jasper to raise his kite.
    """
    # L1
    omar_distance = 240 # 240 feet
    omar_time = 12 # 12 minutes
    omar_rate = omar_distance / omar_time

    # L2
    speed_multiplier = 3 # three times the rate of speed
    jasper_rate = speed_multiplier * omar_rate

    # L3
    jasper_target_height = 600 # 600 feet
    time_for_jasper = jasper_target_height / jasper_rate

    # FA
    answer = time_for_jasper
    return answer