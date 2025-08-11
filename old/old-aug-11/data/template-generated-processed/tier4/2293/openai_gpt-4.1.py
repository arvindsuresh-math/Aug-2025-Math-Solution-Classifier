def solve():
    """Index: 2293.
    Returns: the boy's speed in kilometers per hour.
    """
    # L1
    minutes_in_hour = 60 # 1 hour is equal to 60 minutes
    time_minutes = 45 # 45 minutes
    time_hours = time_minutes / minutes_in_hour

    # L2
    distance_km = 1.5 # 1.5 km
    speed_kmph = distance_km / time_hours

    # FA
    answer = speed_kmph
    return answer