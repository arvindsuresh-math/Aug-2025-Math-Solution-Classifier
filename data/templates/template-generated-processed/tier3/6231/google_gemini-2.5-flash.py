from fractions import Fraction

def solve():
    """Index: 6231.
    Returns: the total miles Ms. Warren ran and walked.
    """
    # L1
    run_time_minutes = 20 # for 20 minutes
    minutes_per_hour = 60 # WK
    run_time_fraction_hour = Fraction(run_time_minutes, minutes_per_hour)

    # L2
    run_speed = 6 # at 6 mph
    run_time_fraction_hour_denominator = run_time_fraction_hour.denominator
    distance_ran = run_speed / run_time_fraction_hour_denominator

    # L3
    walk_time_minutes = 30 # for 30 minutes
    walk_time_fraction_hour = Fraction(walk_time_minutes, minutes_per_hour)

    # L4
    walk_speed = 2 # at 2 mph
    walk_time_fraction_hour_denominator = walk_time_fraction_hour.denominator
    distance_walked = walk_speed / walk_time_fraction_hour_denominator

    # L5
    total_distance = distance_ran + distance_walked

    # FA
    answer = total_distance
    return answer