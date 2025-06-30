def solve(
    mango_trees: int = 60,  # Randy has 60 mango trees
    less_than_half_coconut: int = 5  # He has 5 less than half as many coconut trees as mango trees
):
    """Index: 12.
    Returns: the total number of trees Randy has on his farm.
    """

    #: L1
    half_mango_trees = mango_trees / 2 # eval: 30.0 = 60 / 2

    #: L2
    coconut_trees = half_mango_trees - less_than_half_coconut # eval: 25.0 = 30.0 - 5

    #: L3
    total_trees = mango_trees + coconut_trees # eval: 85.0 = 60 + 25.0

    #: FA
    answer = total_trees
    return answer # eval: return 85.0
