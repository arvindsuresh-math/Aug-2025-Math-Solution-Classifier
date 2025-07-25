from fractions import Fraction

def solve():
    """Index: 833.
    Returns: the total kilometers walked by the two girls.
    """
    # L1
    nadia_distance = 18 # Nadia walked 18 kilometers
    hannah_fraction = Fraction(1, 2) # which was twice as far as Hannah walked
    hannah_distance = hannah_fraction * nadia_distance

    # L2
    total_distance = hannah_distance + nadia_distance

    # FA
    answer = total_distance
    return answer