from fractions import Fraction

def solve():
    """Index: 3593.
    Returns: the additional money Kate needs to buy the pen.
    """
    # L1
    fraction_of_money = Fraction(1, 3) # money for a third of that amount
    pen_cost = 30 # The pen costs $30
    money_kate_has = fraction_of_money * pen_cost

    # L2
    money_needed = pen_cost - money_kate_has

    # FA
    answer = money_needed
    return answer