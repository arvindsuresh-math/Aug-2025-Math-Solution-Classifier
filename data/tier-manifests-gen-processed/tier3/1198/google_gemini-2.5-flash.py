from fractions import Fraction

def solve():
    """Index: 1198.
    Returns: the amount of money Arthur has left.
    """
    # L1
    fraction_spent = Fraction(4, 5) # four-fifths of that
    initial_money = 200 # $200 in his wallet
    money_spent = fraction_spent * initial_money

    # L2
    money_left = initial_money - money_spent

    # FA
    answer = money_left
    return answer