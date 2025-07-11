from fractions import Fraction

def solve():
    """Index: 1446.
    Returns: the difference in the number of jeans and scarves.
    """
    # L1
    black_shirts = 63 # 63 black shirts
    white_shirts = 42 # 42 white shirts
    sum_of_shirts = black_shirts + white_shirts

    # L2
    jeans_numerator = 2 # two-thirds of the sum
    jeans_denominator = 3 # two-thirds of the sum
    jeans_fraction = Fraction(jeans_numerator, jeans_denominator)
    num_jeans = jeans_fraction * sum_of_shirts

    # L3
    num_ties = 34 # 34 ties
    num_belts = 40 # 40 belts
    sum_of_ties_belts = num_ties + num_belts

    # L4
    scarf_divisor = 2 # half the number
    num_scarves = sum_of_ties_belts / scarf_divisor

    # L5
    difference_jeans_scarves = num_jeans - num_scarves

    # FA
    answer = difference_jeans_scarves
    return answer