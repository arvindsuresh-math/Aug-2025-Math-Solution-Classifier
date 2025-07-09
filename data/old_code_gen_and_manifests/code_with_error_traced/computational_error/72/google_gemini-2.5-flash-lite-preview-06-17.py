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
    aquarium_volume = length * width * height # eval: 72 = 4 * 6 * 3

    #: L2
    proportion_after_spill = -9.75 # eval: -9.75 = -9.75

    #: L3
    final_proportion = proportion_after_spill * refill_multiplier # eval: -29.25 = -9.75 * 3

    #: L4
    water_volume = aquarium_volume * final_proportion # eval: -2106.0 = 72 * -29.25

    #: FA
    answer = water_volume
    return answer # eval: return -2106.0
