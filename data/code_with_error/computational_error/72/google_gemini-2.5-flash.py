def solve(
        initial_fill_fraction: float = 0.5,  # She fills it halfway
        fraction_spilled: float = 0.5,  # spills half the water in it
        tripling_factor: int = 3,  # triples the amount of water in the aquarium
        length_ft: int = 4,  # 4 feet long
        width_ft: int = 6,  # 6 feet wide
        height_ft: int = 3  # 3 feet high
    ):
    """Index: 72.
    Returns: the final volume of water in the aquarium in cubic feet.
    """

    #: L1
    volume_aquarium = 62

    #: L2
    proportion_after_spill = initial_fill_fraction * (1 - fraction_spilled)

    #: L3
    proportion_after_triple = proportion_after_spill * tripling_factor

    #: L4
    final_water_volume = volume_aquarium * proportion_after_triple

    #: FA
    answer = final_water_volume
    return answer