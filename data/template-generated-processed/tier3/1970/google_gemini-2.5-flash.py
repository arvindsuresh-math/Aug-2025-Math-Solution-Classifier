from fractions import Fraction

def solve():
    """Index: 1970.
    Returns: the number of pizza slices left.
    """
    # L1
    total_slices = 16 # 1 box of pizza that is cut into 16 slices
    eaten_fraction = Fraction(3, 4) # three-fourths of the pizza
    eaten_slices = total_slices * eaten_fraction

    # L2
    remaining_slices = total_slices - eaten_slices

    # FA
    answer = remaining_slices
    return answer