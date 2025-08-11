from fractions import Fraction

def solve():
    """Index: 361.
    Returns: the distance the ship was blown in a westward direction.
    """
    # L1
    travel_hours = 20 # 20 hours
    speed_km_per_hour = 30 # 30 kilometers per hour
    distance_first_day = travel_hours * speed_km_per_hour

    # L2
    half_multiplier = 2 # WK
    total_destination_distance = half_multiplier * distance_first_day

    # L3
    one_third_fraction = Fraction(1, 3) # one-third of the way
    current_fraction_denominator = 3 # one-third of the way
    current_distance_from_start = one_third_fraction * total_destination_distance

    # L4
    distance_blown_westward = distance_first_day - current_distance_from_start

    # FA
    answer = distance_blown_westward
    return answer