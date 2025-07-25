from fractions import Fraction

def solve():
    """Index: 3843.
    Returns: the number of slices left.
    """
    # L1
    total_slices = 8 # sliced it into 8 pieces
    joe_darcy_fraction = Fraction(1, 2) # gave 1/2 to Joe and Darcy
    slices_given_to_joe_darcy = joe_darcy_fraction * total_slices

    # L2
    carl_fraction = Fraction(1, 4) # gave 1/4 to Carl
    slices_given_to_carl = carl_fraction * total_slices

    # L3
    slices_left = total_slices - slices_given_to_joe_darcy - slices_given_to_carl

    # FA
    answer = slices_left
    return answer