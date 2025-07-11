from fractions import Fraction

def solve():
    """Index: 660.
    Returns: the total number of ants the four children find together.
    """
    # L1
    abe_ants = 4 # Abe finds 4 ants on the sidewalk
    beth_percentage_more = Fraction(50, 100) # 50% more ants than Abe
    additional_beth_ants = beth_percentage_more * abe_ants
    beth_ants = abe_ants + additional_beth_ants

    # L2
    cece_multiplier = 2 # twice as many ants as Abe
    cece_ants = abe_ants * cece_multiplier

    # L3
    duke_divisor = 2 # half as many ants as Abe
    duke_ants = abe_ants / duke_divisor

    # L4
    total_ants = abe_ants + beth_ants + cece_ants + duke_ants

    # FA
    answer = total_ants
    return answer