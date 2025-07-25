def solve():
    """Index: 2293.
    Returns: the boy's speed in kilometers per hour.
    """
    # L1
    minutes_run = 45 # 45 minutes
    minutes_per_hour = 60 # WK
    hours_run = minutes_run / minutes_per_hour

    # L2
    distance_km = 1.5 # 1.5 km
    speed_km_per_hour = distance_km / hours_run

    # FA
    answer = speed_km_per_hour
    return answer