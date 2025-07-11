def solve():
    """Index: 480.
    Returns: Kirt's total earnings after 3 years.
    """
    # L1
    initial_monthly_salary = 6000 # $6000 monthly salary when he started his job
    months_per_year = 12 # WK
    first_year_annual_salary = initial_monthly_salary * months_per_year

    # L2
    increase_percentage_numerator = 30 # salary increased by 30%
    increase_percentage_denominator = 100 # WK
    monthly_increase = initial_monthly_salary * increase_percentage_numerator / increase_percentage_denominator

    # L3
    increased_monthly_salary = initial_monthly_salary + monthly_increase

    # L4
    second_and_third_year_annual_salary = increased_monthly_salary * months_per_year

    # L5
    total_earnings = first_year_annual_salary + second_and_third_year_annual_salary + second_and_third_year_annual_salary

    # FA
    answer = total_earnings
    return answer