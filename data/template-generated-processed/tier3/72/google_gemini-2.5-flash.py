from fractions import Fraction

def solve():
    """Index: 72.
    Returns: the cubic feet of water in the aquarium.
    """
    # L1
    length = 4 # 4 feet long
    width = 6 # 6 feet wide
    height = 3 # 3 feet high
    aquarium_volume = length * width * height

    # L2
    initial_fill_fraction = Fraction(1, 2) # fills it halfway
    spill_fraction = Fraction(1, 2) # spills half the water
    proportion_after_spill = initial_fill_fraction * spill_fraction

    # L3
    refill_multiplier = 3 # triples the amount of water
    proportion_after_refill = refill_multiplier * proportion_after_spill

    # L4
    water_volume = aquarium_volume * proportion_after_refill

    # FA
    answer = water_volume
    return answer