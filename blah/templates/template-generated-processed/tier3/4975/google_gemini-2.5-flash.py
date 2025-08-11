from fractions import Fraction

def solve():
    """Index: 4975.
    Returns: the number of action figures Angela has left.
    """
    # L1
    total_figures = 24 # collection of 24 pieces of rare action figures
    sold_fraction = Fraction(1, 4) # a quarter of them
    sold_figures = total_figures * sold_fraction

    # L2
    remaining_after_sale = total_figures - sold_figures

    # L3
    given_fraction = Fraction(1, 3) # one-third of the remainder
    given_to_daughter = remaining_after_sale * given_fraction

    # L4
    final_remaining = remaining_after_sale - given_to_daughter

    # FA
    answer = final_remaining
    return answer