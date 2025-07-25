from fractions import Fraction

def solve():
    """Index: 1754.
    Returns: the amount of money left with Emma.
    """
    # L1
    initial_money = 2000 # Emma got $2000 from the bank
    furniture_cost = 400 # She bought $400 of furniture
    money_after_furniture = initial_money - furniture_cost

    # L2
    fraction_given_to_anna = Fraction(3, 4) # gave 3/4 of the rest to her friend Anna
    money_given_to_anna = fraction_given_to_anna * money_after_furniture

    # L3
    money_left_with_emma = money_after_furniture - money_given_to_anna

    # FA
    answer = money_left_with_emma
    return answer