from fractions import Fraction

def solve():
    """Index: 5878.
    Returns: the total width of the splashes.
    """
    # L1
    num_pebbles = 6 # 6 pebbles
    pebble_splash_width = Fraction(1, 4) # a 1/4 meter wide
    pebble_total_splash_width = num_pebbles * pebble_splash_width

    # L2
    num_rocks = 3 # 3 rocks
    rock_splash_width = Fraction(1, 2) # 1/2 a meter wide
    rock_total_splash_width = num_rocks * rock_splash_width

    # L3
    num_boulders = 2 # 2 boulders
    boulder_splash_width = 2 # 2 meters wide
    boulder_total_splash_width = num_boulders * boulder_splash_width

    # L4
    total_splash_width = pebble_total_splash_width + rock_total_splash_width + boulder_total_splash_width

    # FA
    answer = total_splash_width
    return answer