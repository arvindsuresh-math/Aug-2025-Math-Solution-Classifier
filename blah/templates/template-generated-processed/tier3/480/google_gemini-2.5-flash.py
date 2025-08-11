from fractions import Fraction

def solve():
    """Index: 480.
    Returns: Kirt's total earnings after 3 years.
    """
    # L1
    monthly_salary = 6000 # a $6000 monthly salary
    months_per_year = 12 # WK
    annual_salary_first_year = monthly_salary * months_per_year

    # L2
    salary_increase_percentage = Fraction(30, 100) # salary increased by 30%
    monthly_increase = monthly_salary * salary_increase_percentage

    # L3
    new_monthly_salary = monthly_salary + monthly_increase

    # L4
    annual_salary_subsequent_years = new_monthly_salary * months_per_year

    # L5
    total_earnings = annual_salary_first_year + annual_salary_subsequent_years + annual_salary_subsequent_years

    # FA
    answer = total_earnings
    return answer