def solve(
    length: int = 4,  # aquarium is 4 feet long
    width: int = 6,   # aquarium is 6 feet wide
    height: int = 3   # aquarium is 3 feet high
):
    """Index: 72.
    Returns: the volume of water in the aquarium after the described events.
    """

    #: L1
    aquarium_volume = length * width * height # eval: 72 = 4 * 6 * 3

    #: L2

    #: L3
    proportion_after_nancy_refill = 3 * height # eval: 9 = 3 * 3

    #: L4
    water_volume = aquarium_volume * proportion_after_nancy_refill # eval: 648 = 72 * 9

    #: FA
    answer = water_volume
    return answer # eval: return 648
