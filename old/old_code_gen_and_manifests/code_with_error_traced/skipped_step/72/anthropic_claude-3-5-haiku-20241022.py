def solve(
        length: int = 4,  # aquarium is 4 feet long
        width: int = 6,   # aquarium is 6 feet wide
        height: int = 3   # aquarium is 3 feet high
    ):
    """Index: 72.
    Returns: the number of cubic feet of water in the aquarium after Nancy's actions.
    """

    #: L1
    aquarium_volume = length * width * height # eval: 72 = 4 * 6 * 3

    #: L2
    volume_after_cat_spill = aquarium_volume * (1/2 * 1/2) # eval: 18.0 = 72 * (1/2 * 1/2)

    #: L3

    #: FA
    answer = width
    return answer # eval: return 6
