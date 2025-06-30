def solve(
    initial_fill_fraction: float = 1/2, # She fills it halfway
    spilled_fraction: float = 1/2, # spills half the water in it
    refill_factor: int = 3, # triples the amount of water in the aquarium
    length: int = 4, # aquarium is 4 feet long
    width: int = 6, # 6 feet wide
    height: int = 3 # and 3 feet high
):
    """Index: 72.
    Returns: the final volume of water in the aquarium in cubic feet.
    """

    #: L1

    #: L2
    proportion_after_spill = initial_fill_fraction * spilled_fraction

    #: L3
    final_proportion = proportion_after_spill * refill_factor

    #: L4
    water_volume = refill_factor * final_proportion

    #: FA
    answer = water_volume
    return answer