from fractions import Fraction

def solve():
    """Index: 4981.
    Returns: the difference in dollars Akeno spent compared to Lev and Ambrocio combined.
    """
    # L1
    lev_fraction = Fraction(1, 3) # one-third of that amount
    akeno_spent = 2985 # Akeno spent $2985
    lev_spent = lev_fraction * akeno_spent

    # L2
    ambrocio_less_amount = 177 # Ambrocio spent $177 less than Lev
    ambrocio_spent = lev_spent - ambrocio_less_amount

    # L3
    difference_akeno_others = akeno_spent - (lev_spent + ambrocio_spent)

    # FA
    answer = difference_akeno_others
    return answer