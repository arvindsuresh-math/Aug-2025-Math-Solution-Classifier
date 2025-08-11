from fractions import Fraction

def solve():
    """Index: 5590.
    Returns: the total number of palm trees in both the desert and the forest combined.
    """
    # L1
    fewer_fraction = Fraction(3, 5) # 3/5 fewer palm trees
    forest_palm_trees = 5000 # which has 5000 palm trees
    fewer_palm_trees = fewer_fraction * forest_palm_trees

    # L2
    desert_palm_trees = forest_palm_trees - fewer_palm_trees

    # L3
    total_palm_trees = forest_palm_trees + desert_palm_trees

    # FA
    answer = total_palm_trees
    return answer