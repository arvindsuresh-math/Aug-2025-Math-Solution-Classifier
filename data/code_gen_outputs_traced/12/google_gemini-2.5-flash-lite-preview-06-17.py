def solve(
    num_mango_trees: int = 60, # Randy has 60 mango trees on his farm
    coconut_trees_offset: int = 5 # He also has 5 less than half as many coconut trees as mango trees
):
    """Index: 12.
    Returns: the total number of trees Randy has on his farm.
    """

    #: L1
    half_mango_trees = num_mango_trees / 2 # eval: 30.0 = 60 / 2

    #: L2
    num_coconut_trees = half_mango_trees - coconut_trees_offset # eval: 25.0 = 30.0 - 5

    #: L3
    total_trees = num_mango_trees + num_coconut_trees # eval: 85.0 = 60 + 25.0

    #: FA
    answer = total_trees
    return answer # eval: return 85.0
