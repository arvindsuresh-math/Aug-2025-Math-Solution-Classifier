from fractions import Fraction

def solve():
    """Index: 3777.
    Returns: the number of more siblings Janet has than Carlos.
    """
    # L1
    masud_siblings = 60 # Masud has 60 siblings
    carlos_fraction = Fraction(3, 4) # 3/4 times as many siblings as Masud
    carlos_siblings = carlos_fraction * masud_siblings

    # L2
    multiplier_four = 4 # four times as many siblings as Masud
    four_times_masud_siblings = multiplier_four * masud_siblings

    # L3
    janet_less_amount = 60 # 60 less than four times as many siblings as Masud
    janet_siblings = four_times_masud_siblings - janet_less_amount

    # L4
    janet_more_than_carlos = janet_siblings - carlos_siblings

    # FA
    answer = janet_more_than_carlos
    return answer