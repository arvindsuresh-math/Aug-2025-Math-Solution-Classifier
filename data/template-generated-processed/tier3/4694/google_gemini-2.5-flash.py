from fractions import Fraction

def solve():
    """Index: 4694.
    Returns: the number of leaves remaining on the tree.
    """
    # L1
    shed_fraction_week1 = Fraction(2, 5) # shed 2/5 of the leaves
    initial_leaves = 1000 # A tree had 1000 leaves
    leaves_shed_week1 = shed_fraction_week1 * initial_leaves

    # L2
    remaining_leaves_after_week1 = initial_leaves - leaves_shed_week1

    # L3
    shed_percentage_week2 = Fraction(40, 100) # shed 40% of the remaining leaves
    leaves_shed_week2 = shed_percentage_week2 * remaining_leaves_after_week1

    # L4
    remaining_leaves_after_week2 = remaining_leaves_after_week1 - leaves_shed_week2

    # L5
    shed_fraction_week3 = Fraction(3, 4) # shed 3/4 times as many leaves as it shed on the second week
    leaves_shed_week3 = shed_fraction_week3 * remaining_leaves_after_week2

    # L6
    final_remaining_leaves = remaining_leaves_after_week2 - leaves_shed_week3

    # FA
    answer = final_remaining_leaves
    return answer