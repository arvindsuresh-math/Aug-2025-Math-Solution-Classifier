from fractions import Fraction

def solve():
    """Index: 1287.
    Returns: the speed Pete can walk backwards in miles per hour.
    """
    # L1
    pete_hands_speed = 2 # Pete walks on his hands at 2 miles per hour
    pete_hands_fraction = Fraction(1, 4) # only one quarter the speed that Tracy can do cartwheels
    tracy_multiplier = 1 / pete_hands_fraction
    tracy_cartwheel_speed = pete_hands_speed * tracy_multiplier

    # L2
    tracy_susan_speed_ratio = 2 # twice as fast as Susan walks forwards
    susan_forward_speed = tracy_cartwheel_speed / tracy_susan_speed_ratio

    # L3
    pete_susan_speed_ratio = 3 # three times faster than Susan walks forwards
    pete_backwards_speed = susan_forward_speed * pete_susan_speed_ratio

    # FA
    answer = pete_backwards_speed
    return answer