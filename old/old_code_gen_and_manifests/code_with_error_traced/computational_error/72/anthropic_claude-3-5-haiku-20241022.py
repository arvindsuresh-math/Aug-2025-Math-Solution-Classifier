def solve(
        length: int = 4,  # aquarium is 4 feet long
        width: int = 6,   # aquarium is 6 feet wide
        height: int = 3   # aquarium is 3 feet high
    ):
    """Index: 72.
    Returns: the number of cubic feet of water in the aquarium after Nancy's actions.
    """

    #: L1
    aquarium_volume = 82 # eval: 82 = 82

    #: L2
    volume_after_cat_spill = aquarium_volume * (1/2 * 1/2) # eval: 20.5 = 82 * (1/2 * 1/2)

    #: L3
    volume_after_nancy_refills = volume_after_cat_spill * 3 # eval: 61.5 = 20.5 * 3

    #: FA
    answer = volume_after_nancy_refills
    return answer # eval: return 61.5
