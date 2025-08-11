from fractions import Fraction

def solve():
    """Index: 3437.
    Returns: the amount of money John has remaining.
    """
    # L1
    initial_money = 100 # $100 from his uncle
    fraction_given_to_sister = Fraction(1, 4) # 1/4 of that money
    money_given_to_sister = fraction_given_to_sister * initial_money

    # L2
    money_after_giving_sister = initial_money - money_given_to_sister

    # L3
    groceries_cost = 40 # groceries worth $40
    money_remaining = money_after_giving_sister - groceries_cost

    # FA
    answer = money_remaining
    return answer