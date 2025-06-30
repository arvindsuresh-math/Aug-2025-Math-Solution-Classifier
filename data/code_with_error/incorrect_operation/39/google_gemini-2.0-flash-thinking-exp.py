def solve(
    anna_candy_per_house: int = 14, # she gets 14 pieces of candy per house
    billy_candy_per_house: int = 11, # he gets 11 pieces of candy per house
    anna_houses: int = 60, # the first subdivision has 60 houses
    billy_houses: int = 75 # the second subdivision has 75 houses
):
    """Index: 39.
    Returns: the difference in the number of pieces of candy Anna gets compared to Billy.
    """

    #: L1
    anna_total_candy = anna_candy_per_house - anna_houses

    #: L2
    billy_total_candy = billy_candy_per_house * billy_houses

    #: L3
    difference = anna_total_candy - billy_total_candy

    #: FA
    answer = difference
    return answer