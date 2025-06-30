def solve(
        num_mango_trees: int = 60, # Randy has 60 mango trees
        less_than_half_coconut_trees: int = 5 # 5 less than half as many coconut trees
    ):
    """Index: 12.
    Returns: the total number of trees Randy has on his farm.
    """
    #: L1
    half_mango_trees = num_mango_trees / 2 # eval: 30.0 = 60 / 2
    #: L2
    num_coconut_trees = half_mango_trees - less_than_half_coconut_trees # eval: 25.0 = 30.0 - 5
    #: L3
    total_trees = num_mango_trees + num_coconut_trees # eval: 85.0 = 60 + 25.0
    answer = total_trees # FINAL ANSWER # eval: 85.0 = 85.0 # FINAL ANSWER
    return answer # eval: return 85.0