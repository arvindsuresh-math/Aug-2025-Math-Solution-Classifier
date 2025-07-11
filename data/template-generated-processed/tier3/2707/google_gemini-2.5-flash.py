from fractions import Fraction

def solve():
    """Index: 2707.
    Returns: the total kilometers driven by Renaldo and Ernesto.
    """
    # L1
    renaldo_distance = 15 # Renaldo drove 15 kilometers

    # L2
    one_third_fraction = Fraction(1, 3) # one-third of Renaldo's distance
    additional_distance = 7 # 7 kilometers more than one-third of Renaldo's distance
    ernesto_distance = one_third_fraction * renaldo_distance + additional_distance

    # L3
    total_distance = renaldo_distance + ernesto_distance

    # FA
    answer = total_distance
    return answer