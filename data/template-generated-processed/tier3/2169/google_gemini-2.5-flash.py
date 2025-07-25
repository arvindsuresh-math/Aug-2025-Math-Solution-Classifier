from fractions import Fraction

def solve():
    """Index: 2169.
    Returns: the number of minutes John won the race by.
    """
    # L1
    race_distance = 5 # 5-mile race
    johns_speed = 15 # 15 mph
    johns_race_time_fraction_hours = Fraction(race_distance, johns_speed)

    # L2
    minutes_per_hour = 60 # WK
    hour_denominator = johns_race_time_fraction_hours.denominator
    johns_race_time_minutes = minutes_per_hour / hour_denominator

    # L3
    next_fastest_time_minutes = 23 # 23 minutes
    time_difference_minutes = next_fastest_time_minutes - johns_race_time_minutes

    # FA
    answer = time_difference_minutes
    return answer