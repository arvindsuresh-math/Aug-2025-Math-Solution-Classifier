def solve(
    mango_trees: int = 60,  # Randy has 60 mango trees
    coconut_tree_reduction: int = 5  # 5 less than half as many coconut trees
):
    """Index: 12.
    Returns: the total number of trees on Randy's farm."""

    #: L1
    half_mango_trees = mango_trees / 2 # eval: 30.0 = 60 / 2

    #: L2
    coconut_trees = half_mango_trees - coconut_tree_reduction # eval: 25.0 = 30.0 - 5

    #: L3
    total_trees = mango_trees + coconut_trees # eval: 85.0 = 60 + 25.0

    #: FA
    answer = total_trees
    return answer # eval: return 85.0
