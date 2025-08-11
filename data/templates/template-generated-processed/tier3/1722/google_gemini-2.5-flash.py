from fractions import Fraction

def solve():
    """Index: 1722.
    Returns: Skye's average speed for the entire race.
    """
    # L1
    distance1 = 3 # For the first 3 kilometers
    speed1 = 150 # his speed was 150 kilometers per hour
    time1 = Fraction(distance1, speed1)

    # L2
    speed_increase = 50 # speed was 50 kilometers per hour more
    speed2 = speed1 + speed_increase

    # L3
    distance2 = 2 # For the next 2 kilometers
    time2 = Fraction(distance2, speed2)

    # L4
    speed_multiplier = 2 # speed was twice as fast
    speed3 = speed1 * speed_multiplier

    # L5
    distance3 = 1 # For the remaining 1 kilometer
    time3 = Fraction(distance3, speed3)

    # L6
    total_time = time1 + time2 + time3

    # L7
    total_track_distance = 6 # a 6-kilometer track
    average_speed = total_track_distance / total_time

    # FA
    answer = average_speed
    return answer