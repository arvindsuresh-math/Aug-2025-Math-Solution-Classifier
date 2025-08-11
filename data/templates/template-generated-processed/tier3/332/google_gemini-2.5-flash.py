from fractions import Fraction

def solve():
    """Index: 332.
    Returns: the money Dorothy has left after paying taxes.
    """
    # L1
    tax_rate = Fraction(18, 100) # 18% of this amount
    annual_income = 60000 # $60000 a year
    tax_amount = tax_rate * annual_income

    # L2
    money_left = annual_income - tax_amount

    # FA
    answer = money_left
    return answer