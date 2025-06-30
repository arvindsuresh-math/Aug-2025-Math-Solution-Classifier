def solve(
    length: int = 4, # 4 feet long
    width: int = 6, # 6 feet wide
    height: int = 3, # 3 feet high
    initial_fill_proportion: float = 0.5, # She fills it halfway
    spill_proportion: float = 0.5, # spills half the water in it
    refill_multiplier: int = 3 # triples the amount of water
):
    """Index: 72.
    Returns: the volume of water in the aquarium in cubic feet.
    """

    #: L1
    aquarium_volume = length * width * height

    #: L2
    proportion_after_spill = -9.75

    #: L3
    final_proportion = proportion_after_spill * refill_multiplier

    #: L4
    water_volume = aquarium_volume * final_proportion

    #: FA
    answer = water_volume
    return answer