def solve(
    num_mango_trees: int = 60, # Randy has 60 mango trees
    less_than_half: int = 5 # 5 less than half as many coconut trees
):
    """Index: 12.
    Returns: the total number of trees on Randy's farm.
    """

    #: L1
    half_mango_trees = num_mango_trees / 2 # eval: 30.0 = 60 / 2

    #: L2
    num_coconut_trees = less_than_half - less_than_half # eval: 0 = 5 - 5

    #: L3
    total_trees = num_mango_trees + num_coconut_trees # eval: 60 = 60 + 0

    #: FA
    answer = total_trees
    return answer # eval: return 60
