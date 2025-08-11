def solve():
    """Index: 922.
    Returns: the total amount of money earned in both companies.
    """
    # L1
    old_company_years = 3 # she worked at her old company for 3 years
    months_per_year = 12 # WK
    old_company_months = old_company_years * months_per_year

    # L2
    old_company_monthly_salary = 5000 # earning $5000 per month
    old_company_total_earnings = old_company_monthly_salary * old_company_months

    # L3
    new_company_raise_percentage = 20 # earning 20% more
    percentage_divisor = 100 # WK
    new_company_raise_amount = (new_company_raise_percentage / percentage_divisor) * old_company_monthly_salary

    # L4
    new_company_monthly_salary = old_company_monthly_salary + new_company_raise_amount

    # L5
    new_company_extra_months = 5 # five months longer
    new_company_months = old_company_months + new_company_extra_months

    # L6
    new_company_total_earnings = new_company_monthly_salary * new_company_months

    # L7
    total_earnings_both_companies = new_company_total_earnings + old_company_total_earnings

    # FA
    answer = total_earnings_both_companies
    return answer