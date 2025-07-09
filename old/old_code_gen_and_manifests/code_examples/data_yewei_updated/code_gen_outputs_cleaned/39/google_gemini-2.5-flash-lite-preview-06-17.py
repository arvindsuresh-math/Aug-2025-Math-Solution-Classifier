def solve(
    anna_candy_per_house: int = 14, # Anna gets 14 pieces of candy per house
    anna_houses: int = 60, # the first subdivision has 60 houses
    billy_candy_per_house: int = 11, # Billy gets 11 pieces of candy per house
    billy_houses: int = 75 # the second subdivision has 75 houses
):
    """Index: 39.
    Returns: the difference in the number of candy pieces Anna gets compared to Billy.
    """
    #: L1
    anna_total_candy = anna_candy_per_house * anna_houses

    #: L2
    billy_total_candy = billy_candy_per_house * billy_houses

    #: L3
    candy_difference = anna_total_candy - billy_total_candy

    answer = candy_difference # FINAL ANSWER
    return answer