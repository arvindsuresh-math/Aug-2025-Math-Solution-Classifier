from fractions import Fraction

def solve():
    """Index: 5538.
    Returns: the number of bulls on the farm.
    """
    # L1
    cows_ratio_part = 10 # 10:27
    bulls_ratio_part = 27 # 10:27
    total_ratio_parts = cows_ratio_part + bulls_ratio_part

    # L2
    total_cattle = 555 # 555 cattle on the farm
    bulls_fraction = Fraction(bulls_ratio_part, total_ratio_parts)
    num_bulls = bulls_fraction * total_cattle

    # FA
    answer = num_bulls
    return answer