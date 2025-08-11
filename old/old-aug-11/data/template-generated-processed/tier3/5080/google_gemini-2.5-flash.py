from fractions import Fraction

def solve():
    """Index: 5080.
    Returns: the total amount of money in the joint savings account.
    """
    # L1
    kimmie_earnings = 450 # Kimmie received $450
    less_fraction = Fraction(1, 3) # 1/3 less money
    zahra_less_money = less_fraction * kimmie_earnings

    # L2
    zahra_earnings = kimmie_earnings - zahra_less_money

    # L3
    savings_fraction = Fraction(1, 2) # save half of their earnings
    kimmie_saved = savings_fraction * kimmie_earnings

    # L4
    zahra_saved = savings_fraction * zahra_earnings

    # L5
    total_savings = kimmie_saved + zahra_saved

    # FA
    answer = total_savings
    return answer