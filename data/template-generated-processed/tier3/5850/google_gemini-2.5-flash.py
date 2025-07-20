from fractions import Fraction

def solve():
    """Index: 5850.
    Returns: the total amount of money the company paid to the remaining employees.
    """
    # L1
    layoff_fraction = Fraction(1, 3) # 1/3 of its employees
    total_employees = 450 # The total number of employees in a company is 450
    laid_off_employees = layoff_fraction * total_employees

    # L2
    remaining_employees = total_employees - laid_off_employees

    # L3
    monthly_salary_per_employee = 2000 # each employee earns $2000 per month
    total_money_paid = remaining_employees * monthly_salary_per_employee

    # FA
    answer = total_money_paid
    return answer