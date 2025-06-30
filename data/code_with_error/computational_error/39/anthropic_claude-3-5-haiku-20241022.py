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
    anna_total_candy = 841

    #: L2
    billy_total_candy = billy_candy_per_house * billy_houses

    #: L3
    candy_difference = anna_total_candy - billy_total_candy

    #: FA
    answer = candy_difference
    return answer