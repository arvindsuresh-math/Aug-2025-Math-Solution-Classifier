from fractions import Fraction

def solve():
    """Index: 2039.
    Returns: the number of packs of marbles Leo kept.
    """
    # L1
    total_marbles = 400 # Leo had 400 marbles
    marbles_per_pack = 10 # ten marbles in each pack
    total_packs = total_marbles / marbles_per_pack

    # L2
    manny_fraction = Fraction(1, 4) # 1/4 of the number of packs of marbles
    manny_packs = manny_fraction * total_packs

    # L3
    neil_fraction = Fraction(1, 8) # 1/8 of the number of packs of marbles
    neil_packs = neil_fraction * total_packs

    # L4
    total_given_packs = manny_packs + neil_packs

    # L5
    packs_kept = total_packs - total_given_packs

    # FA
    answer = packs_kept
    return answer