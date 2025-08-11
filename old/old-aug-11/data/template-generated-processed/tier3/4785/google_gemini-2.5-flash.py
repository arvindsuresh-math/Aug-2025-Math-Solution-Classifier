from fractions import Fraction

def solve():
    """Index: 4785.
    Returns: the number of times Rosie circles the track.
    """
    # L1
    lou_miles_run = 3 # running three miles
    track_length = Fraction(1, 4) # one-quarter of a mile long
    lou_circles = lou_miles_run / track_length

    # L2
    rosie_speed_multiplier = 2 # twice the speed of her husband
    rosie_miles_run = lou_miles_run * rosie_speed_multiplier

    # L3
    rosie_circles = rosie_miles_run / track_length

    # FA
    answer = rosie_circles
    return answer