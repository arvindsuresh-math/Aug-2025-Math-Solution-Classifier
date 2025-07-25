from fractions import Fraction

def solve():
    """Index: 3952.
    Returns: the distance Luis will go in 15 minutes.
    """
    # L1
    total_distance = 80 # driving 80 miles
    total_time_hours = 2 # in 2 hours
    miles_per_hour = total_distance / total_time_hours

    # L2
    minutes_per_hour = 60 # WK
    miles_per_minute = Fraction(miles_per_hour, minutes_per_hour)

    # L3
    target_minutes = 15 # in 15 minutes
    distance_in_15_minutes = miles_per_minute * target_minutes

    # FA
    answer = distance_in_15_minutes
    return answer