def solve(
        length: int = 4,  # aquarium is 4 feet long
        width: int = 6,   # aquarium is 6 feet wide
        height: int = 3   # aquarium is 3 feet high
    ):
    """Index: 72.
    Returns: the number of cubic feet of water in the aquarium.
    """
    #: L1
    aquarium_volume = length * width * height

    #: L2
    volume_after_cat_spill = aquarium_volume * (1/2) * (1/2)

    #: L3
    volume_after_nancy_refills = volume_after_cat_spill * 3

    #: L4
    answer = volume_after_nancy_refills  # FINAL ANSWER
    return answer