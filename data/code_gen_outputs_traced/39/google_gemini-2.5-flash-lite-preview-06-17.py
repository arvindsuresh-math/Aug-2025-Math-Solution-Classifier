def solve(
    anna_candy_per_house: int = 14, # Anna gets 14 pieces of candy per house
    anna_houses: int = 60, # the first subdivision has 60 houses
    billy_candy_per_house: int = 11, # Billy gets 11 pieces of candy per house
    billy_houses: int = 75 # the second subdivision has 75 houses
):
    """Index: 39.
    Returns: the difference in the number of candy pieces collected by Anna and Billy.
    """
    #: L1
    anna_total_candy = anna_candy_per_house * anna_houses # eval: 840 = 14 * 60
    #: L2
    billy_total_candy = billy_candy_per_house * billy_houses # eval: 825 = 11 * 75
    #: L3
    difference_in_candy = anna_total_candy - billy_total_candy # eval: 15 = 840 - 825
    answer = difference_in_candy # FINAL ANSWER # eval: 15 = 15 # FINAL ANSWER
    return answer # eval: return 15