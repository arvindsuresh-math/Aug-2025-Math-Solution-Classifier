from fractions import Fraction

def solve():
    """Index: 2995.
    Returns: the total number of trees on the farm.
    """
    # L1
    percentage_cut = Fraction(20, 100) # cut 20% of them
    initial_trees = 400 # 400 trees on her farm
    trees_cut = percentage_cut * initial_trees

    # L2
    trees_remaining = initial_trees - trees_cut

    # L3
    trees_planted_per_cut_tree = 5 # plants 5 new trees
    new_trees_planted = trees_cut * trees_planted_per_cut_tree

    # L4
    total_trees_on_farm = trees_remaining + new_trees_planted

    # FA
    answer = total_trees_on_farm
    return answer