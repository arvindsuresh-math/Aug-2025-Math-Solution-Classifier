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

    #: L3
    difference_in_candy = anna_total_candy - anna_houses # eval: 780 = 840 - 60

    #: FA
    answer = difference_in_candy
    return answer # eval: return 780
