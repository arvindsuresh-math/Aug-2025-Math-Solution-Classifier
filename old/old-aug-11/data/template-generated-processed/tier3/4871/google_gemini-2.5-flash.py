from fractions import Fraction

def solve():
    """Index: 4871.
    Returns: the total number of chickens that do not lay eggs.
    """
    # L1
    total_chickens = 80 # 80 chickens
    rooster_fraction = Fraction(1, 4) # 1/4 are roosters
    num_roosters = total_chickens * rooster_fraction

    # L2
    num_hens = total_chickens - num_roosters

    # L3
    laying_hens_fraction = Fraction(3, 4) # three-fourths of those hens lay eggs
    num_laying_hens = num_hens * laying_hens_fraction

    # L4
    num_non_laying_hens = num_hens - num_laying_hens

    # L5
    total_non_laying_chickens = num_non_laying_hens + num_roosters

    # FA
    answer = total_non_laying_chickens
    return answer