from fractions import Fraction

def solve():
    """Index: 4158.
    Returns: the total number of working light bulbs.
    """
    # L1
    num_lamps = 20 # 20 lamps
    bulbs_per_lamp = 7 # seven light bulbs in each lamp
    total_bulbs = num_lamps * bulbs_per_lamp

    # L2
    fraction_burnt_out_lamps = Fraction(1, 4) # 1/4 of them
    lamps_with_burnt_out_bulbs = fraction_burnt_out_lamps * num_lamps

    # L3
    burnt_out_bulbs_per_lamp = 2 # 2 burnt-out light bulbs each
    total_burnt_out_bulbs = burnt_out_bulbs_per_lamp * lamps_with_burnt_out_bulbs

    # L4
    working_bulbs = total_bulbs - total_burnt_out_bulbs

    # FA
    answer = working_bulbs
    return answer