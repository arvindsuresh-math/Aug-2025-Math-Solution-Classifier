def solve():
    """Index: 5330.
    Returns: the amount of money Steve takes home.
    """
    # L1
    annual_salary = 40000 # Steve makes 40000$ a year
    tax_percent_decimal = 0.20 # loses 20 percent to taxes
    taxes_amount = annual_salary * tax_percent_decimal

    # L2
    healthcare_percent_decimal = 0.10 # 10 percent to healthcare
    healthcare_amount = annual_salary * healthcare_percent_decimal

    # L3
    union_dues = 800 # 800$ to local union dues
    dues_amount = union_dues

    # L4
    take_home_pay = annual_salary - taxes_amount - healthcare_amount - dues_amount

    # FA
    answer = take_home_pay
    return answer