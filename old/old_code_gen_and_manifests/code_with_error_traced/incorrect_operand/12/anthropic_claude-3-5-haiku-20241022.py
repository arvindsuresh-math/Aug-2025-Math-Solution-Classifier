def solve(
    mango_trees: int = 60,  # Randy has 60 mango trees
    coconut_tree_reduction: int = 5  # 5 less than half as many coconut trees
):
    """Index: 12.
    Returns: the total number of trees on Randy's farm."""

    #: L1
    half_mango_trees = coconut_tree_reduction / 2 # eval: 2.5 = 5 / 2

    #: L2
    coconut_trees = half_mango_trees - coconut_tree_reduction # eval: -2.5 = 2.5 - 5

    #: L3
    total_trees = mango_trees + coconut_trees # eval: 57.5 = 60 + -2.5

    #: FA
    answer = total_trees
    return answer # eval: return 57.5
