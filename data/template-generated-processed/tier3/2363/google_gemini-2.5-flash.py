from fractions import Fraction

def solve():
    """Index: 2363.
    Returns: the total number of sheep and humans on the island.
    """
    # L1
    centipedes = 100 # the number of centipedes is 100
    centipede_human_ratio = 2 # twice as many centipedes as humans
    humans = centipedes / centipede_human_ratio

    # L2
    sheep_ratio = Fraction(1, 2) # half as many sheep as humans
    sheep = sheep_ratio * humans

    # L3
    total_sheep_humans = sheep + humans

    # FA
    answer = total_sheep_humans
    return answer