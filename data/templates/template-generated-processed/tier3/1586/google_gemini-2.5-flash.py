def solve():
    """Index: 1586.
    Returns: the average speed of the car in miles per hour.
    """
    # L1
    hours_traveled = 2 # 2 hours 20 minutes
    minutes_traveled_part = 20 # 2 hours 20 minutes
    minutes_per_hour = 60 # WK
    total_minutes = hours_traveled * minutes_per_hour + minutes_traveled_part

    # L2
    distance_miles = 280 # 280 miles
    speed_miles_per_minute = distance_miles / total_minutes

    # L3
    average_speed_mph = speed_miles_per_minute * minutes_per_hour

    # FA
    answer = average_speed_mph
    return answer