from fractions import Fraction

def solve():
    """Index: 332.
    Returns: the amount of money Dorothy has left after paying taxes.
    """
    # L1
    tax_rate = Fraction(18, 100) # 18% of this amount in taxes
    annual_income = 60000 # Dorothy earns $60000 a year
    taxes_paid = tax_rate * annual_income

    # L2
    money_left = annual_income - taxes_paid

    # FA
    answer = money_left
    return answer