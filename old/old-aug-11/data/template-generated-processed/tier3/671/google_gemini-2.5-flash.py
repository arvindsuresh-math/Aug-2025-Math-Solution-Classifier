from fractions import Fraction

def solve():
    """Index: 671.
    Returns: the number of ripe mangoes remaining.
    """
    # L1
    ripe_fraction = Fraction(3, 5) # 3/5 of the mangoes
    total_mangoes = 400 # 400 mangoes on the tree
    ripe_mangoes = ripe_fraction * total_mangoes

    # L2
    eaten_percentage = Fraction(60, 100) # 60% of the ripe mangoes
    mangoes_eaten = eaten_percentage * ripe_mangoes

    # L3
    remaining_ripe_mangoes = ripe_mangoes - mangoes_eaten

    # FA
    answer = remaining_ripe_mangoes
    return answer