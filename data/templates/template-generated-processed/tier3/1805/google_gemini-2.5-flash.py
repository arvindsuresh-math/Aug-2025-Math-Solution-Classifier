from fractions import Fraction

def solve():
    """Index: 1805.
    Returns: the total number of doves Giselle has now.
    """
    # L1
    initial_doves = 20 # 20 female doves
    eggs_per_dove = 3 # laid 3 eggs each
    total_eggs = initial_doves * eggs_per_dove

    # L2
    hatch_fraction = Fraction(3, 4) # 3/4 of the eggs hatched
    hatched_birds = hatch_fraction * total_eggs

    # L3
    total_doves = initial_doves + hatched_birds

    # FA
    answer = total_doves
    return answer