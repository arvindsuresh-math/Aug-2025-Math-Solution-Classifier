def solve(
        anna_candy_per_house: int = 14,  # Anna gets 14 pieces of candy per house
        billy_candy_per_house: int = 11,  # Billy gets 11 pieces of candy per house
        anna_houses: int = 60,  # first subdivision has 60 houses
        billy_houses: int = 75  # second subdivision has 75 houses
    ):
    """Index: 39.
    Returns: the difference in the number of candy pieces between Anna and Billy.
    """

    #: L1

    #: L2
    billy_total_candy = billy_candy_per_house * billy_houses # eval: 825 = 11 * 75

    #: L3
    candy_difference = billy_candy_per_house - billy_total_candy # eval: -814 = 11 - 825

    #: FA
    answer = candy_difference
    return answer # eval: return -814
