from fractions import Fraction

def solve():
    """Index: 4903.
    Returns: half the difference in the amount contributed.
    """
    # L1
    julie_donation = 4700 # Julie donated $4700
    margo_donation = 4300 # Margo donated $4300
    difference_in_contribution = julie_donation - margo_donation

    # L2
    half_fraction = Fraction(1, 2) # Half the difference
    half_difference = half_fraction * difference_in_contribution

    # FA
    answer = half_difference
    return answer