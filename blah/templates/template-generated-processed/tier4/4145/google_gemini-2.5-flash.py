from fractions import Fraction

def solve():
    """Index: 4145.
    Returns: Ben's monthly income before taxes.
    """
    # L1
    car_payment = 400 # car payment is $400
    car_expense_percent = 0.2 # 20% of his after-tax income on his car
    after_tax_salary = car_payment / car_expense_percent

    # L2
    total_proportion = 1 # WK
    tax_rate_fraction = Fraction(1, 3) # 1/3 of his gross income in taxes
    proportion_kept_after_tax = total_proportion - tax_rate_fraction

    # L3
    before_tax_salary = after_tax_salary / proportion_kept_after_tax

    # FA
    answer = before_tax_salary
    return answer