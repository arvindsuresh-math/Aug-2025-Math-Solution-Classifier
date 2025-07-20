from fractions import Fraction

def solve():
    """Index: 5795.
    Returns: the number of carnations Ariana bought.
    """
    # L1
    roses_fraction = Fraction(2, 5) # 2/5 of which were roses
    total_flowers = 40 # a bunch of 40 flowers
    num_roses = roses_fraction * total_flowers

    # L2
    num_tulips = 10 # 10 were tulips
    roses_and_tulips = num_roses + num_tulips

    # L3
    num_carnations = total_flowers - roses_and_tulips

    # FA
    answer = num_carnations
    return answer