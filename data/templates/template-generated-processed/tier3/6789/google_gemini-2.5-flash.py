from fractions import Fraction

def solve():
    """Index: 6789.
    Returns: Jebb's take-home pay.
    """
    # L1
    pay = 650 # his pay is $650
    tax_percentage = Fraction(10, 100) # pay 10% for the tax
    tax_amount = pay * tax_percentage

    # L2
    take_home_pay = pay - tax_amount

    # FA
    answer = take_home_pay
    return answer