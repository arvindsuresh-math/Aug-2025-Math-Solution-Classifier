def solve():
    """Index: 5879.
    Returns: the number of spots Jean has located on her sides.
    """
    # L1
    spots_on_upper_torso = 30 # 30 spots on her upper torso
    half_multiplier = 2 # Half of her spots
    total_spots = spots_on_upper_torso * half_multiplier

    # L2
    back_hindquarters_divisor = 3 # one-third of the spots
    spots_on_back_hindquarters = total_spots / back_hindquarters_divisor

    # L3
    spots_on_sides = total_spots - spots_on_upper_torso - spots_on_back_hindquarters

    # FA
    answer = spots_on_sides
    return answer