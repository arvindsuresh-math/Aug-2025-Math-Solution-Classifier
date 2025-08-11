from fractions import Fraction

def solve():
    """Index: 3436.
    Returns: the number of lemons Cristine has left.
    """
    # L1
    num_dozens = 1 # a dozen lemons
    lemons_per_dozen = 12 # WK
    total_lemons_bought = num_dozens * lemons_per_dozen

    # L2
    fraction_given = Fraction(1, 4) # 1/4 of them
    lemons_given_to_neighbor = total_lemons_bought * fraction_given

    # L3
    lemons_left = total_lemons_bought - lemons_given_to_neighbor

    # FA
    answer = lemons_left
    return answer