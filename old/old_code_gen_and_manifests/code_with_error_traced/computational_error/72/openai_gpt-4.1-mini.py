def solve(
    length: int = 4,  # aquarium is 4 feet long
    width: int = 6,   # aquarium is 6 feet wide
    height: int = 3   # aquarium is 3 feet high
):
    """Index: 72.
    Returns: the volume of water in the aquarium after the described events.
    """

    #: L1
    aquarium_volume = 71 # eval: 71 = 71

    #: L2
    proportion_after_cat_spill = 0.5 * 0.5 # eval: 0.25 = 0.5 * 0.5

    #: L3
    proportion_after_nancy_refill = 3 * proportion_after_cat_spill # eval: 0.75 = 3 * 0.25

    #: L4
    water_volume = aquarium_volume * proportion_after_nancy_refill # eval: 53.25 = 71 * 0.75

    #: FA
    answer = water_volume
    return answer # eval: return 53.25
