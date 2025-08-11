from fractions import Fraction

def solve():
    """Index: 6215.
    Returns: the total number of jumps by Hattie and Lorelei in two rounds.
    """
    # L1
    hattie_jumps_round1 = 180 # Hattie does 180 jumps in the first round
    lorelei_fraction_round1 = Fraction(3, 4) # Lorelei jumps 3/4 as many times as Hattie
    lorelei_jumps_round1 = lorelei_fraction_round1 * hattie_jumps_round1

    # L2
    hattie_fraction_round2 = Fraction(2, 3) # Hattie managed to jump 2/3 times the number of jumps she did in the first round
    hattie_jumps_round2 = hattie_fraction_round2 * hattie_jumps_round1

    # L3
    lorelei_additional_jumps_round2 = 50 # Lorelei does 50 more jumps than Hattie
    lorelei_jumps_round2 = hattie_jumps_round2 + lorelei_additional_jumps_round2

    # L4
    total_jumps = lorelei_jumps_round2 + hattie_jumps_round2 + lorelei_jumps_round1 + hattie_jumps_round1

    # FA
    answer = total_jumps
    return answer