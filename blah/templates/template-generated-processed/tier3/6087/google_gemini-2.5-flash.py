from fractions import Fraction

def solve():
    """Index: 6087.
    Returns: the total amount of money in the bank after 2 years.
    """
    # L1
    initial_deposit = 100 # Steve puts $100 into the bank
    interest_factor = Fraction(110, 100) # Each year he earns 10% interest
    money_after_year1 = initial_deposit * interest_factor

    # L2
    money_after_year2 = money_after_year1 * interest_factor

    # FA
    answer = money_after_year2
    return answer