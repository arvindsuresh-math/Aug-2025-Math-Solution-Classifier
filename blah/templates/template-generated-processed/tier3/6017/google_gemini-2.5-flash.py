from fractions import Fraction

def solve():
    """Index: 6017.
    Returns: the total distance Stephen covered.
    """
    # L1
    fraction_numerator = 3 # 3/4 of the mountain's height
    fraction_denominator = 4 # 3/4 of the mountain's height
    mountain_height = 40000 # 40,000 foot tall mountain
    distance_up_one_trip = Fraction(fraction_numerator, fraction_denominator) * mountain_height

    # L2
    distance_one_round_trip = distance_up_one_trip + distance_up_one_trip

    # L3
    num_round_trips = 10 # 10 round trips
    total_distance_covered = num_round_trips * distance_one_round_trip

    # FA
    answer = total_distance_covered
    return answer