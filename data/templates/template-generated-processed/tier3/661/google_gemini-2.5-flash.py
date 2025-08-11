from fractions import Fraction

def solve():
    """Index: 661.
    Returns: the number of nuts left.
    """
    # L1
    total_nuts = 30 # 30 different nuts in a bowl
    eaten_fraction = Fraction(5, 6) # 5/6 of the nuts were eaten
    nuts_eaten = total_nuts * eaten_fraction

    # L2
    nuts_left = total_nuts - nuts_eaten

    # FA
    answer = nuts_left
    return answer