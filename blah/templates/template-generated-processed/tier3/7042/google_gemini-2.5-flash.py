from fractions import Fraction

def solve():
    """Index: 7042.
    Returns: the distance the bus traveled in miles.
    """
    # L1
    minutes_per_hour = 60 # WK

    # L2
    travel_minutes = 42 # 42 minutes
    travel_hours = Fraction(travel_minutes, minutes_per_hour)

    # L3
    speed_mph = 50 # speed of 50 mph
    distance_traveled = speed_mph * travel_hours

    # FA
    answer = distance_traveled
    return answer