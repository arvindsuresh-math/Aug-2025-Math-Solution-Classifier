from fractions import Fraction

def solve():
    """Index: 2107.
    Returns: Rhett's monthly rent expense.
    """
    # L1
    monthly_salary = 5000 # currently paid $5000 per month
    tax_rate = Fraction(10, 100) # 10% tax
    taxes_paid = tax_rate * monthly_salary

    # This step is implicit in the solution, calculating salary after taxes before L2 uses it.
    salary_after_taxes = monthly_salary - taxes_paid

    # L2
    payment_fraction = Fraction(3, 5) # 3/5 of his next month's salary after taxes
    total_late_payment = payment_fraction * salary_after_taxes

    # L3
    number_of_late_payments = 2 # two of his monthly rent payments
    monthly_rent_expense = total_late_payment / number_of_late_payments

    # FA
    answer = monthly_rent_expense
    return answer