from fractions import Fraction

def solve():
    """Index: 3323.
    Returns: the total time in hours to push the car back to town.
    """
    # L1
    distance_phase1 = 3 # For the first three miles
    speed_phase1 = 6 # speed of 6 miles per hour
    time_phase1 = Fraction(distance_phase1, speed_phase1)

    # L2
    distance_phase2 = 3 # for the next 3 miles
    speed_phase2 = 3 # speed of 3 miles per hour
    time_phase2 = distance_phase2 / speed_phase2

    # L3
    distance_phase3 = 4 # For the last four miles
    speed_phase3 = 8 # speed of 8 miles per hour
    time_phase3 = Fraction(distance_phase3, speed_phase3)

    # L4
    total_time = time_phase1 + time_phase2 + time_phase3

    # FA
    answer = total_time
    return answer