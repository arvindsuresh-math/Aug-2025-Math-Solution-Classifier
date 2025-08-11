from fractions import Fraction

def solve():
    """Index: 6840.
    Returns: the amount of money Bob has left.
    """
    # L1
    initial_money = 80 # Bob started out the week with $80
    monday_fraction = Fraction(1, 2) # half the money
    money_after_monday = initial_money - (monday_fraction * initial_money)

    # L2
    tuesday_fraction = Fraction(1, 5) # one-fifth of the amount left from Monday
    money_after_tuesday = money_after_monday - (tuesday_fraction * money_after_monday)

    # L3
    wednesday_fraction = Fraction(3, 8) # 3/8ths of the amount left from Tuesday
    money_after_wednesday = money_after_tuesday - (wednesday_fraction * money_after_tuesday)

    # FA
    answer = money_after_wednesday
    return answer