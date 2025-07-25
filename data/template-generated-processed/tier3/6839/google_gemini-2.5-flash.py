from fractions import Fraction

def solve():
    """Index: 6839.
    Returns: the amount of money Rachel has left.
    """
    # L1
    initial_money = 200 # Rachel earned $200 babysitting
    lunch_fraction = Fraction(1, 4) # spent 1/4 of the money on lunch
    spent_on_lunch = lunch_fraction * initial_money

    # L2
    dvd_fraction = Fraction(1, 2) # spent 1/2 of the money on a DVD
    spent_on_dvd = dvd_fraction * initial_money

    # L3
    money_left = initial_money - spent_on_lunch - spent_on_dvd

    # FA
    answer = money_left
    return answer