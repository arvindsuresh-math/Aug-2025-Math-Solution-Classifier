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
    proportion_after_spill = initial_fill_proportion * spill_proportion # eval: 0.25 = 0.5 * 0.5
    #: L3
    final_proportion = proportion_after_spill * refill_multiplier # eval: 0.75 = 0.25 * 3
    #: L4
    water_volume = aquarium_volume * final_proportion # eval: 54.0 = 72 * 0.75
    answer = water_volume # FINAL ANSWER # eval: 54.0 = 54.0 # FINAL ANSWER
    return answer # eval: return 54.0