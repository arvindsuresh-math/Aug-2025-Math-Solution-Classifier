from fractions import Fraction

def solve():
    """Index: 6271.
    Returns: the total amount Greg paid for lunch, tax, and tip.
    """
    # L1
    lunch_cost = 100 # lunch that cost $100
    sales_tax_percentage = Fraction(4, 100) # sales tax in New York is 4%
    sales_tax_amount = lunch_cost * sales_tax_percentage

    # L2
    tip_percentage = Fraction(6, 100) # he left a 6% tip
    tip_amount = lunch_cost * tip_percentage

    # L3
    total_tax_and_tip = sales_tax_amount + tip_amount

    # L4
    total_paid = lunch_cost + total_tax_and_tip

    # FA
    answer = total_paid
    return answer