from fractions import Fraction

def solve():
    """Index: 5036.
    Returns: the number of lollipops Lou received.
    """
    # L1
    initial_lollipops = 42 # Marlon had 42 lollipops
    fraction_given_to_emily = Fraction(2, 3) # gave her 2/3 of his lollipops
    lollipops_given_to_emily = initial_lollipops * fraction_given_to_emily

    # L2
    lollipops_left_after_emily = initial_lollipops - lollipops_given_to_emily

    # L3
    lollipops_kept_by_marlon = 4 # Marlon kept 4 lollipops
    lollipops_given_to_lou = lollipops_left_after_emily - lollipops_kept_by_marlon

    # FA
    answer = lollipops_given_to_lou
    return answer