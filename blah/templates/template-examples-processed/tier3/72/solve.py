from fractions import Fraction

def solve():
    """Index: 72.
    Returns: how many cubic feet of water are in the aquarium.
    """
    # L1
    length = 4 # 4 feet long
    width = 6 # 6 feet wide
    height = 3 # 3 feet high
    total_volume = length * width * height

    # L2
    initial_fill_proportion = Fraction(1, 2) # fills it halfway
    spilled_proportion = Fraction(1, 2) # spills half the water
    proportion_after_spill = initial_fill_proportion * spilled_proportion

    # L3
    refill_multiplier = 3 # triples the amount of water
    final_proportion = proportion_after_spill * refill_multiplier

    # L4
    water_volume = total_volume * final_proportion

    # FA
    answer = water_volume
    return answer