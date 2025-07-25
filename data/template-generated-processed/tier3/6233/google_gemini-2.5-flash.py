from fractions import Fraction

def solve():
    """Index: 6233.
    Returns: the number of girls at the party.
    """
    # L1
    total_children = 50 # 50 children at the party
    boys_fraction = Fraction(3, 5) # Three-fifths of them are boys
    num_boys = total_children * boys_fraction

    # L2
    num_girls = total_children - num_boys

    # FA
    answer = num_girls
    return answer