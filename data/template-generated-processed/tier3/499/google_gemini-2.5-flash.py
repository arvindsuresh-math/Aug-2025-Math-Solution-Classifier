from fractions import Fraction

def solve():
    """Index: 499.
    Returns: the total money earned by Salvadore and Santo.
    """
    # L1
    salvadore_earnings = 1956 # Salvadore earned $1956
    santo_multiplier = Fraction(1, 2) # half of what Salvadore earned
    santo_earnings = santo_multiplier * salvadore_earnings

    # L2
    total_earnings = salvadore_earnings + santo_earnings

    # FA
    answer = total_earnings
    return answer