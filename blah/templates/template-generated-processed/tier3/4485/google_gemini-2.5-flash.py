from fractions import Fraction

def solve():
    """Index: 4485.
    Returns: the speed Jack needs to jog in miles per hour.
    """
    # L1
    num_blocks = 16 # 16 blocks away
    miles_per_block = Fraction(1, 8) # each block is 1/8th of a mile
    total_distance_miles = num_blocks * miles_per_block

    # L2
    time_minutes = 10 # melt in 10 minutes
    minutes_per_hour = 60 # WK
    time_hours = Fraction(time_minutes, minutes_per_hour)

    # L3
    required_speed_mph = total_distance_miles / time_hours

    # FA
    answer = required_speed_mph
    return answer