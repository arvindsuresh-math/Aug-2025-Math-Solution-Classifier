from fractions import Fraction

def solve():
    """Index: 2469.
    Returns: the number of pink crayons.
    """
    # L1
    green_fraction = Fraction(2, 3) # 2/3 the number of green crayons as blue crayons
    blue_crayons = 6 # 6 crayons are blue
    green_crayons = green_fraction * blue_crayons

    # L2
    total_crayons = 24 # 24 crayons total
    red_crayons = 8 # 8 crayons are red
    pink_crayons = total_crayons - red_crayons - blue_crayons - green_crayons

    # FA
    answer = pink_crayons
    return answer