def solve():
    """Index: 6327.
    Returns: the number of employees who did not get any increase.
    """
    # L1
    total_employees = 480 # Out of 480 employees
    salary_increase_percentage_numerator = 10 # 10% got a salary increase
    percentage_denominator = 100 # WK
    employees_salary_increase = total_employees * salary_increase_percentage_numerator / percentage_denominator

    # L2
    travel_allowance_percentage_numerator = 20 # 20% got a travel allowance increase
    employees_travel_allowance_increase = total_employees * travel_allowance_percentage_numerator / percentage_denominator

    # L3
    total_employees_with_increase = employees_salary_increase + employees_travel_allowance_increase

    # L4
    employees_no_increase = total_employees - total_employees_with_increase

    # FA
    answer = employees_no_increase
    return answer