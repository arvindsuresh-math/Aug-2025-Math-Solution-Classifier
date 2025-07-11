def solve():
    """Index: 244.
    Returns: the distance the fox would make.
    """
    # L1
    total_minutes = 120 # 120 minutes
    minutes_per_hour = 60 # 1 hour is 60 minutes
    total_hours = total_minutes / minutes_per_hour

    # L2
    speed_km_per_hour = 50 # maximum speed of 50 kilometers per hour
    distance_km = speed_km_per_hour * total_hours

    # FA
    answer = distance_km
    return answer