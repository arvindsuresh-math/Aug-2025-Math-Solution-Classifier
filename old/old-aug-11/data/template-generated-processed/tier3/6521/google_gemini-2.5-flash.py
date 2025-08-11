from fractions import Fraction

def solve():
    """Index: 6521.
    Returns: the number of birches in the forest.
    """
    # L1
    spruce_percentage = Fraction(10, 100) # Spruces make up 10% of all the trees
    total_trees = 4000 # total of 4000 trees
    num_spruces = spruce_percentage * total_trees

    # L2
    pine_percentage = Fraction(13, 100) # pines 13%
    num_pines = pine_percentage * total_trees

    # L3
    num_oaks = num_spruces + num_pines

    # L4
    num_birches = total_trees - num_oaks - num_pines - num_spruces

    # FA
    answer = num_birches
    return answer