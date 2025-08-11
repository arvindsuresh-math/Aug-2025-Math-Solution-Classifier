def solve():
    """Index: 7074.
    Returns: the car's speed in miles per hour.
    """
    # L1
    distance_miles = 360 # 360 miles
    initial_hours = 4 # 4 hours
    initial_minutes = 30 # 30 minutes
    minutes_per_hour = 60 # WK
    total_time_hours = initial_hours + initial_minutes / minutes_per_hour

    # L2
    speed_mph = distance_miles / total_time_hours

    # FA
    answer = speed_mph
    return answer