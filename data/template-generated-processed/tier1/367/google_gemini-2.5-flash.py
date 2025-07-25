def solve():
    """Index: 367.
    Returns: Emily's new salary after adjusting for employee raises.
    """
    # L1
    employee_desired_salary = 35000 # make $35,000 per year
    employee_current_salary = 20000 # make $20,000 per year
    additional_per_employee = employee_desired_salary - employee_current_salary

    # L2
    num_employees = 10 # 10 employees
    total_additional_cost = additional_per_employee * num_employees

    # L3
    emily_original_salary = 1000000 # $1,000,000 per year
    emily_new_salary = emily_original_salary - total_additional_cost

    # FA
    answer = emily_new_salary
    return answer