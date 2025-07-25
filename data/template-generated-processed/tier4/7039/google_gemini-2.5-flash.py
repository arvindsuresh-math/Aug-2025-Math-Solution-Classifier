def solve():
    """Index: 7039.
    Returns: Carson's speed in miles per hour.
    """
    # L1
    jerry_one_way_time_minutes = 15 # 15 minutes to make a one-way trip
    carson_time_multiplier = 2 # twice as long as Jerry
    carson_time_minutes = jerry_one_way_time_minutes * carson_time_multiplier

    # L2
    minutes_per_hour = 60 # WK
    carson_time_hours = carson_time_minutes / minutes_per_hour

    # L3
    school_distance_miles = 4 # school is 4 miles away
    carson_speed_mph = school_distance_miles / carson_time_hours

    # FA
    answer = carson_speed_mph
    return answer