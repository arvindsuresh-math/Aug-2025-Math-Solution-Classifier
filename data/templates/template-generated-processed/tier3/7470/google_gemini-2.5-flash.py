from fractions import Fraction

def solve():
    """Index: 7470.
    Returns: the speed at which Colin can skip.
    """
    # L1
    bruce_speed = 1 # Bruce skips at 1 mile per hour
    tony_multiplier = 2 # twice the speed
    tony_speed = bruce_speed * tony_multiplier

    # L2
    brandon_fraction = Fraction(1, 3) # one-third the speed
    brandon_speed = tony_speed * brandon_fraction

    # L3
    colin_multiplier = 6 # six times the speed
    colin_speed = brandon_speed * colin_multiplier

    # FA
    answer = colin_speed
    return answer