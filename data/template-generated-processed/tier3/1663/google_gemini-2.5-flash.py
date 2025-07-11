from fractions import Fraction

def solve():
    """Index: 1663.
    Returns: the difference in the number of novels Jordan read compared to Alexandre.
    """
    # L1
    jordan_novels = 120 # Jordan read 120 French novels
    alexandre_fraction = Fraction(1, 10) # 1/10 of what Jordan read
    alexandre_novels = jordan_novels * alexandre_fraction

    # L2
    difference_in_novels = jordan_novels - alexandre_novels

    # FA
    answer = difference_in_novels
    return answer