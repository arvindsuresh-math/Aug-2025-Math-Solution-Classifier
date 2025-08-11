from fractions import Fraction

def solve():
    """Index: 5468.
    Returns: the total number of fruits remaining in all the trees.
    """
    # L1
    num_trees = 8 # eight orange trees
    fruits_per_tree = 200 # each tree has 200 fruits
    total_initial_oranges = num_trees * fruits_per_tree

    # L2
    fraction_picked = Fraction(2, 5) # picks 2/5 of the oranges
    oranges_picked_per_tree = fraction_picked * fruits_per_tree

    # L3
    total_oranges_picked = num_trees * oranges_picked_per_tree

    # L4
    remaining_oranges = total_initial_oranges - total_oranges_picked

    # FA
    answer = remaining_oranges
    return answer