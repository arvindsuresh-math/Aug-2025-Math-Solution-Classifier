from fractions import Fraction

def solve():
    """Index: 72.
    Returns: the number of cubic feet of water in the aquarium after all events.
    """
    # L1
    length = 4 # 4 feet long
    width = 6 # 6 feet wide
    height = 3 # 3 feet high
    aquarium_volume = length * width * height

    # L2
    initial_fill_fraction = Fraction(1, 2) # fills it halfway
    spill_fraction = Fraction(1, 2) # spills half the water in it
    after_spill_fraction = initial_fill_fraction * spill_fraction

    # L3
    refill_multiplier = 3 # triples the amount of water
    after_refill_fraction = refill_multiplier * after_spill_fraction

    # L4
    final_water_volume = aquarium_volume * after_refill_fraction

    # FA
    answer = final_water_volume
    return answer