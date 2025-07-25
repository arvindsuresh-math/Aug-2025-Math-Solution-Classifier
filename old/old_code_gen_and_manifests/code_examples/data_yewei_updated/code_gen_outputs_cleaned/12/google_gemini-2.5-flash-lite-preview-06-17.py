def solve(
    num_mango_trees: int = 60, # Randy has 60 mango trees on his farm
    coconut_trees_less_than_half_mango: int = 5 # He also has 5 less than half as many coconut trees as mango trees
):
    """Index: 12.
    Returns: the total number of trees Randy has on his farm.
    """
    #: L1
    half_mango_trees = num_mango_trees / 2

    #: L2
    num_coconut_trees = half_mango_trees - coconut_trees_less_than_half_mango

    #: L3
    total_trees = num_mango_trees + num_coconut_trees

    answer = total_trees # FINAL ANSWER
    return answer