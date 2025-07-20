from fractions import Fraction

def solve():
    """Index: 4291.
    Returns: the total amount of money Lizzy will have.
    """
    # L1
    initial_money = 30 # Lizzy had $30
    loaned_money = 15 # loaned out $15
    money_left_after_loan = initial_money - loaned_money

    # L2
    interest_rate = Fraction(20, 100) # interest of 20%
    returned_money_with_interest = loaned_money + (loaned_money * interest_rate)

    # L3
    total_money_lizzy_has = money_left_after_loan + returned_money_with_interest

    # FA
    answer = total_money_lizzy_has
    return answer