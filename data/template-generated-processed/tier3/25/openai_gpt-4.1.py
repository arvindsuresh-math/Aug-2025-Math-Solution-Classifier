from fractions import Fraction

def solve():
    """Index: 25.
    Returns: the total number of tennis balls Ralph did not hit.
    """
    # L1
    first_batch = 100 # Out of the first 100 balls
    not_hit_fraction_first = Fraction(3, 5) # not able to hit 3/5 of them
    not_hit_first = not_hit_fraction_first * first_batch

    # L2
    second_batch = 75 # Of the next 75 tennis balls
    not_hit_fraction_second = Fraction(2, 3) # not able to hit 2/3 of them
    not_hit_second = not_hit_fraction_second * second_batch

    # L3
    total_not_hit = not_hit_first + not_hit_second

    # FA
    answer = total_not_hit
    return answer