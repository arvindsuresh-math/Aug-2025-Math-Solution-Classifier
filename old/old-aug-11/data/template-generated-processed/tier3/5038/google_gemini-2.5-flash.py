from fractions import Fraction

def solve():
    """Index: 5038.
    Returns: the number of peanuts remaining in the jar.
    """
    # L1
    total_peanuts = 148 # 148 peanuts in a jar
    brock_fraction = Fraction(1, 4) # one-fourth of the peanuts
    peanuts_brock_ate = total_peanuts * brock_fraction

    # L2
    bonita_ate = 29 # Bonita ate 29 peanuts
    remaining_peanuts = total_peanuts - peanuts_brock_ate - bonita_ate

    # FA
    answer = remaining_peanuts
    return answer