def solve():
    """Index: 4482.
    Returns: the number of each kind of fruit tree planted.
    """
    # L1
    total_streets = 18 # There are eighteen streets in the neighborhood
    every_other_divisor = 2 # Every other tree is half the trees
    fruit_trees = total_streets / every_other_divisor

    # L2
    kinds_of_fruit_trees = 3 # equal numbers of plum, pear, and apricot trees
    trees_per_kind = fruit_trees / kinds_of_fruit_trees

    # FA
    answer = trees_per_kind
    return answer