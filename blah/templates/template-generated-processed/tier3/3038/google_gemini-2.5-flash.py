def solve():
    """Index: 3038.
    Returns: the average speed of the Starship Conundrum in parsecs per hour.
    """
    # L1
    hours_in_earth_day = 24 # WK
    multiplier_for_twice = 2 # WK
    twice_earth_day_hours = hours_in_earth_day * multiplier_for_twice

    # L2
    hours_less = 8 # eight hours less
    travel_time_hours = twice_earth_day_hours - hours_less

    # L3
    distance_parsecs = 4000 # distance between these two planets is 4,000 parsecs
    average_speed = distance_parsecs / travel_time_hours

    # FA
    answer = average_speed
    return answer