from fractions import Fraction

def solve():
    """Index: 6625.
    Returns: the number of apples Ivan has leftover.
    """
    # L1
    num_mini_pies = 24 # If Ivan bakes 24 mini pies
    apples_per_mini_pie = Fraction(1, 2) # which only use 1/2 an apple each
    apples_used_for_mini_pies = num_mini_pies * apples_per_mini_pie

    # L2
    initial_apples = 48 # Ivan buys 48 apples
    apples_leftover = initial_apples - apples_used_for_mini_pies

    # FA
    answer = apples_leftover
    return answer