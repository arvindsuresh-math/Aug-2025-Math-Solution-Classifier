def solve(
        num_mango_trees: int = 60, # Randy has 60 mango trees
        less_than_half_coconut_trees: int = 5 # 5 less than half as many coconut trees
    ):
    """Index: 12.
    Returns: the total number of trees Randy has on his farm.
    """

    #: L1

    #: L2
    num_coconut_trees = num_mango_trees - less_than_half_coconut_trees # eval: 55 = 60 - 5

    #: L3
    total_trees = num_mango_trees + num_coconut_trees # eval: 115 = 60 + 55

    #: FA
    answer = total_trees
    return answer # eval: return 115
