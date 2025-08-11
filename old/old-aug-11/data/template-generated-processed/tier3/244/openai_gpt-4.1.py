def solve():
    """Index: 244.
    Returns: the distance the fox would run in 120 minutes at maximum speed.
    """
    # L1
    total_minutes = 120 # 120 minutes
    minutes_per_hour = 60 # WK
    total_hours = total_minutes / minutes_per_hour

    # L2
    speed_per_hour = 50 # 50 kilometers per hour
    distance = speed_per_hour * total_hours

    # FA
    answer = distance
    return answer