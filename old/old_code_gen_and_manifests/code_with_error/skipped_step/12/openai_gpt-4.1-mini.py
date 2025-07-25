def solve(
    mango_trees: int = 60,  # Randy has 60 mango trees
    less_than_half_coconut: int = 5  # He has 5 less than half as many coconut trees as mango trees
):
    """Index: 12.
    Returns: the total number of trees Randy has on his farm.
    """

    #: L1

    #: L2
    coconut_trees = less_than_half_coconut - less_than_half_coconut

    #: L3
    total_trees = mango_trees + coconut_trees

    #: FA
    answer = total_trees
    return answer