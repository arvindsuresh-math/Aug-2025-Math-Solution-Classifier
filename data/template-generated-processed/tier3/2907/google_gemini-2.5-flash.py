from fractions import Fraction

def solve():
    """Index: 2907.
    Returns: the number of trees that are not pine trees.
    """
    # L1
    total_trees = 350 # There are 350 trees in the park
    pine_percentage = Fraction(70, 100) # 70% of which are pine trees
    pine_trees = total_trees * pine_percentage

    # L2
    not_pine_trees = total_trees - pine_trees

    # FA
    answer = not_pine_trees
    return answer