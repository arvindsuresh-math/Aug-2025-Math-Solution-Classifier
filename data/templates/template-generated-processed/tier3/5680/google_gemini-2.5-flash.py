from fractions import Fraction

def solve():
    """Index: 5680.
    Returns: Jonessa's take-home pay.
    """
    # L1
    total_pay = 500 # pay is $500
    tax_percentage = Fraction(10, 100) # Ten percent
    tax_amount = total_pay * tax_percentage

    # L2
    take_home_pay = total_pay - tax_amount

    # FA
    answer = take_home_pay
    return answer